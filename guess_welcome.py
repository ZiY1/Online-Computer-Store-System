import tkinter as tk 
import tkinter.ttk as ttk 

# python files
import main as home
import guess_page
import sign_up_page


class guest_welcome_page(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self,master) 
        self.master.title("Guest Home Page")
        self.master.geometry( "1350x676" )
        self.master.configure( background = "light blue" )
        self.create_widgets()

    def create_widgets(self):
        self.top = self.winfo_toplevel() 
        self.style = tk.ttk.Style()

        # Title 
        self.style.configure( "LabelTitle.TLabel", 
                               anchor = "center", 
                               font = ("Helvetica", 26)    
                            )
        self.LabelTitle = tk.ttk.Label( self.top, 
                                        text = "Welcome to Lenovo Online Store Guest!\n\tHow can we help you?", 
                                        style =  "LabelTitle.TLabel"  
                                      )
        self.LabelTitle.place( relx = 0.205, rely = 0.100, 
                               relwidth = 0.632, relheight = 0.195 
                            )

        # Continue as guest button 
        self.style.configure(   "CommandContinue.TButton", 
                                anchor="center",
                                font=("Helvetica", 18)
                        
                            )

        self.CommandContinue = tk.ttk.Button(self.top, 
                                            text="Continue as a guest", 
                                            command=self.command_continue,
                                            style="CommandContinue.TButton"
                                            )
        
        self.CommandContinue.place( relx=0.180, rely=0.430, 
                                    relwidth=0.680, relheight=0.120
                                  )

        # Sign Up Button 
        self.style.configure(   "GuestSignUp.TButton", 
                                anchor="center",
                                font=("Helvetica", 18)
                            )
        self.GuestSignUp = tk.ttk.Button(   self.top, 
                                            text="Sign up today", 
                                            command=self.guest_sign_up, 
                                            style="GuestSignUp.TButton"
                                        )
        self.GuestSignUp.place(  relx=0.180, rely=0.580,
                                 relwidth=0.680, relheight=0.120
                              )

		# Back
        self.style.configure(   "CommandBack.TButton", 
                                font=('Helvetica',16)
                            )
        self.CommandBack = tk.ttk.Button(   self.top, 
                                            text="Back",
                                            command=self.command_back,
                                            style="CommandBack.TButton"
                                        )
        self.CommandBack.place(relx=0.796, rely=0.886, relwidth=0.190, relheight=0.093)

        
    def command_continue(self, event=None):
        self.top.destroy()
        guess_page.guess_page()
        
    def guest_sign_up(self, event=None):
        self.top.destroy()
        sign_up_page.sign_up_page()


    def command_back(self, event=None):
        self.top.destroy()
        home.HomePage()


