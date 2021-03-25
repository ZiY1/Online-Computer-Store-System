import tkinter as tk  
import tkinter.ttk as ttk 

from tkinter.messagebox import askyesno
from PIL import ImageTk, Image

# python scripts 
import guess_welcome
import registered_login 
import privileged_user_login

class HomePage(tk.Frame):
    
    def __init__( self, master = None ):
        tk.Frame.__init__(self, master) 
        self.master.title( "Home Page" )
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        self.create_widgets()


    def create_widgets(self):
        self.top = self.winfo_toplevel()
        self.style = tk.ttk.Style()    # Style
        
        #---------------------------------Title----------------------------------------
        self.style.configure( 
                            "LabelTitle.TLabel", 
                            anchor = "center", 
                            font = ("Helvetica", 26),
                            background = '#49A',
                            foreground = "black" 
                     )
        self.LabelTitle =  tk.ttk.Label( self.top, 
                                      text = "Online Computer Store Log in System", 
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

        #-------------------------Visitor/Browser's Section Button--------------------
        self.style.configure( "CommandGuest.TButton",  
                              anchor = "center", 
                              font = ( "Helvetica", 18 ),
                              background = "green",
                              foreground = "black"                                
                            )
                            
        self.CommandGuest = tk.ttk.Button(  self.top, 
                                        text = "Guest",
                                        command = self.command_guest, 
                                        style = "CommandGuest.TButton"  
                                      )
        self.CommandGuest.place( relx = 0.37, rely = 0.600, relwidth = 0.300, relheight = 0.071 )
        #---------------------------------------------------------------------------------------

        #-------------------Registered Customer's Section Button--------------------------------
        self.style.configure( "CommandCustomer.TButton", 
                               anchor = "center",  
                               font = ("Helvetica", 18 ),
                               background = "green",
                               foreground = "black"    
                            )
        self.CommandCustomer = tk.ttk.Button(  self.top, 
                                           text = "Registered Customer",  
                                           command = self.command_customer, 
                                           style = "CommandCustomer.TButton"
                                        )
        self.CommandCustomer.place( relx = 0.37, rely = 0.700, relwidth = 0.300, relheight = 0.071)
        #-----------------------------------------------------------------------------------

        #-----------------------Privileged User's Section Button----------------------------
        self.style.configure( "CommandVIP.TButton", 
                               anchor = "center", 
                               font = ( "Helvetica", 18 ), 
                               background = "green",
                               foreground = "black" 
                            )
        self.CommandVIP = tk.ttk.Button( self.top, 
                                     text = "Privileged User", 
                                     command = self.command_vip,
                                     style = "CommandVIP.TButton"
                                   )
        self.CommandVIP.place( relx = 0.37, rely = 0.800, relwidth = 0.300, relheight = 0.071 )
        #-------------------------------------------------------------------------------

        #----------------------------Exit Button---------------------------------------
        self.style.configure( "CommandExit.TButton", font = ("Helvetica", 16),
                                background = "green",   foreground = "black" )
        self.CommandExit = tk.ttk.Button(  self.top, 
                                       text = "Exit",
                                       command = self.command_exit,
                                       style = "CommandExit.TButton" 
        )
        self.CommandExit.place( relx = 0.873, rely = 0.917, relwidth = 0.119, relheight = 0.065)
        #---------------------------------------------------------------------------------

    def command_guest(self, event = None):
        self.top.destroy() 
        guess_welcome.guest_welcome_page()



    def command_customer(self, event = None):
        self.top.destroy()
        registered_login.registered_login()


    def command_vip(self, event = None):
        self.top.destroy() 
        privileged_user_login.privilaged_user_login()


    def command_exit(self, event = None):
        if askyesno("Exit", "Do you want to exit?"):
    	    self.top.destroy()
        
        



#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    HomePage(top).mainloop()    








    







