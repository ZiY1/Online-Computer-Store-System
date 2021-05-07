import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

import datetime

# python script 
import setting_account

class search_info(tk.Frame):

    def __init__(self, customer_name = None, 
                     customer_Id = None, customer_username = None, master = None):
        tk.Frame.__init__(self,master)

        self.master.title( "Search Info Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        

        self.create_widgets()


    def create_widgets(self):
        
        # Create main frame
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
        self.my_canvas.configure( background = "light blue" )


        
        #-----------------------title page--------------------------------------------
        self.style = tk.ttk.Style()
        self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )

        self.LabelTitle = tk.ttk.Label( self.second_frame, 
                                           text = f"Search Info", 
                                           style = "LabelTitle.TLabel" 
                                          )
        self.LabelTitle.grid( row = 0, column = 0, padx = 50)
        #-----------------------------------------------------------------------------


        #------------------Label Clerk Header Section-------------------------------------------

        self.style.configure( "LabelClerk.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 26,"bold"),
                               background = 'light blue'    
                            )

        self.LabelClerk = tk.ttk.Label( self.second_frame, 
                                           text = f"Clerks:", 
                                           style = "LabelClerk.TLabel" 
                                          )

        self.LabelClerk.grid( row = 5, column = 0)
        #-------------------------------------------------------------------------------

        #---------------------Label Clerk Sub header Sections-------------------------------------

        self.style.configure( "Label_Sub_Header.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.Label_Clerk_Name = tk.ttk.Label( self.second_frame, 
                                           text =  "Clerk's Name", 
                                           style = "Label_Sub_Header.TLabel" 
                                          )
        self.Label_Clerk_Name.grid( row = 6, column = 0, columnspan = 1)


        self.Label_Clerk_Contact = tk.ttk.Label( self.second_frame, 
                                           text = "Contact info", 
                                           style = "Label_Sub_Header.TLabel" 
                                          )
        self.Label_Clerk_Contact.grid( row = 6, column = 1, padx = 50)
        

        self.Label_Clerk_Warnings = tk.ttk.Label( self.second_frame, 
                                           text = "Warnings", 
                                           style = "Label_Sub_Header.TLabel" 
                                          )
        self.Label_Clerk_Warnings.grid( row = 6, column = 2, padx = 50)
        
        #-------------------------------------------------------------------------------


        df_staff = pd.read_excel( "csv_files/privileged_users.xlsx" )
        
        df_clerks = df_staff[ ( df_staff["Type_user"] == "clerk") & ( df_staff['Status'] == "active") ]
        
        self.clerk_images = list()
                
        for i in range( len(df_clerks)):
            #tk.Button(second_frame, text = f"Button {thing}").grid( row = thing, column = 0)
            clerk_name = df_clerks['Name'].iloc[i]
            clerk_username = df_clerks['Username'].iloc[i]
            clerk_warnings = df_clerks['Warnings'].iloc[i]
        
            image_tempo = Image.open( f"images/icons/clerk.png" )

            image_tempo = image_tempo.resize(  ( 120, 60), Image.ANTIALIAS )

            self.clerk_images.append(None)
            self.clerk_images[i] = ImageTk.PhotoImage( image_tempo  )
            self.style.configure( "Label_entry.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = 'light blue'    
                            )
            
            tk.Label( self.second_frame, text = f"{clerk_name}", image = self.clerk_images[i],
                        compound = tk.TOP,
                        font = "Bold").grid( row = 7 + i , column = 0, pady = 10 )
            
            Label_clerk_username = tk.ttk.Label(self.second_frame, text = f"{clerk_username}", 
                   style = "Label_entry.TLabel" )
            
            Label_clerk_username.grid( row = 7 +i, column = 1, pady = 10)

            Label_clerk_warnings = tk.ttk.Label( self.second_frame, text = f"{clerk_warnings}",
                    style = "Label_entry.TLabel")
            Label_clerk_warnings.grid( row = 7 +i, column = 2, pady = 10)

        
        #------------------Label Delivery Company Header Section---------------------------

        self.style.configure( "Label_Delivery_Company.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 26,"bold"),
                               background = 'light blue'    
                            )

        self.Label_Delivery_Company = tk.ttk.Label( self.second_frame, 
                                           text = f"Delivery Companies:", 
                                           style = "Label_Delivery_Company.TLabel" 
                                          )

        self.Label_Delivery_Company.grid( row = 7 + len(df_clerks), column = 0,
                                    pady = 50)
        #-------------------------------------------------------------------------------

        #---------------------Label Delivery Company Sub header Sections-------------------------------------

        self.style.configure( "Label_Sub_Header_delivery.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.Label_Delivery_Name = tk.ttk.Label( self.second_frame, 
                                           text =  "Delivery Company Name", 
                                           style = "Label_Sub_Header_delivery.TLabel" 
                                          )
        self.Label_Delivery_Name.grid( row = 8 + len(df_clerks), column = 0, columnspan = 1)


        self.Label_Delivery_Contact = tk.ttk.Label( self.second_frame, 
                                           text = "Contact info", 
                                           style = "Label_Sub_Header_delivery.TLabel" 
                                          )
        self.Label_Delivery_Contact.grid( row = 8 + len(df_clerks), column = 1, padx = 50)
        

        self.Label_Delivery_Warning = tk.ttk.Label( self.second_frame, 
                                           text = "Warnings", 
                                           style = "Label_Sub_Header_delivery.TLabel" 
                                          )
        self.Label_Delivery_Warning.grid( row = 8 + len(df_clerks), column = 2, padx = 50)
        
        #-------------------------------------------------------------------------------
        
        
        df_delivery = df_staff[ (df_staff['Type_user'] == "delivery") & (df_staff['Status'] == "active") ]

        self.delivery_images = list()
        for i in range( len(df_delivery) ):
            delivery_name = df_delivery['Name'].iloc[i]
            delivery_username = df_delivery['Username'].iloc[i]
            delivery_warnings = df_delivery['Warnings'].iloc[i]
            
            
            image_tempo = Image.open( f"images/icons/delivery_truck.png" )
            image_tempo = image_tempo.resize(  ( 120, 60), Image.ANTIALIAS )

            self.delivery_images.append(None)
            self.delivery_images[i] = ImageTk.PhotoImage( image_tempo  )
            self.style.configure( "Label_delivery_entry.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = 'light blue'    
                            )
            
            tk.Label( self.second_frame, text = f"{delivery_name}", 
                    image = self.delivery_images[i],
                    compound = tk.TOP,
                    font = "Bold").grid( row = 9 + len(df_clerks) + i , column = 0, pady = 10 )
            

            Label_delivery_username = tk.ttk.Label(self.second_frame, 
                    text = f"{delivery_username}", 
                    style = "Label_delivery_entry.TLabel" )
            
            Label_delivery_username.grid( row = 9 + len(df_clerks) + i, column = 1, pady = 10)

            Label_delivery_warnings = tk.ttk.Label( self.second_frame, 
                    text = f"{delivery_warnings}", 
                    style = "Label_delivery_entry.TLabel")
            Label_delivery_warnings.grid( row = 9 + len(df_clerks) + i, column = 2, pady = 10)


        
        #------------------Label Computer Company Header Section---------------------------

        self.style.configure( "Label_Computer_Company.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 26,"bold"),
                               background = 'light blue'    
                            )

        self.Label_Computer_Company = tk.ttk.Label( self.second_frame, 
                                           text = f"Computer Companies:", 
                                           style = "Label_Computer_Company.TLabel" 
                                          )

        self.Label_Computer_Company.grid( row = 9 + len(df_clerks) + len(df_delivery), 
                                column = 0, pady = 50)
        #-------------------------------------------------------------------------------


        #---------------------Label Computer Company Sub header Sections-------------------------------------

        self.style.configure( "Label_Sub_Header_computer.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.Label_Computer_Name = tk.ttk.Label( self.second_frame, 
                                           text =  "Computer Company Name", 
                                           style = "Label_Sub_Header_computer.TLabel" 
                                          )
        self.Label_Computer_Name.grid( row = 10 + len(df_clerks) + len(df_delivery), 
                                    column = 0, columnspan = 1)


        self.Label_Computer_Contact = tk.ttk.Label( self.second_frame, 
                                           text = "Contact info", 
                                           style = "Label_Sub_Header_computer.TLabel" 
                                          )
        self.Label_Computer_Contact.grid( row = 10 + len(df_clerks) + len(df_delivery), 
                                        column = 1, padx = 50)
        

        self.Label_Computer_Warning = tk.ttk.Label( self.second_frame, 
                                           text = "Warnings", 
                                           style = "Label_Sub_Header_computer.TLabel" 
                                          )
        self.Label_Computer_Warning.grid( row = 10 + len(df_clerks) + len(df_delivery),
                                         column = 2, padx = 50)
        
        #-------------------------------------------------------------------------------
        
        
        df_computer = df_staff[ ( (df_staff['Type_user'] == "computer") | ( df_staff['Type_user'] == 'computer company' ) ) & (df_staff['Status'] == "active") ]

        self.computer_images = list()
        for i in range( len(df_computer) ):
            computer_name = df_computer['Name'].iloc[i]
            computer_username = df_computer['Username'].iloc[i] 
            computer_warnings = df_computer['Warnings'].iloc[i]
            
            
            image_tempo = Image.open( f"images/icons/company.png" )
            image_tempo = image_tempo.resize(  ( 120, 60), Image.ANTIALIAS )

            self.computer_images.append(None)
            self.computer_images[i] = ImageTk.PhotoImage( image_tempo  )
            self.style.configure( "Label_computer_entry.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = 'light blue'    
                            )

            tk.Label( self.second_frame, text = f"{computer_name}", 
                    image = self.computer_images[i],
                    compound = tk.TOP,
                    font = "Bold").grid( row = 11 + len(df_clerks) + len(df_delivery) + i , 
                                column = 0, pady = 10 )
            

            Label_computer_username = tk.ttk.Label(self.second_frame, 
                    text = f"{computer_username}", 
                    style = "Label_computer_entry.TLabel" )
            
            Label_computer_username.grid( row = 11 + len(df_clerks) + len(df_delivery) + i, 
                                column = 1, pady = 10)

            Label_computer_warnings = tk.ttk.Label( self.second_frame, 
                    text = f"{computer_warnings}", 
                    style = "Label_computer_entry.TLabel")
            Label_computer_warnings.grid( row = 11 + len(df_clerks) + len(df_delivery) + i ,
                             column = 2, pady = 10)


        last_block = tk.ttk.Label( self.second_frame, 
                       text = "", style = "Label_computer_entry.TLabel", 
                                 )
        last_block.grid( row = 11 + len(df_clerks) + len(df_delivery) + len(df_computer), 
                     column = 1 , pady = 25)


        #------------------------Go Back section--------------------------------
        image_tempo3 = Image.open( f"images/icons/go_back.png" )
        image_tempo3 = image_tempo3.resize( (25,25), Image.ANTIALIAS )
        
        self.image_back = ImageTk.PhotoImage( image_tempo3)

        self.back_button = tk.Button( self.second_frame, text = "Back", 
                                        image = self.image_back, 
                                        command = self.go_back, compound = "left")
        self.back_button.grid( row = 0, column = 4, padx = 10)   

                         
        #------------------------------------------------------------------------




    def go_back(self):
        self.master.destroy()
        setting_account.setting_account(customer_name = self.Customer_Name, 
          customer_Id = self.Customer_Id, customer_username = self.Customer_username)
        


