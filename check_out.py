import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

import datetime

# python script 
import customer_page 
import generalized_item


class check_out(tk.Frame):

    def __init__(self,  coming_from = None, item_name = None, customer_name = None, 
                     customer_Id = None, customer_username = None, master = None):
        tk.Frame.__init__(self,master)

        self.master.title( "Check out Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue")

        # User-info account 
        self.Customer_Id = customer_Id 
        self.Customer_Name  = customer_name
        self.Customer_username = customer_username
        
        # Back page coming from 
        self.coming_from_page = coming_from


        # item name 
        self.item_name = item_name


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


        df_orders = pd.read_excel( "csv_files/orders.xlsx" )
        df_items = pd.read_excel( "csv_files/items.xlsx" )
        df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ]
        
        total = df_user_shopping_cart['Item_Price'].sum()
        self.total_sum = float(total)
        self.total = "{:,.2f}".format(total)
        self.total_items = len(df_user_shopping_cart)

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
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )

        self.LabelTitle = tk.ttk.Label( self.second_frame, 
                                           text = f"Check out page\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )
        self.LabelTitle.grid( row = 0, column = 3, columnspan = 1, rowspan = 1,
             padx = 30)
        #-----------------------------------------------------------------------------

        #---------shopping cart section-------------------------------------------

        self.style.configure( "LabelShopping.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 36,"bold"),
                               background = 'light blue'    
                            )

        self.LabelShopping = tk.ttk.Label( self.second_frame, 
                                           text = f"Shopping cart:", 
                                           style = "LabelShopping.TLabel" 
                                          )

        self.LabelShopping.grid( row = 5, column = 0)
        #-------------------------------------------------------------------------------

        #---------label shopping cart section-------------------------------------------

        self.style.configure( "LabelShopp.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 26, "bold"),
                               background = 'light blue'    
                            )

        self.LabelItem = tk.ttk.Label( self.second_frame, 
                                           text = "   Item", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelItem.grid( row = 6, column = 0, columnspan = 1)

        self.LabelPrice = tk.ttk.Label( self.second_frame, 
                                           text = "  Price", 
                                           style = "LabelShopp.TLabel" 
                                          )
        self.LabelPrice.grid( row = 6, column = 1, columnspan = 1)
        

        #-------------------------------------------------------------------------------
    




        self.images = list()
        self.remove_buttons = list()
        self.images_delete = list()
        self.label_images = list()
        for i in range( len(df_user_shopping_cart)):
            #tk.Button(second_frame, text = f"Button {thing}").grid( row = thing, column = 0)
            item_name = df_user_shopping_cart['Item_Name'].iloc[i]
            item_price = df_user_shopping_cart['Item_Price'].iloc[i]
            item_price = "$ {:,.2f}".format(item_price)
            item_type = df_items[df_items['Name'] == item_name ]['Type'].iloc[-1]
            item_customized = df_user_shopping_cart['Customized'].iloc[i]
            
            custom = "\n(Customized)" if item_customized == "Customized" else ""
            
            image_tempo2 = Image.open( f"images/icons/garbage_can.png" )
            image_tempo2 = image_tempo2.resize( (25,25), Image.ANTIALIAS )
            self.images_delete.append(None)
            self.images_delete[i] = ImageTk.PhotoImage( image_tempo2)

            self.remove_buttons.append(None)
            self.remove_buttons[i] = tk.Button( self.second_frame, text = "remove", 
            image = self.images_delete[i], 
            command = lambda name = item_name: self.remove_from_cart(name), compound = "left")

            self.remove_buttons[i].grid( row = 7 + i, column = 3 )

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

            self.images.append(None)
            self.images[i] = ImageTk.PhotoImage( image_tempo  )
            self.style.configure( "Label_imag.TLabel", 
                               anchor = "left", 
                               font = ("Bold", 16),
                               background = 'light blue'    
                            )
             
            self.label_images.append(None)
            self.label_images[i] = tk.Label( self.second_frame, text = f"{item_name}" + custom, 
                    image = self.images[i],
                    compound = tk.TOP,
                    font = "Bold").grid( row = 7 + i , column = 0, pady = 10 )
        
            self.LabelPrice = tk.ttk.Label(self.second_frame, text = f"{item_price}",
              font = "Bold", style =  "Label_imag.TLabel")

            self.LabelPrice.grid( row = 7 + i, column = 1)




        self.style.configure( "LastLabel.TLabel", 
                               anchor = "left", 
                               font = ("Bold", 26),
                               background = 'light blue'    
                            )        
        self.Last_label = tk.ttk.Label( self.second_frame, text = "",
                    style = "LastLabel.TLabel")
        self.Last_label.grid( row = 7 + len(df_user_shopping_cart) + 5, column = 2, 
                            pady = 100)


        self.style.configure( "Labelsubtotal.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 20, "bold"),
                               background = 'light blue'    
                            )

        self.LabelTotal = tk.ttk.Label( self.second_frame, 
                                           text = f"Subtotal ({self.total_items} items):", 
                                           style = "Labelsubtotal.TLabel" 
                                          )
        self.LabelTotal.grid( row = 7 + len(df_user_shopping_cart), column = 0, columnspan = 1)
        
        self.LabelTotal2 = tk.ttk.Label( self.second_frame, 
                                           text = f"$ {self.total}", 
                                           style = "Labelsubtotal.TLabel" 
                                          )
        self.LabelTotal2.grid( row = 7 + len(df_user_shopping_cart), column = 1, columnspan = 1)
        

        if( len(df_user_shopping_cart) == 0  ):
            
            image_tempo3 = Image.open( f"images/icons/sad_computer.png" )
            image_tempo3 = image_tempo3.resize( (120,120), Image.ANTIALIAS )
            
            self.sad_computer = ImageTk.PhotoImage( image_tempo3)
            self.sad_computer.image = image_tempo3
            sad_computer_label = tk.Label( self.second_frame, 
                        text = "Shopping cart empty",font = "Bold",
                        image = self.sad_computer, compound = tk.TOP)
            
            sad_computer_label.grid( row = 10, column = 3, pady = 20 )
        else:
            self.button_place_order = tk.Button( self.second_frame, 
                    text = "Place order", bg = "light goldenrod",
                    height = 2, width = 30,
                    command = self.place_order )    
            
            self.button_place_order.grid( row = 7 + len(df_user_shopping_cart),
                     column = 3)



        #------------------------Go Back section--------------------------------

        
        image_tempo3 = Image.open( f"images/icons/go_back.png" )
        image_tempo3 = image_tempo3.resize( (25,25), Image.ANTIALIAS )
        
        self.image_back = ImageTk.PhotoImage( image_tempo3)

        self.back_button = tk.Button( self.second_frame, text = "Back     ", 
                                        image = self.image_back, 
                                        command = self.go_back, compound = "left")
        self.back_button.grid( row = 0, column = 7 )   
                     
        #------------------------------------------------------------------------



    def remove_from_cart(self,item_name):
        df_orders = pd.read_excel( "csv_files/orders.xlsx" )
        df_items = pd.read_excel( "csv_files/items.xlsx" )
        df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.Customer_username) 
        & (df_orders['Order_Status'] == "in cart") & (df_orders["Item_Name"] == item_name )]

        df_user_shopping_cart.loc[:, ("Order_Status")].iloc[0] = "cancelled"
        
        df_orders[ (df_orders['Username'] == self.Customer_username) &
         (df_orders['Order_Status'] == 'in cart') & 
         (df_orders['Item_Name'] == item_name) ] = df_user_shopping_cart

        df_orders.to_excel( "csv_files/orders.xlsx", index = False)

        df_orders2 = pd.read_excel( "csv_files/orders.xlsx" )
        df_items = pd.read_excel( "csv_files/items.xlsx" )
        
        df_user_shopping_cart2 = df_orders2[ (df_orders2["Username"] == self.Customer_username) & 
                (df_orders2['Order_Status'] == "in cart") ]
        
        self.master.destroy()

        check_out( coming_from = self.coming_from_page, 
                item_name = self.item_name, customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, customer_username = self.Customer_username)

         
        

    def go_back(self):

        self.master.destroy()        
        if self.coming_from_page == "Main_Page2":
            customer_page.customer_page(customer_name = self.Customer_Name,
                customer_username = self.Customer_username,
                customer_Id =  self.Customer_Id)
        else:
            generalized_item.generalized_item( coming_from = self.coming_from_page, 
                    item_name = self.item_name, customer_name = self.Customer_Name, 
                     customer_Id = self.Customer_Id, 
                     customer_username = self.Customer_username)
        

    def place_order(self):
        
        df_customers = pd.read_excel( "csv_files/registered_customers.xlsx" )

        df_user_info = df_customers[ df_customers['Username'] == self.Customer_username]
        
        user_Balance = float( df_user_info["Balance"].iloc[-1] ) 

        if float(self.total_sum) > user_Balance: # Not enough money
            price_ = "$ {:,.2f}".format(user_Balance)
            tk.messagebox.showerror( "Error", "You do not have enough funds to complete this order.\n" + 
                                    f"Your current funds:   {price_}" )
        else: # Complete the transaction and send the order to clerk and delivery companies
            
            #----------------------------Charge the user-------------------------------------
            df_user_info.loc[:,("Balance")] = user_Balance - self.total_sum 
            df_customers[ df_customers['Username'] == self.Customer_username] = df_user_info
            df_customers.to_excel( "csv_files/registered_customers.xlsx", index = False)
            #--------------------------------------------------------------------------------

            #-------------Place the in-cart orders in processing status----------------------
            df_orders = pd.read_excel( "csv_files/orders.xlsx" )
            df_customer_cart = df_orders[ (df_orders['Username'] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ]
            df_update_sales = df_customer_cart            
            df_customer_cart.loc[:,('Order_Status')] = "processing"
            now = datetime.datetime.now()
            date_processed = now.strftime("%m/%d/%Y, %H:%M:%S")

            df_customer_cart.loc[:,('Date order processed')] = date_processed
            df_orders[ (df_orders['Username'] == self.Customer_username) & (df_orders['Order_Status'] == "in cart") ] = df_customer_cart
            df_orders.to_excel( "csv_files/orders.xlsx", index = False)
            #--------------------------------------------------------------------------------

            #---------------------------Update the number of sales--------------------------------
            df_items = pd.read_excel("csv_files/items.xlsx")

            for i in range( len(df_update_sales)):
                item_sold = df_update_sales['Item_Name'].iloc[i]
                tempo_df = df_items[ df_items['Name'] == item_sold]
                tempo_df['Number of Sales'] += 1
                df_items[ df_items['Name'] == item_sold] = tempo_df
            df_items.to_excel("csv_files/items.xlsx", index = False)
            #-------------------------------------------------------------------------------


            #---------------------Send "email" receipt to customer---------------------
            now = datetime.datetime.now()
            date_send = now.strftime("%m/%d/%Y, %H:%M:%S")

            message1 = f"Dear {self.Customer_Name},\n\n"
            message2 = "Your Order has been placed. Here are the details of your order. Our delivery team will notify you once your package arrives.\n"
            message3 = "In the meantime, you can track your order by the tracking order.\n"
            #df_customer_cart
            track_order = df_customer_cart["Tracking Order"].iloc[-1]
            total_sum = float ( df_customer_cart["Item_Price"].sum() )

            
            total_sum = "$ {:,.2f}".format(total_sum)
            message4 = f"\t\t\t\tTracking Order: {track_order}\n"
            
            message5 = "\t\t{0}\t\t\t\t\t\t\t{1}\n".format( "Item Name", "Item Price")
            message6 = ""
            
            for i in range( len(df_customer_cart) ):
                item = str ( df_customer_cart["Item_Name"].iloc[i])
                custom = str( df_customer_cart["Customized"].iloc[i] )
            
                custom = " (Customized)" if custom == "Customized" else ""
                price = float ( df_customer_cart["Item_Price"].iloc[i] )
                price = "$ {:,.2f}".format(price)
                
                name_printed = item + custom
                price += f"\t{len(name_printed)}"
                name_printed = name_printed + "\t\t" if len(name_printed) <= 30 else name_printed 
                message6 += "\t{0:<60s}\t\t\t{1:<20s}\n".format( name_printed, price )
                
            
            message7 = f"\t\t\t\t\t\t\t\t\t\tSubtotal:  {total_sum}"
            message8 = "\nThanks, Lenovo Team"
            message = message1 + message2 + message3 + message4 + message5 + message6 + message7 + message8 

            df_emails = pd.read_excel( "csv_files/emails.xlsx")
            
            Id = len(df_emails) 
            tempo = pd.DataFrame( [[Id, self.Customer_username, "Lenovo Store", date_send,"Order Placed", message,"unread"]],
                        columns = ['ID', 'for_username', 'From', 'Date_received', 'Subject', 'Message', 'Status'])
            df_emails = df_emails.append(tempo)

            df_emails.to_excel("csv_files/emails.xlsx", index = False)
            
            #-------------------------------------------------------------------------------


            #----------------------------Send the collected money to the manager-----------------
            df_staffs = pd.read_excel("csv_files/privileged_users.xlsx")
            df_manager = df_staffs[df_staffs["Username"] == "admin@lenovo.com" ]
            current_income = float ( df_manager["Income"].iloc[-1] )
            df_manager.loc[:,("Income")] = self.total_sum + current_income
            
            df_staffs[df_staffs["Username"] == "admin@lenovo.com"] = df_manager
            df_staffs.to_excel( "csv_files/privileged_users.xlsx", index = False )
            #----------------------------------------------------------------------------------







            #---------------------Show success message---------------------------------------
            tk.messagebox.showinfo("Success", "Your order has been placed.\n"+ 
                "You will receive an order receipt" )
            #--------------------------------------------------------------------------------


            self.master.destroy()

            check_out( coming_from = self.coming_from_page, 
                item_name = self.item_name, customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, customer_username = self.Customer_username)





