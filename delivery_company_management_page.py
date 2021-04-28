import tkinter as tk  
import tkinter.ttk as ttk 


# python scripts 
import privileged_user_login as pul
import privileged_edit_complaint

class delivery_company_management_page(tk.Frame):

	def __init__(self, name, username, master=None):
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username

		self.master.title("Delivery Company Management Page")
		self.master.geometry("989x776")
		self.master.configure( background = "light blue" )

		self.create_widgets()


	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		#Title
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 21),background = '#49A')
		self.LabelTitle = tk.ttk.Label(self.top, text="Delivery Company Management", 
                                        style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.263, rely=0.021, relwidth=0.47, relheight=0.07)
    
		self.style.configure("LabelTitle2.TLabel", font=("Helvetica", 16),background = 'light blue')
		self.LabelTitle2 = tk.ttk.Label(self.top, text = "Hello, "+ self.name, style = "LabelTitle2.TLabel")
		self.LabelTitle2.place(relx=0.8, rely=0.0003, relwidth=0.38, relheight=0.06)

		self.style.configure("AllCommand.TButton", font=("Helvetica", 14))
		# Row 1: 
		self.DealWithComplaint = tk.ttk.Button(self.top, text="Deal With Complaints", command=self.deal_with_complaint, style="AllCommand.TButton")
		self.DealWithComplaint.place(relx=0.16, rely=0.2, relwidth=0.23, relheight=0.065)





		# Log out button
		self.LogOut = tk.ttk.Button(self.top, text="Log Out", command=self.log_out, style="AllCommand.TButton")
		self.LogOut.place(relx=0.89, rely=0.076, relwidth=0.1, relheight=0.05)


	def deal_with_complaint(self):
		type_privileged_user = 'delivery'
		self.top.destroy()
		privileged_edit_complaint.edit_complaint_page(type_privileged_user, self.name, self.username)

	def log_out(self):
		self.top.destroy()
		pul.privilaged_user_login()