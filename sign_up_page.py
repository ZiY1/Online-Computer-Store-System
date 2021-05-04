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



# TODO: line 200, 203
class sign_up_page(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self,master) 
        self.master.title("Sign Up Page")
        self.master.geometry( "550x450" )
        self.master.configure( background = "light blue" )
        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel() 
        self.style = tk.ttk.Style()
        # Title 
        self.style.configure( "LabelTitle.TLabel", 
                               relief=tk.SUNKEN,
                               anchor = "center", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "Customer Sign up", 
                                        style =  "LabelTitle.TLabel"  
                                      )
        self.LabelTitle.place( relx = 0.195, rely = 0.07, 
                               relwidth = 0.632, relheight = 0.155 
                            )

        # Name 
        self.TextNameVar = tk.StringVar(value="Last Name + First Name")
        self.TextName = tk.Entry( self.top, textvariable = self.TextNameVar) 
        self.TextName.place( relx = 0.350, rely = 0.410, relwidth = 0.5550, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = 'light blue'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Name: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.0455, rely=0.390, relwidth=0.250, relheight=0.125)
		

        # Email Address 
        self.UsernameVar = tk.StringVar(value="Please enter email")
        self.TextUsername =  tk.Entry( self.top, textvariable = self.UsernameVar ) 
        self.TextUsername.place( relx=0.350, rely=0.540, relwidth=0.5550, relheight=0.080 )


        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = 'light blue'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Username: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely=0.520, relwidth=0.250, relheight=0.125 )
		

        # Password 
        self.PasswordVar = tk.StringVar()
        self.TextPassword = tk.Entry( self.top, textvariable = self.PasswordVar) 
        self.TextPassword.place( relx = 0.350, rely = 0.670, relwidth = 0.5550, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = 'light blue'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Password: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely = 0.652, relwidth=0.250, relheight=0.125)

        # Sign up button
        self.style.configure("CommandSignUp.TButton", anchor="center", font=("Helvetica", 16) )
        self.CommandSignUp = tk.ttk.Button(self.top, text="Sign Up", 
                                command=self.command_sign_up, style="CommandSignUp.TButton")
		
        self.CommandSignUp.place(relx=0.420, rely=0.8, relwidth=0.200, relheight=0.095)

        #Go Back Home Page Button
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16) )
        self.CommandBack = tk.ttk.Button(self.top, text="Back to Home", 
                                command=self.command_back, style="CommandBack.TButton")
		
        self.CommandBack.place(relx=0.7, rely=0.9, relwidth=0.290, relheight=0.095)




    def command_sign_up(self):
        
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

    #--------------Check if username suspended------------------------------
        flag_suspended, flag_last_time_notify = self.is_suspended('customer', Username)
    #--------------Check if the username is already registered------------
        if not flag_suspended:
            df = pd.read_excel( "csv_files/registered_customers.xlsx" )
            df_active = df[df['Status'] == 'active']

            if Username.lower() in list( df_active['Username']):
                # we have duplicate accounts
                flag_duplicates =  True
                tk.messagebox.showerror( "Error","username is taken" )
            else: # We do not have duplicates
                flag_duplicates = False 
                Id = len(df)
                tempo = pd.DataFrame( [[ Id , Name, Username.lower(), Password, "empty","0","empty","0.00","", "active"]],
                            columns = ['ID', 'Name', 'Username', 'Password', 'Credit card account',
                            'Warnings', 'Home Address','Balance', 'Phone number', "Status"])
                df = df.append(tempo)
        else:
            if flag_last_time_notify:
                CurrentWarning, SuspendReason = self.update_suspend_file('customer', Username)
                tk.messagebox.showerror( "Error", "Application denied, this account has been suspended, and this is the last time we notify you with details.\n"
                                         + "\nCurrent Warning: " + str(CurrentWarning)
                                        + "\nSuspend Justification: " + str(SuspendReason))
                # TODO: Inform the user's inbox
            else:
                tk.messagebox.showerror( "Error", "Application denied")
                # TODO: Inform the user's inbox
    #-----------------------------------------------------------------------

        if (not flag_suspended) and (not flag_duplicates) and flag_valid_email and flag_password_valid and flag_valid_name: 
            df.to_excel( "csv_files/registered_customers.xlsx", index = False)
            tk.messagebox.showinfo("Success", f"Congratulation {Name}, you have created a new account" )         
            self.top.destroy()       
            registered_login.registered_login() 



    def is_suspended(self, type_user, username):
        df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
        df_suspend_user = df_suspend[df_suspend['Type_user'] == type_user]
        flag_last_time_notify = False
        flag_suspended = False
        if username.lower() in list(df_suspend_user['Username']):
            flag_suspended = True
            df_user_row = df_suspend_user[df_suspend_user['Username'] == username]
            if df_user_row['Customer_deny_notify'].iloc[-1] == 1:
                flag_last_time_notify = True
        else:
            flag_last_time_notify = False
        return flag_suspended, flag_last_time_notify


    def update_suspend_file(self, type_user, username):
        # Fetch out suspend reason, last time notify decrease 1
        df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
        df_suspend_user = df_suspend[df_suspend['Type_user'] == type_user]
        df_user_row = df_suspend_user[df_suspend_user['Username'] == username]
        SuspendReason = df_user_row['Suspend_reason'].iloc[-1]
        CurrentWarning = df_user_row['Current_warnings'].iloc[-1]
        df_suspend.loc[df_suspend['Username'] == username, 'Customer_deny_notify'] = 0
        df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
        #print(SuspendReason)
        return CurrentWarning, SuspendReason


    def command_back(self):
        self.top.destroy()
        home.HomePage()        
