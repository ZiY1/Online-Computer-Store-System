import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts 
import manager_management_page as mmp
import manager_edit_account as mea
import view_account_table as vat


class view_account_page(tk.Frame):

	def __init__(self,  name, username, master=None): #name, username,
		tk.Frame.__init__(self, master)

		self.admin_name = name
		self.admin_username = username

		self.master.title("View Account Page")
		self.master.geometry("463x425")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="View Account Information ", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.079)

		# Row 1 View clerks button
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="Clerk Accounts:", style='Label1.TLabel')
		self.Label1.place(relx=0.11, rely=0.2, relwidth=0.6, relheight=0.062)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandClerk = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_users('clerk'), style="CommandView.TButton")
		self.CommandClerk.place(relx=0.7, rely=0.185, relwidth=0.18, relheight=0.09)

		# Row 2 View computer companies button
		self.Label2 = tk.ttk.Label(self.top, text="Computer Company Accounts:", style='Label1.TLabel')
		self.Label2.place(relx=0.11, rely=0.33, relwidth=0.6, relheight=0.062)

		self.CommandComputer = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_users('computer_company'), style="CommandView.TButton")
		self.CommandComputer.place(relx=0.7, rely=0.315, relwidth=0.18, relheight=0.09)

		# Row 3 View delivery companies button
		self.Label3 = tk.ttk.Label(self.top, text="Delivery Company Accounts:", style='Label1.TLabel')
		self.Label3.place(relx=0.11, rely=0.46, relwidth=0.6, relheight=0.062)

		self.CommandDelivery = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_users('delivery'), style="CommandView.TButton")
		self.CommandDelivery.place(relx=0.7, rely=0.445, relwidth=0.18, relheight=0.09)

		# Row 4 View customers button
		self.Label4 = tk.ttk.Label(self.top, text="Customer Accounts:", style='Label1.TLabel')
		self.Label4.place(relx=0.11, rely=0.59, relwidth=0.6, relheight=0.062)

		self.CommandCustomer = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_users('customer'), style="CommandView.TButton")
		self.CommandCustomer.place(relx=0.7, rely=0.575, relwidth=0.18, relheight=0.09)

		# Row 5 View suspended users button
		self.Label5 = tk.ttk.Label(self.top, text="Suspended Accounts:", style='Label1.TLabel')
		self.Label5.place(relx=0.11, rely=0.72, relwidth=0.6, relheight=0.062)

		self.CommandSuspend = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_users('suspend'), style="CommandView.TButton")
		self.CommandSuspend.place(relx=0.7, rely=0.705, relwidth=0.18, relheight=0.09)

		# Edit Button
		self.style.configure("CommandEdit.TButton", font=("Helvetica",14))
		self.CommandEdit = tk.ttk.Button(self.top, text="Edit Accounts", command=self.command_edit, style="CommandEdit.TButton")
		self.CommandEdit.place(relx=0.2, rely=0.86, relwidth=0.28, relheight=0.09)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Back", command=self.command_cancel, style="CommandEdit.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.86, relwidth=0.19, relheight=0.09)


	def command_view_users(self, type_user):
		vat.view_account_table(type_user, "463x425")

	def command_edit(self):
		self.top.destroy()
		mea.edit_account_page(self.admin_name, self.admin_username)

	def command_cancel(self):
		self.top.destroy()
		mmp.manager_management_page(self.admin_name, self.admin_username)


# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    view_account_page(top).mainloop()    