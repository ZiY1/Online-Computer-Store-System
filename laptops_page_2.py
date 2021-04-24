import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

import numpy as np 
import pandas as pd
# python scripts
import laptops_page
import guess_page 
import customer_page

import generalized_item

class laptops_page_2(tk.Frame):

    def __init__(self,customer_name = None, customer_Id = None,  
                    customer_username = None, master = None):
        tk.Frame.__init__(self, master)
        self.master.title( "Mac and Linux Laptops Page" )
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
                               anchor = "center", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                            text = "Mac & Linux Laptops", 
                                            style =  "LabelTitle.TLabel" 
                                        )

            self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.3 , relheight = 0.1 
                            )
        else:
            self.style.configure( "LabelTitle.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                           text = f"Mac & Linux Laptops\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )

        #------------------------------------------------------------


        df = pd.read_excel( "csv_files/items.xlsx" )
        df_laptop = df[ ( df['Type'] == "Laptop" ) & ( df['Brand'] != 'Lenovo' ) ]

        plus_x = 0
        plus_y = 0 
        plus_relx = 0 
        plus_rely = 0 
    
        self.Buttons = []

        for i in range( len(df_laptop)):
            laptop_name = df_laptop.iloc[i]['Name']
            image_tempo = Image.open( f"images/Lenovo_Laptops/{laptop_name}.png" )
            image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
            self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
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
        



        #-------------------------Back Button----------------------------

        self.style.configure(   "CommandBack.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text = "Go Back to Lenovo Laptops",
                                            command = self.command_back,
                                            style="CommandBack.TButton"
                                        )
        self.CommandBack.place(relx=0.770, rely=0.1, relwidth= 0.22, relheight=0.05)

    #-----------------------------------------------------------



        #-------------------------Back To main Page Button----------------------------

        self.style.configure(   "Command_Back_Main_Page.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.Command_Back_Main_Page = tk.ttk.Button(   self.top, 
                                            text = "Go Back to Main Page",
                                            command = self.Command_Back_Main_Page,
                                            style = "Command_Back_Main_Page.TButton"
                                        )
        self.Command_Back_Main_Page.place(relx = 0.770, rely= 0.03, relwidth= 0.22, relheight=0.05)

    #-----------------------------------------------------------



    def command_back(self): # We go back to laptops one page
        if self.Customer_Name == None: # We are in a guess account
            self.top.destroy()
            laptops_page.laptops_page()
        else:  # We are in a user account
            self.top.destroy() 
            laptops_page.laptops_page( customer_name= self.Customer_Name, 
              customer_username = self.Customer_username, 
              customer_Id = self.Customer_Id )

    def Command_Back_Main_Page(self): # Go back to Main Page
        if self.Customer_Name == None: # We are in a guess account
            self.top.destroy()
            guess_page.guess_page()
        else: # We are in the user account
            self.top.destroy() 
            customer_page.customer_page( customer_name = self.Customer_Name, 
            customer_username = self.Customer_username, customer_Id = self.Customer_Id)


    def command_laptop(self, computer_name):
        laptop_name = computer_name
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account
            generalized_item.generalized_item( coming_from = "mac_linux_laptop_page", 
            item_name = laptop_name)
        else: # We are in the user account
            generalized_item.generalized_item( coming_from = "mac_linux_laptop_page", 
            item_name = laptop_name, customer_name = self.Customer_Name, 
            customer_Id = self.Customer_Id, customer_username = self.Customer_username )
