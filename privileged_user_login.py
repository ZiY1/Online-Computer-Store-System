import tkinter as tk  
import tkinter.ttk as ttk 

import pandas as pd 
import numpy as np 

# python files
import main as home
import computer_management_page

class privilaged_user_login(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master )
        self.master.title( "Privilaged user login page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )

        self.create_widgets()



    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()

        #------------------Title-------------------------------------------
        self.style.configure("LabelTitle.TLabel", font=("Helvetica", 26),background = '#49A')
        self.LabelTitle = tk.ttk.Label(self.top, text="Login As: ", 
                                        style="LabelTitle.TLabel", anchor = "center")
        self.LabelTitle.place(relx=0.01, rely=0.024, relwidth=0.632, relheight=0.17)
    
        self.LabelTitle2 = tk.ttk.Label(self.top, text = "Manager", style = "LabelTitle.TLabel")
        self.LabelTitle2.place( relx = 0.38, rely = 0.024, relwidth = 0.632, relheight = 0.17)
        #-------------------------------------------------------------------------------------







        #---------------------Radio Buttons------------------------------------------------
        
        self.RadioVar = tk.IntVar()
        self.RadioVar.set(3)
        self.RadioButton0 = tk.Radiobutton(self.top, variable=self.RadioVar, value=0, 
                                            text="I am from Computer Company", 
                                        command=lambda: self.radio_clicked(self.RadioVar.get()))
        self.RadioButton0.place(relx=0.35, rely=0.215, relwidth=0.350, relheight=0.08)

        self.RadioButton1 = tk.Radiobutton(self.top, variable=self.RadioVar, 
                                        value=1, text="I am from Delivery Company", 
                                        command=lambda: self.radio_clicked(self.RadioVar.get()))
        self.RadioButton1.place( relx=0.35, rely=0.290, relwidth=0.350, relheight= 0.08)
        
        self.RadioButton2 = tk.Radiobutton(self.top, variable=self.RadioVar, value=2, 
                                        text="I am a Store Clerk", 
                                    command=lambda: self.radio_clicked(self.RadioVar.get()))
        self.RadioButton2.place(relx=0.70, rely=0.215, relwidth=0.350, relheight= 0.08)

        self.RadioButton3 = tk.Radiobutton(self.top, variable=self.RadioVar, value=3, 
                                        text="I am a Manager", 
                                        command=lambda: self.radio_clicked(self.RadioVar.get()))
        self.RadioButton3.place(relx=0.70, rely=0.290, relwidth=0.350, relheight= 0.08)

        #-------------------------------------------------------------------------------------------

        
		#-------------------------------User name----------------------------------------------
        self.TextNameVar = tk.StringVar()
        self.TextUserName = tk.Entry(self.top, textvariable=self.TextNameVar)
        self.TextUserName.place(relx=0.350, rely=0.430, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelName.TLabel", font=("Helvetica", 16), 
                                background = '#49A' )
        self.LabelUserName = tk.ttk.Label(self.top, text="User name: ",
                                    style="LabelName.TLabel", anchor = "center")
        self.LabelUserName.place(relx=0.08, rely=0.410, relwidth=0.250, relheight=0.125)
        #---------------------------------------------------------------------------------------

        
		#-------------------------Password---------------------------------------------------
        self.TextPasswordVar = tk.StringVar()
        self.TextPassword = tk.ttk.Entry(self.top, textvariable=self.TextPasswordVar, show="*")
        self.TextPassword.place(relx=0.350, rely=0.560, relwidth=0.550, relheight=0.080)

        self.style.configure("LabelPassword.TLabel", font=("Helvetica", 16), background = '#49A')
        self.LabelPassword = tk.ttk.Label(self.top, text="Password: ", 
                                        style="LabelPassword.TLabel", anchor = "center")
        self.LabelPassword.place(relx=0.08, rely=0.540, relwidth=0.250, relheight=0.125)
        #-------------------------------------------------------------------------------------

        
        
		#------------------------------Login Button-------------------------------------------
        self.style.configure("CommandLogin.TButton", anchor="center",font=("Helvetica", 16),
                                     background = "green", foreground = "black")
        self.CommandLogin = tk.ttk.Button(self.top, text="Login", 
                                    command=self.command_login, style="CommandLogin.TButton")
        self.CommandLogin.place(relx=0.450, rely=0.700, relwidth=0.200, relheight=0.095)
        #--------------------------------------------------------------------------------------

		#---------------------------------Back-------------------------------------------------
        self.style.configure("CommandBack.TButton", font=('Helvetica',16), 
                                  background = "green", foreground = "black")
        self.CommandBack = tk.ttk.Button(self.top, text="Back", command=self.command_back, 
                                    style="CommandBack.TButton")
        self.CommandBack.place(relx=0.796, rely=0.90, relwidth=0.190, relheight=0.083)
        #--------------------------------------------------------------------------------------


    def radio_clicked(self, value):
        if value == 0:
            self.iden = "Computer Company"
        elif value == 1:
            self.iden = "Delivery Company"
        elif value == 2:
            self.iden = "Store Clerk"
        else:
            self.iden = "Manager"

        self.style.configure("LabelTitle.TLabel", font=("Helvetica", 26))
        self.LabelTitle = tk.ttk.Label(self.top, text=self.iden, style="LabelTitle.TLabel")
        self.LabelTitle.place(relx=0.38, rely=0.024, relwidth=0.632, relheight=0.17)



		



    def command_login(self, event = None):

        df = pd.read_excel( "csv_files/privileged_users.xlsx" )
        UserName = self.TextUserName.get()
        Password = self.TextPassword.get()

        if self.RadioVar.get() == 0: # for computer companies
            #\-self.computer_login()
            df_computer_companies = df[ df['Type_user'] == 'computer_company' ]

            #----Verify if the credentials are correct-------------
            flag_user_valid, flag_pass_valid= self.verify_access(df_computer_companies, 
                                                        UserName, Password) 
            #------------------------------------------------------
            

            if flag_user_valid and flag_pass_valid: 
                self.top.destroy()
                computer_management_page.computer_management_page()
            else:
                tk.messagebox.showerror( "Error", "Invalid username and password" )


        elif self.RadioVar.get() == 1: # for delivery companies
            #\-self.delivery_login()
            df_delivery_companies = df[ df['Type_user'] == 'delivery' ]

            #----Verify if the credentials are correct-------------
            flag_user_valid, flag_pass_valid= self.verify_access(df_delivery_companies, 
                                                        UserName, Password) 
            #------------------------------------------------------

            if flag_user_valid and flag_pass_valid: 
                pass
            else:
                tk.messagebox.showerror( "Error", "Invalid username and password" )


        elif self.RadioVar.get() == 2: # for the clerk staff
            #\-self.clerk_login()
            df_clerks = df[ df.Type_user == 'clerk' ]

            #----Verify if the credentials are correct-------------
            flag_user_valid, flag_pass_valid= self.verify_access(df_clerks, 
                                                        UserName, Password) 
            #------------------------------------------------------

            if flag_user_valid and flag_pass_valid: 
                pass
            else:
                tk.messagebox.showerror( "Error", "Invalid username and password" )


        else: # for the super manager
            #\-self.manager_login()
            df_admin = df[ df['Type_user'] == 'Super user' ]

            #----Verify if the credentials are correct-------------------------
            flag_user_valid, flag_pass_valid= self.verify_access(df_admin, 
                                                        UserName, Password) 
            #------------------------------------------------------------------

            if flag_user_valid and flag_pass_valid: 
                pass
            else:
                tk.messagebox.showerror( "Error", "Invalid username and password" )




    def verify_access(self, df, username, password): 
        if username in list( df['Username'] ):
            flag_valid_username = True
        else:
            flag_valid_username = False 

        if password in list(df['Password']):
            flag_valid_password = True 
        else:
            flag_valid_password = False

        return flag_valid_username, flag_valid_password



    def command_back(self):
        self.top.destroy()
        home.HomePage()





