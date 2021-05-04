import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

import datetime

# python script 
import customer_page 
import generalized_email

class emails_page(tk.Frame):

    def __init__(self, customer_name = None, customer_Id = None, 
                       customer_username = None, master = None):
        tk.Frame.__init__(self,master)

        self.master.title( "Email Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        
        
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

        #-------------------------Lenovo Icon -------------------------------------------
        image_tempo = Image.open( "images/lenovo_icon_2.png" )
        #image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
        
        self.my_image = ImageTk.PhotoImage( image_tempo  )
        self.label_image = tk.Label(self.second_frame ,image = self.my_image )
        self.label_image.image = self.my_image 
        self.label_image.grid()
        
        #-------------------------------------------------------------------------------

        #-----------------------title page--------------------------------------------
        self.style = tk.ttk.Style()
        self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 26, "bold"),
                               background = '#49A'    
                            )

        self.LabelTitle = tk.ttk.Label( self.second_frame, 
                                           text = f"Email Page", 
                                           style = "LabelTitle.TLabel" 
                                          )
        self.LabelTitle.grid( row = 0, column = 2, columnspan = 1, rowspan = 1,
             padx = 30)
        #-----------------------------------------------------------------------------


        
        #-----------------------------label Email Section-----------------------------------------

        self.style.configure( "LabelEmail.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica",36, "bold"),
                               background = 'light blue'    
                            )

        self.LabelEmail = tk.ttk.Label( self.second_frame, 
                                           text = f"Emails:", 
                                           style = "LabelEmail.TLabel" 
                                          )

        self.LabelEmail.grid( row = 5, column = 0)
        

        self.style.configure( "Labelsubheader.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica",26, "bold"),
                               background = 'light blue'    
                            )

        self.LabelSubject = tk.ttk.Label( self.second_frame, 
                                           text = "  Subject  ", 
                                           style = "Labelsubheader.TLabel" 
                                          )
        self.LabelSubject.grid( row = 6, column = 0)


        self.LabelFrom = tk.ttk.Label( self.second_frame, 
                                           text = "From", 
                                           style = "Labelsubheader.TLabel" 
                                          )
        self.LabelFrom.grid( row = 6, column = 1)
        

        self.LabelDate = tk.ttk.Label( self.second_frame, 
                                           text = "  Date ", 
                                           style = "Labelsubheader.TLabel" 
                                          )
        self.LabelDate.grid( row = 6, column = 2)
        

        #-------------------------------------------------------------------------------
    


        df_emails = pd.read_excel( "csv_files/emails.xlsx" )

        df_user_emails = df_emails[ df_emails["for_username"] == self.Customer_username ]


        self.label_subjects = list()
        self.label_from = list()
        self.label_dates = list()
        self.images_mail = list()
        self.mail_buttons = list()
        for i in range( len(df_user_emails)):
            self.label_subjects.append(None)
            self.label_from.append(None)
            self.label_dates.append(None)
            self.style.configure( "Label_each_row.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica",14),
                               background = 'light blue'    
                            )
            current_subject = str(df_user_emails['Subject'].iloc[i])
            self.label_subjects[i] = tk.ttk.Label( self.second_frame, 
                                            text = f"{current_subject}", 
                                            style = "Label_each_row.TLabel" 
                                            )
            self.label_subjects[i].grid( row = 7 + i, column = 0, pady = 20)

            current_from = str(df_user_emails['From'].iloc[i])
            self.label_from[i] = tk.ttk.Label( self.second_frame, 
                                            text = f"{current_from}", 
                                            style = "Label_each_row.TLabel" 
                                            )
            self.label_from[i].grid( row = 7 + i, column = 1, pady = 20)

            
            current_date = str(df_user_emails['Date_received'].iloc[i])
            self.label_dates[i] = tk.ttk.Label( self.second_frame, 
                                            text = f"{current_date}", 
                                            style = "Label_each_row.TLabel" 
                                            )
            self.label_dates[i].grid( row = 7 + i, column = 2, pady = 20)
                
            

            #image button sending the user to that message
            current_status = str( df_user_emails["Status"].iloc[i] )
            current_id = df_user_emails["ID"].iloc[i]
            if current_status == "unread":
                image_tempo2 = Image.open( f"images/icons/email.png" )
            else:
                image_tempo2 = Image.open( f"images/icons/read_email.png" )
            image_tempo2 = image_tempo2.resize( (25,25), Image.ANTIALIAS )
            
            self.images_mail.append(None)
            self.images_mail[i] = ImageTk.PhotoImage( image_tempo2)

            self.mail_buttons.append(None)
            self.mail_buttons[i] = tk.Button( self.second_frame, text = "read me", 
            image = self.images_mail[i], 
            command = lambda Id = current_id: self.read_email(Id), compound = "left")

            self.mail_buttons[i].grid( row = 7 + i, column = 3, pady = 20)
            #                     -                           #


        #------------------------Back Section------------------------------------
        image_tempo3 = Image.open( f"images/icons/go_back.png" )
        image_tempo3 = image_tempo3.resize( (25,25), Image.ANTIALIAS )
        
        self.image_back = ImageTk.PhotoImage( image_tempo3)

        self.back_button = tk.Button( self.second_frame, text = "Back     ", 
                                        image = self.image_back, 
                                        command = self.go_back, compound = "left")
        self.back_button.grid( row = 0, column = 7 )   
        #-------------------------------------------------------------------------



    def read_email(self,Id):
        self.master.destroy()
        generalized_email.generalized_email(customer_name = self.Customer_Name, 
        customer_Id = self.Customer_Id, customer_username = self.Customer_username,
        email_Id = Id)


    def go_back(self):
        self.master.destroy()
        customer_page.customer_page( customer_name = self.Customer_Name,
         customer_username = self.Customer_username, 
         customer_Id = self.Customer_Id)

        
