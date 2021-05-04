import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

import datetime

# python script 
import emails_page

class generalized_email(tk.Frame):

    def __init__(self, customer_name = None, customer_Id = None, 
                       customer_username = None, email_Id = None, master = None):
        tk.Frame.__init__(self,master)

        self.master.title( "Read Email Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        
        self.email_Id = email_Id
        
        self.create_widgets()


    def create_widgets(self):
        
        #Create main frame
        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack(fill = tk.BOTH, expand = 1 )

        self.mainframe.configure(background = "light blue")
        

        #create a Main Frame
        self.my_canvas = tk.Canvas(self.mainframe)
        self.my_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1) 

        # Add a scrollbar to the canvas
        self.my_scrollbar = tk.ttk.Scrollbar(self.mainframe, orient = tk.VERTICAL, 
                        command = self.my_canvas.yview)

        self.my_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        # Configure the canvas
        self.my_canvas.configure(yscrollcommand = self.my_scrollbar.set)
        self.my_canvas.bind( '<Configure>', 
            lambda e: self.my_canvas.configure( scrollregion = self.my_canvas.bbox("all")) )

        # create another frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas)

        # add that new frame to a window in the canvas
        self.my_canvas.create_window((0,0), window = self.second_frame, anchor = "nw")

        self.second_frame.configure( background = "light blue")
        self.my_canvas.configure( background = "light blue")


        #-----------------------title page--------------------------------------------
        self.style = tk.ttk.Style()
        self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 26),
                               background = 'light blue'    
                            )

        self.LabelTitle = tk.ttk.Label( self.second_frame, 
                                           text = "", 
                                           style = "LabelTitle.TLabel" 
                                          )
        #self.LabelTitle.grid()
        #-----------------------------------------------------------------------------

        # Gather the email data

        df_emails = pd.read_excel( "csv_files/emails.xlsx" )

        df_email_info = df_emails[ df_emails["ID"] == self.email_Id ]
        email_subject = df_email_info['Subject'].iloc[-1]
        email_from = df_email_info["From"].iloc[-1]
        email_message = df_email_info["Message"].iloc[-1]
        email_status = df_email_info["Status"].iloc[-1]
        #
        
        
        if email_status == "unread":
            df_email_info.loc[:,('Status')] = "read"
            df_emails[ df_emails["ID"] == self.email_Id] = df_email_info 
            df_emails.to_excel( "csv_files/emails.xlsx",index = False )

        #-----------------------------label Email Section-----------------------------------------

        self.style.configure( "LabelHeader.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica",26, "bold"),
                               background = 'light blue'    
                            )

        self.LabelSubject = tk.ttk.Label( self.second_frame, 
                                           text = f"Subject: {email_subject}", 
                                           style = "LabelHeader.TLabel" 
                                          )

        self.LabelSubject.grid( row = 5, column = 0)
        

       
        self.LabelFrom = tk.ttk.Label( self.second_frame, 
                                           text = f"From: {email_from}", 
                                           style = "LabelHeader.TLabel" 
                                          )
        self.LabelFrom.grid( row = 6, column = 0)


        self.style.configure( "Labelmessage.TLabel", 
                               anchor = "left", 
                               font = ("Times",15 ),
                               background = 'light blue'    
                            )


        self.LabelMessage = tk.ttk.Label( self.second_frame, 
                                           text = f"{email_message}", 
                                           style = "Labelmessage.TLabel" 
                                          )
        self.LabelMessage.grid( row = 7, column = 0, columnspan = 1)
        
        #-------------------------------------------------------------------------------



        #------------------------Back Section------------------------------------
        image_tempo3 = Image.open( f"images/icons/go_back.png" )
        image_tempo3 = image_tempo3.resize( (25,25), Image.ANTIALIAS )
        
        self.image_back = ImageTk.PhotoImage( image_tempo3)

        self.back_button = tk.Button( self.second_frame, text = "Back     ", 
                                        image = self.image_back, 
                                        command = self.go_back, compound = "left")
        self.back_button.grid( row = 0, column = 7 )   
        #-------------------------------------------------------------------------




    def go_back(self):
        self.master.destroy()
        emails_page.emails_page( customer_name = self.Customer_Name, 
        customer_Id = self.Customer_Id, customer_username = self.Customer_username)
        
