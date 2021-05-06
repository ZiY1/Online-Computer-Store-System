import tkinter as tk 
import tkinter.ttk as ttk 

import re   # used for checking if a string input follows a given format
import numpy as np
import pandas as pd

# python files
import provide_credit_card 
from tkinter.messagebox import askyesno

import warnings
warnings.filterwarnings("ignore")

class add_funds(tk.Frame):

    def __init__(self, customer_name, customer_Id, customer_username,
                master = None):
        tk.Frame.__init__(self,master) 
        self.master.title("Add funds Page")
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
                                        text = "Add Funds to your credit card account", 
                                        style =  "LabelTitle.TLabel"  
                                      )
        self.LabelTitle.place( relx = 0.205, rely = 0.03, 
                               relwidth = 0.632, relheight = 0.15
                            )
        #------------------------------------------------------------------------------------------

        #------------------------Add funds Section------------------------------------------- 
        self.AddfundsVar = tk.StringVar()
        self.Addfunds = tk.Entry( self.top, textvariable = self.AddfundsVar ) 
        self.Addfunds.place( relx = 0.370, rely = 0.32, relwidth = 0.3, relheight = 0.080)

        
        self.style.configure( "Labelmoney.TLabel", font = ("Bold", 18), 
         background = "light blue")
        self.money_sign = tk.ttk.Label( self.top, text = "$", 
        style = "Labelmoney.TLabel" ,anchor = "w")
        self.money_sign.place( relx = 0.345, rely = 0.355, relwidth = 0.015, relheight = 0.05)


        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = 'light blue'   )

        self.LabelTitle = tk.ttk.Label(self.top, text = "Add funds: ", 
                                        style="LabelName.TLabel", anchor = "center")

        self.LabelTitle.place(  relx = 0.26, rely = 0.355, relwidth=0.08, relheight=0.05)
		#----------------------------------------------------------------------------------------


        #--------------------------Confirm Button---------------------------------------
        self.style.configure("Command.TButton", anchor="center", font=("Helvetica", 16),
                               background = "green", foreground = "black" )
        self.Confirm_Button = tk.ttk.Button(self.top, text = "Confirm", 
                        command = self.command_confirm, style = "Command.TButton")
		
        self.Confirm_Button.place(relx = 0.38, rely = 0.45, relwidth = 0.07, relheight=0.05)

        #-----------------------------------------------------------------------------------------


        #-----------------------See my Current Balance-------------------------------------
        
        self.style.configure( "Labelmoney2.TLabel", font = ("Bold", 18), 
         background = "light blue")
        self.money_sign2 = tk.ttk.Label( self.top, text = "$", 
        style = "Labelmoney2.TLabel" ,anchor = "w")
        self.money_sign2.place( relx = 0.345, rely = 0.255, relwidth = 0.015, relheight = 0.05)


        self.style.configure("LabelName.TLabel", font = ("Helvetica", 16),
                                                            background = 'light blue'   )

        self.Label_balance = tk.ttk.Label(self.top, text = "Current Balance: ", 
                                        style="LabelName.TLabel", anchor = "center")

        self.Label_balance.place(  relx = 0.22, rely = 0.255, relwidth=0.125, relheight=0.05)
		
        df = pd.read_excel( "csv_files/registered_customers.xlsx" )
        df_user_info = df[ df['Username'] == self.customer_username ]
        current_balance = float (df_user_info['Balance'].iloc[-1] )
        current_balance = "{:,.2f}".format(current_balance)

        self.style.configure("LabelName2.TLabel", font = ("Helvetica", 16),
                                                            background = 'white'   )


        self.current_balance = tk.ttk.Label(self.top, text = f"{current_balance:} ", 
                                        style="LabelName2.TLabel", anchor = "w")

        self.current_balance.place( relx = 0.370, rely = 0.22, relwidth = 0.3, relheight = 0.080)
		
        #----------------------------------------------------------------------------------




        #------------------------- Go Back Section---------------------------------
        self.style.configure("CommandBack.TButton", anchor="center", font=("Helvetica", 16),
                                    background = "green", foreground= "black" )
        self.Back_Button = tk.ttk.Button(self.top, text = "Back", 
                    command=self.command_back, style="CommandBack.TButton")
		
        self.Back_Button.place(relx = 0.85, rely = 0.12, relwidth = 0.1, relheight = 0.05)
        #------------------------------------------------------------------------------------


    def command_confirm(self):
        if askyesno("Confirm", "Are you sure you want to add funds to your account?"):           
            
            Amount = self.Addfunds.get()
            flag_invalid = False

            if len( Amount.split(".") ) == 2:
                if len(Amount.split(".")[1]) != 2: # We need the format $ X.XX e.g 3.03 3.16 3.00
                    flag_invalid = True   
            else: # The user did not provide the cent part
                flag_invalid = True             

            try: 
                Amount = float(Amount)
                if Amount < 0: # We are not adding negative numbers to fund balance
                    flag_invalid = True
            except:
                flag_invalid = True

            if flag_invalid:
                tk.messagebox.showerror( "Error", 
                   message = "Invalid input provided.\n" +
                   "Try an input which follows the currency format 0.00" )
            else:
                df = pd.read_excel( "csv_files/registered_customers.xlsx" )
                df_user_info = df[df['Username'] == self.customer_username]
                df_user_info['Balance'].iloc[-1] += Amount

                df[ df['Username'] == self.customer_username] = df_user_info

                df.to_excel( "csv_files/registered_customers.xlsx", index = False)
                
                tk.messagebox.showinfo( "Success",
                    "Funds had been added to your account" )

                #-----------------------See my Current Balance-------------------------------------
        
                self.style.configure( "Labelmoney2.TLabel", font = ("Bold", 18), 
                background = "light blue")
                self.money_sign2 = tk.ttk.Label( self.top, text = "$", 
                style = "Labelmoney2.TLabel" ,anchor = "w")
                self.money_sign2.place( relx = 0.345, rely = 0.255, relwidth = 0.015, relheight = 0.05)


                self.style.configure("LabelName3.TLabel", font = ("Helvetica", 16),
                                                                    background = 'light blue'   )

                self.Label_balance = tk.ttk.Label(self.top, text = "Current Balance: ", 
                                                style="LabelName3.TLabel", anchor = "center")

                self.Label_balance.place(  relx = 0.22, rely = 0.255, relwidth= 0.125, relheight= 0.05)
                
                self.style.configure("LabelName4.TLabel", font = ("Helvetica", 16),
                                                                    background = 'white'   )
                
                df = pd.read_excel( "csv_files/registered_customers.xlsx" )
                df_user_info = df[ df['Username'] == self.customer_username ]
                current_balance = round( float(df_user_info['Balance'].iloc[-1] ),2)
                current_balance = "{:,.2f}".format(current_balance)
                self.current_balance = tk.ttk.Label(self.top, text = f"{current_balance} ", 
                                                style="LabelName4.TLabel", anchor = "w")

                self.current_balance.place( relx = 0.370, rely = 0.22, relwidth = 0.3, relheight = 0.080)
                
                #----------------------------------------------------------------------------------


        

            
    def command_back(self):
        self.top.destroy()
        provide_credit_card.provide_credit_card( customer_name = self.customer_name, 
                    customer_Id = self.customer_Id, 
                    customer_username = self.customer_username)        
