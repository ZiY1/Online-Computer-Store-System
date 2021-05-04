import tkinter as tk  
import tkinter.ttk as ttk 

from PIL import ImageTk, Image
import pandas as pd 
import numpy as np 

# python scripts 
import setting_account

class account_info_page(tk.Frame):
    
    def __init__( self, customer_name, customer_Id, customer_username, master = None ): #customer_name, customer_Id, customer_username ,
        tk.Frame.__init__(self, master) 
        self.master.title( "Account Info Page" )
        self.master.geometry( "989x676" )
        self.master.configure( background = "light blue" )
      
        
        # User account info 
        self.Customer_Name = customer_name
        self.Customer_username = customer_username 
        self.Customer_Id = customer_Id

        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()    # Style
        
        #---------------------------------Title----------------------------------------
        self.style.configure( 
                            "LabelTitle.TLabel", 
                            relief = tk.SUNKEN,
                            anchor = "center", 
                            font = ("Helvetica", 23),
                            background = '#49A',
                            foreground = "black" 
                     )
        self.LabelTitle =  tk.ttk.Label( self.top, 
                                      text = "Account Info", 
                                      style = "LabelTitle.TLabel"        
                                    )   
        self.LabelTitle.place( relx = 0.26, rely = 0.035, relwidth = 0.49, relheight = 0.085 )
        #----------------------------------------------------------------------------------

        df_customers = pd.read_excel("csv_files/registered_customers.xlsx")

        df_user_info = df_customers[ df_customers["Username"] == self.Customer_username]

        user_ID = df_user_info["ID"].iloc[-1]
        user_Name = df_user_info["Name"].iloc[-1]
        user_Username = df_user_info["Username"].iloc[-1]
        user_Password = df_user_info["Password"].iloc[-1]
        user_credit_card = "Not available" if df_user_info["Credit card account"].iloc[-1] == "empty" else df_user_info["Credit card account"].iloc[-1]
        user_balance =  "{:,.2f}".format(df_user_info["Balance"].iloc[-1])
        user_balance = "$ " + user_balance
        user_address = "Not available" if df_user_info["Home Address"].iloc[-1] == "empty" else df_user_info["Home Address"].iloc[-1]
        user_warnings = df_user_info["Warnings"].iloc[-1]
        

        self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",20, "bold"), background = "light blue")
        self.style.configure("LabelContent.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")

        Label_names = ["Customer Id", "Customer Name", "Customer Username", "Password", "Credit card account", "Current Balance", "Home Address", "Warnings"]
        Label_content = [user_ID, user_Name, user_Username, user_Password,user_credit_card, user_balance, user_address, user_warnings]
        self.Labels = list()
        self.Labels_content = list()
        plus_rely = 0
        
        for i in range(len(Label_names)):
            self.Labels.append(None)
            self.Labels[i] =  tk.ttk.Label( self.top, 
                                        text = f"{Label_names[i]}:", 
                                        style = "LabelHeadline.TLabel"        
                                        )   
            self.Labels[i].place( relx = 0.3, rely = 0.135 + plus_rely, relwidth = 0.49, relheight = 0.085 )
            
            self.Labels_content.append(None)
            self.Labels_content[i] =  tk.ttk.Label( self.top, 
                                        text = f"{Label_content[i]}", 
                                        style = "LabelContent.TLabel"        
                                        )   
            self.Labels_content[i].place( relx = 0.6, rely = 0.135 + plus_rely, relwidth = 0.49, relheight = 0.085 )
            
            plus_rely += 0.10
            
        


    #---------------------------Go Back Button---------------------------------------
        self.style.configure( "Command_Go_Back.TButton", font = ("Helvetica", 16),
                                background = "green",   foreground = "black" )
        self.CommandExit = tk.ttk.Button(  self.top, 
                                       text = "Back",
                                       command = self.Command_Go_Back,
                                       style = "Command_Go_Back.TButton" 
        )
        self.CommandExit.place( relx = 0.86, rely = 0.92, relwidth = 0.119, relheight = 0.065)
    #---------------------------------------------------------------------------------


    def Command_Go_Back(self):
        self.top.destroy()
        setting_account.setting_account(customer_name = self.Customer_Name,  
        customer_username = self.Customer_username, customer_Id = self.Customer_Id)
