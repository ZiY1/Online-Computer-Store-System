import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

import datetime

# python script 
import setting_account

class purchase_history_page(tk.Frame):

    def __init__(self, customer_name = None, 
                     customer_Id = None, customer_username = None, master = None):
        tk.Frame.__init__(self,master)

        self.master.title( "Purchase History Page" )
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


        '''
        #-------------------------Lenovo Icon -------------------------------------------
        image_tempo = Image.open( "images/lenovo_icon_2.png" )
        #image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
        
        self.my_image = ImageTk.PhotoImage( image_tempo  )
        self.label_image = tk.Label(self.second_frame ,image = self.my_image )
        self.label_image.image = self.my_image 
        self.label_image.grid()
        #-------------------------------------------------------------------------------
        '''

        #-----------------------title page--------------------------------------------
        self.style = tk.ttk.Style()
        self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )

        self.LabelTitle = tk.ttk.Label( self.second_frame, 
                                           text = f"Purchase History Page\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )
        self.LabelTitle.grid( row = 0, column = 0, padx = 50)
        #-----------------------------------------------------------------------------


        #------------------Purchase History section-------------------------------------------

        self.style.configure( "LabelShopping.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 26,"bold"),
                               background = 'light blue'    
                            )

        self.LabelPurchaseHistory = tk.ttk.Label( self.second_frame, 
                                           text = f"Purchase History:", 
                                           style = "LabelShopping.TLabel" 
                                          )

        self.LabelPurchaseHistory.grid( row = 5, column = 0)
        #-------------------------------------------------------------------------------

        #---------labels section-------------------------------------------

        self.style.configure( "LabelShopp.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.LabelPicture = tk.ttk.Label( self.second_frame, 
                                           text = "   Item", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelPicture.grid( row = 6, column = 0, columnspan = 1)

        self.LabelPrice = tk.ttk.Label( self.second_frame, 
                                           text = "Price", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelPrice.grid( row = 6, column = 1, padx = 50)
        

        self.LabelDate = tk.ttk.Label( self.second_frame, 
                                           text = "Date Purchased", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelDate.grid( row = 6, column = 2, padx = 50)
        

        self.LabelDate = tk.ttk.Label( self.second_frame, 
                                           text = "Date Purchased", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelDate.grid( row = 6, column = 2, padx = 50)
        
        self.LabelStatus = tk.ttk.Label( self.second_frame, 
                                           text = "Status", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelStatus.grid( row = 6, column = 3)
        

        self.LabelID = tk.ttk.Label( self.second_frame, 
                                           text = "Order ID", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelID.grid( row = 6, column = 4, padx = 50)
        

        #-------------------------------------------------------------------------------


        df_orders = pd.read_excel( "csv_files/orders.xlsx" )
        df_items = pd.read_excel( "csv_files/items.xlsx" )
        df_user_history = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] != "in cart") & (df_orders['Order_Status'] != "cancelled") ]
        

        self.item_images = list()
                
        for i in range( len(df_user_history)):
            #tk.Button(second_frame, text = f"Button {thing}").grid( row = thing, column = 0)
            item_name = df_user_history['Item_Name'].iloc[i]
            item_price = df_user_history['Item_Price'].iloc[i]
            item_date = df_user_history['Date order processed'].iloc[i]
            item_status = df_user_history['Order_Status'].iloc[i]
            item_Id = df_user_history['Order_Id'].iloc[i]
            item_custom = df_user_history['Customized'].iloc[i]
            item_type = df_items[df_items['Name'] == item_name ]['Type'].iloc[-1]
            
            custom = "\n(Customized)" if item_custom == "Customized" else ""

            if item_type == 'Desktop':
                image_tempo = Image.open( f"images/Lenovo_Desktops/{item_name}.png" )
            elif item_type == 'Laptop':
                image_tempo = Image.open( f"images/Lenovo_Laptops/{item_name}.png" )
            elif item_type == 'workstation':
                image_tempo = Image.open( f"images/workstations/{item_name}.png" )
            elif item_type == "server":
                image_tempo = Image.open( f"images/servers/{item_name}.png" )
            elif item_type == "mainframe":
                image_tempo = Image.open( f"images/mainframes/{item_name}.png" )
            elif item_type == "Computer Part":
                image_tempo = Image.open( f"images/computer_parts/{item_name}.png" )
            

            image_tempo = image_tempo.resize(  (220,160), Image.ANTIALIAS )

            self.item_images.append(None)
            self.item_images[i] = ImageTk.PhotoImage( image_tempo  )
            self.style.configure( "Label_imag.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = 'light blue'    
                            )
            
            tk.Label( self.second_frame, text = f"{item_name}" + custom, image = self.item_images[i],
                        compound = tk.TOP,
                        font = "Bold").grid( row = 7 + i , column = 0, pady = 10 )
            
            item_price = "$ {:,.2f}".format(item_price)
                
            self.Label_Price = tk.ttk.Label( self.second_frame, text = f"{item_price}",
                    style = "Label_imag.TLabel")
            self.Label_Price.grid( row = 7 +i, column = 1)

            self.Label_Date = tk.ttk.Label(self.second_frame, text = f"{item_date}",
              style =  "Label_imag.TLabel")

            self.Label_Date.grid( row = 7 + i, column = 2)

            
            self.Label_Status = tk.ttk.Label(self.second_frame, text = f"{item_status}",
              style =  "Label_imag.TLabel")

            self.Label_Status.grid( row = 7 + i, column = 3)
            
            self.Label_ID = tk.ttk.Label(self.second_frame, text = f"{item_Id}",
              style =  "Label_imag.TLabel")

            self.Label_ID.grid( row = 7 + i, column = 4)




        self.style.configure( "Labelsubtotal.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.LabelTotal = tk.ttk.Label( self.second_frame, 
                                           text = f"{len(df_user_history)} items purchased", 
                                           style = "Labelsubtotal.TLabel" 
                                          )
        self.LabelTotal.grid( row = 7 + len(df_user_history), column = 0, pady = 30)
        
        
        if( len(df_user_history) == 0  ):
            
            image_tempo3 = Image.open( f"images/icons/monkey.png" )
            image_tempo3 = image_tempo3.resize( (120,120), Image.ANTIALIAS )
            
            self.sad_computer = ImageTk.PhotoImage( image_tempo3)
            self.sad_computer.image = image_tempo3
            sad_computer_label = tk.Label( self.second_frame, 
                        text = "You have not made any purchase",font = "Bold",
                        image = self.sad_computer, compound = tk.TOP)
            
            sad_computer_label.grid( row = 10, column = 1, pady = 20 )
        


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
        


