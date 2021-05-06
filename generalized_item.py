import tkinter as tk
import tkinter.ttk as ttk 

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd

import string, random # to generate random tracking orders

# python scripts
import laptops_page 
import laptops_page_2
import mainframes_page 
import desktops_page
import workstations_page
import servers_page
import computer_parts_page

import guess_page
import customer_page

import purpose_computer_page
import OS_computer_page
import Arch_computer_page

import check_out
import discussion_table
import discussion_page


import select_computer_parts

class generalized_item(tk.Frame):

    def __init__(self, coming_from = None, item_name = None, customer_name = None, 
                     customer_Id = None, customer_username = None, master = None ):

        tk.Frame.__init__(self, master)
        self.item_name = item_name
        
        #---------------Get the corresponding data for the Item------------------
        df = pd.read_excel( "csv_files/items.xlsx" )

        df_item_info = df[ ( df['Name'] == self.item_name)  ]

        self.item_type = df_item_info['Type'].iloc[-1].title()

        self.item_price = df_item_info['Price'].iloc[-1]
        self.item_price_f = "$ {:,.2f}".format(self.item_price)
               
        self.item_features = df_item_info['Features'].iloc[-1]

        self.item_purpose = df_item_info['Purpose'].iloc[-1]
        self.item_OS = df_item_info['OS'].iloc[-1]
        self.item_architecture = df_item_info['Architecture'].iloc[-1]
        self.item_star = df_item_info['overall review'].iloc[-1]
        self.item_CPU = df_item_info['CPU cores'].iloc[-1]
        self.item_GPU = df_item_info['Graphic Card'].iloc[-1]
        #---------------------------------------------------------------------------

        
        
        self.master.title( f"{self.item_type} {self.item_name} Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        
        
        # Back page coming from 
        self.coming_from_page = coming_from

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
                               font = ("Helvetica", 16),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                            text = f"{self.item_name}", 
                                            style =  "LabelTitle.TLabel" 
                                        )

            self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.31 , relheight = 0.1 
                            )
        else:
            self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN, 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = '#49A'    
                            )

            self.LabelTitle = tk.ttk.Label( self.top, 
                                           text = f"{self.item_name}\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.31 , relheight = 0.15 
                            )

        #------------------Item Picture --------------------------------------
        item_name = self.item_name
        
        if self.item_type == "Laptop":
            image_tempo = Image.open( f"images/Lenovo_Laptops/{item_name}.png" )
        elif self.item_type == "Desktop":
            image_tempo = Image.open( f"images/Lenovo_Desktops/{item_name}.png" )
        elif self.item_type == "Server":
            image_tempo = Image.open( f"images/servers/{item_name}.png" )
        elif self.item_type == "Mainframe":
            image_tempo = Image.open( f"images/mainframes/{item_name}.png")
        elif self.item_type == "Workstation":
            image_tempo = Image.open( f"images/workstations/{item_name}.png" ) 
        elif self.item_type == "Computer Part":
            image_tempo = Image.open( f"images/computer_parts/{item_name}.png" )
        
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_item = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_item = tk.Label( image = self.lenovo_item )
        self.Lenovo_item.image = self.lenovo_item 
        self.Lenovo_item.place( x = 20, y = 140 )
        #-------------------------------------------------------------------------


        #----Computer Architecture, OS, Purpose and Price Display --------------------
        if self.item_type != "Computer Part":
            self.style.configure( "Label_Item_Info.TLabel", 
                                anchor = "left", 
                                font = ("Bold", 18),
                                background = 'light blue'    
                                )

            self.Label_Item_Info = tk.ttk.Label( self.top, 
                                                text = f"Architecture: {self.item_architecture}\nOS:  {self.item_OS}\nMain Purpose: {self.item_purpose}\nPrice: {self.item_price_f }", 
                                                style =  "Label_Item_Info.TLabel" 
                                            )

            self.Label_Item_Info.place( relx = 0.17, rely = 0.2, 
                                relwidth = 0.24 , relheight = 0.16 
                                )
        else:
            self.style.configure( "Label_Item_Info.TLabel", 
                                anchor = "left", 
                                font = ("Bold", 18),
                                background = 'light blue'    
                                )

            self.Label_Item_Info = tk.ttk.Label( self.top, 
                                                text = f"\n\n\nPrice: { self.item_price_f}", 
                                                style =  "Label_Item_Info.TLabel" 
                                            )

            self.Label_Item_Info.place( relx = 0.17, rely = 0.2, 
                                relwidth = 0.24 , relheight = 0.16 
                                )

        #---------------------------------------------------------------------------------





        #---------------Item Features Display ---------------------------------------

        name_feature = "Computer" if self.item_type != "Computer Part" else "Item"
        self.style.configure( "Label_Item_Feature.TLabel", 
                               anchor = "left", 
                               font = ("Bold", 14),
                               background = 'light blue'    
                            )


        self.Label_Item_Features = tk.ttk.Label( self.top, 
                                            text = f"{name_feature} Features:\n\n{self.item_features}", 
                                            style =  "Label_Item_Feature.TLabel" 
                                        )

        self.Label_Item_Features.place( relx = 0.45, rely = 0.23, 
                               relwidth = 0.55 , relheight = 0.7 
                            )

        #---------------------------------------------------------------------------------


        #-------------------------Overall Review Star--------------------------------------

        self.style.configure( "Label_Item_St.TLabel", 
                               anchor = "left", 
                               font = ("Bold", 12),
                               background = '#49A',
                               foreground = "black"    
                            )

        self.Label_Item_Stars = tk.ttk.Label( self.top, 
                    text = f"Overall Rating:", 
                    style =  "Label_Item_St.TLabel" 
                                        )

        self.Label_Item_Stars.place( relx = 0, rely = 0.46, 
                               relwidth = 0.1 , relheight = 0.05 
                            )


        star_review = self.star_printer( self.item_star ) 

        self.style.configure( "Label_Item_Star.TLabel", 
                               anchor = "left", 
                               font = ("Bold", 18),
                               background = '#49A',
                               foreground = "gold"    
                            )

        self.Label_Item_Stars = tk.ttk.Label( self.top, 
                    text = f"{star_review}", 
                    style =  "Label_Item_Star.TLabel" 
                                        )

        self.Label_Item_Stars.place( relx = 0.1, rely = 0.46, 
                               relwidth = 0.1 , relheight = 0.05 
                            )
        #----------------------------------------------------------------------------------


        #---------------------------Post a Review Section---------------------------------------
        if self.Customer_Name != None:
            image_tempo = Image.open( f"images/icons/review.png" )
            image_tempo = image_tempo.resize(  (25,25), Image.ANTIALIAS )
            self.post_review_pic = ImageTk.PhotoImage(  image_tempo )
            
            post_review_button = tk.Button(self.top, 
                    command = self.command_post_review,
                    text = "Post a review", image = self.post_review_pic,
                    compound = "left")
            post_review_button.place(relx = 0.25, rely= 0.46, relwidth= 0.1, relheight = 0.05)
        #---------------------------------------------------------------------------------------



        #---------------------------Customer Review Section---------------------------------

        image_tempo = Image.open( f"images/reviews-customer-logo.png" )
        image_tempo = image_tempo.resize(  (200,100), Image.ANTIALIAS )
        self.customer_review_pic = ImageTk.PhotoImage(  image_tempo )
        
        customer_review_button = tk.Button(self.top, 
                  command = self.command_reviews,
                  text = "", image = self.customer_review_pic,
                  compound = "left")
        customer_review_button.place(relx = 0.01, rely= 0.53, relwidth= 0.15, relheight=0.15)
        #-----------------------------------------------------------------------------------


        #--------------------------Shopping cart section-----------------------------------
        if self.Customer_Name !=  None: 
            image_tempo = Image.open( f"images/shopping-cart.png" )
            image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
            self.customer_shopping_pic = ImageTk.PhotoImage(  image_tempo )
            
            shopping_cart_button = tk.Button(self.top, 
                  command = self.add_to_shopping_cart,
                  text = "Add to Cart", image = self.customer_shopping_pic,
                  compound = "left")
            shopping_cart_button.place(relx = 0.17, rely= 0.38, relwidth= 0.13, relheight=0.07)

        #-----------------Check out Section----------------------
            image_tempo = Image.open( f"images/checkout.png" )
            image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
            self.checkout_pic = ImageTk.PhotoImage(  image_tempo )
            
            df_orders = pd.read_excel("csv_files/orders.xlsx")

            df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ]

            items_in_cart = len(df_user_shopping_cart)
            if items_in_cart == 0: 
                checkout_button = tk.Button(self.top, 
                    command = self.command_checkout,
                    text = "", image = self.checkout_pic,
                    compound = "bottom")
                checkout_button.place(relx = 0.77, rely= 0.05, relwidth= 0.07, relheight=0.1)
            else:
                checkout_button = tk.Button(self.top, 
                    command = self.command_checkout,
                    text = f"{items_in_cart} items", image = self.checkout_pic,
                    compound = "bottom")
                checkout_button.place(relx = 0.77, rely= 0.05, relwidth= 0.07, relheight=0.1)
        #----------------------------------------------------------




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

        if self.coming_from_page == "laptops_page":
            if self.Customer_Name == None: # We are on the guess page 
                laptops_page.laptops_page(customer_name = None, customer_username = None,
                            customer_Id = None)
            else: # We are on the user page
                laptops_page.laptops_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id )
        
        elif self.coming_from_page == "mac_linux_laptop_page":
            if self.Customer_Name == None: # We are on the guess page
                laptops_page_2.laptops_page_2(customer_name = None, customer_username = None,
                            customer_Id = None)
            else: # We are on the user page 
                laptops_page_2.laptops_page_2(customer_name = self.Customer_Name, 
                                customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id)
        
        elif self.coming_from_page == "purpose_computer_page":
            if self.Customer_Name == None: # We are on the guess page
                purpose_computer_page.purpose_computers_page( purpose_name = self.item_purpose,
                customer_name = None, customer_username = None,   customer_Id = None)
            else: # We are on the user page 
                purpose_computer_page.purpose_computers_page( purpose_name = self.item_purpose,
                    customer_name = self.Customer_Name, customer_username = self.Customer_username,
                    customer_Id = self.Customer_Id)
        elif self.coming_from_page == "Main_Page":
            if self.Customer_Name == None: # We are on the guess page 
                guess_page.guess_page()
            else: # We are on the user page
                customer_page.customer_page(customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, 
                customer_username = self.Customer_username)

        elif self.coming_from_page == "OS_computer_page":
            if self.Customer_Name == None: # We are on the guess page 
                OS_computer_page.OS_computers_page(OS_name = self.item_OS)
            else: # We are on the user page
                OS_computer_page.OS_computers_page( OS_name = self.item_OS,
                customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                customer_username = self.Customer_username)
        elif self.coming_from_page == "Arch_computer_page":
            if self.Customer_username == None: # We are on the guess page
                Arch_computer_page.Arch_computers_page(Arch_name = self.item_architecture)
            else: # We are on the user page
                Arch_computer_page.Arch_computers_page(Arch_name = self.item_architecture, 
                customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                customer_username = self.Customer_username)
        elif self.coming_from_page == "server_page":
            if self.Customer_username == None: # We are on the guess page
                servers_page.servers_page()
            else: # We are on the user page
                servers_page.servers_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id )
        elif self.coming_from_page == "desktops_page":
            if self.Customer_username == None: # We are on the guess page 
                desktops_page.desktops_page()
            else: # We are on the user page
                desktops_page.desktops_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id )
        elif self.coming_from_page == "workstations_page":
            if self.Customer_username == None: # We are on the guess page
                workstations_page.workstations_page()
            else: # We are on the user page
                workstations_page.workstations_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id )
        elif self.coming_from_page == "mainframe_page":
            if self.Customer_username == None: # We are on the guess page
                mainframes_page.mainframes_page()
            else: # We are on the user page
                mainframes_page.mainframes_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                                customer_Id = self.Customer_Id )

        elif self.coming_from_page == "computer_parts_page":
            if self.Customer_username == None: # We are on the guess page
                computer_parts_page.computer_parts_page()
            else: # We are on the user page
                computer_parts_page.computer_parts_page(customer_name = self.Customer_Name, 
                        customer_username = self.Customer_username,
                        customer_Id = self.Customer_Id )




    def star_printer(self, star_numbers):
        star_numbers = round(star_numbers)
        if star_numbers == 0:
            return "☆☆☆☆☆"
        elif star_numbers == 1:
            return "★☆☆☆☆"
        elif star_numbers == 2:
            return "★★☆☆☆"
        elif star_numbers == 3:
            return "★★★☆☆"
        elif star_numbers == 4:
            return "★★★★☆"
        elif star_numbers == 5:
            return "★★★★★"

    def command_reviews(self):
        df = pd.read_excel( "csv_files/discussions.xlsx" )
        df_no_violated = df[df['Status'] == "Non-Violated"]
        df_computer = df_no_violated[df_no_violated['Computer Name'] == self.item_name]
        if self.Customer_username is None:
            discussion_type = "Guest"
            if len(df_computer) == 0:
                tk.messagebox.showinfo("Info", "No comment of this computer posted")
            else:
                self.top.destroy()
                discussion_table.discussion_table(coming_from = self.coming_from_page, 
                coming_from_discuss = "generalized_item",
                item_name = self.item_name, customer_name = None, 
                customer_Id = None, customer_username = None, 
                discussion_type = discussion_type, df = df_computer)
        else:
            discussion_type = "All"
            if len(df_computer) == 0:
                tk.messagebox.showinfo("Info", "No comment of this computer posted")
            else:
                self.top.destroy()
                discussion_table.discussion_table(coming_from = self.coming_from_page, 
                coming_from_discuss = "generalized_item",
                item_name = self.item_name, customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, customer_username = self.Customer_username, 
                discussion_type = discussion_type, df = df_computer)


    def add_to_shopping_cart(self):
        
        if self.item_type == "Laptop".title() or self.item_type == "workstation".title() or self.item_type == "Desktop".title():
            select_computer_parts.select_computer_parts( my_geometry = "550x450",
            coming_from = self.coming_from_page,
            item_arch = self.item_architecture,
            item_name = self.item_name, item_price = self.item_price, 
            item_type = self.item_type, item_CPU = self.item_CPU, 
            item_GPU = self.item_GPU, item_purpose = self.item_purpose,
            customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
            customer_username = self.Customer_username)
            
            generalized_item(coming_from = self.coming_from_page, item_name = self.item_name, 
                    customer_name = self.Customer_Name, 
                    customer_Id = self.Customer_Id, customer_username = self.Customer_username)
        else:    
            df_orders = pd.read_excel("csv_files/orders.xlsx")

            item_name = self.item_name
            item_price = self.item_price
            
            # Order_Id | Username | Item_Name | Customized | Item_Price |Tracking Order | Date order processed 
            # | Delivery_Company_Assigned | Home address | Order_Status

            df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ]

            if len(df_user_shopping_cart) == 0: # we do not have any items in the user shopping cart
            
                #----------------Generate a new random tracking order---------------------------------------
                random_number = str( random.random() +1 ).split(".")[1]
                letters = string.ascii_lowercase 
                random_str = ''.join(random.choice(letters) for i in range(6))
                tracking_order = ''.join(random.choice( random_str + random_number) for i in range(26) )
                tracking_order += str(self.Customer_Id)
                #--------------------------------------------------------------------------------------
            else: # we have items in the user shopping cart 
                # no need of generating a new tracking order
                tracking_order = df_user_shopping_cart['Tracking Order'].iloc[-1]
                
            order_id = len(df_orders)
            tempo = pd.DataFrame( [[ order_id, self.Customer_username, item_name, "Default" ,item_price, tracking_order, "empty", "empty", "empty","in cart" ]],
                            columns = ["Order_Id", "Username", "Item_Name", "Customized" ,"Item_Price", "Tracking Order", "Date order processed", "Delivery_Company_Assigned", "Home address", "Order_Status"])

            df_orders = df_orders.append(tempo)
            df_orders.to_excel( "csv_files/orders.xlsx", index = False)



        #-----------------Check out Section----------------------
            image_tempo = Image.open( f"images/checkout.png" )
            image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
            self.checkout_pic = ImageTk.PhotoImage(  image_tempo )
            
            df_orders = pd.read_excel("csv_files/orders.xlsx")

            df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ]

            items_in_cart = len(df_user_shopping_cart)
            if items_in_cart == 0: 

                checkout_button = tk.Button(self.top, 
                    command = self.command_checkout,
                    text = "", image = self.checkout_pic,
                    compound = "bottom")
                checkout_button.place(relx = 0.77, rely= 0.05, relwidth= 0.07, relheight=0.1)
            else:
                checkout_button = tk.Button(self.top, 
                    command = self.command_checkout,
                    text = f"{items_in_cart} items", image = self.checkout_pic,
                    compound = "bottom")
                checkout_button.place(relx = 0.77, rely= 0.05, relwidth= 0.07, relheight=0.1)
        
        #----------------------------------------------------------
            



    def command_checkout(self):
        df2 =  pd.read_excel( "csv_files/registered_customers.xlsx" )

        df_user = df2[ df2['Username'] == self.Customer_username]

        if df_user['Credit card account'].iloc[-1] == 'empty':
            tk.messagebox.showerror( "Error", 
                    "There is no credit card linked to your account.\n" + 
                    "A credit card account is necessary for making a purchase" )
        elif float(df_user['Balance'].iloc[-1] ) == 0.00:
            tk.messagebox.showerror("Error",
                    "Your current balance is $ 0.00\n" + 
                    "Go to Settings to provide funds to your account")
        else:
            self.top.destroy()
            check_out.check_out(coming_from = self.coming_from_page, 
                    item_name = self.item_name, customer_name = self.Customer_Name, 
                    customer_Id = self.Customer_Id, 
                    customer_username = self.Customer_username) 
        

    def command_post_review(self):
        
        df_orders = pd.read_excel( "csv_files/orders.xlsx" )
        
        
        df_user_history = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] != "in cart") & (df_orders['Order_Status'] != "cancelled") ]
        
        
        if self.item_name not in list(df_user_history["Item_Name"] ):
            tk.messagebox.showerror( "Error", "Before posting a review on an item " +
              "you need to purchase it" )
        else:
            self.top.destroy()
            discussion_page.discussion_page(coming_from = self.coming_from_page, 
            item_name = self.item_name, customer_name = self.Customer_Name, 
            customer_Id = self.Customer_Id, customer_username = self.Customer_username,
			master = None)


