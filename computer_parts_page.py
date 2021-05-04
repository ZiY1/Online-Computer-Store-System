import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd

# python scripts
import guess_page 
import customer_page

import generalized_item 

class computer_parts_page(tk.Frame):

    def __init__(self, customer_name = None, customer_username = None,
                        customer_Id = None,master = None):
        tk.Frame.__init__(self, master)
        self.master.title( "Computer Parts Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")


        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username

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
                            relief = tk.SUNKEN, 
                            anchor = "center", 
                            font = ("Helvetica", 26),
                            background = '#49A'    
                                )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                            text = "Lenovo Computer Parts", 
                                            style =  "LabelTitle.TLabel" 
                                        )

            self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.3 , relheight = 0.1 
                            )
        else:
            self.style.configure( "LabelTitle.TLabel", 
                            relief = tk.SUNKEN,
                            anchor = "left", 
                            font = ("Helvetica", 20),
                            background = '#49A'    
                                )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                           text = f"Lenovo Computer Parts\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )


                            
        #---------------------------------------------------------------------------
        
        
        #---------------------Lenovo Computer Parts Section-----------------------------------------
        df = pd.read_excel( "csv_files/items.xlsx" )
        df_parts = df[ ( df['Type'] == "Computer Part" ) ]

        plus_x = 0
        plus_y = 0 
        plus_relx = 0
        plus_rely = 0  
        
        self.lenovo_images = []
        self.Buttons = []
        for i in range( len(df_parts) ):
            part_name = df_parts.iloc[i]['Name']
            image_tempo = Image.open( f"images/computer_parts/{part_name}.png" )
            image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
            self.lenovo_images.append(None)

            self.lenovo_images[i] = ImageTk.PhotoImage(  image_tempo )
            self.Buttons.append(None)
            
            self.Buttons[i] = tk.Button( self.top, 
             command = lambda name = part_name: self.command_part(name), 
             text = part_name, fg = "black", image = self.lenovo_images[i],
             activebackground = "light blue", compound = "top")

            self.Buttons[i].place( relx = 0 + plus_relx, rely = 0.2 + plus_rely, 
                                    relwidth = 0.1625, relheight = 0.27)
            plus_relx += 0.1655 

            if plus_relx > 0.9: 
                plus_relx = 0  
                plus_rely += 0.35
            
            '''
            self.Lenovo_laptop_1 = tk.Label( image = self.lenovo_laptop )
            self.Lenovo_laptop_1.image = self.lenovo_laptop 

        
            self.Lenovo_laptop_1.place(x = 0 + plus_x, y = 140 + plus_y)
            plus_x += 210 
            self.Buttons.append(None)
            self.style.configure( f"{laptop_name}_bt.TButton",  
                            anchor = "center", 
                            font = ( "Helvetica", 8 ),
                            background = "green",
                            foreground = "black"                                
                        )
            self.Buttons[i] = tk.ttk.Button(self.top, text = f"{laptop_name}",
            command = lambda computer_name = laptop_name: self.command_laptop(computer_name),
            style = f"{laptop_name}_bt.TButton"  )
            self.Buttons[i].place( relx = 0 + plus_relx, rely = 0.45 + plus_rely, 
                                    relwidth = 0.1495, relheight = 0.051)
            plus_relx += 0.1635 

            if plus_x > 1100: 
                plus_x = 0 
                plus_relx = 0 
                plus_y += 240 
                plus_rely += 0.35
            '''
        #--------------------------------------------------------------------------------------------
        
        



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
        if self.Customer_Name == None: # We are in a guess account
            self.top.destroy()
            guess_page.guess_page()
        else:                          # We are in a customer account
            self.top.destroy()
            customer_page.customer_page(customer_name = self.Customer_Name, 
                        customer_Id = self.Customer_Id,  
                        customer_username = self.Customer_username)


    def command_part(self, part_name):
        laptop_name = part_name
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account
            generalized_item.generalized_item(coming_from = "computer_parts_page", 
            item_name = laptop_name )
        else: # We are in the user account 
            generalized_item.generalized_item( coming_from = "computer_parts_page", 
            item_name = laptop_name, 
            customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
            customer_username = self.Customer_username)
