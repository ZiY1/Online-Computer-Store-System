import tkinter as tk  
import tkinter.ttk as ttk 

from PIL import ImageTk, Image
import pandas as pd 
import numpy as np 
import re

# python scripts 
import customer_page
import provide_credit_card
import complaint_page
import discussion_table
import purchase_history_page
import account_info_page
import search_info

class setting_account(tk.Frame):
    
    def __init__( self, customer_name, customer_Id, customer_username, master = None ): #customer_name, customer_Id, customer_username ,
        tk.Frame.__init__(self, master) 
        self.master.title( "Setting Account Page" )
        self.master.geometry( "989x676" )
        self.master.configure( background = "light blue" )
      
        
        # User account info 
        self.customer_name = customer_name
        self.customer_username = customer_username 
        self.customer_Id = customer_Id

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
                                      text = "User Account Settings ", 
                                      style = "LabelTitle.TLabel"        
                                    )   
        self.LabelTitle.place( relx = 0.26, rely = 0.035, relwidth = 0.49, relheight = 0.085 )
        #----------------------------------------------------------------------------------

        #-------------------------Purchase History Section Button--------------------
        self.style.configure( "Command_Purchase_History.TButton",  
                              anchor = "left", 
                              font = ( "Helvetica", 14 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.Command_Purchase_History = tk.ttk.Button(  self.top, 
                                        text = "Check My Purchase History",
                                        command = self.Command_Purchase_History, 
                                        style = "Command_Purchase_History.TButton"  
                                      )
        self.Command_Purchase_History.place( relx = 0.1, rely = 0.2, relwidth = 0.300, relheight = 0.071 )
        #---------------------------------------------------------------------------------------

        #---------Provide/Update credit card information Section Button--------------------------------
        self.style.configure( "Command_Credit_Card_Info.TButton", 
                               anchor = "left",  
                               font = ("Helvetica", 14 ),
                               background = "green",
                               foreground = "black"    
                            )
        self.Command_Credit_Card_Info = tk.ttk.Button(  self.top, 
                            text = "Provide/Update My Credit Card",  
                                           command = self.Command_Credit_Card_Info, 
                                           style = "Command_Credit_Card_Info.TButton"
                                        )
        self.Command_Credit_Card_Info.place( relx = 0.1, rely = 0.35, relwidth = 0.300, relheight = 0.071)
        #-----------------------------------------------------------------------------------

        #-----------------------Track my current Package Section Button----------------------------
        self.style.configure( "Command_Track_Package.TButton", 
                               anchor = "left", 
                               font = ( "Helvetica", 14 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.Command_Track_Package = tk.ttk.Button( self.top, 
                                     text = "Track My Current Package", 
                                     command = self.Command_Track_Package,
                                     style = "Command_Track_Package.TButton"
                                   )
        self.Command_Track_Package.place( relx = 0.1, rely = 0.5, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------


        #-----Search Info about clerks/delivery/companies Section Button------------------
        self.style.configure( "Command_Search_info.TButton", 
                               anchor = "left", 
                               font = ( "Helvetica", 14 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.Button_Search_info = tk.ttk.Button( self.top, 
                                     text = "Search Info", 
                                     command = self.Command_Search_info,
                                     style = "Command_Search_info.TButton"
                                   )
        self.Button_Search_info.place( relx = 0.1, rely = 0.65, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------






        #----------------------View my account information Section Button--------------------
        self.style.configure( "Command_Account_info.TButton",  
                              anchor = "left", 
                              font = ( "Helvetica", 14 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.Button_account_info = tk.ttk.Button(  self.top, 
                                        text = "View My Account Information",
                                        command = self.command_account_info, 
                                        style = "Command_Account_info.TButton"  
                                      )
        self.Button_account_info.place( relx = 0.6, rely = 0.2, relwidth = 0.300, relheight = 0.071 )
        #---------------------------------------------------------------------------------------

        #---------Place a complaint Section Button--------------------------------
        self.style.configure( "Command_Place_Complaint.TButton", 
                               anchor = "left",  
                               font = ("Helvetica", 14 ),
                               background = "green",
                               foreground = "black"    
                            )
        self.Command_Place_Complaint = tk.ttk.Button(  self.top, 
                            text = "Complaint and Report",  
                                           command = self.Command_Place_Complaint, 
                                           style = "Command_Place_Complaint.TButton"
                                        )
        self.Command_Place_Complaint.place( relx = 0.6, rely = 0.35, relwidth = 0.300, relheight = 0.071)
        #-----------------------------------------------------------------------------------


        #-----------------View All My Review Section Button----------------------------
        self.style.configure( "Command_Check_Review.TButton", 
                               anchor = "left", 
                               font = ( "Helvetica", 14 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.Command_Check_Review = tk.ttk.Button( self.top, 
                                     text = "Check All My Reviews", 
                                     command = self.Command_Check_Review,
                                     style = "Command_Check_Review.TButton"
                                   )
        self.Command_Check_Review.place( relx = 0.6, rely = 0.5, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------

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


    def Command_Purchase_History(self):
        self.top.destroy() 
        purchase_history_page.purchase_history_page(customer_name = self.customer_name, 
                customer_Id = self.customer_Id, 
                customer_username = self.customer_username)



    def Command_Credit_Card_Info(self):
        self.top.destroy()
        provide_credit_card.provide_credit_card(customer_name = self.customer_name, 
                customer_Id = self.customer_Id, 
                customer_username = self.customer_username )


    def Command_Track_Package(self):
        self.top.destroy() 


    def command_account_info(self):
        self.top.destroy()
        account_info_page.account_info_page( customer_name = self.customer_name, 
        customer_Id = self.customer_Id, customer_username = self.customer_username)        
        

    def Command_Place_Complaint(self):
        self.top.destroy()
        complaint_page.complaint_page(self.customer_name, self.customer_Id, self.customer_username)

    def Command_Check_Review(self):
        discussion_type = "Me All"
        df = pd.read_excel( "csv_files/discussions.xlsx" )
        df_no_violated = df[df['Status'] == "Non-Violated"]
        df_me = df_no_violated[df_no_violated['Username'] == self.customer_username]
        if len(df_me) == 0:
          tk.messagebox.showinfo("Info", "You haven't posted any comment yet")
        else:
          self.top.destroy()
          discussion_table.discussion_table(coming_from = None, 
                coming_from_discuss = "setting_account",
                item_name = None, customer_name = self.customer_name, 
                customer_Id = self.customer_Id, 
                customer_username = self.customer_username, 
                discussion_type = discussion_type, df = df_me)


    def Command_Go_Back(self):
        self.top.destroy()
        customer_page.customer_page(customer_name = self.customer_name,  
        customer_username = self.customer_username, customer_Id = self.customer_Id)


    def Command_Search_info(self):
          self.top.destroy()
          search_info.search_info( customer_name = self.customer_name, 
                     customer_Id = self.customer_Id, 
                     customer_username = self.customer_username)

# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    setting_account(top).mainloop()   