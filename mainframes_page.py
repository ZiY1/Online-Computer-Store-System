import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd

# python scripts
import guess_page 
import customer_page
import generalized_item 



class mainframes_page(tk.Frame):

    def __init__(self, customer_name = None, customer_username = None,
                        customer_Id = None,master = None):
        tk.Frame.__init__(self, master)
        self.master.title( "Mainframes Page" )
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
                                            text = "Mainframes", 
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
                                           text = f"Mainframes\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )


                            
    #----------------------Mainframe Page Section-------------------------------
        df = pd.read_excel( "csv_files/items.xlsx" ) 
        df_mainframe = df[ df['Type'] == 'mainframe']

        plus_x = 0 
        plus_y = 0 
        plus_relx = 0 
        plus_rely = 0 
         
        self.Buttons = []
        for i in range(len(df_mainframe)):
            mainframe_name = df_mainframe.iloc[i]['Name']
        
            image_tempo = Image.open( f"images/mainframes/{mainframe_name}.png" )
            image_tempo = image_tempo.resize(  (400,200), Image.ANTIALIAS )
            self.mainframe = ImageTk.PhotoImage(  image_tempo )
            
            self.mainframe_1 = tk.Label( image = self.mainframe )
            self.mainframe_1.image = self.mainframe 
            
        
            self.mainframe_1.place( x = 0 + plus_x, y = 135 + plus_y)
            plus_x += 847 
            self.Buttons.append(None)

            self.style.configure( f"{mainframe_name}_bt.TButton",  
                                anchor = "center", 
                                font = ( "Helvetica", 8 ),
                                background = "green",
                                foreground = "black"                                
                                )
                                
            self.Buttons[i] = tk.ttk.Button(  self.top, 
                text = f"{mainframe_name}",
                command = lambda computer_name = mainframe_name: self.command_mainframe(computer_name), 
                style = f"{mainframe_name}_bt.TButton"  
                                            )
            self.Buttons[i].place( relx = 0.001 + plus_relx, rely = 0.5 + plus_rely, 
                                relwidth = 0.3125, relheight = 0.051 )
            
            plus_relx += 0.66

            if plus_x > 900:
                plus_x = 0 
                plus_relx = 0
                plus_y += 260 
                plus_rely += 0.388  
            

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


    def command_mainframe(self, computer_name):
        mainframe_name = computer_name
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account
            generalized_item.generalized_item(coming_from = "mainframe_page", 
            item_name = mainframe_name )
        else: # We are in the user account 
            generalized_item.generalized_item( coming_from = "mainframe_page", 
            item_name = mainframe_name, 
            customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
            customer_username = self.Customer_username)


