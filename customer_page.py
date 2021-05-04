import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

import numpy as np
import pandas as pd

# python script 
import main as home 

#-----Computer System-------------
import laptops_page
import setting_account
import workstations_page
import mainframes_page
import servers_page
import desktops_page
#-------------------------------


#-------Popular Computers Page---
import generalized_item
#------------------------------



#----------Purpose Section Page------------
import purpose_computer_page
#-----------------------------------------

#-----------OS Section Page--------
import OS_computer_page
#----------------------------------

#-----------Arch Section Page-----
import Arch_computer_page
#---------------------------------

#-----------Computer Parts Page-----
import computer_parts_page
#-----------------------------------

#-----------Email Page------------
import emails_page
#---------------------------------

#------------Check out Page------
import check_out 
#--------------------------------

class customer_page(tk.Frame):

    def __init__(self, customer_name, customer_username, customer_Id, master = None):
        tk.Frame.__init__(self, master)
        
        self.customer_name = customer_name 
        self.customer_username = customer_username
        self.customer_Id = customer_Id  
        
        self.master.title( "Customer_Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style  = tk.ttk.Style()

        #--------------------Lenovo Icon Image---------------------
        image_tempo = Image.open( "images/lenovo_icon_2.png" )
        self.my_image = ImageTk.PhotoImage( image_tempo  )
        
        self.label_image = tk.Label( image = self.my_image )
        self.label_image.image = self.my_image 
        self.label_image.place( x = 0, y = 0 )
        #----------------------------------------------------------

        
        #------------------------Title----------------------------- 
        
        self.style.configure( "LabelTitle.TLabel", 
                               relief=tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 20),
                               background = '#49A'    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = f"  HOME PAGE\nWelcome {self.customer_name}!", 
                                        style =  "LabelTitle.TLabel" 
                                      )
        self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )
        #------------------------------------------------------------



        #--------------------Computer System Label-----------------------
        self.style.configure( "Computer_System_Label.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "center", 
                               font = ("Helvetica", 16),
                               background = '#49A'  
                            )
        self.Computer_System_Label = tk.ttk.Label( self.top, 
                                        text = "Recommended Computer Systems", 
                                        style =  "Computer_System_Label.TLabel" 
                                      )
        self.Computer_System_Label.place( relx = 0, rely = 0.2, 
                               relwidth = 0.410 , relheight = 0.1 
                            )
        #-----------------------------------------------------------------



    #-----------------3 Computer System--------------------------
                    
        #--------Read the 3 Computer System chosen by Lenovo Admin--------
        self.computer_systems = self.manager_system_inputs()
        #-----------------------------------------------------------------
        
        plus_x = 0 
        plus_relx = 0 

        self.system_images = []
        self.System_Buttons = []

        for i in range( len(self.computer_systems) ):
            system_name = self.computer_systems[i]
         
            image_tempo = Image.open( f"images/computer_systems/{system_name}.png" )
            
            image_tempo = image_tempo.resize( (160,160), Image.ANTIALIAS)
            
            self.system_images.append(None)
            self.system_images[i] = ImageTk.PhotoImage(  image_tempo )
            
            self.System_Buttons.append(None)

            self.System_Buttons[i] = tk.Button( self.top, text = f"{system_name}", fg = "black",
                command = lambda name_system = system_name: self.command_button_system(name_system),
                image = self.system_images[i], activebackground = "light blue", compound = "top")
            
            self.System_Buttons[i].place( relx = 0 + plus_relx, rely = 0.32, 
                                    relwidth = 0.13, relheight = 0.26 )
            plus_relx += 0.14

            
    #-----------------------------------------------------------------

    #----------------------3 Most popular computers Section--------------------

        #-----------------3 Most popular computers LABEL----------------
        self.style.configure( "Popular_Computers_Label.TLabel", 
                               relief = tk.SUNKEN,
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = '#49A'  
                            )
        self.Popular_Computers_Label = tk.ttk.Label( self.top, 
                                        text = "Top 3 Best Selling Computers", 
                                        style =  "Popular_Computers_Label.TLabel" 
                                      )

        self.Popular_Computers_Label.place( relx = 0.43, rely = 0.2, 
                               relwidth = 0.580 , relheight = 0.1 
                            )
         
        #-------------------------------------------------------------

            #---------Get the most popular(best selling computers)------------
        df = pd.read_excel( "csv_files/items.xlsx" )
        df_all_computers = df[ df['Type'] != "Computer Part" ]

        df_all_computers = df_all_computers.sort_values( by = "Number of Sales", ascending = False) 
        popular_computers = df_all_computers[:3]

            #---------------------------------------------------------------------

        plus_x = 0 
        plus_y = 0 
        plus_relx = 0 

        self.lenovo_images = []
        self.Computer_Buttons = []
        for i in range(len(popular_computers)):
            computer_name = popular_computers.iloc[i]['Name']
            computer_type = popular_computers.iloc[i]['Type']

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
            
            image_tempo = image_tempo.resize(  (220,160), Image.ANTIALIAS )
            self.lenovo_images.append(None)

            self.lenovo_images[i] = ImageTk.PhotoImage(  image_tempo )
            self.Computer_Buttons.append(None)
            
            self.Computer_Buttons[i] = tk.Button( self.top, 
             command = lambda name = computer_name, type_ = computer_type : self.command_computers(name,type_), 
             text = f"{computer_name}", fg = "black", image = self.lenovo_images[i],
             activebackground = "light blue", compound = "top")

            self.Computer_Buttons[i].place( relx = 0.4315 + plus_relx, rely = 0.32, 
                                    relwidth = 0.175, relheight = 0.26)
            plus_relx += 0.19 

    #---------------------------------------------------------------------------------



    #------------------------Operating System Section--------------------------------

        #--------------------Label for operating system: Mac, Windows, Linux-------------------
        self.style.configure( "Popular_Computers_Label.TLabel", 
                            relief = tk.SUNKEN,
                            anchor = "left", 
                            font = ("Helvetica", 16),
                            background = '#49A'  
                            )

        self.Popular_Computers_Label = tk.ttk.Label( self.top, 
                                        text = "Operating\nSystems:", 
                                        style =  "Popular_Computers_Label.TLabel" 
                                    )

        self.Popular_Computers_Label.place( relx = 0, rely = 0.6, 
                               relwidth = 0.09 , relheight = 0.175 
                            )
        #---------------------------------------------------------------------------------------

        #----------------------Picture windows-mac-linux----------------------------------------
        image_tempo = Image.open( f"images/operating_systems/mac_linux_windows_banner.png" )
        image_tempo = image_tempo.resize(  (400,115), Image.ANTIALIAS )
        self.operating_systems = ImageTk.PhotoImage(  image_tempo )
        
        self.label_operating_systems = tk.Label( image = self.operating_systems )
        self.label_operating_systems.image = self.operating_systems 
        self.label_operating_systems.place( x = 120, y = 404 )
        #---------------------------------------------------------------------------------------

        
        OS_list = ['Windows', 'Linux', 'Mac' ] 
        self.OS_Buttons = list()
        plus_relx = 0 
        for i in range( len(OS_list) ):
            OS_name = OS_list[i]
            self.style.configure( f"{OS_name}_bt.TButton",  
                                anchor = "center", 
                                font = ( "Helvetica", 8 ),
                                background = "green",
                                foreground = "black"                                
                                )
            self.OS_Buttons.append(None)       

            self.OS_Buttons[i] = tk.ttk.Button(  self.top, 
                text = f"{OS_name}" ,
                command = lambda name_OS = OS_name: self.command_OS(name_OS) , 
                style = f"{OS_name}_bt.TButton"  
                                              )

            self.OS_Buttons[i].place( relx = 0.3 + plus_relx, rely = 0.72,
                                        relwidth = 0.08, relheight = 0.04)
            
            plus_relx -= 0.1

        
    #-------------------------------------------------------------------------------



    #------------------Architecture Section------------------------------

        #---------------------Label for architecture---------------------
        self.style.configure( "Architecture_Label.TLabel", 
                            relief = tk.SUNKEN,
                            anchor = "left", 
                            font = ("Helvetica", 15),
                            background = '#49A'  
                            )

        self.Architecture_Label = tk.ttk.Label( self.top, 
                                        text = "Architecture:", 
                                        style =  "Architecture_Label.TLabel" 
                                      )
        
        self.Architecture_Label.place( relx = 0, rely = 0.77, 
                               relwidth = 0.09 , relheight = 0.2 
                            )
        #-----------------------------------------------------------------




    #---------------------Picture Intell Arm logo-------------------------
        image_tempo = Image.open( f"images/architecture/intel_amd3.png" )
        image_tempo = image_tempo.resize(  (400,115), Image.ANTIALIAS )
        self.architecture = ImageTk.PhotoImage(  image_tempo )
        
        self.label_architecture = tk.Label( image = self.architecture )
        self.label_architecture.image = self.architecture 
        self.label_architecture.place( x = 120, y = 524 )
    #----------------------------------------------------------------------

    
        Architecture_List = ['AMD Ryzen', 'Intel']

        plus_relx = 0 
        self.Arch_Buttons = list()
        for i in range( len(Architecture_List) ):
            arch_name = Architecture_List[i]

            self.style.configure( f"{arch_name}_bt.TButton",  
                                anchor = "center", 
                                font = ( "Helvetica", 8 ),
                                background = "green",
                                foreground = "black"                                
                                )
            
            self.Arch_Buttons.append(None)
            self.Arch_Buttons[i] = tk.ttk.Button(  self.top, 
                    text = f"{arch_name}" ,
                    command = lambda name_arch = arch_name: self.command_arch(name_arch) , 
                    style = f"{arch_name}_bt.TButton"  
                                        )

            self.Arch_Buttons[i].place( relx = 0.142 + plus_relx, rely = 0.9,
                                     relwidth = 0.07, relheight = 0.04 )
            plus_relx += 0.12


    #--------------------------------------------------------------------

    #-----------------------Check out Section-------------------------------
        image_tempo = Image.open( f"images/checkout.png" )
        image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
        self.checkout_pic = ImageTk.PhotoImage(  image_tempo )
        
        df_orders = pd.read_excel("csv_files/orders.xlsx")

        df_user_shopping_cart = df_orders[ (df_orders["Username"] == self.customer_username) & (df_orders['Order_Status'] == "in cart") ]

        items_in_cart = len(df_user_shopping_cart)
        if items_in_cart == 0: 
            checkout_button = tk.Button(self.top, 
                command = self.command_checkout,
                text = "", image = self.checkout_pic,
                compound = "bottom")
            checkout_button.place(relx = 0.79, rely= 0.095, relwidth= 0.07, relheight=0.1)
        else:
            checkout_button = tk.Button(self.top, 
                command = self.command_checkout,
                text = f"{items_in_cart} items", image = self.checkout_pic,
                compound = "bottom")
            checkout_button.place(relx = 0.79, rely= 0.095, relwidth= 0.07, relheight=0.1)
    #-----------------------------------------------------------------------





    #---------------------Computer Parts Section-------------------------------------
        image_tempo = Image.open( f"images/computer_parts/cpu_gpu.png" )
        self.image_part = image_tempo.resize(  (300,220), Image.ANTIALIAS )
        
        self.computer_parts_image = ImageTk.PhotoImage(  self.image_part )
        self.computer_parts_image.image = self.image_part
        
        self.button_computer_parts_ = tk.Button(  self.top, 
                text = "Computer Parts",
                command = self.command_computer_parts, 
                image = self.computer_parts_image,
                compound = "top"
                                      )
        self.button_computer_parts_.place( relx = 0.752, rely = 0.61,
                                     relwidth = 0.235, relheight = 0.36 )
    #----------------------------------------------------------------------------------




    #-----------------------------------------------------------------------



    #---------------------Main Purpose Section------------------------------

        #-------------------Image for main purpose computer--------------------
        image_tempo = Image.open( f"images/main_purpose/main_purpose.png" )
        image_tempo = image_tempo.resize(  (400,240), Image.ANTIALIAS )
        self.gpu_cpu = ImageTk.PhotoImage(  image_tempo )
        
        self.label_gpu_cpu = tk.Label( image = self.gpu_cpu )
        self.label_gpu_cpu.image = self.gpu_cpu
        self.label_gpu_cpu.place( x = 553, y = 411 )
        #-----------------------------------------------------------------------

        
        Purpose_list = [ 'Gaming', 'Scientific', 'Business' ] 
 
        plus_relx = 0 
        plus_rely  = 0
        flag_row = True 
        self.Purpose_Buttons = list()

        for i in range( len(Purpose_list) ):
            purpose_name = Purpose_list[i] 

            self.style.configure( f"{purpose_name}_bt.TButton",  
                                anchor = "center", 
                                font = ( "Helvetica", 8 ),
                                background = "green",
                                foreground = "black"                                
                                )
            
            self.Purpose_Buttons.append(None)  
            self.Purpose_Buttons[i] = tk.ttk.Button(  self.top, 
                text = f"{purpose_name} Computers",
                command = lambda name_purpose = purpose_name :self.command_purpose_computers(name_purpose), 
                style = f"{purpose_name}_bt.TButton"  
                                                   )
            self.Purpose_Buttons[i].place( relx = 0.5 + plus_relx, rely = 0.735 + plus_rely,
                                        relwidth = 0.086, relheight = 0.04 )
            plus_relx += 0.15
            if plus_relx == 0.3:
                plus_rely += 0.17
                plus_relx = 0.15

    #-----------------------------------------------------------------------










    #-------------------------Log out----------------------------
        image_tempo = Image.open( f"images/icons/sign_out.png" )
        image_tempo = image_tempo.resize( (25,25), Image.ANTIALIAS )
            
        self.image_sign_out = ImageTk.PhotoImage( image_tempo)

        self.sign_out_button = tk.Button( self.top, text = "Sign out", 
          image = self.image_sign_out, command = self.log_out, compound = "left")

        self.sign_out_button.place( relx = 0.870, rely = 0.15, relwidth = 0.12, relheight = 0.05)


    #-----------------------------------------------------------


    #-------------------------Settings Button----------------------------
        
        image_tempo = Image.open( f"images/icons/settings.png" )
        image_tempo = image_tempo.resize( (25,25), Image.ANTIALIAS )
            
        self.image_settings = ImageTk.PhotoImage( image_tempo)

        self.settings_button = tk.Button( self.top, text = "Settings", 
          image = self.image_settings, command = self.command_Settings, compound = "left")

        self.settings_button.place( relx = 0.870, rely = 0.095, relwidth = 0.12, relheight = 0.05)

    #------------------------------------------------------------------------------------


    #-----------------------Email Section-----------------------------------------------------
        df_emails = pd.read_excel("csv_files/emails.xlsx")
        df_emails_user = df_emails[ (df_emails["for_username"] == self.customer_username) & (df_emails["Status"] == "unread" ) ]
        unread_mails_n = len(df_emails_user)
        if len(df_emails_user) == 0:
            image_tempo = Image.open( f"images/icons/closed_mailbox.png" )
            image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
            self.email_pic = ImageTk.PhotoImage(  image_tempo )
            
            email_button = tk.Button(self.top, 
                command = self.command_email,
                text = "", image = self.email_pic,
                compound = "bottom")
            email_button.place(relx = 0.71, rely= 0.095, relwidth= 0.07, relheight=0.1)
        else:
            image_tempo = Image.open( f"images/icons/open_mailbox.png" )
            image_tempo = image_tempo.resize(  (70,35), Image.ANTIALIAS )
            self.email_pic = ImageTk.PhotoImage(  image_tempo )
            
            mail_ = "mail" if unread_mails_n == 1 else "mails"
            email_button = tk.Button(self.top, 
                command = self.command_email,
                text = f"{unread_mails_n} new {mail_}", foreground = "red",
                image = self.email_pic, compound = "bottom")
            email_button.place(relx = 0.71, rely= 0.095, relwidth= 0.07, relheight=0.1)

    #----------------------------------------------------------------------------------------------







    def log_out(self, event=None):
        if askyesno("Log out", f"{self.customer_name}, are you sure you want to log out?"):
            self.top.destroy()
            home.HomePage()        

    
    def command_Settings(self):
        self.top.destroy()
        setting_account.setting_account(customer_name = self.customer_name , 
        customer_Id = self.customer_Id, customer_username = self.customer_username  )
        

    #------------ Commands for the 3 systems chosen by the manager--------------
    def command_button_system(self, system_name):
        system_selected = system_name

        if system_selected == "laptops": 
            self.top.destroy()      
            laptops_page.laptops_page(customer_name= self.customer_name, 
                        customer_Id = self.customer_Id, customer_username = self.customer_username)
        elif system_selected == "mainframes":
            self.top.destroy()
            mainframes_page.mainframes_page( customer_name= self.customer_name, 
                        customer_Id = self.customer_Id, customer_username = self.customer_username)
        elif system_selected == "workstations":
            self.top.destroy()
            workstations_page.workstations_page(customer_name = self.customer_name, 
            customer_username = self.customer_username, customer_Id = self.customer_Id)
        elif system_selected == "servers":
            self.top.destroy()
            servers_page.servers_page(customer_name = self.customer_name, 
            customer_username = self.customer_username, customer_Id = self.customer_Id)
        elif system_selected == "desktops":
            self.top.destroy()
            desktops_page.desktops_page(customer_name = self.customer_name, 
            customer_username = self.customer_username, customer_Id = self.customer_Id)

    #-------------------------------------------------------------------------



    #----------------- Commands for the most popular computers---------
        
    def command_computers(self, computer_name, computer_type):
        self.top.destroy()
        generalized_item.generalized_item( coming_from = "Main_Page", 
        item_name = computer_name, customer_name = self.customer_name, 
        customer_Id = self.customer_Id, customer_username = self.customer_username)
            
    #-------------------------------------------------------------------

    
    #-------------Commands for the OS: Windows, Mac, Linux-----------
    def command_OS(self, OS_name_):
        self.top.destroy()

        if OS_name_ == "Windows":
            OS_computer_page.OS_computers_page(OS_name = "Windows", 
                customer_name = self.customer_name, customer_Id = self.customer_Id, 
                customer_username = self.customer_username)
            
        elif OS_name_ == "Mac":
            OS_computer_page.OS_computers_page(OS_name = "Mac", 
                customer_name = self.customer_name, customer_Id = self.customer_Id, 
                customer_username = self.customer_username)
            
        elif OS_name_ == "Linux":
            OS_computer_page.OS_computers_page(OS_name = "Linux",
                customer_name = self.customer_name, customer_Id = self.customer_Id, 
                customer_username = self.customer_username)
            
    #------------------------------------------------------------------

    #-----------------Commands for architectures: Intel and Arm--------
    def command_arch(self, arch_name_):
        self.top.destroy()
        if arch_name_ == "Intel":
            Arch_computer_page.Arch_computers_page(Arch_name = "Intel",
                customer_name = self.customer_name, customer_Id = self.customer_Id, 
                customer_username = self.customer_username)
        elif arch_name_ == "AMD Ryzen":
            Arch_computer_page.Arch_computers_page(Arch_name = "AMD Ryzen",
                customer_name = self.customer_name, customer_Id = self.customer_Id, 
                customer_username = self.customer_username)
    
    #------------------------------------------------------------------ 


    #-----------------Command for Computer Parts-----------------
    def command_computer_parts(self):
        self.top.destroy()
        computer_parts_page.computer_parts_page( customer_name = self.customer_name,
            customer_Id = self.customer_Id, customer_username = self.customer_username)
    
    #---------------------------------------------------------------

    #--------------------Command Main Purpose-----------------------
    def command_purpose_computers(self, purpose_name_):
        self.top.destroy()
        if purpose_name_ == "Gaming":
            purpose_computer_page.purpose_computers_page( purpose_name = "Gaming", 
            customer_name = self.customer_name, customer_username = self.customer_username, 
            customer_Id = self.customer_Id)        
        elif purpose_name_ == "Business":
            purpose_computer_page.purpose_computers_page( purpose_name = "Business", 
            customer_name = self.customer_name, customer_username = self.customer_username, 
            customer_Id = self.customer_Id)
        elif purpose_name_ == "Scientific":
            purpose_computer_page.purpose_computers_page( purpose_name = "Scientific", 
            customer_name = self.customer_name, customer_username = self.customer_username, 
            customer_Id = self.customer_Id)
    #---------------------------------------------------------------

    #----------------Check out Command-----------------------------------
    def command_checkout(self):
        df2 =  pd.read_excel( "csv_files/registered_customers.xlsx" )

        df_user = df2[ df2['Username'] == self.customer_username]

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
            check_out.check_out(coming_from = "Main_Page2", item_name = None, 
                customer_name = self.customer_name, 
                customer_Id = self.customer_Id, customer_username = self.customer_username) 
        

    #--------------------------------------------------------------------


    #---------------------Email Section--------------------------------------
    def command_email(self):
        self.top.destroy()
        emails_page.emails_page( customer_name = self.customer_name,
         customer_Id = self.customer_Id, customer_username = self.customer_username)
    #-------------------------------------------------------------------------


    #------------Manager deciding what system should be on the homepage-------
    def manager_system_inputs(self):
        df = pd.read_excel( "csv_files/suggested_systems.xlsx" )
        System1 = str(df.iloc[0,0])
        System2 = str(df.iloc[1,0])
        System3 = str(df.iloc[2,0])
        return System1, System2, System3 

    #--------------------------------------------------------------------------  





