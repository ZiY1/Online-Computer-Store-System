import tkinter as tk  
import tkinter.ttk as ttk 

from PIL import ImageTk, Image

# python scripts 
import customer_page
import provide_credit_card


class setting_account(tk.Frame):
    
    def __init__( self, customer_name, customer_Id, customer_username ,master = None ):
        tk.Frame.__init__(self, master) 
        self.master.title( "Setting Account Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
      
        
        # User account info 
        self.customer_name = customer_name
        self.customer_username = customer_username 
        self.customer_Id = customer_Id

        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()    # Style
        
        #---------------------------------Title----------------------------------------
        self.style.configure( 
                            "LabelTitle.TLabel", 
                            anchor = "center", 
                            font = ("Helvetica", 23),
                            background = '#49A',
                            foreground = "black" 
                     )
        self.LabelTitle =  tk.ttk.Label( self.top, 
                                      text = "User settings account", 
                                      style = "LabelTitle.TLabel"        
                                    )   
        self.LabelTitle.place( relx = 0.25, rely = 0.500, relwidth = 0.572, relheight = 0.095 )
        #----------------------------------------------------------------------------------

        #--------------------------IMAGE---------------------------------------------

        self.my_image = ImageTk.PhotoImage( Image.open( "images/lenovo_icon.jpg" )  )
        
        self.label_image = tk.Label( image = self.my_image)
        self.label_image.image = self.my_image 
        self.label_image.place( x = 250, y = 0 )
        #-----------------------------------------------------------------------------

        #-------------------------Purchase History Section Button--------------------
        self.style.configure( "Command_Purchase_History.TButton",  
                              anchor = "left", 
                              font = ( "Helvetica", 14 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.Command_Purchase_History = tk.ttk.Button(  self.top, 
                                        text = "Check my purchase history",
                                        command = self.Command_Purchase_History, 
                                        style = "Command_Purchase_History.TButton"  
                                      )
        self.Command_Purchase_History.place( relx = 0, rely = 0.600, relwidth = 0.300, relheight = 0.071 )
        #---------------------------------------------------------------------------------------

        #---------Provide/Update credit card information Section Button--------------------------------
        self.style.configure( "Command_Credit_Card_Info.TButton", 
                               anchor = "left",  
                               font = ("Helvetica", 14 ),
                               background = "green",
                               foreground = "black"    
                            )
        self.Command_Credit_Card_Info = tk.ttk.Button(  self.top, 
                            text = "Provide/Update your credit card information",  
                                           command = self.Command_Credit_Card_Info, 
                                           style = "Command_Credit_Card_Info.TButton"
                                        )
        self.Command_Credit_Card_Info.place( relx = 0, rely = 0.700, relwidth = 0.300, relheight = 0.071)
        #-----------------------------------------------------------------------------------

        #-----------------------Track my current Package Section Button----------------------------
        self.style.configure( "Command_Track_Package.TButton", 
                               anchor = "left", 
                               font = ( "Helvetica", 14 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.Command_Track_Package = tk.ttk.Button( self.top, 
                                     text = "Track my current package", 
                                     command = self.Command_Track_Package,
                                     style = "Command_Track_Package.TButton"
                                   )
        self.Command_Track_Package.place( relx = 0, rely = 0.800, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------



        #----------------------View my account information Section Button--------------------
        self.style.configure( "Command_Account_info.TButton",  
                              anchor = "left", 
                              font = ( "Helvetica", 14 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.Command_Account_info = tk.ttk.Button(  self.top, 
                                        text = "View my account information",
                                        command = self.Command_Account_info, 
                                        style = "Command_Account_info.TButton"  
                                      )
        self.Command_Account_info.place( relx = 0.7, rely = 0.600, relwidth = 0.300, relheight = 0.071 )
        #---------------------------------------------------------------------------------------

        #---------Place a complaint Section Button--------------------------------
        self.style.configure( "Command_Place_Complaint.TButton", 
                               anchor = "left",  
                               font = ("Helvetica", 14 ),
                               background = "green",
                               foreground = "black"    
                            )
        self.Command_Place_Complaint = tk.ttk.Button(  self.top, 
                            text = "Place a complaint",  
                                           command = self.Command_Place_Complaint, 
                                           style = "Command_Place_Complaint.TButton"
                                        )
        self.Command_Place_Complaint.place( relx = 0.7, rely = 0.700, relwidth = 0.300, relheight = 0.071)
        #-----------------------------------------------------------------------------------

        #-----------------Check my inbox Section Button----------------------------
        self.style.configure( "Command_Check_Inbox.TButton", 
                               anchor = "left", 
                               font = ( "Helvetica", 14 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.Command_Check_Inbox = tk.ttk.Button( self.top, 
                                     text = "Check my inbox", 
                                     command = self.Command_Check_Inbox,
                                     style = "Command_Check_Inbox.TButton"
                                   )
        self.Command_Check_Inbox.place( relx = 0.7, rely = 0.800, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------


    #---------------------------Go Back Button---------------------------------------
        self.style.configure( "Command_Go_Back.TButton", font = ("Helvetica", 16),
                                background = "green",   foreground = "black" )
        self.CommandExit = tk.ttk.Button(  self.top, 
                                       text = "Go Back",
                                       command = self.Command_Go_Back,
                                       style = "Command_Go_Back.TButton" 
        )
        self.CommandExit.place( relx = 0.873, rely = 0.88, relwidth = 0.119, relheight = 0.065)
    #---------------------------------------------------------------------------------









    def Command_Purchase_History(self):
        self.top.destroy() 



    def Command_Credit_Card_Info(self):
        self.top.destroy()
        provide_credit_card.provide_credit_card(customer_name = self.customer_name, 
                customer_Id = self.customer_Id, 
                customer_username = self.customer_username )


    def Command_Track_Package(self):
        self.top.destroy() 


    def Command_Go_Back(self):
        self.top.destroy()


    def Command_Account_info(self):
        self.top.destroy()        
        

    def Command_Place_Complaint(self):
        self.top.destroy()

    def Command_Check_Inbox(self):
        self.top.destroy()


    def Command_Go_Back(self):
        self.top.destroy()
        customer_page.customer_page(customer_name = self.customer_name,  
        customer_username = self.customer_username, customer_Id = self.customer_Id)

