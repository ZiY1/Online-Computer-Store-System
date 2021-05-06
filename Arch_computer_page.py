import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd 


# python scripts
import guess_page 
import customer_page


import generalized_item

class Arch_computers_page(tk.Frame):

    def __init__(self, Arch_name = None ,customer_name = None, customer_username = None,
                        customer_Id = None,master = None):
        tk.Frame.__init__(self, master)
        self.Arch = Arch_name

        self.master.title( f"{self.Arch} Computers Page" )
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
                               font = ("Helvetica", 18),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                            text = f"Recommended {self.Arch} Computers", 
                                            style =  "LabelTitle.TLabel" 
                                        )

            self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.35 , relheight = 0.1 
                            )
        else:
            self.style.configure( "LabelTitle.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 18),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                           text = f"Recommended {self.Arch} Computers\n\tHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.35 , relheight = 0.15 
                            )        
        #------------------------------------------------------------

        df = pd.read_excel("csv_files/items.xlsx")
        df_Arch = df[ ( df['Architecture'] == self.Arch ) &( (df['Type'] == 'Laptop') | (df['Type'] == 'Desktop') | (df['Type'] == 'workstation')  )] # Architecture e.g: Intel, AMD Ryzen 
        df_Arch = df_Arch.sort_values(by = 'Number of Sales', ascending = False) # sort in popular order

        plus_x = 0 
        plus_y = 0

        plus_relx = 0 
        plus_rely = 0 

        self.lenovo_images = []
        self.Buttons = []
        for i in range( 10 ): # Only the top 10 sold computers will be shown
            computer_name = df_Arch.iloc[i]['Name']
            computer_type = df_Arch.iloc[i]['Type']

            if computer_type == 'Desktop':
                image_tempo = Image.open( f"images/Lenovo_Desktops/{computer_name}.png" )
            elif computer_type == 'Laptop':
                image_tempo = Image.open( f"images/Lenovo_Laptops/{computer_name}.png" )
            elif computer_type == 'workstation':
                image_tempo = Image.open( f"images/workstations/{computer_name}.png" )
            elif computer_type == "server":
                image_tempo = Image.open( f"images/servers/{computer_name}.png" )
            elif computer_type == "mainframe":
                image_tempo = Image.open( f"images/mainframes/{computer_name}.png" )

            image_tempo = image_tempo.resize( (230,200), Image.ANTIALIAS )
            
            self.lenovo_images.append(None)
            self.lenovo_images[i] = ImageTk.PhotoImage(  image_tempo )
            self.Buttons.append(None)
            
            self.Buttons[i] = tk.Button( self.top, 
             command = lambda name = computer_name,type_ = computer_type : self.command_computers(name,type_), 
             text = f"{computer_name}", fg = "black", image = self.lenovo_images[i],
             activebackground = "light blue", compound = "top")

            self.Buttons[i].place( relx = 0 + plus_relx, rely = 0.2 + plus_rely, 
                                    relwidth = 0.18, relheight = 0.33)
            plus_relx += 0.195 

            if plus_relx > 0.9: 
                plus_relx = 0  
                plus_rely += 0.37
            
            
            
            '''
            self.computer = ImageTk.PhotoImage(image_tempo)
            self.computer_1 = tk.Label( image  = self.computer)
            self.computer_1.image = self.computer

                
            self.computer_1.place(x = 0 + plus_x, y = 140 + plus_y )
            plus_x += 250 
            self.Buttons.append(None)
            self.style.configure( f"{computer_name}_bt.TButton", anchor = "center", 
                            font = ("Helvetica", 8), background = "green", 
                            foreground = "black")
            self.Buttons[i] = tk.ttk.Button( self.top, text = f"{computer_name}", 
                    command = lambda name = computer_name,type_ = computer_type : self.command_computers(name,type_),
                    style = f"{computer_name}_bt.TButton" 
                    )
            self.Buttons[i].place( relx = 0 + plus_relx , rely = 0.5 + plus_rely, 
                                    relwidth = 0.16, relheight = 0.051 )
            
            plus_relx += 0.195
            if plus_x > 1000:
                plus_x = 0 
                plus_relx = 0
                plus_y += 240
                plus_rely += 0.35 
            '''

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



    def command_computers(self, computer_name, computer_type):
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account
            generalized_item.generalized_item( coming_from = "Arch_computer_page",
                item_name = computer_name) 
        else: # We are in the user account
            generalized_item.generalized_item( coming_from = "Arch_computer_page",
                item_name = computer_name, customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, customer_username = self.Customer_username)
        

            



