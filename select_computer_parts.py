import tkinter as tk
import tkinter.ttk as ttk 

from PIL import ImageTk, Image 

import numpy as np
import pandas as pd
import string, random # to generate random tracking orders

import generalized_item


class select_computer_parts(tk.Frame):

    def __init__(self,my_geometry,coming_from, item_arch , item_name, item_price, 
        item_type, item_CPU, item_GPU, item_purpose,
         customer_name, customer_Id, customer_username, master = None):
                     # New page to select the parts for the computer
        tk.Frame.__init__(self, master)
        self.my_geometry = my_geometry
        #self.master.title( f"Choose Computer Parts Page" )
        #self.master.geometry( self.my_geometry )
        
        #--computer_info 
        self.item_name = item_name
        self.item_price = item_price
        self.item_type = item_type
        self.item_CPU = item_CPU
        self.item_GPU = item_GPU
        self.item_purpose = item_purpose
        self.item_arch = item_arch
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

        if self.item_purpose.lower() == "gaming" or self.item_type.lower() == "workstation":
            self.type_of_batteries = [ "Default Durable Type (+$0.00)", 
                                "Highly Durable Type (+$25.00)" ]
        elif self.item_GPU in ["AMD Radeon™ Graphics", "Intel® Iris® Xe Graphics",
                            "NVIDIA® GeForce®", "Integrated PowerVR GX6250", "NVIDIA® Graphics",
                            "Radeon Pro"]:
            self.type_of_batteries = [ "Default Durable Type (+$0.00)", 
                            "Highly Durable Type (+$25.00)" ]
        else:
            self.type_of_batteries = [ "Regular Type (+$0.00)", "Durable Type (+$25.00)",
                            "Highly Durable Type (+$50.00)"  ]
            
        self.combobox_battery = tk.ttk.Combobox(self.top, value = self.type_of_batteries, 
                    width = 15)

        self.combobox_battery.set(self.type_of_batteries[0])
        self.combobox_battery["state"] = 'readonly'
        self.combobox_battery.place( relx = 0.45, rely = 0.1, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose Screen resolution-----------------------------------------
        self.LabelScreen = tk.Label(self.top, text = "Screen Resolution: ", 
                            background = "light blue")
        self.LabelScreen.place( relx = 0.2, rely = 0.2, relwidth = 0.21, relheight = 0.04)

        if self.item_purpose.lower() == "gaming":
            self.type_of_screen = [ "Default 4k(Ultra HD) (+$0.00)", 
                        "8k (+$25.00)", "10k (+$50.00)"]
        else:
            self.type_of_screen = [ "Default FHD (+$0.00)", "2k(Quad HD) (+$25.00)",
                        "4k(Ultra HD) (+$50.00)","8k (+$75.00)"]
            
        self.combobox_screen = tk.ttk.Combobox(self.top, value = self.type_of_screen, 
                    width = 15)
        self.combobox_screen.set(self.type_of_screen[0])
        self.combobox_screen["state"] = 'readonly'
        self.combobox_screen.place( relx = 0.45, rely = 0.2, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose Extra RAM-----------------------------------------
        self.LabelRAM = tk.Label(self.top, text = "Extra RAM: ", 
                            background = "light blue")
        self.LabelRAM.place( relx = 0.2, rely = 0.3, relwidth = 0.21, relheight = 0.04)

        self.type_of_RAM = [ "No extra RAM (+$0.00)", "Extra 8 GB (+$25.00)",
                             "Extra 16 GB (+$50.00)" ]
        
        self.combobox_RAM = tk.ttk.Combobox(self.top, value = self.type_of_RAM, 
                    width = 15)
        self.combobox_RAM.set(self.type_of_RAM[0])
        self.combobox_RAM["state"] = 'readonly'
        self.combobox_RAM.place( relx = 0.45, rely = 0.3, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        

        #-----------------------------Choose Hard Disk Memory--------------------------------------
        self.LabelHardDisk = tk.Label(self.top, text = "Hard Disk storage: ", 
                            background = "light blue")
        self.LabelHardDisk.place( relx = 0.2, rely = 0.4, relwidth = 0.21, relheight = 0.04)

        self.type_of_HardDisk = [ "Regular (+$0.00)", "Extra 1TB (+$50.00)",
                             "Extra 2TB (+$100.00)"] 
        
        
        self.combobox_HardDisk = tk.ttk.Combobox(self.top, value = self.type_of_HardDisk, 
                    width = 15)
        self.combobox_HardDisk.set(self.type_of_HardDisk[0])
        self.combobox_HardDisk["state"] = 'readonly'
        self.combobox_HardDisk.place( relx = 0.45, rely = 0.4, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose GPU--------------------------------------

        self.LabelGPU = tk.Label(self.top, text = "GPU: ", 
                            background = "light blue")
        self.LabelGPU.place( relx = 0.2, rely = 0.5, relwidth = 0.21, relheight = 0.04)

        if self.item_purpose.lower() == "gaming": # self.item_GPU
            
            if self.item_arch == "AMD Ryzen":
                list_GPU = ['NVIDIA® GeForce®', 'Radeon Pro', 'ATI Mobility Radeon',
                            'AMD Radeon™ Graphics',
                            'NVIDIA® GeForce® RTX™', 'NVIDIA® GeForce® GTX',
                            'NVIDIA® Graphics', 'NVIDIA® GTX'
                            ]
            else:
                list_GPU = ['NVIDIA® GeForce®', 'Intel® Iris® Xe Graphics',
                            'NVIDIA® GeForce® RTX™', 'NVIDIA® GeForce® GTX',
                            'NVIDIA® Graphics', 'NVIDIA® GTX'
                           ]
            
            self.type_of_GPU = [ f"Default {self.item_GPU} (+$0.00)" ]
            for gpu in list_GPU:
                if self.item_GPU != gpu:
                    self.type_of_GPU.append(f"{gpu} (+$250.00)")
        else:
            if self.item_arch == "AMD Ryzen":  
                list_GPU = ['NVIDIA® GeForce®','NVIDIA® Quadro®','AMD Radeon™ Graphics',
                            'NVIDIA® GeForce® RTX™','ATI Mobility Radeon','ATI Radeon HD 5670',
                            'Radeon Pro', 'NVIDIA® GeForce® GTX',
                            'NVIDIA® Graphics', 'NVIDIA® GTX']
            else:
                list_GPU = ['NVIDIA® GeForce®','NVIDIA® Quadro®',
                            'Intel® UHD Graphics', 'Intel® Iris® Xe Graphics', 
                            'NVIDIA® GeForce® RTX™','NVIDIA® GeForce® GTX',
                            'NVIDIA® Graphics','NVIDIA® GTX']
            
            self.type_of_GPU = [ f"Default {self.item_GPU} (+$0.00)" ]
            for gpu in list_GPU:
                if gpu != self.item_GPU:
                    self.type_of_GPU.append(f"{gpu} (+$250.00)")

        self.combobox_GPU = tk.ttk.Combobox(self.top, value = self.type_of_GPU, 
                    width = 15)
        
        
        self.combobox_GPU.set(self.type_of_GPU[0])
        self.combobox_GPU["state"] = 'readonly'
        self.combobox_GPU.place( relx = 0.45, rely = 0.5, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------


        #-----------------------------Choose CPU--------------------------------------
        self.LabelCPU = tk.Label(self.top, text = "CPU cores: ", 
                            background = "light blue")
        self.LabelCPU.place( relx = 0.2, rely = 0.6, relwidth = 0.21, relheight = 0.04)

        if self.item_type.lower() == "Laptop".lower() or self.item_type.lower() == "Desktop".lower() :
            start_CPU = self.item_CPU 
            self.type_of_CPU = [f"Default {start_CPU} cores (+$0.00)"]
            price = 0.00
            for i in range(start_CPU +2, 10, 2):
                price += 100
                price_f = "${:,.2f}".format(price)
                self.type_of_CPU.append( f"{i} cores (+{price_f})"  )
        elif self.item_type.lower() == "workstation".lower() and int(self.item_CPU) >= 10:
            start_CPU = self.item_CPU - 6
            self.type_of_CPU = [f"Default {start_CPU} cores (+$0.00)"]
            price = 0.00 
            for i in range(start_CPU + 2, self.item_CPU +2,2):
                price += 100
                price_f = "${:,.2f}".format(price)
                self.type_of_CPU.append( f"{i} cores (+{price_f})" )
        elif self.item_type.lower() == "workstation".lower() and int( self.item_CPU) < 10:
            start_CPU = self.item_CPU 
            self.type_of_CPU = [f"Default {start_CPU} cores (+$0.00)"]
            price = 0.00
            for i in range(start_CPU +2, 10, 2):
                price += 100
                price_f = "${:,.2f}".format(price)
                self.type_of_CPU.append( f"{i} cores (+{price_f})"  )


        self.combobox_CPU = tk.ttk.Combobox(self.top, value = self.type_of_CPU, 
                    width = 15)

        self.combobox_CPU.set(self.type_of_CPU[0])
        self.combobox_CPU["state"] = 'readonly'
        self.combobox_CPU.place( relx = 0.45, rely = 0.6, relwidth = 0.47, relheight = 0.04)
        #---------------------------------------------------------------------------------------



        #----------------------------Confirm Button------------------------------------------
        self.Button_confirm = tk.Button ( self.top, text = "Confirm", bg = "light green",
          command = self.Command_confirm)
        self.Button_confirm.place( relx = 0.25, rely = 0.7, relwidth = 0.1, relheight = 0.05 )
        #------------------------------------------------------------------------------------

        
        #----------------------------Cancel Button------------------------------------------
        self.Button_cancel = tk.Button ( self.top, text = "Cancel", bg = "red",
          command = self.Command_cancel)
        self.Button_cancel.place( relx = 0.55, rely = 0.7, relwidth = 0.1, relheight = 0.05 )
        #------------------------------------------------------------------------------------




    def Command_confirm(self):
        battery_choice = self.combobox_battery.get()     # 1.
        screen_choice  = self.combobox_screen.get()      # 2.
        RAM_choice = self.combobox_RAM.get()             # 3.
        Hard_disk_choice = self.combobox_HardDisk.get()  # 4.
        GPU_choice = self.combobox_GPU.get()             # 5.
        CPU_choice = self.combobox_CPU.get()             # 6.

        tempo_GPU, tempo_screen, tempo_battery = self.auxiliary_get_gpu_screen_battery( GPU_choice,
                                        screen_choice, battery_choice)

        '''
            GPU_choices = [ 'NVIDIA® GeForce®', 'NVIDIA® Quadro®','AMD Radeon™ Graphics',
                        'Intel® UHD Graphics',  'Integrated PowerVR GX6250',
                        'Intel® Iris® Xe Graphics', 'NVIDIA® GeForce® RTX™',
                        'ATI Mobility Radeon',  'ATI Radeon HD 5670',
                        'Radeon Pro',   'NVIDIA® GeForce® GTX',
                        'NVIDIA® Graphics', 'NVIDIA® GTX' ]

            screen_choices = ['FHD', '2k(Quad HD)', '4k(Ultra HD)', '8k', '10k']

            battery_choices = [ 'Regular Type', 'Durable Type', 'Highly Durable Type' ]
        '''       
        flag_invalid_choice = False
        if tempo_GPU in ['NVIDIA® Quadro®', 'Intel® UHD Graphics', 'ATI Radeon HD 5670' ]:
            if tempo_screen in ['4k(Ultra HD)', '8k', '10k']:
                flag_invalid_choice = True
                self.top.destroy()
                tk.messagebox.showerror( "Constraint", 
                f"You need a more powerful GPU for that screen resolution {tempo_screen}.")
        
        elif tempo_GPU in [ 'NVIDIA® Quadro®','AMD Radeon™ Graphics',
                'Intel® UHD Graphics',  'Integrated PowerVR GX6250', 'Intel® Iris® Xe Graphics', 
                'ATI Mobility Radeon',  'ATI Radeon HD 5670', 'NVIDIA® Graphics' ]:
            
            if tempo_screen in ['8k', '10k']:
                flag_invalid_choice = True
                self.top.destroy()
                tk.messagebox.showerror( "Constraint", 
                f"You need a more powerful GPU for that screen resolution {tempo_screen}." )

        elif tempo_GPU in ['NVIDIA® GeForce®', 'NVIDIA® Quadro®','AMD Radeon™ Graphics',
                        'Intel® UHD Graphics',  'Integrated PowerVR GX6250',
                        'Intel® Iris® Xe Graphics', 'ATI Mobility Radeon',  'ATI Radeon HD 5670',
                        'Radeon Pro', 'NVIDIA® Graphics', 'NVIDIA® GTX' ]:
            if tempo_screen in ['10k']:
                flag_invalid_choice = True
                self.top.destroy()
                tk.messagebox.showerror("Constraint",
                f"You need a more powerful GPU for that screen resolution {tempo_screen}.")


        if tempo_GPU in [ 'NVIDIA® GeForce®','AMD Radeon™ Graphics',
                        'Integrated PowerVR GX6250',
                        'Intel® Iris® Xe Graphics', 'NVIDIA® GeForce® RTX™',
                        'ATI Mobility Radeon', 'Radeon Pro', 'NVIDIA® GeForce® GTX',
                        'NVIDIA® Graphics', 'NVIDIA® GTX']:
            if tempo_battery in ['Regular Type']:
                flag_invalid_choice = True
                self.top.destroy()
                tk.messagebox.showerror( "Constraint", 
                "You need a more powerful battery for that\n" +
                f"GPU selected {tempo_GPU}.")
        '''
        elif tempo_GPU in ['NVIDIA® GeForce® RTX™', 'NVIDIA® GeForce® GTX' ]:
            if tempo_battery in ['Regular Type', 'Durable Type']:
                flag_invalid_choice = True
                self.top.destroy()
                tk.messagebox.showerror( "Constraint",
                "You need a more powerful battery for that\n" +
                f"GPU selected {tempo_GPU}." )
        '''
        if not flag_invalid_choice:
            self.additional_price = 0 
            '''
                    self.type_of_batteries: 25
                    self.type_of_screen:    25
                    self.type_of_RAM:       25
                    self.type_of_HardDisk:  50
                    self.type_of_GPU: each 250     
                    self.type_of_CPU:      100
            '''
        
            for i in range( len(self.type_of_batteries) ): 
                if self.type_of_batteries[i] == battery_choice:
                    add_ = 25*i
                    self.additional_price += add_
                    break 

            for i in range( len(self.type_of_screen) ): 
                if self.type_of_screen[i] == screen_choice:
                    add_ = 25*i
                    self.additional_price += add_
                    break 

            for i in range( len(self.type_of_RAM) ): 
                if self.type_of_RAM[i] == RAM_choice:
                    add_ = 25*i
                    self.additional_price += add_
                    break 

            for i in range( len(self.type_of_HardDisk) ): 
                if self.type_of_HardDisk[i] == Hard_disk_choice:
                    add_ = 50*i
                    self.additional_price += add_
                    break 

            
            for i in range( len(self.type_of_GPU) ): 
                if self.type_of_GPU[i] == GPU_choice and i != 0:
                    add_ = 250
                    self.additional_price += add_
                    break 

            for i in range( len(self.type_of_CPU) ): 
                if self.type_of_CPU[i] == CPU_choice:
                    add_ = 100*i
                    self.additional_price += add_
                    break 





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
        
    
    def auxiliary_get_gpu_screen_battery(self, GPU_choice, screen_choice, battery_choice):
        
        tempo_ = GPU_choice.split()
        tempo_GPU = ""

        for word in tempo_:
            if word != "Default" and word != "(+$250.00)" and word != "(+$0.00)":
                tempo_GPU += word + " "

        tempo_GPU = tempo_GPU.strip()

        tempo_ = battery_choice.split()
        tempo_battery = ""

        for word in tempo_:
            if word != "Default" and word != "(+$0.00)" and word != "(+$25.00)" and word != "(+$50.00)":
                tempo_battery += word + " "

        tempo_battery = tempo_battery.strip()

        
        tempo_ = screen_choice.split()
        tempo_screen = ""

        for word in tempo_:
            if word != "Default" and word != "(+$0.00)" and word != "(+$25.00)" and word != "(+$50.00)" and word != "(+$75.00)":
                tempo_screen += word + " "
        
        tempo_screen = tempo_screen.strip()
        
        return tempo_GPU, tempo_screen, tempo_battery
