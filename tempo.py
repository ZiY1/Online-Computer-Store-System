import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

# python scripts
import guess_page 
import customer_page
import laptops_page_2
import generalized_laptop 

class laptops_page(tk.Frame):

    def __init__(self, customer_name = None, customer_username = None,
                        customer_Id = None,master = None):
        tk.Frame.__init__(self, master)
        self.master.title( "Laptops Page" )
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
                                            text = "Lenovo Laptops", 
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
                                           text = f"Lenovo Laptops\nHello, {self.Customer_Name}", 
                                           style = "LabelTitle.TLabel" 
                                          )

            self.LabelTitle.place( relx = 0.4, rely = 0, 
                               relwidth = 0.3 , relheight = 0.15 
                            )


                            
        #------------------------------------------------------------


        #------------------Lenovo Laptop 1--------------------------------------
        laptop_name = "Lenovo Chromebook S330"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_1 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_1.image = self.lenovo_laptop 
        self.Lenovo_laptop_1.place( x = 0, y = 140 )

        # Button Lenovo laptop # 1
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_1 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_1, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_1.place( relx = 0.001, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        
        #------------------Lenovo Laptop 2--------------------------------------
        laptop_name = "Lenovo IdeaPad 3i Gaming"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_2 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_2.image = self.lenovo_laptop 
        self.Lenovo_laptop_2.place( x = 210.5, y = 140 )

        # Button Lenovo laptop # 2
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_2 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_2, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_2.place( relx = 0.165, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        #------------------Lenovo Laptop 3--------------------------------------
        laptop_name = "Lenovo IdeaPad Gaming 3"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_3 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_3.image = self.lenovo_laptop 
        self.Lenovo_laptop_3.place( x = 421, y = 140 )

        # Button Lenovo laptop # 3
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_3 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_3, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_3.place( relx = 0.329, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        
        #------------------Lenovo Laptop 4--------------------------------------
        laptop_name = "Lenovo IdeaPad Slim 7"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_4 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_4.image = self.lenovo_laptop 
        self.Lenovo_laptop_4.place( x = 631.5, y = 140 )

        # Button Lenovo laptop # 4
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_4 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_4, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_4.place( relx = 0.493, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        #------------------Lenovo Laptop 5--------------------------------------
        laptop_name = "Lenovo Legion 5i"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_5 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_5.image = self.lenovo_laptop 
        self.Lenovo_laptop_5.place( x = 842, y = 140 )

        # Button Lenovo laptop # 5
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_5 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_5, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_5.place( relx = 0.657, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        
        #------------------Lenovo Laptop 6--------------------------------------
        laptop_name = "Lenovo Legion 7i"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_6 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_6.image = self.lenovo_laptop 
        self.Lenovo_laptop_6.place( x = 1052.5, y = 140 )

        # Button Lenovo laptop # 6
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_6 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_6, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_6.place( relx = 0.821, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------

    #------------------Lenovo Laptop 7--------------------------------------
        laptop_name = "Lenovo Legion Y740"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_7 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_7.image = self.lenovo_laptop 
        self.Lenovo_laptop_7.place( x = 0, y = 350 )

        # Button Lenovo laptop # 7
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_7 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_7, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_7.place( relx = 0.001, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------



        #------------------Lenovo Laptop 8--------------------------------------
        laptop_name = "Lenovo ThinkPad P15"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_8 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_8.image = self.lenovo_laptop 
        self.Lenovo_laptop_8.place( x = 210.5, y = 350 )

        # Button Lenovo laptop # 8
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_8 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_8, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_8.place( relx = 0.165, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        #------------------Lenovo Laptop 9--------------------------------------
        laptop_name = "Lenovo ThinkPad X1 Carbon"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_9 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_9.image = self.lenovo_laptop 
        self.Lenovo_laptop_9.place( x = 421, y = 350 )

        # Button Lenovo laptop # 9
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_9 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_9, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_9.place( relx = 0.329, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        
        #------------------Lenovo Laptop 10--------------------------------------
        laptop_name = "Lenovo ThinkPad X390 Yoga Laptop"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_10 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_10.image = self.lenovo_laptop 
        self.Lenovo_laptop_10.place( x = 631.5, y = 350 )

        # Button Lenovo laptop # 10
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_10 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_10, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_10.place( relx = 0.493, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        #------------------Lenovo Laptop 11--------------------------------------
        laptop_name = "Lenovo Yoga 9i"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_11 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_11.image = self.lenovo_laptop 
        self.Lenovo_laptop_11.place( x = 842, y = 350 )

        # Button Lenovo laptop # 11
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_11 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_11, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_11.place( relx = 0.657, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        
        #------------------Lenovo Laptop 12--------------------------------------
        laptop_name = "Lenovo Yoga C940"
        image_tempo = Image.open( f"images/Lenovo_Computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.lenovo_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Lenovo_laptop_12 = tk.Label( image = self.lenovo_laptop )
        self.Lenovo_laptop_12.image = self.lenovo_laptop 
        self.Lenovo_laptop_12.place( x = 1052.5, y = 350 )

        # Button Lenovo laptop # 12
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_laptop_12 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_12, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.button_laptop_12.place( relx = 0.821, rely = 0.75, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------




        #-------------------------Mac & Linux Button----------------------------

        self.style.configure(   "Command_Mac_Linux.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text = "Looking for mac and linux laptops?",
                                            command = self.command_mac_linux_laptops,
                                            style="Command_Mac_Linux.TButton"
                                        )
        self.CommandBack.place(relx=0.700, rely=0.85, relwidth= 0.28, relheight=0.05)

    #-----------------------------------------------------------





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




    def command_mac_linux_laptops(self):
        if self.Customer_Name == None: # We are in a guess account
            self.top.destroy()
            laptops_page_2.laptops_page_2()
        else: # We are in a registered account
            self.top.destroy()
            laptops_page_2.laptops_page_2(customer_name = self.Customer_Name, 
                        customer_Id = self.Customer_Id,  
                        customer_username = self.Customer_username)




    def command_laptop_1(self):
        # Lenovo Chromebook S330
        laptop_name = "Lenovo Chromebook S330"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )



    def command_laptop_2(self):
        # Lenovo IdeaPad 3i Gaming
        
        laptop_name = "Lenovo IdeaPad 3i Gaming"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_3(self):
        # Lenovo IdeaPad Gaming 3
        
        laptop_name = "Lenovo IdeaPad Gaming 3"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_4(self):
        # Lenovo IdeaPad Slim 7
        
        laptop_name = "Lenovo IdeaPad Slim 7"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_5(self):
        # Lenovo Legion 5i
        
        laptop_name = "Lenovo Legion 5i"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    
    def command_laptop_6(self):
        # Lenovo Legion 7i
        
        laptop_name = "Lenovo Legion 7i"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_7(self):
        # Lenovo Legion Y740
        
        laptop_name = "Lenovo Legion Y740"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_8(self):
        # Lenovo ThinkPad P15
        
        laptop_name = "Lenovo ThinkPad P15"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True)


    def command_laptop_9(self):
        # Lenovo ThinkPad X1 Carbon
        
        laptop_name = "Lenovo ThinkPad X1 Carbon"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True)


    def command_laptop_10(self):
        # Lenovo ThinkPad X390 Yoga Laptop
        
        laptop_name = "Lenovo ThinkPad X390 Yoga Laptop"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )


    def command_laptop_11(self):
        # Lenovo Yoga 9i
        
        laptop_name = "Lenovo Yoga 9i"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True)


    def command_laptop_12(self):
        # Lenovo Yoga C940
        
        laptop_name = "Lenovo Yoga C940"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name,
            customer_name = None, customer_Id = None, customer_username = None, 
                     lenovo_laptop = True)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = True )



