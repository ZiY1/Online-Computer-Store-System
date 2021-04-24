import tkinter as tk 
import tkinter.ttk as ttk 

import re   # used for checking if a string input follows a given format
import numpy as np
import pandas as pd

import credit_card_checker # used for checking a credit card number is valid

# python files
import setting_account
import add_funds 

import warnings
warnings.filterwarnings("ignore")

class provide_credit_card(tk.Frame):

    def __init__(self, customer_name, customer_Id, customer_username,
                master = None):
        tk.Frame.__init__(self,master) 
        self.master.title("Credit Card Page")
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        
        self.customer_name = customer_name
        self.customer_username = customer_username 
        self.customer_Id = customer_Id

        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel() 
        self.style = tk.ttk.Style()
     
        #--------------------------------Title--------------------------------------------------- 
        self.style.configure( "LabelTitle.TLabel", 
                               anchor = "center", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "Add a credit or debit card", 
                                        style =  "LabelTitle.TLabel"  
                                      )
        self.LabelTitle.place( relx = 0.205, rely = 0.03, 
                               relwidth = 0.632, relheight = 0.15
                            )
        #------------------------------------------------------------------------------------------

        #----------------------------Card Number Section------------------------------------------- 
        self.CardnumberVar = tk.StringVar()
        self.Cardnumber = tk.Entry( self.top, textvariable = self.CardnumberVar) 
        self.Cardnumber.place( relx = 0.350, rely = 0.22, relwidth = 0.3, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Card Number: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely = 0.2, relwidth=0.250, relheight=0.125)
		#----------------------------------------------------------------------------------------


        #-----------------------------Name on Card Section---------------------------------------- 
        self.CardName = tk.StringVar()
        self.TextName =  tk.Entry( self.top, textvariable = self.CardName ) 
        self.TextName.place( relx=0.350, rely = 0.380, relwidth = 0.3, relheight=0.080 )

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Name on Card: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely = 0.360, relwidth=0.250, relheight=0.125 )
		#------------------------------------------------------------------------------------------

        #---------------------------Expiration Date Section---------------------------------------- 
        month_options = ["",'01','02','03','04','05','06','07','08','09','10','11','12']
        year_options = ["",'2022','2023','2024','2025','2026','2027','2028','2029','2030']


        self.Exp_MonthVar = tk.StringVar()
        self.Exp_MonthVar.set(month_options[0])
        self.Exp_Month = tk.OptionMenu(self.top, self.Exp_MonthVar, *month_options) 
        self.Exp_Month.place( relx = 0.350, rely = 0.54, relwidth = 0.1, relheight = 0.080)

        self.Exp_YearVar = tk.StringVar()
        self.Exp_YearVar.set( year_options[0])
        self.Exp_Year = tk.OptionMenu(self.top, self.Exp_YearVar, *year_options) 
        self.Exp_Year.place( relx = 0.47, rely = 0.54, relwidth = 0.1, relheight = 0.080)

        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = '#49A'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Expiration Date: ", 
                                        style="LabelName.TLabel", anchor = "center")
        self.LabelTitle.place(  relx=0.08, rely = 0.52, relwidth=0.250, relheight=0.125)
        #------------------------------------------------------------------------------------------


        #--------------------------Add your card info Button---------------------------------------
        self.style.configure("Command.TButton", anchor="center", font=("Helvetica", 16),
                               background = "green", foreground = "black" )
        self.CommandSignUp = tk.ttk.Button(self.top, text = "Add your card", 
                        command = self.command_add_card, style = "Command.TButton")
		
        self.CommandSignUp.place(relx = 0.35, rely = 0.65, relwidth = 0.13, relheight=0.05)

        #-----------------------------------------------------------------------------------------

        #--------------------------Add funds to account-------------------------------------------
        self.style.configure("Command.TButton", anchor="center", font=("Helvetica", 16),
                               background = "green", foreground = "black" )
        self.Command_addFunds = tk.ttk.Button(self.top, text = "Add Funds to account", 
                        command = self.command_add_funds, style = "Command.TButton")
		
        self.Command_addFunds.place(relx = 0.55, rely = 0.65, relwidth = 0.18, relheight=0.05)
        
        #-----------------------------------------------------------------------------------------


        #------------------------- Go Back to Main Page Customer---------------------------------
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16),
                                    background = "green", foreground= "black" )
        self.CommandBack = tk.ttk.Button(self.top, text = "Back", 
                                command=self.command_back, style="CommandBack.TButton")
		
        self.CommandBack.place(relx = 0.85, rely = 0.12, relwidth = 0.1, relheight = 0.05)
        #------------------------------------------------------------------------------------


    def command_add_card(self):
        
        Card_No = self.Cardnumber.get()
        Name = self.TextName.get()
        Exp_Month = self.Exp_MonthVar.get() 
        Exp_Year = self.Exp_YearVar.get() 

        
        #-----------------------Check if the Name is valid-------------------

        regex_name = "[a-zA-Z]+[\s][a-zA-Z]+[-\']?[a-zA-Z]+"
        regex_name2 = "[a-zA-Z]+[\s][a-zA-Z]+[-\']?[a-zA-Z]+[\s][a-zA-Z]+"
        if(  re.fullmatch(regex_name, Name) or re.fullmatch(regex_name2,Name) ):
            flag_valid_name = True
            Name = Name.lower().title()
        else:
            flag_valid_name = False
            tk.messagebox.showerror( "Error", "invalid Name" )

        #-------------------------------------------------------------------

        #----------------------Check if the Expiration Date is valid---------
        if Exp_Month == "" or Exp_Year == "":
            flag_valid_exp_date = False
            tk.messagebox.showerror( "Error", "invalid Expiration Date")
        else:
            flag_valid_exp_date = True

        #-------------------------------------------------------------------

        #----------------Check if credit card number is valid--------------------- 
        Card_No = Card_No.strip()
        flag_valid_credit_card = credit_card_checker.CreditCardChecker( Card_No).valid()

        if not flag_valid_credit_card:
            tk.messagebox.showerror("Error", "invalid credit card number")

        #-------------------------------------------------------------------------


        if flag_valid_name and flag_valid_exp_date and flag_valid_credit_card:

            # Modify the excel file by adding the credit card number        
            df = pd.read_excel( "csv_files/registered_customers.xlsx" )
            df_user_info = df[df['Username'] == self.customer_username]



            #---------------Check if the credit card number is not repeated-----------
            
            Card = Card_No.replace(" ", "")

            flag_duplicate_credit_card = False
            flag_already_linked = False
            for i in range( len(df)):
                card_checked = df['Credit card account'].iloc[i].replace( " ", "" )
                if df['Username'].iloc[i] != self.customer_username and Card == card_checked:
                    flag_duplicate_credit_card = True

                if df['Username'].iloc[i] == self.customer_username and Card == card_checked:
                    flag_already_linked = True


            if flag_already_linked:  #df_user_info['Credit card account'].iloc[-1] == Card_No:
                tk.messagebox.showerror( "Error", 
                    "the credit card provided is already linked to your account" )
            elif flag_duplicate_credit_card:
                tk.messagebox.showerror( "Error", 
                 "the credit card provided belongs to another user in the system")
            elif df_user_info['Credit card account'].iloc[-1] != "empty":

                if tk.messagebox.askyesno(title = "Warning", 
                   message = "You already have a credit card linked to your account.\n" + 
                   "Do you want to update your credit card account?\n" + 
                   "Your current funds will reset to $0.00"):
                   df_user_info.loc[:,('Credit card account')] = str(Card_No)
                   df_user_info.loc[:, ('Balance') ] = float(0.00)
                   df[ df['Username'] == self.customer_username] = df_user_info
                   df.to_excel( "csv_files/registered_customers.xlsx", index = False)
                
                    # send the okay to the user of the system
                   tk.messagebox.showinfo("Success", 
                                        "Your credit card info has been updated" )

            else:
                df_user_info.loc[:,('Credit card account')] = str(Card_No)
                df[ df['Username'] == self.customer_username] = df_user_info
                df.to_excel( "csv_files/registered_customers.xlsx", index = False)
                
                # send the okay to the user of the system
                tk.messagebox.showinfo("Success", 
                                    "Your credit card info has been updated" )


    def command_add_funds(self):
        
        df = pd.read_excel( "csv_files/registered_customers.xlsx" )
        df_user_info = df[df['Username'] == self.customer_username]
        
        user_card = str(df_user_info['Credit card account'].iloc[-1] ) 
        
          
        if user_card == "empty":
            tk.messagebox.showerror( "Error",
                "There is no credit card linked to your account" )  
        else:
            self.top.destroy()
            add_funds.add_funds( customer_name = self.customer_name,
              customer_Id = self.customer_Id,
              customer_username = self.customer_username )



            
    def command_back(self):
        self.top.destroy()
        
        setting_account.setting_account( customer_name = self.customer_name, 
                    customer_Id = self.customer_Id, 
                    customer_username = self.customer_username)        
