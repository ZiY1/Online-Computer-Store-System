import tkinter as tk  
import tkinter.ttk as ttk 


# python scripts 
import privileged_user_login as pul
import manager_edit_account as mea
import manager_view_account as mva
import manager_edit_taboo as met
import view_account_table as vat
import manager_choose_system as mcs
import manager_edit_discussion as med
import privileged_edit_complaint as pec
import manager_view_suspicious_bidding as mvsb

class manager_management_page(tk.Frame):

	def __init__(self, name, username, master=None):
		tk.Frame.__init__(self, master)

		self.admin_name = name
		self.admin_username = username

		self.master.title("Manager Management Page")
		self.master.geometry("989x876")
		self.master.configure( background = "light blue" )

		self.create_widgets()


	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		#Title
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 21),background = '#49A')
		self.LabelTitle = tk.ttk.Label(self.top, text="Manager Management", 
                                        style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.263, rely=0.021, relwidth=0.47, relheight=0.07)
    
		self.style.configure("LabelTitle2.TLabel", font=("Helvetica", 16),background = 'light blue')
		self.LabelTitle2 = tk.ttk.Label(self.top, text = "Hello, "+ self.admin_name, style = "LabelTitle2.TLabel")
		self.LabelTitle2.place(relx=0.83, rely=0.0003, relwidth=0.38, relheight=0.06)
        

        #Frame View
		self.style.configure("Frame1.TLabelframe", font=("Helvetica", 15), background = "light blue")
		self.Frame1 = tk.ttk.LabelFrame(self.top, text="View", style="Frame1.TLabelframe")
		self.Frame1.place(relx=0.009, rely=0.129, relwidth=0.487, relheight=0.865)
		

		#Frame Modification
		self.Frame2 = tk.ttk.LabelFrame(self.top, text="Modification", style="Frame1.TLabelframe")
		self.Frame2.place(relx=0.504, rely=0.129, relwidth=0.487, relheight=0.865)
		


		# Row 1:  View account info and Edit account info
		self.style.configure("AllCommand.TButton", font=("Helvetica", 14))

		self.ViewAccount = tk.ttk.Button(self.Frame1, text="View Account Information", command=self.view_account, style="AllCommand.TButton")
		self.ViewAccount.place(relx=0.296, rely=0.1, relwidth=0.49, relheight=0.065)

		self.EditAccount = tk.ttk.Button(self.Frame2, text="Edit Account Information", command=self.edit_account, style="AllCommand.TButton")
		self.EditAccount.place(relx=0.296, rely=0.1, relwidth=0.49, relheight=0.065)

		# Row 2: View taboo list and Edit taboo list
		self.ViewTaboo = tk.ttk.Button(self.Frame1, text="View Taboo Word List", command=lambda: vat.view_account_table('taboo_list', "989x876", self.admin_username), style="AllCommand.TButton")
		self.ViewTaboo.place(relx=0.296, rely=0.2, relwidth=0.49, relheight=0.065)

		self.EditTaboo = tk.ttk.Button(self.Frame2, text="Edit Taboo Word List", command=self.edit_taboo, style="AllCommand.TButton")
		self.EditTaboo.place(relx=0.296, rely=0.2, relwidth=0.49, relheight=0.065)

		# Row 3
		self.ViewSusBidding = tk.ttk.Button(self.Frame1, text="View Suspicious Bidding", command=self.view_sus_bidding, style="AllCommand.TButton")
		self.ViewSusBidding.place(relx=0.296, rely=0.3, relwidth=0.49, relheight=0.065)

		self.EditDiscussion = tk.ttk.Button(self.Frame2, text="Edit Discussion Reports", command=self.edit_discussion, style="AllCommand.TButton")
		self.EditDiscussion.place(relx=0.296, rely=0.3, relwidth=0.49, relheight=0.065)

		# Row 4
		self.ViewItem = tk.ttk.Button(self.Frame1, text="View All Items", command=lambda: vat.view_account_table('all_items', "989x876", self.admin_username), style="AllCommand.TButton")
		self.ViewItem.place(relx=0.296, rely=0.4, relwidth=0.49, relheight=0.065)

		self.EditComplaint = tk.ttk.Button(self.Frame2, text="Edit Complaints", command=self.edit_complaint, style="AllCommand.TButton")
		self.EditComplaint.place(relx=0.296, rely=0.4, relwidth=0.49, relheight=0.065)

		# Row 5
		self.EditSystem = tk.ttk.Button(self.Frame2, text="Edit Suggested Systems", command=self.edit_system, style="AllCommand.TButton")
		self.EditSystem.place(relx=0.296, rely=0.5, relwidth=0.49, relheight=0.065)

		# Log out button
		self.LogOut = tk.ttk.Button(self.top, text="Log Out", command=self.log_out, style="AllCommand.TButton")
		self.LogOut.place(relx=0.89, rely=0.076, relwidth=0.1, relheight=0.05)






	def view_account(self):
		self.top.destroy()
		mva.view_account_page(self.admin_name, self.admin_username)

	def view_sus_bidding(self):
		self.top.destroy()
		mvsb.manager_view_suspicious_bidding(self.admin_name, self.admin_username)

	def edit_account(self):
		self.top.destroy()
		mea.edit_account_page(self.admin_name, self.admin_username)

	def edit_taboo(self):
		self.top.destroy()
		met.edit_taboo_page("manager_management_page", self.admin_name, self.admin_username)

	def edit_discussion(self):
		self.top.destroy()
		med.edit_discussion_page(self.admin_name, self.admin_username)

	def edit_complaint(self):
		self.top.destroy()
		pec.edit_complaint_page("manager", self.admin_name, self.admin_username)

	def edit_system(self):
		self.top.destroy()
		mcs.edit_system_page(self.admin_name, self.admin_username)



	def log_out(self):
		self.top.destroy()
		pul.privilaged_user_login()



# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    manager_management_page(top).mainloop()    