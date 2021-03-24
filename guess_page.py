import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image



# python script 
import guess_welcome 


class guess_page(tk.Frame):

    def __init__(self,master = None):
        tk.Frame.__init__(self, master) 
        self.master.title( "Guess_Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style  = tk.ttk.Style()

        #--------------------Lenovo Icon Image---------------------
        image_tempo = Image.open( "images/lenovo_icon_2.png" )
        #image_tempo = image_tempo.resize(  (500,100), Image.ANTIALIAS )
        self.my_image = ImageTk.PhotoImage( image_tempo  )
        
        self.label_image = tk.Label( image = self.my_image )
        self.label_image.image = self.my_image 
        self.label_image.place( x = 0, y = 0 )
        #----------------------------------------------------------

        
        #------------------------Title----------------------------- 
        
        self.style.configure( "LabelTitle.TLabel", 
                               anchor = "center", 
                               font = ("Helvetica", 26),
                               background = '#49A'    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "HOME PAGE", 
                                        style =  "LabelTitle.TLabel" 
                                      )
        self.LabelTitle.place( relx = 0.4, rely = 0.05, 
                               relwidth = 0.3 , relheight = 0.1 
                            )
        #------------------------------------------------------------
        
        #--------------------Computer System Label-----------------------
        self.style.configure( "Computer_System_Label.TLabel", 
                               anchor = "left", 
                               font = ("Helvetica", 16),
                               background = '#49A'  
                            )
        self.Computer_System_Label = tk.ttk.Label( self.top, 
                                        text = "Recommended Computer Systems", 
                                        style =  "Computer_System_Label.TLabel" 
                                      )
        self.Computer_System_Label.place( relx = 0, rely = 0.2, 
                               relwidth = 0.305 , relheight = 0.1 
                            )
        #-----------------------------------------------------------------



    #-----------------3 Computer System--------------------------
        

            #---------- Computer System # 1 ----------------$
        system_name_1 = "personal computers"  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_1}.png" )
        image_tempo = image_tempo.resize(  (385,140), Image.ANTIALIAS )
        self.system1 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_system1 = tk.Label( image = self.system1 )
        self.label_system1.image = self.system1 
        self.label_system1.place( x = 0, y = 204 )

        # Buttton Computer System # 1
        self.style.configure( "Computer_system_bt1.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_system_1 = tk.ttk.Button(  self.top, 
                                        text = f"{system_name_1}",
                                        command = self.command_button_system_1, 
                                        style = "Computer_system_bt1.TButton"  
                                      )
        self.button_system_1.place( relx = 0.2, rely = 0.45, relwidth = 0.1, relheight = 0.051 )



            #---------------$$$$$$$$$$$$$--------------------------

    #---------- Computer System # 2 ----------------%
        system_name_2 = "workstations"  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_2}.png" )
        image_tempo = image_tempo.resize(  (385,140), Image.ANTIALIAS )
        self.system2 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_system2 = tk.Label( image = self.system2 )
        self.label_system2.image = self.system2 
        self.label_system2.place( x = 0, y = 342 )

        # Buttton Computer System # 2
        self.style.configure( "Computer_system_bt2.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_system_2 = tk.ttk.Button(  self.top, 
                                        text = f"{system_name_2}",
                                        command = self.command_button_system_2, 
                                        style = "Computer_system_bt2.TButton"  
                                      )
        self.button_system_2.place( relx = 0.2, rely = 0.652, relwidth = 0.1, relheight = 0.051 )



            #---------------%%%%%%%%%%%%%%%%%%%%%%--------------------------




    #---------- Computer System # 3 ----------------=
       
        system_name_3 = "mainframes"  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_3}.png" )
        image_tempo = image_tempo.resize(  (385,140), Image.ANTIALIAS )
        self.system3 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_system3 = tk.Label( image = self.system3 )
        self.label_system3.image = self.system3 
        self.label_system3.place( x = 0, y = 475 )

        # Buttton Computer System # 3
        self.style.configure( "Computer_system_bt3.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_system_3 = tk.ttk.Button(  self.top, 
                                        text = f"{system_name_3}",
                                        command = self.command_button_system_3, 
                                        style = "Computer_system_bt3.TButton"  
                                      )
        self.button_system_3.place( relx = 0.2, rely = 0.869, relwidth = 0.1, relheight = 0.051 )



            #---------------==========================--------------------------
        
    #-----------------------------------------------------------------

    #-----------------3 Most popular computers LABEL----------------
        self.style.configure( "Popular_Computers_Label.TLabel", 
                               anchor = "middle", 
                               font = ("Helvetica", 16),
                               background = '#49A'  
                            )
        self.Popular_Computers_Label = tk.ttk.Label( self.top, 
                                        text = "     Top 3 Best Selling Computers", 
                                        style =  "Popular_Computers_Label.TLabel" 
                                      )
        self.Popular_Computers_Label.place( relx = 0.33, rely = 0.2, 
                               relwidth = 0.305 , relheight = 0.1 
                            )
         
    #-------------------------------------------------------------




    #----------------------3 Most popular computers--------------------

        #-------------------Most popular computer #1------------------$
        computer_name_1 = "Lenovo ThinkPad X390 Yoga Laptop"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_1}.png" )
        image_tempo = image_tempo.resize(  (385,105), Image.ANTIALIAS )
        self.computer1 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer1 = tk.Label( image = self.computer1 )
        self.label_computer1.image = self.computer1 
        self.label_computer1.place( x = 424, y = 204 )

        # Buttton Computer # 1
        self.style.configure( "Popular_Computer_bt1.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_computer_1 = tk.ttk.Button(  self.top, 
                                        text = f"{computer_name_1}",
                                        command = self.command_button_computer_1, 
                                        style = "Popular_Computer_bt1.TButton"  
                                      )
        self.button_computer_1.place( relx = 0.3325, rely = 0.475, relwidth = 0.3, relheight = 0.051 )



            #---------------$$$$$$$$$$$$$--------------------------



     #-------------------Most popular computer #2------------------%
        computer_name_2 = "Lenovo Legion 7i"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_2}.png" )
        image_tempo = image_tempo.resize(  (385,105), Image.ANTIALIAS )
        self.computer2 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer2 = tk.Label( image = self.computer2 )
        self.label_computer2.image = self.computer2 
        self.label_computer2.place( x = 424, y = 360 )

        # Buttton Computer # 2
        self.style.configure( "Popular_Computer_bt2.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_computer_2 = tk.ttk.Button(  self.top, 
                                        text = f"{computer_name_2}",
                                        command = self.command_button_computer_2, 
                                        style = "Popular_Computer_bt2.TButton"  
                                      )
        self.button_computer_2.place( relx = 0.3325, rely = 0.712, relwidth = 0.3, relheight = 0.051 )



            #---------------%%%%%%%%%%%%%%%%%%%%%%%%--------------------------




     #-------------------Most popular computer #3------------------=
        computer_name_3 = "Lenovo Chromebook S330"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_3}.png" )
        image_tempo = image_tempo.resize(  (385,105), Image.ANTIALIAS )
        self.computer3 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer3 = tk.Label( image = self.computer3 )
        self.label_computer3.image = self.computer3 
        self.label_computer3.place( x = 424, y = 510 )

        # Buttton Computer # 3
        self.style.configure( "Popular_Computer_bt3.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_computer_3 = tk.ttk.Button(  self.top, 
                                        text = f"{computer_name_3}",
                                        command = self.command_button_computer_3, 
                                        style = "Popular_Computer_bt3.TButton"  
                                      )
        self.button_computer_3.place( relx = 0.3325, rely = 0.932, relwidth = 0.3, relheight = 0.051 )



            #---------------==========================--------------------------













    #---------------------------------------------------------------------------------






    #-------------------------Back Button----------------------------

        self.style.configure(   "CommandBack.TButton", 
                                font=('Helvetica',16)
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text="Back",
                                            command=self.command_back,
                                            style="CommandBack.TButton"
                                        )
        self.CommandBack.place(relx=0.796, rely=0.886, relwidth=0.190, relheight=0.093)



        #-----------------------------------------------------------




    def command_back(self, event=None):
        self.top.destroy()
        guess_welcome.guest_welcome_page()        


    #------------ Commands for the 3 systems chosen by the manager--------------
    def command_button_system_1(self):
        self.top.destroy()

    def command_button_system_2(self):
        self.top.destroy()

    def command_button_system_3(self):
        self.top.destroy()
    #-------------------------------------------------------------------------

    #----------------- Commands for the most popular computers---------
    def command_button_computer_1(self):
        self.top.destroy()

    def command_button_computer_2(self):
        self.top.destroy()

    def command_button_computer_3(self):
        self.top.destroy()

    #-------------------------------------------------------------------