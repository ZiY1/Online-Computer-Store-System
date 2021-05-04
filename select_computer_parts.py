import tkinter as tk
import tkinter.ttk as ttk 

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd
import string, random # to generate random tracking orders

import generalized_item


class select_computer_parts(tk.Frame):

    def __init__(self,my_geometry,coming_from, item_name, item_price, 
         customer_name, customer_Id, customer_username, master = None):
                     # New page to select the parts for the computer
        tk.Frame.__init__(self, master)
        self.my_geometry = my_geometry
        #self.master.title( f"Choose Computer Parts Page" )
        #self.master.geometry( self.my_geometry )
        
        #--computer_info 
        self.item_name = item_name
        self.item_price = item_price

        #---User_info
        self.Customer_Name = customer_name
        self.Customer_Id = customer_Id
        self.Customer_username = customer_username

        self.coming_from = coming_from 

        
        self.create_widgets()



    def create_widgets(self):
        self.top = tk.Toplevel()
        self.top.geometry(newGeometry = self.my_geometry)
        self.top.title("Choose Computer Parts")
        self.top.configure( background = "light blue")
        self.style = tk.ttk.Style()

        self.style.configure( "LabelTitle.TLabel", 
                               relief = tk.SUNKEN, 
                               anchor = "left", 
                               font = ("Helvetica", 10),
                               background = '#49A'    
                            )

        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "Choose Parts", 
                                        style = "LabelTitle.TLabel" 
                                        )

        self.LabelTitle.place( relx = 0.4, rely = 0, 
                            relwidth = 0.25 , relheight = 0.07 
                        )


        #-----------------------------Choose Battery type-----------------------------------------
        self.LabelBattery = tk.Label(self.top, text = "Type of Battery: ", 
                            background = "light blue")
        self.LabelBattery.place( relx = 0.2, rely = 0.1, relwidth = 0.21, relheight = 0.04)

        self.type_of_batteries = [ "Regular Type (+$0.00)", "Durable Type (+$25.00)",
                             "Highly Durable Type (+$50.00)"  ]
        
        self.combobox_battery = tk.ttk.Combobox(self.top, value = self.type_of_batteries, 
                    width = 15)
        self.combobox_battery.set(self.type_of_batteries[0])
        self.combobox_battery["state"] = 'readonly'
        self.combobox_battery.place( relx = 0.45, rely = 0.1, relwidth = 0.34, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose Screen size-----------------------------------------
        self.LabelScreen = tk.Label(self.top, text = "Screen Resolution: ", 
                            background = "light blue")
        self.LabelScreen.place( relx = 0.2, rely = 0.2, relwidth = 0.21, relheight = 0.04)

        self.type_of_screen = [ "Regular resolution (+$0.00)", "4k(Ultra HD) (+$25.00)",
                             "8k (+$50.00)", "10k (+$75.00)"  ]
        
        self.combobox_screen = tk.ttk.Combobox(self.top, value = self.type_of_screen, 
                    width = 15)
        self.combobox_screen.set(self.type_of_screen[0])
        self.combobox_screen["state"] = 'readonly'
        self.combobox_screen.place( relx = 0.45, rely = 0.2, relwidth = 0.34, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose Extra RAM-----------------------------------------
        self.LabelRAM = tk.Label(self.top, text = "Extra RAM: ", 
                            background = "light blue")
        self.LabelRAM.place( relx = 0.2, rely = 0.3, relwidth = 0.21, relheight = 0.04)

        self.type_of_RAM = [ "No extra RAM (+$0.00)", "Extra 8 GB (+$25.00)",
                             "Extra 32 GB (+$50.00)", "Extra 64 GB (+$75.00)"  ]
        
        self.combobox_RAM = tk.ttk.Combobox(self.top, value = self.type_of_RAM, 
                    width = 15)
        self.combobox_RAM.set(self.type_of_RAM[0])
        self.combobox_RAM["state"] = 'readonly'
        self.combobox_RAM.place( relx = 0.45, rely = 0.3, relwidth = 0.34, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        

        #-----------------------------Choose Hard Disk Memory--------------------------------------
        self.LabelHardDisk = tk.Label(self.top, text = "Hard Disk storage: ", 
                            background = "light blue")
        self.LabelHardDisk.place( relx = 0.2, rely = 0.4, relwidth = 0.21, relheight = 0.04)

        self.type_of_HardDisk = [ "Regular (+$0.00)", "Extra 1 TB (+$50.00)",
                             "Extra 2 TB (+$100.00)"] 
        
        self.combobox_HardDisk = tk.ttk.Combobox(self.top, value = self.type_of_HardDisk, 
                    width = 15)
        self.combobox_HardDisk.set(self.type_of_HardDisk[0])
        self.combobox_HardDisk["state"] = 'readonly'
        self.combobox_HardDisk.place( relx = 0.45, rely = 0.4, relwidth = 0.34, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose GPU--------------------------------------
        self.LabelGPU = tk.Label(self.top, text = "GPU: ", 
                            background = "light blue")
        self.LabelGPU.place( relx = 0.2, rely = 0.5, relwidth = 0.21, relheight = 0.04)

        self.type_of_GPU = [ "Regular (+$0.00)", "Powerful GPU(+$250.00)"]
        
        self.combobox_GPU = tk.ttk.Combobox(self.top, value = self.type_of_GPU, 
                    width = 15)
        self.combobox_GPU.set(self.type_of_GPU[0])
        self.combobox_GPU["state"] = 'readonly'
        self.combobox_GPU.place( relx = 0.45, rely = 0.5, relwidth = 0.34, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #----------------------------Confirm Button------------------------------------------
        self.Button_confirm = tk.Button ( self.top, text = "Confirm", bg = "light green",
          command = self.Command_confirm)
        self.Button_confirm.place( relx = 0.25, rely = 0.6, relwidth = 0.1, relheight = 0.05 )
        #------------------------------------------------------------------------------------

        
        #----------------------------Cancel Button------------------------------------------
        self.Button_cancel = tk.Button ( self.top, text = "Cancel", bg = "red",
          command = self.Command_cancel)
        self.Button_cancel.place( relx = 0.55, rely = 0.6, relwidth = 0.1, relheight = 0.05 )
        #------------------------------------------------------------------------------------




    def Command_confirm(self):
        battery_choice = self.combobox_battery.get()
        screen_choice  = self.combobox_screen.get()
        RAM_choice = self.combobox_RAM.get()
        Hard_disk_choice = self.combobox_HardDisk.get()
        GPU_choice = self.combobox_GPU.get()

        self.additional_price = 0 
        '''
        self.type_of_batteries = [ "Regular Type (+$0.00)", "Durable Type (+$25.00)",
                             "Highly Durable Type (+$50.00)"  ]

        self.type_of_screen = [ "Regular resolution (+$0.00)", "4k(Ultra HD) (+$25.00)",
                             "8k (+$50.00)", "10k (+$75.00)"  ]
        
        self.type_of_RAM = [ "No extra RAM (+$0.00)", "Extra 8 GB (+$25.00)","Extra 32 GB (+$50.00)", "Extra 64 GB (+$75.00)"  ]

        self.type_of_HardDisk = [ "Regular (+$0.00)", "Extra 1 TB (+$50.00)",
                             "Extra 2 TB (+$100.00)"] 
        
        self.type_of_GPU = [ "Regular (+$0.00)", "Powerful GPU(+$250.00)"]
        '''

        if battery_choice == "Regular Type (+$0.00)":
            self.additional_price += 0 
        elif battery_choice == "Durable Type (+$25.00)":
            self.additional_price += 25.00
        elif battery_choice == "Highly Durable Type (+$50.00)":
            self.additional_price += 50.00

        if screen_choice == "Regular resolution (+$0.00)":
            self.additional_price += 0 
        elif screen_choice == "4k(Ultra HD) (+$25.00)":
            self.additional_price += 25.00
        elif screen_choice == "8k (+$50.00)":
            self.additional_price += 50.00
        elif screen_choice == "10k (+$75.00)":
            self.additional_price += 75.00

        if RAM_choice == "No extra RAM (+$0.00)":
            self.additional_price += 0 
        elif RAM_choice == "Extra 8 GB (+$25.00)":
            self.additional_price += 25.00
        elif RAM_choice == "Extra 32 GB (+$50.00)":
            self.additional_price += 50.00
        elif RAM_choice == "Extra 64 GB (+$75.00)":
            self.additional_price += 75.00

        if Hard_disk_choice == "Regular (+$0.00)":
            self.additional_price += 0
        elif Hard_disk_choice == "Extra 1 TB (+$50.00)":
            self.additional_price += 50.00
        elif Hard_disk_choice == "Extra 2 TB (+$100.00)":
            self.additional_price += 100.00 

        
        if GPU_choice == "Regular (+$0.00)":
            self.additional_price += 0
        elif GPU_choice == "Powerful GPU(+$250.00)":
            self.additional_price += 250.00


        df_orders = pd.read_excel("csv_files/orders.xlsx")

        item_name = self.item_name
        item_price = self.item_price
        
        # Order_Id | Username | Item_Name | Tracking Order | Date order processed 
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
            
        customized = "Customized" if self.additional_price > 0 else "Default"
        order_id = len(df_orders)
        tempo = pd.DataFrame( [[ order_id, self.Customer_username, item_name, customized ,item_price + self.additional_price, tracking_order, "empty", "empty", "empty","in cart" ]],
                        columns = ["Order_Id", "Username", "Item_Name","Customized" ,"Item_Price", "Tracking Order", "Date order processed", "Delivery_Company_Assigned", "Home address", "Order_Status"])

        df_orders = df_orders.append(tempo)
        df_orders.to_excel( "csv_files/orders.xlsx", index = False)


        self.top.destroy()
        
        generalized_item.generalized_item(coming_from = self.coming_from,
                item_name = self.item_name, 
                customer_name = self.Customer_Name, 
                customer_Id = self.Customer_Id, customer_username = self.Customer_username)

    
    def Command_cancel(self):
        self.top.destroy()
        