import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd 

# python scripts
import guess_page 
import customer_page

import generalized_item 



class servers_page(tk.Frame):

    def __init__(self, customer_name = None, customer_username = None,
                        customer_Id = None,master = None):
        tk.Frame.__init__(self, master)
        self.master.title( "Servers Page" )
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
                                            text = "Lenovo Servers", 
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
                                           text = f"Lenovo Servers\n\tHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )


                            
    #------------------------------------------------------------
        df = pd.read_excel( "csv_files/items.xlsx" ) 
        df_server = df[ df['Type'] == 'server']

        plus_x = 0 
        plus_y = 0 
        plus_relx = 0 
        plus_rely = 0
        
        self.Buttons = []
        for i in range( len( df_server)):
            server_name = df_server.iloc[i]['Name'] 
         
            image_tempo = Image.open( f"images/servers/{server_name}.png" )
            image_tempo = image_tempo.resize(  (400,200), Image.ANTIALIAS )
            self.server = ImageTk.PhotoImage(  image_tempo )
            
            self.lenovo_server_1 = tk.Label( image = self.server )
            self.lenovo_server_1.image = self.server
         
            self.lenovo_server_1.place( x = 0 + plus_x, y = 135 + plus_y )
            plus_x += 847
            self.Buttons.append(None)

            self.style.configure( f"{server_name}_bt.TButton",  
                    anchor = "center", 
                    font = ( "Helvetica", 8 ),
                    background = "green",
                    oreground = "black"                                
                                )
                        
            self.Buttons[i] = tk.ttk.Button(  self.top, 
                        text = f"{server_name}",
                        command = lambda computer_name = server_name: self.command_server(computer_name), 
                        style = f"{server_name}_bt.TButton"  
                                        )
            self.Buttons[i].place( relx = 0.001 + plus_relx, rely = 0.5 + plus_rely, 
                                    relwidth = 0.3125, relheight = 0.051 )
            plus_relx += 0.66

            if plus_x > 900:
                    plus_x = 0 
                    plus_relx = 0 
                    plus_y += 260
                    plus_rely += 0.388
        



    #------------------------------------------------------------------------------




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


    def command_server(self, computer_name):
        server_name = computer_name
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account
            generalized_item.generalized_item(coming_from = "server_page", 
            item_name = server_name )
        else: # We are in the user account 
            generalized_item.generalized_item( coming_from = "server_page", 
            item_name = server_name, 
            customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
            customer_username = self.Customer_username)


    
