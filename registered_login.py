import tkinter as tk
import tkinter.ttk as ttk 

import numpy as np
import pandas as pd


# python files 
import main as home 
import customer_page
import sign_up_page

class registered_login(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master) 
        self.master.title( "Registered Costumer Login" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel()
        
        self.style = tk.ttk.Style()

		#--------------------------Title Label-------------------------------------------
        self.style.configure("LabelTitle.TLabel", anchor="center", 
                                font=("Helvetica", 26), background = '#49A')
		
        self.LabelTitle = tk.ttk.Label(self.top, text="Customer Log In", style="LabelTitle.TLabel")
		
        self.LabelTitle.place(relx=0.205, rely=0.08, relwidth=0.632, relheight=0.195)
        #-------------------------------------------------------------------------------


        #---------------------------User Name------------------------------------------
        self.TextNameVar = tk.StringVar()
        self.TextUserName = tk.Entry(self.top, textvariable=self.TextNameVar)
        self.TextUserName.place(relx=0.350, rely=0.430, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelName.TLabel", font=("Helvetica", 16), background = '#49A')
        self.LabelUserName = tk.ttk.Label(self.top, text= "Username: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelUserName.place(relx=0.08, rely=0.410, relwidth=0.250, relheight=0.125)

        #--------------------------------------------------------------------------------


        #--------------------------Password---------------------------------------------
        self.TextPasswordVar = tk.StringVar()
        self.TextPassword = tk.Entry(self.top, textvariable=self.TextPasswordVar, show="*")
        self.TextPassword.place(relx=0.350, rely=0.560, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelPassword.TLabel", font=("Helvetica", 16) , background = '#49A')
        self.LabelPassword = tk.ttk.Label(self.top, text="Password: ", 
                                            style="LabelPassword.TLabel", anchor = "center")
        self.LabelPassword.place(relx=0.08, rely=0.540, relwidth=0.250, relheight=0.125)
        #------------------------------------------------------------------------------


        #-------------------------------Log In Button---------------------------------
        	
        self.style.configure("CommandLogin.TButton", anchor="center",font=("Helvetica", 16),  
                              background = "green", foreground= "black")
        self.CommandLogin = tk.ttk.Button(self.top, text="Login", command=self.command_login,
                                         style="CommandLogin.TButton")
        self.CommandLogin.place(relx=0.180, rely=0.700, relwidth=0.200, relheight=0.095)
        #-------------------------------------------------------------------------------

        #--------------------------------Sign Up Button----------------------------------
        # sign_up_page
        self.style.configure("CommandSignUp.TButton", anchor="center",font=("Helvetica", 16),
                                background = "green", foreground = "black" )
        self.CommandSignUp = tk.ttk.Button(self.top, text="Sign Up", 
                                command=self.command_sign_up, style="CommandSignUp.TButton")
        self.CommandSignUp.place(relx=0.550, rely=0.700, relwidth=0.200, relheight=0.095)





        #--------------------------------------------------------------------------------

        #-------------------------------Back button------------------------------------------
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16),
                                    background = "green", foreground= "black" )
        self.CommandBack = tk.ttk.Button(self.top, text="Go Back", 
                                command=self.command_back, style="CommandBack.TButton")
		
        self.CommandBack.place(relx=0.8, rely=0.9, relwidth=0.200, relheight=0.095)
        #--------------------------------------------------------------------------------------


    def command_login(self):
        Username = self.TextUserName.get()
        Password = self.TextPassword.get()

        Username = Username.lower() # it's not usercase sensitive

        df = pd.read_excel( "csv_files/registered_customers.xlsx" )
        
        #--------Check if the username provided is registered-------------
        if Username not in list(df['Username']):
            flag_username_registered = False
            tk.messagebox.showerror( "Error", "invalid email username" )
        else:
            flag_username_registered = True
        #-----------------------------------------------------------------


        #-----------check if the password provided matches the username-----
        user_info_df = df[df['Username'] == Username ] # dataframe containing the customer info 

        
        if user_info_df['Password'].iloc[-1] == Password:
            flag_correct_password = True
        else:
            flag_correct_password = False
            tk.messagebox.showerror( "Error", "incorrect password provided" )


        #-------------------------------------------------------------------


        if flag_username_registered and flag_correct_password:
            self.top.destroy()
            Customer_Name = user_info_df['Name'].iloc[-1] 
            Customer_Username = user_info_df['Username'].iloc[-1]
            Customer_Id = user_info_df['ID'].iloc[-1]

            customer_page.customer_page(Customer_Name, Customer_Username, Customer_Id)
            


    def command_back(self):
        self.top.destroy()
        home.HomePage()

    def command_sign_up(self):
        self.top.destroy()
        sign_up_page.sign_up_page()
