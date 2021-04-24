import tkinter as tk 
import tkinter.ttk as ttk 
import numpy as np
import pandas as pd
import re


# python files
#import guess_welcome
import customer_page
import main as home
import registered_login



class sign_up_page(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self,master) 
        self.master.title("Sign Up Page")
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        
        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel() 
        self.style = tk.ttk.Style()
        # Title 
        self.style.configure( "LabelTitle.TLabel", 
                               anchor = "center", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "Customer Sign up", 
                                        style =  "LabelTitle.TLabel"  
                                      )
        self.LabelTitle.place( relx = 0.205, rely = 0.100, 
                               relwidth = 0.632, relheight = 0.195 
                            )

        # Name 
        self.TextNameVar = tk.StringVar()
        self.TextName = tk.Entry( self.top, textvariable = self.TextNameVar) 
        self.TextName.place( relx = 0.350, rely = 0.410, relwidth = 0.5550, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Name: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely=0.390, relwidth=0.250, relheight=0.125)
		

        # Email Address 
        self.UsernameVar = tk.StringVar()
        self.TextUsername =  tk.Entry( self.top, textvariable = self.UsernameVar ) 
        self.TextUsername.place( relx=0.350, rely=0.540, relwidth=0.550, relheight=0.080 )


        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Username(email): ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely=0.520, relwidth=0.250, relheight=0.125 )
		

        # Password 
        self.PasswordVar = tk.StringVar()
        self.TextPassword = tk.Entry( self.top, textvariable = self.PasswordVar) 
        self.TextPassword.place( relx = 0.350, rely = 0.670, relwidth = 0.5550, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Password: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely = 0.652, relwidth=0.250, relheight=0.125)

        # Sign up button
        self.style.configure("CommandSignUp.TButton", anchor="center", font=("Helvetica", 16),
                               background = "green", foreground = "black" )
        self.CommandSignUp = tk.ttk.Button(self.top, text="Sign Up", 
                                command=self.command_sign_up, style="CommandSignUp.TButton")
		
        self.CommandSignUp.place(relx=0.420, rely=0.8, relwidth=0.200, relheight=0.095)

        #------------------------- Go Back Home Page Button---------------------------------
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16),
                                    background = "green", foreground= "black" )
        self.CommandBack = tk.ttk.Button(self.top, text="Go Back to Home Page", 
                                command=self.command_back, style="CommandBack.TButton")
		
        self.CommandBack.place(relx=0.8, rely=0.9, relwidth=0.200, relheight=0.095)
        #------------------------------------------------------------------------------------




    def command_sign_up(self):
        #   self.TextName,      self.TextNameVar
        #   self.TextUsername,  self.UsernameVar
        #   self.TextPassword,   self.PasswordVar
        
        Name = self.TextName.get()
        Username = self.TextUsername.get()
        Password = self.TextPassword.get()

    #-----------------------Check if the Name is valid()-------------

        regex_name = "[a-zA-Z]+[\s][a-zA-Z]+[\-\']?[a-zA-Z]+"
        regex_name2= "[a-zA-Z]+[\s][a-zA-Z]+[-\']?[a-zA-Z]+[\s][a-zA-Z]+"
        if(  re.fullmatch(regex_name, Name) or re.fullmatch(regex_name2, Name) ):
            flag_valid_name = True
            Name = Name.lower().title()
        else:
            flag_valid_name = False
            tk.messagebox.showerror( "Error", "invalid Name" )

    #-------------------------------------------------------------------


    #----------------Check if the username is a working email----------------
        
        regex = "[A-Za-z0-9_]+[@]\w+[.]\w{2,3}$"
        if(  re.fullmatch(regex, Username) ):
            flag_valid_email = True
            Username = Username.lower()
        else:
            flag_valid_email = False
            tk.messagebox.showerror( "Error", "invalid email username" )
    #-------------------------------------------------------------------------

    #---------------------check if the password is valid(no empty)-----------------------
        if Password != "":
            flag_password_valid = True
        else:
            tk.messagebox.showerror( "Error", "invalid password" )
            flag_password_valid = False

    #-----------------------------------------------------------------------

    #--------------Check if the username is already registered------------
        df = pd.read_excel( "csv_files/registered_customers.xlsx" )

        flag_duplicates = False 
        if (len(df) == 0 ):
            Id = 0
            tempo = pd.DataFrame( [["0", Name, Username.lower(), Password, "empty","0", "","0.00",""]],
                            columns = ['ID', 'Name', 'Username', 'Password', 'Credit card account',
                            'Warnings', 'Home Address', 'Balance', 'Phone number'] 
                            )
            df = df.append(tempo)
             
        else:
            if Username.lower() in list( df['Username']):
                # we have duplicate accounts
                flag_duplicates = True
                tk.messagebox.showerror( "Error","username is taken" )
            else:
                Id = int( df['ID'].iloc[-1] )
                Id += 1 
                tempo = pd.DataFrame( [[ str(Id) , Name, Username.lower(), Password, "empty","0","","0.00",""] ],
                              columns = ['ID', 'Name', 'Username', 'Password', 'Credit card account',
                              'Warnings', 'Home Address','Balance', 'Phone number'] 
                            )
                df = df.append(tempo)
                

    #-----------------------------------------------------------------------

        if (not flag_duplicates) and flag_valid_email and flag_password_valid and flag_valid_name: 
            df.to_excel( "csv_files/registered_customers.xlsx", index = False)            
                    
            tk.messagebox.showinfo("Success", 
                            f"Congratulation {Name}, you have created a new account" )

            self.top.destroy()
            registered_login.registered_login()

            

    def command_back(self):
        self.top.destroy()
        home.HomePage()        
