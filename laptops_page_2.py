import tkinter as tk 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

# python scripts
import laptops_page
import generalized_laptop
import guess_page 
import customer_page

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


        #------------------Mac Laptop 1--------------------------------------
        laptop_name = "Apple MacBook Air"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_1 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_1.image = self.mac_laptop 
        self.Mac_laptop_1.place( x = 0, y = 140 )

        # Button Mac laptop # 1
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


        
        #------------------Mac Laptop 2--------------------------------------
        laptop_name = "Apple MacBook Pro 13"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_2 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_2.image = self.mac_laptop 
        self.Mac_laptop_2.place( x = 210.5, y = 140 )

        # Button Mac laptop # 2
        self.style.configure( f"{laptop_name}_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.mac_laptop_2 = tk.ttk.Button(  self.top, 
                                        text = f"{laptop_name}",
                                        command = self.command_laptop_2, 
                                        style = f"{laptop_name}_bt.TButton"  
                                      )
        self.mac_laptop_2.place( relx = 0.165, rely = 0.45, relwidth = 0.1495, relheight = 0.051 )
        #------------------------------------------------------------------------------


        #------------------Mac Laptop 3--------------------------------------
        laptop_name = "Apple MacBook Retina 12"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_3 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_3.image = self.mac_laptop 
        self.Mac_laptop_3.place( x = 421, y = 140 )

        # Button Mac laptop # 3
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


        #------------------Mac Laptop 4--------------------------------------
        laptop_name = "Apple Titanium PowerBook G4"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_4 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_4.image = self.mac_laptop 
        self.Mac_laptop_4.place( x = 631.5, y = 140 )

        # Button Mac laptop # 4
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


        #------------------Mac Laptop 5--------------------------------------
        laptop_name = "Apple MacBook Air Core 2 Duo"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_5 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_5.image = self.mac_laptop 
        self.Mac_laptop_5.place( x = 842, y = 140 )

        # Button Mac laptop # 5
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


        
        #------------------Mac Laptop 6--------------------------------------
        laptop_name = "Apple MacBook A1181"
        image_tempo = Image.open( f"images/Lenovo_Computers/Mac_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.mac_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Mac_laptop_6 = tk.Label( image = self.mac_laptop )
        self.Mac_laptop_6.image = self.mac_laptop 
        self.Mac_laptop_6.place( x = 1052.5, y = 140 )

        # Button Mac laptop # 6
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

    #------------------Linux Laptop 7--------------------------------------
        laptop_name = "Dell XPS 7390"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_7 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_7.image = self.linux_laptop 
        self.Linux_laptop_7.place( x = 0, y = 350 )

        # Button Linux laptop # 7
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



        #------------------Linux Laptop 8--------------------------------------
        laptop_name = "System76 Serval WS"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_8 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_8.image = self.linux_laptop 
        self.Linux_laptop_8.place( x = 210.5, y = 350 )

        # Button Linux laptop # 8
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


        #------------------Linux Laptop 9--------------------------------------
        laptop_name = "Purism Librem 13"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_9 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_9.image = self.linux_laptop 
        self.Linux_laptop_9.place( x = 421, y = 350 )

        # Button Linux laptop # 9
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


        
        #------------------Linux Laptop 10--------------------------------------
        laptop_name = "System76 Galago Pro"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_10 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_10.image = self.linux_laptop 
        self.Linux_laptop_10.place( x = 631.5, y = 350 )

        # Button Linux laptop # 10
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


        #------------------Linux Laptop 11--------------------------------------
        laptop_name = "System76 Oryx Pro"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_11 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_11.image = self.linux_laptop 
        self.Linux_laptop_11.place( x = 842, y = 350 )

        # Button Linux laptop # 11
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


        
        #------------------Linux Laptop 12--------------------------------------
        laptop_name = "System76 Darter Pro"
        image_tempo = Image.open( f"images/Lenovo_Computers/Linux_computers/{laptop_name}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.linux_laptop = ImageTk.PhotoImage(  image_tempo )
        
        self.Linux_laptop_12 = tk.Label( image = self.linux_laptop )
        self.Linux_laptop_12.image = self.linux_laptop 
        self.Linux_laptop_12.place( x = 1052.5, y = 350 )

        # Button Linux laptop # 12
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
        self.Command_Back_Main_Page.place(relx=0.770, rely= 0.03, relwidth= 0.22, relheight=0.05)

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



    def command_laptop_1(self):
        # Apple MacBook Air
        laptop_name = "Apple MacBook Air"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop= False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False)

        


    def command_laptop_2(self):
        # Apple MacBook Pro 13
        laptop_name = "Apple MacBook Pro 13"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )



    def command_laptop_3(self):
        # Apple MacBook Retina 12
        laptop_name = "Apple MacBook Retina 12"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_4(self):
        # Apple Titanium PowerBook G4
        laptop_name = "Apple Titanium PowerBook G4"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_5(self):
        # Apple MacBook Air Core 2 Duo
        laptop_name = "Apple MacBook Air Core 2 Duo"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    
    def command_laptop_6(self):
        # Apple MacBook A1181
        laptop_name = "Apple MacBook A1181"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


#----------Linux Commands----------------
    def command_laptop_7(self):
        # Dell XPS 7390
        laptop_name = "Dell XPS 7390"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_8(self):
        # System76 Serval WS
        laptop_name = "System76 Serval WS"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_9(self):
        # Purism Librem 13
        laptop_name = "Purism Librem 13"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_10(self):
        # System76 Galago Pro
        laptop_name = "System76 Galago Pro"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_11(self):
        # System76 Oryx Pro
        laptop_name = "System76 Oryx Pro"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )


    def command_laptop_12(self):
        # System76 Darter Pro
        laptop_name = "System76 Darter Pro"
        self.top.destroy()

        if self.Customer_Name == None: # We are in the guess account 
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, lenovo_laptop = False)
        else: # We are in the user account
            generalized_laptop.generalized_laptop( laptop_name = laptop_name, 
                 customer_name = self.Customer_Name, customer_Id = self.Customer_Id, 
                 customer_username = self.Customer_username, lenovo_laptop = False )



