import tkinter as tk  
import tkinter.ttk as ttk 

import pandas as pd 
import numpy as np 

# python files
import main as home
import manager_management_page as manager_page
import clerk_management_page as clerk_page
import delivery_company_management_page as delivery_page
import computer_company_management_page as cc_page
class privilaged_user_login(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master )
        self.master.title( "Privilaged user login page" )
        self.master.geometry( "550x450" )
        self.master.configure( background = "light blue" )

        self.create_widgets()



    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()

        # Title
        self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, font=("Helvetica", 26),background = '#49A')
        self.LabelTitle = tk.ttk.Label(self.top, text="Login As: Manager", 
                                        style="LabelTitle.TLabel")
        self.LabelTitle.place(relx=0.085, rely=0.024, relwidth=0.85, relheight=0.155)
    
        # self.LabelTitle2 = tk.ttk.Label(self.top, text = "Manager", style = "LabelTitle.TLabel")
        # self.LabelTitle2.place(relx=0.38, rely=0.024, relwidth=0.57, relheight=0.18)

        # Radio Buttons
        self.RadioVar = tk.IntVar()
        self.RadioVar.set(3)
        self.RadioButton0 = tk.Radiobutton(self.top, variable=self.RadioVar, value=0, 
                                            text="I am from Computer Company", 
                                        command=lambda: self.radio_clicked(self.RadioVar.get()), background = 'light blue')
        self.RadioButton0.place(relx=0.2, rely=0.215)

        self.RadioButton1 = tk.Radiobutton(self.top, variable=self.RadioVar, 
                                        value=1, text="I am from Delivery Company", 
                                        command=lambda: self.radio_clicked(self.RadioVar.get()), background = 'light blue')
        self.RadioButton1.place(relx=0.55, rely=0.215)
        
        self.RadioButton2 = tk.Radiobutton(self.top, variable=self.RadioVar, value=2, 
                                        text="I am a Store Clerk", 
                                    command=lambda: self.radio_clicked(self.RadioVar.get()), background = 'light blue')
        self.RadioButton2.place(relx=0.2, rely=0.290)

        self.RadioButton3 = tk.Radiobutton(self.top, variable=self.RadioVar, value=3, 
                                        text="I am a Manager",
                                        command=lambda: self.radio_clicked(self.RadioVar.get()), background = 'light blue')
        self.RadioButton3.place(relx=0.55, rely=0.290)

        
		# Username
        self.TextNameVar = tk.StringVar()
        self.TextUserName = tk.Entry(self.top, textvariable=self.TextNameVar)
        self.TextUserName.place(relx=0.350, rely=0.430, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelName.TLabel", font=("Helvetica", 16), 
                                background = 'light blue' )
        self.LabelUserName = tk.ttk.Label(self.top, text="User name: ",
                                    style="LabelName.TLabel", anchor = "center")
        self.LabelUserName.place(relx=0.08, rely=0.410, relwidth=0.250, relheight=0.125)

        
		# Password
        self.TextPasswordVar = tk.StringVar()
        self.TextPassword = tk.ttk.Entry(self.top, textvariable=self.TextPasswordVar, show="*")
        self.TextPassword.place(relx=0.350, rely=0.560, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelPassword.TLabel", font=("Helvetica", 16), background = 'light blue')
        self.LabelPassword = tk.ttk.Label(self.top, text="Password: ", 
                                        style="LabelPassword.TLabel", anchor = "center")
        self.LabelPassword.place(relx=0.08, rely=0.540, relwidth=0.250, relheight=0.125)       
        
		# Login Button
        self.style.configure("CommandLogin.TButton", anchor="center",font=("Helvetica", 16))
        self.CommandLogin = tk.ttk.Button(self.top, text="Login", 
                                    command=self.command_login, style="CommandLogin.TButton")
        self.CommandLogin.place(relx=0.410, rely=0.700, relwidth=0.200, relheight=0.095)

		# Back
        self.style.configure("CommandBack.TButton", font=('Helvetica',16))
        self.CommandBack = tk.ttk.Button(self.top, text="Back", command=self.command_back, 
                                    style="CommandBack.TButton")
        self.CommandBack.place(relx=0.796, rely=0.90, relwidth=0.190, relheight=0.083)

    def radio_clicked(self,value):
        if value == 0:
            self.iden = "Login As: Computer Company"
        elif value == 1:
            self.iden = "Login As: Delivery Company"
        elif value == 2:
            self.iden = "Login As: Store Clerk"
        else:
            self.iden = "Login As: Manager"

        self.style.configure("LabelTitle.TLabel", font=("Helvetica", 26))
        self.LabelTitle = tk.ttk.Label(self.top, text = self.iden, style="LabelTitle.TLabel")
        self.LabelTitle.place(relx=0.085, rely=0.024, relwidth=0.85, relheight=0.155)

		
    def command_login(self, event = None):

        df = pd.read_excel( "csv_files/privileged_users.xlsx" )
        df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
        UserName = self.TextUserName.get().lower()
        Password = str(self.TextPassword.get())

        if self.RadioVar.get() == 0: # for computer companies
            type_user = 'computer_company'
            # check if suspended
            flag_suspended, flag_last_chance_login = self.is_suspended(type_user, UserName)

            if (not flag_suspended):
                df_computer_companies = df[ df['Type_user'] == type_user ]
                # Verify if the credentials are correct
                flag_user_valid, flag_pass_valid= self.verify_access(df_computer_companies, 
                                                        UserName, Password) 

                if flag_user_valid and flag_pass_valid:
                    df_computer_row = df_computer_companies[df_computer_companies['Username'] == UserName]
                    CCName = df_computer_row['Name'].iloc[-1]
                    self.top.destroy()
                    cc_page.computer_company_management_page(CCName, UserName)
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )
            else:
                df_computer_companies = df_suspend[ df_suspend['Type_user'] == type_user ]
                #----Verify if the credentials are correct-------------
                flag_user_valid, flag_pass_valid= self.verify_access(df_computer_companies, 
                                                        UserName, Password) 
                #------------------------------------------------------
                if flag_user_valid and flag_pass_valid and flag_last_chance_login:
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showwarning( "Info", "Your account is suspended, you have one last chance to login and clean up your account\n" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
                    df_computer_row = df_computer_companies[df_computer_companies['Username'] == UserName]
                    CCName = df_computer_row['Name'].iloc[-1]
                    self.top.destroy()
                    cc_page.computer_company_management_page(CCName, UserName)
                elif flag_user_valid and flag_pass_valid and (not flag_last_chance_login):
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showerror( "error", "Your account is suspended, you cannot login anymore" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )


        elif self.RadioVar.get() == 1: # for delivery companies
            type_user = 'delivery'
            #-------check if suspended-----------------------------------------------------
            flag_suspended, flag_last_chance_login = self.is_suspended(type_user, UserName)
            #------------------------------------------------------------------------------

            if (not flag_suspended):
                df_delivery_companies = df[ df['Type_user'] == type_user ]
                #----Verify if the credentials are correct-------------
                flag_user_valid, flag_pass_valid= self.verify_access(df_delivery_companies, 
                                                        UserName, Password) 
                #------------------------------------------------------
                if flag_user_valid and flag_pass_valid:
                    df_delivery_row = df_delivery_companies[df_delivery_companies['Username'] == UserName]
                    DeliveryName = df_delivery_row['Name'].iloc[-1]
                    self.top.destroy()
                    delivery_page.delivery_company_management_page(DeliveryName, UserName)
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )
            else:
                df_delivery_companies = df_suspend[ df_suspend['Type_user'] == type_user ]
                #----Verify if the credentials are correct-------------
                flag_user_valid, flag_pass_valid= self.verify_access(df_delivery_companies, 
                                                        UserName, Password) 
                #------------------------------------------------------
                if flag_user_valid and flag_pass_valid and flag_last_chance_login:
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showwarning( "Info", "Your account is suspended, you have one last chance to login and clean up your account\n" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
                    df_delivery_row = df_delivery_companies[df_delivery_companies['Username'] == UserName]
                    DeliveryName = df_delivery_row['Name'].iloc[-1]
                    self.top.destroy()
                    delivery_page.delivery_company_management_page(DeliveryName, UserName)
                elif flag_user_valid and flag_pass_valid and (not flag_last_chance_login):
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showerror( "error", "Your account is suspended, you cannot login anymore" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )


        elif self.RadioVar.get() == 2: # for the clerk staff
            type_user = 'clerk'
            #-------check if suspended-----------------------------------------------------
            flag_suspended, flag_last_chance_login = self.is_suspended(type_user, UserName)
            #------------------------------------------------------------------------------

            if (not flag_suspended):
                df_clerks = df[ df['Type_user'] == type_user ]
                #----Verify if the credentials are correct-------------
                flag_user_valid, flag_pass_valid= self.verify_access(df_clerks, 
                                                        UserName, Password) 
                #------------------------------------------------------
                if flag_user_valid and flag_pass_valid: 
                    df_clerk_row = df_clerks[df_clerks['Username'] == UserName]
                    ClerkName = df_clerk_row['Name'].iloc[-1] 
                    self.top.destroy()
                    clerk_page.clerk_management_page(ClerkName, UserName)
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )
            else:
                df_clerks = df_suspend[ df_suspend['Type_user'] == type_user ]
                #----Verify if the credentials are correct-------------
                flag_user_valid, flag_pass_valid= self.verify_access(df_clerks, 
                                                        UserName, Password) 
                #------------------------------------------------------
                if flag_user_valid and flag_pass_valid and flag_last_chance_login:
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showwarning( "Info", "Your account is suspended, you have one last chance to login and clean up your account\n" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
    
                    df_clerk_row = df_clerks[df_clerks['Username'] == UserName]
                    ClerkName = df_clerk_row['Name'].iloc[-1]
                    self.top.destroy() 
                    clerk_page.clerk_management_page(ClerkName, UserName)
                elif flag_user_valid and flag_pass_valid and (not flag_last_chance_login):
                    CurrentWarning, SuspenReason = self.update_suspend_file(type_user, UserName, flag_last_chance_login)
                    tk.messagebox.showerror( "error", "Your account is suspended, you cannot login anymore" 
                                            + "\nCurrent Warning: " + str(CurrentWarning)
                                            + "\nSuspend Justification: " + str(SuspenReason))
                else:
                    tk.messagebox.showerror( "Error", "Invalid username and password" )


        else: # for the super manager
            df_admin = df[ df['Type_user'] == 'Super user' ]

            #----Verify if the credentials are correct-------------------------
            flag_user_valid, flag_pass_valid= self.verify_access(df_admin, 
                                                        UserName, Password) 
            #------------------------------------------------------------------

            if flag_user_valid and flag_pass_valid: 
                self.top.destroy()
                Admin_Name = df_admin['Name'].iloc[-1]
                Admin_Username = df_admin['Username'].iloc[-1]
                #Admin_Password = df_admin['Password'].iloc[-1]
                manager_page.manager_management_page(Admin_Name, Admin_Username)
            else:
                tk.messagebox.showerror( "Error", "Invalid username and password" )




    def verify_access(self, df, username, password): 
        flag_valid_username = False
        flag_valid_password = False
        if username in list( df['Username'] ):
            flag_valid_username = True
            df_user_row = df[df['Username'] == username]
            user_password = str(df_user_row['Password'].iloc[-1])
            if user_password == password:
                flag_valid_password = True
        return flag_valid_username, flag_valid_password


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


    def command_back(self):
        self.top.destroy()
        home.HomePage()


# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    privilaged_user_login(top).mainloop()    


