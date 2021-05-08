import tkinter as tk
import tkinter.ttk as ttk 

import numpy as np
import pandas as pd
import datetime


# python files 
import main as home 
import customer_page
import sign_up_page

class registered_login(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master) 
        self.master.title( "Registered Costumer Login" )
        self.master.geometry( "550x450" )
        self.master.configure( background = "light blue" )
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel()
        
        self.style = tk.ttk.Style()

		# Title Label
        self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 26), background = '#49A')
        self.LabelTitle = tk.ttk.Label(self.top, text="Customer Login", style="LabelTitle.TLabel")
        self.LabelTitle.place(relx=0.195, rely=0.07, relwidth=0.632, relheight=0.155)


        # User Name
        self.TextNameVar = tk.StringVar()
        self.TextUserName = tk.Entry(self.top, textvariable=self.TextNameVar)
        self.TextUserName.place(relx=0.350, rely=0.430, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelName.TLabel", font=("Helvetica", 16), background = 'light blue')
        self.LabelUserName = tk.ttk.Label(self.top, text= "Username: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelUserName.place(relx=0.08, rely=0.410, relwidth=0.250, relheight=0.125)


        # Password
        self.TextPasswordVar = tk.StringVar()
        self.TextPassword = tk.Entry(self.top, textvariable=self.TextPasswordVar, show="*")
        self.TextPassword.place(relx=0.350, rely=0.560, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelPassword.TLabel", font=("Helvetica", 16) , background = 'light blue')
        self.LabelPassword = tk.ttk.Label(self.top, text="Password: ", 
                                            style="LabelPassword.TLabel", anchor = "center")
        self.LabelPassword.place(relx=0.08, rely=0.540, relwidth=0.250, relheight=0.125)


        # Log In Button
        self.style.configure("CommandLogin.TButton", anchor="center",font=("Helvetica", 16))
        self.CommandLogin = tk.ttk.Button(self.top, text="Login", command=self.command_login,
                                         style="CommandLogin.TButton")
        self.CommandLogin.place(relx=0.280, rely=0.700, relwidth=0.200, relheight=0.095)

        # Sign Up Button
        # sign_up_page
        self.style.configure("CommandSignUp.TButton", anchor="center",font=("Helvetica", 16))
        self.CommandSignUp = tk.ttk.Button(self.top, text="Sign Up", 
                                command=self.command_sign_up, style="CommandSignUp.TButton")
        self.CommandSignUp.place(relx=0.560, rely=0.700, relwidth=0.200, relheight=0.095)


        # Back button
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16) )
        self.CommandBack = tk.ttk.Button(self.top, text="Back", 
                                command=self.command_back, style="CommandBack.TButton")
        self.CommandBack.place(relx=0.796, rely=0.90, relwidth=0.190, relheight=0.083)


    def command_login(self):
        Username = self.TextUserName.get().lower()
        Password = self.TextPassword.get()

        df = pd.read_excel( "csv_files/registered_customers.xlsx" )
        type_user = 'customer'
        #Check if the username is suspended
        flag_suspended, flag_last_chance_login = self.is_suspended(type_user, Username)

        if (not flag_suspended):
            flag_username_registered, flag_correct_password = self.verify_access(df, Username, Password)

            if flag_username_registered and flag_correct_password:
                self.top.destroy()
                user_info_df = df[df['Username'] == Username ]
                Customer_Name = user_info_df['Name'].iloc[-1] 
                Customer_Username = user_info_df['Username'].iloc[-1]
                Customer_Id = user_info_df['ID'].iloc[-1]
                customer_page.customer_page(Customer_Name, Customer_Username, Customer_Id)
        else:
            df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
            df_customer = df_suspend[ df_suspend['Type_user'] == type_user]
            flag_username_registered, flag_correct_password = self.verify_access(df_customer, Username, Password)
            if flag_username_registered and flag_correct_password and flag_last_chance_login:
                CurrentWarning, SuspendReason = self.update_suspend_file('customer', Username, flag_last_chance_login)
                tk.messagebox.showwarning( "Warning", "Your account is suspended, you have one last chance to login and clean up your account\n" 
                                        + "\nCurrent Warning: " + str(CurrentWarning)
                                        + "\nSuspend Justification: " + str(SuspendReason))
                self.top.destroy()
                
                user_info_df = df_customer[df_customer['Username'] == Username ]
                Customer_Name = user_info_df['Name'].iloc[-1] 
                Customer_Username = user_info_df['Username'].iloc[-1]
                Customer_Id = user_info_df['ID'].iloc[-1]
                
                message1 = f"Dear {Customer_Name},\n\n"
                message2 = "We regret to inform you that your account has been suspended. You are allowed one last login"
                message3 = " to clean up your account.\n"
                message4 = "\nThanks, Lenovo Admin"
                message = message1 + message2 + message3 + message4 
                df_emails = pd.read_excel( "csv_files/emails.xlsx")
            
                Id = len(df_emails)
                now = datetime.datetime.now()
                date_send = now.strftime("%m/%d/%Y, %H:%M:%S") 
                
                tempo = pd.DataFrame( [[Id, Customer_Username, "Lenovo Admin", date_send, "Account Suspended", message, "unread"]],
                            columns = ['ID', 'for_username', 'From', 'Date_received', 'Subject', 'Message', 'Status'])
                df_emails = df_emails.append(tempo)

                df_emails.to_excel("csv_files/emails.xlsx", index = False)    
                

                customer_page.customer_page(Customer_Name, Customer_Username, Customer_Id)
            elif flag_username_registered and flag_correct_password and not flag_last_chance_login:
                CurrentWarning, SuspendReason = self.update_suspend_file('customer', Username, flag_last_chance_login)
                tk.messagebox.showerror( "error", "Your account is suspended, you cannot login anymore" 
                                         + "\nCurrent Warning: " + str(CurrentWarning)
                                         + "\nSuspend Justification: " + str(SuspendReason))


    def command_back(self):
        self.top.destroy()
        home.HomePage()

    def command_sign_up(self):
        self.top.destroy()
        sign_up_page.sign_up_page()

    def verify_access(self, df, username, password):
        # Check if the username provided is registered
        if username not in list(df['Username']):
            flag_username_registered = False
            tk.messagebox.showerror( "Error", "invalid email username" )
        else:
            flag_username_registered = True

        # Check if the password provided matches the username
        user_info_df = df[df['Username'] == username ] # dataframe containing the customer info 

        if flag_username_registered and str(user_info_df['Password'].iloc[-1]) == password:
            flag_correct_password = True
        else:
            flag_correct_password = False
            tk.messagebox.showerror( "Error", "incorrect password provided" )

        return flag_username_registered, flag_correct_password

    def is_suspended(self, type_user, username):
        df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
        df_suspend_user = df_suspend[df_suspend['Type_user'] == type_user]
        flag_last_chance_login = False
        if username.lower() in list(df_suspend_user['Username']):
            flag_suspended = True
            df_user_row = df_suspend_user[df_suspend_user['Username'] == username]
            if df_user_row['Chance_login'].iloc[-1] == 1:
                flag_last_chance_login = True
        else:
            flag_suspended = False
        return flag_suspended, flag_last_chance_login

    def update_suspend_file(self, type_user, username, flag_last_chance_login):
        # Fetch out suspend reason, last chance login decrease 1
        df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
        df_suspend_user = df_suspend[df_suspend['Type_user'] == type_user]
        df_user_row = df_suspend_user[df_suspend_user['Username'] == username]
        SuspendReason = df_user_row['Suspend_reason'].iloc[-1]
        CurrentWarning = df_user_row['Current_warnings'].iloc[-1]
        if flag_last_chance_login:
            df_suspend.loc[df_suspend['Username'] == username, 'Chance_login'] = 0
            df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
        return CurrentWarning, SuspendReason