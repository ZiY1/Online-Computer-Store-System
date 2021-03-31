import tkinter as tk
import tkinter.ttk as ttk 

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd

# python scripts
import laptops_page 


class generalized_laptop(tk.Frame):

    def __init__(self, laptop_name = None, customer_name = None, 
                     customer_Id = None, customer_username = None, 
                     lenovo_laptop = None, master = None ):

        tk.Frame.__init__(self, master)
        self.laptop_name = laptop_name
        self.master.title( f"Laptop {self.laptop_name} Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        
        self.lenovo_laptop = lenovo_laptop 
        #print(self.lenovo_laptop)
        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()


        #--------------------Lenovo Icon Image---------------------
        image_tempo = Image.open( "images/lenovo_icon_2.png" )
        #image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
        
        self.my_image = ImageTk.PhotoImage( image_tempo  )
        self.label_image = tk.Label( image = self.my_image )
        self.label_image.image = self.my_image 
        self.label_image.place( x = 0, y = 0 )
        #----------------------------------------------------------





         #------------------------Title----------------------------- 
        if self.Customer_Name == None:
            self.style.configure( "LabelTitle.TLabel", 
                               anchor = "center", 
                               font = ("Helvetica", 16),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                            text = f"{self.laptop_name}", 
                                            style =  "LabelTitle.TLabel" 
                                        )

            self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.3 , relheight = 0.1 
                            )
        else:
            self.style.configure( "LabelTitle.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                           text = f"{self.laptop_name}\n\tHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )

        #------------------Laptop Picture --------------------------------------
        laptop_name = self.laptop_name
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_1 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_1.image = self.lenovo_laptop 
        self.Lenovo_laptop_1.place( x = 0, y = 140 )
        #-------------------------------------------------------------------------


        #---------------Get the corresponding data for the laptop------------------
        df = pd.read_excel( "csv_files/items.xlsx" )

        laptop_info = df[ (df['Type'] == 'Laptop') & ( df['Name'] == laptop_name)  ]

        laptop_price = laptop_info['Price'].iloc[-1]
        laptop_features = laptop_info['Features'].iloc[-1]
        #---------------------------------------------------------------------------


        #-------------------------Back Button----------------------------

        self.style.configure(   "CommandBack.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text = "Back",
                                            command = self.command_back,
                                            style="CommandBack.TButton"
                                        )
        self.CommandBack.place(relx=0.870, rely=0.1, relwidth= 0.13, relheight=0.05)

    #-----------------------------------------------------------




    def command_back(self):
        self.top.destroy()

        if self.Customer_Name == None: # We are on the guess page 
            laptops_page.laptops_page(customer_name = None, customer_username = None,
                           customer_Id = None)
        else: # We are on the user page
            laptops_page.laptops_page(customer_name = self.Customer_Name, 
                    customer_username = self.Customer_username,
                            customer_Id = self.Customer_Id )
          
