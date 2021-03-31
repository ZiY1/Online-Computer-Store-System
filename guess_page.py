import tkinter as tk 
import tkinter.ttk as ttk 
from PIL import ImageTk, Image



# python script 
import guess_welcome 
import sign_up_page
import registered_login
#----computer systems Pages--
import laptops_page



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
        

            #---------- Computer System # 1 ----------------$


        self.computer_systems = self.manager_system_inputs()
        system_name_1 = self.computer_systems[0]  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_1}.png" )
        image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
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
        self.button_system_1.place( relx = 0, rely = 0.54, relwidth = 0.1285, relheight = 0.051 )



            #---------------$$$$$$$$$$$$$--------------------------

    #---------- Computer System # 2 ----------------%
        system_name_2 = self.computer_systems[1]  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_2}.png" )
        image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
        self.system2 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_system2 = tk.Label( image = self.system2 )
        self.label_system2.image = self.system2 
        self.label_system2.place( x = 179.5, y = 204 )

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
        self.button_system_2.place( relx = 0.14, rely = 0.54, relwidth = 0.1285, relheight = 0.051 )



            #---------------%%%%%%%%%%%%%%%%%%%%%%--------------------------




    #---------- Computer System # 3 ----------------=
       
        system_name_3 = self.computer_systems[2]  # store manager input 
        image_tempo = Image.open( f"images/computer_systems/{system_name_3}.png" )
        image_tempo = image_tempo.resize(  (160,160), Image.ANTIALIAS )
        self.system3 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_system3 = tk.Label( image = self.system3 )
        self.label_system3.image = self.system3 
        self.label_system3.place( x = 361, y = 204 )

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
        self.button_system_3.place( relx = 0.28, rely = 0.54, relwidth = 0.1285, relheight = 0.051 )



            #---------------==========================--------------------------
        
    #-----------------------------------------------------------------

    #-----------------3 Most popular computers LABEL----------------
        self.style.configure( "Popular_Computers_Label.TLabel", 
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




    #----------------------3 Most popular computers--------------------

        #-------------------Most popular computer #1------------------$
        computer_name_1 = "Lenovo ThinkPad X390 Yoga Laptop"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_1}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.computer1 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer1 = tk.Label( image = self.computer1 )
        self.label_computer1.image = self.computer1 
        self.label_computer1.place( x = 553, y = 204 )

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
        self.button_computer_1.place( relx = 0.4315, rely = 0.54, relwidth = 0.15, relheight = 0.051 )



            #---------------$$$$$$$$$$$$$--------------------------



     #-------------------Most popular computer #2------------------%
        computer_name_2 = "Lenovo Legion 7i"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_2}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.computer2 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer2 = tk.Label( image = self.computer2 )
        self.label_computer2.image = self.computer2 
        self.label_computer2.place( x = 818, y = 204 )

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
        self.button_computer_2.place( relx = 0.637, rely = 0.54, relwidth = 0.15, relheight = 0.051 )



            #---------------%%%%%%%%%%%%%%%%%%%%%%%%--------------------------




     #-------------------Most popular computer #3------------------=
        computer_name_3 = "Lenovo Chromebook S330"  # read it from the csv file  
        image_tempo = Image.open( f"images/Lenovo_computers/{computer_name_3}.png" )
        image_tempo = image_tempo.resize(  (190,160), Image.ANTIALIAS )
        self.computer3 = ImageTk.PhotoImage(  image_tempo )
        
        self.label_computer3 = tk.Label( image = self.computer3 )
        self.label_computer3.image = self.computer3 
        self.label_computer3.place( x = 1080, y = 204 )

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
        self.button_computer_3.place( relx = 0.8425, rely = 0.54, relwidth = 0.15, relheight = 0.051 )



            #---------------==========================--------------------------













    #---------------------------------------------------------------------------------



    #------------------------Operating System Section--------------------------------

        # Label for operating system: Mac, Windows, Linux
        self.style.configure( "Popular_Computers_Label.TLabel", 
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
        #-------------------

        # Picture windows-mac-linux
        image_tempo = Image.open( f"images/operating_systems/mac_linux_windows_banner.png" )
        image_tempo = image_tempo.resize(  (400,115), Image.ANTIALIAS )
        self.operating_systems = ImageTk.PhotoImage(  image_tempo )
        
        self.label_operating_systems = tk.Label( image = self.operating_systems )
        self.label_operating_systems.image = self.operating_systems 
        self.label_operating_systems.place( x = 120, y = 404 )
        #-----------

        # Button Windows 
        self.style.configure( "Windows_Computer_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_windows_computers = tk.ttk.Button(  self.top, 
                                        text = "Windows" ,
                                        command = self.command_windows , 
                                        style = "Windows_Computer_bt.TButton"  
                                      )
        self.button_windows_computers.place( relx = 0.3, rely = 0.72,
                                     relwidth = 0.08, relheight = 0.04)

        # Button Mac
        self.style.configure( "Mac_Computer_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_mac_computers = tk.ttk.Button(  self.top, 
                                        text = "Mac" ,
                                        command = self.command_mac , 
                                        style = "Mac_Computer_bt.TButton"  
                                      )
        self.button_mac_computers.place( relx = 0.1225, rely = 0.72,
                                     relwidth = 0.07, relheight = 0.04 )




        # Button Linux
        self.style.configure( "Linux_Computer_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_linux_computers = tk.ttk.Button(  self.top, 
                                        text = "Linux" ,
                                        command = self.command_linux , 
                                        style = "Linux_Computer_bt.TButton"  
                                      )
        self.button_linux_computers.place( relx = 0.2125, rely = 0.72,
                                     relwidth = 0.07, relheight = 0.04)
        

    #-------------------------------------------------------------------------------



    #------------------Architecture Section------------------------------


        # Label for architecture
        self.style.configure( "Architecture_Label.TLabel", 
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
        #-------------------




    # Picture Intell Arm logo
        image_tempo = Image.open( f"images/architecture/intel_arm.png" )
        image_tempo = image_tempo.resize(  (400,115), Image.ANTIALIAS )
        self.architecture = ImageTk.PhotoImage(  image_tempo )
        
        self.label_architecture = tk.Label( image = self.architecture )
        self.label_architecture.image = self.architecture 
        self.label_architecture.place( x = 120, y = 524 )
    #-----------

    # Intell Button
        self.style.configure( "Intel_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_intel = tk.ttk.Button(  self.top, 
                                        text = "Intel" ,
                                        command = self.command_intel , 
                                        style = "Intel_bt.TButton"  
                                      )
        self.button_intel.place( relx = 0.142, rely = 0.9,
                                     relwidth = 0.07, relheight = 0.04 )
    #----------------

    # Arm Button
        self.style.configure( "Arm_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_arm = tk.ttk.Button(  self.top, 
                                        text = "Arm" ,
                                        command = self.command_arm , 
                                        style = "Arm_bt.TButton"  
                                      )
        self.button_arm.place( relx = 0.285, rely = 0.9,
                                     relwidth = 0.07, relheight = 0.04 )
    #----------------





    #--------------------------------------------------------------------


    #---------------------Computer Parts Section-------------------------------------
        image_tempo = Image.open( f"images/computer_parts/cpu_gpu.png" )
        image_tempo = image_tempo.resize(  (290,220), Image.ANTIALIAS )
        self.gpu_cpu = ImageTk.PhotoImage(  image_tempo )
        
        self.label_gpu_cpu = tk.Label( image = self.gpu_cpu )
        self.label_gpu_cpu.image = self.gpu_cpu
        self.label_gpu_cpu.place( x = 976, y = 411 )


    # Computer Parts Button
        self.style.configure( "computer_parts_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_computer_parts = tk.ttk.Button(  self.top, 
                                        text = "Computer Parts" ,
                                        command = self.command_computer_parts , 
                                        style = "computer_parts_bt.TButton"  
                                      )
        self.button_computer_parts.place( relx = 0.92, rely = 0.88,
                                     relwidth = 0.07, relheight = 0.051 )
    #----------------




    #-----------------------------------------------------------------------



    #---------------------Main Purpose Section------------------------------


        # Image for main purpose
        image_tempo = Image.open( f"images/main_purpose/main_purpose.png" )
        image_tempo = image_tempo.resize(  (400,240), Image.ANTIALIAS )
        self.gpu_cpu = ImageTk.PhotoImage(  image_tempo )
        
        self.label_gpu_cpu = tk.Label( image = self.gpu_cpu )
        self.label_gpu_cpu.image = self.gpu_cpu
        self.label_gpu_cpu.place( x = 553, y = 411 )
        #--------------------------



        # Gaming Computers Button
        self.style.configure( "gaming_computers_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_gaming_computers = tk.ttk.Button(  self.top, 
                                        text = "Gaming Computers" ,
                                        command = self.command_gaming_computers , 
                                        style = "gaming_computers_bt.TButton"  
                                      )
        self.button_gaming_computers.place( relx = 0.5, rely = 0.735,
                                     relwidth = 0.08, relheight = 0.051 )
    #----------------


    # Business Computers Button
        self.style.configure( "business_computers_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_business_computers = tk.ttk.Button(  self.top, 
                                        text = "Business Computers" ,
                                        command = self.command_business_computers , 
                                        style = "business_computers_bt.TButton"  
                                      )
        self.button_business_computers.place( relx = 0.6475, rely = 0.9,
                                     relwidth = 0.1, relheight = 0.051 )
    #----------------



    # Scientific Computers Button
        self.style.configure( "scientific_computers_bt.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 8 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.button_scientific_computers = tk.ttk.Button(  self.top, 
                                        text = "Scientific Computers" ,
                                        command = self.command_scientific_computers , 
                                        style = "scientific_computers_bt.TButton"  
                                      )
        self.button_scientific_computers.place( relx = 0.64, rely = 0.735,
                                     relwidth = 0.1, relheight = 0.051 )
    #----------------



    #-----------------------------------------------------------------------









    #-------------------------Back Button----------------------------

        self.style.configure(   "CommandBack.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text="Back",
                                            command=self.command_back,
                                            style="CommandBack.TButton"
                                        )
        self.CommandBack.place(relx=0.870, rely=0.15, relwidth= 0.13, relheight=0.05)

    #-----------------------------------------------------------


    #-------------------------Sign up Button----------------------------
        self.style.configure(   "Sign_UP.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.CommandSign_up = tk.ttk.Button(   self.top, 
                                            text = "Sign Up",
                                            command = self.command_sign_up,
                                            style = "Sign_UP.TButton"
                                        )
        self.CommandSign_up.place(relx=0.870, rely=0.095, relwidth= 0.13, relheight=0.05)
    #-----------------------------------------------------------


    #-------------------------Log In Button----------------------------
        self.style.configure(   "Command_Log_In.TButton", 
                                font=('Helvetica',16),
                                background = "green",
                                foreground = "black"
                            )
        self.Command_Log_In = tk.ttk.Button(   self.top, 
                                            text = "Log In",
                                            command = self.Command_Log_In,
                                            style = "Command_Log_In.TButton"
                                        )
        self.Command_Log_In.place(relx=0.734, rely=0.15, relwidth= 0.13, relheight=0.05)
    #-----------------------------------------------------------







    def command_back(self, event=None):
        self.top.destroy()
        guess_welcome.guest_welcome_page()        

    def command_sign_up(self):
        self.top.destroy()
        sign_up_page.sign_up_page()

    def Command_Log_In(self):
        self.top.destroy()
        registered_login.registered_login()


    #------------ Commands for the 3 systems chosen by the manager--------------
    def command_button_system_1(self):
        system_1 = self.computer_systems[0].lower()
        if system_1 == "laptops": 
            self.top.destroy()
            laptops_page.laptops_page()
        elif system_1 == "mainframes":
            self.top.destroy()
        elif system_1 == "workstations":
            self.top.destroy()
        elif system_1 == "servers":
            self.top.destroy()
        elif system_1 == "supercomputers":
            self.top.destroy()

    def command_button_system_2(self):
        system_2 = self.computer_systems[1].lower()
        
        if system_2 == "laptops": 
            self.top.destroy()
            laptops_page.laptops_page()
        elif system_2 == "mainframes":
            self.top.destroy()
        elif system_2 == "workstations":
            self.top.destroy()
        elif system_2 == "servers":
            self.top.destroy()
        elif system_2 == "supercomputers":
            self.top.destroy()


    def command_button_system_3(self):
        system_3 = self.computer_systems[2].lower()

        if system_3 == "laptops": 
            self.top.destroy()
            laptops_page.laptops_page()
        elif system_3 == "mainframes":
            self.top.destroy()
        elif system_3 == "workstations":
            self.top.destroy()
        elif system_3 == "servers":
            self.top.destroy()
        elif system_3 == "supercomputers":
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


    #-------------Commands for the OS: Windows, Mac, Linux-----------
    def command_windows(self):
        self.top.destroy()

    def command_mac(self):
        self.top.destroy()

    def command_linux(self):
        self.top.destroy()
    #------------------------------------------------------------------

    #-----------------Commands for architectures: Intel and Arm--------
    def command_intel(self):
        self.top.destroy()
    
    def command_arm(self):
        self.top.destroy()
    #------------------------------------------------------------------ 


    #-----------------Command for Computer Parts-----------------
    def command_computer_parts(self):
        self.top.destroy()

    #---------------------------------------------------------------

    #--------------------Command Main Purpose-----------------------
    def command_gaming_computers(self):
        self.top.destroy()

    def command_business_computers(self):
        self.top.destroy()

    def command_scientific_computers(self):
        self.top.destroy()
    #---------------------------------------------------------------



    #------------Manager deciding what system should be on the homepage-------
    def manager_system_inputs(self, system1 = None, system2 = None,
                              system3 = None, default = True):
        if default:
            system_1 = "laptops"
            system_2 = "workstations"
            system_3 = "mainframes"
        else:
            system_1 = system1
            system_2 = system2
            system_3 = system3 


        return (system_1, system_2, system_3)  

    #--------------------------------------------------------------------------  