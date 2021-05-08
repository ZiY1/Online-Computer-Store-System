import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
import datetime

# python scripts 
import main as home
import report_table
import complaint_table
import setting_account


class complaint_page(tk.Frame):

	def __init__(self, customer_name, customer_Id, customer_username , master=None):
		tk.Frame.__init__(self, master)

		self.type_user = 'customer'
		self.name = customer_name
		self.id = customer_Id
		self.username = customer_username

		self.master.title("Complaint & Report Page")
		self.master.geometry("563x625")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Complaint & Report", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.077)

		# Row 01: Report I Casted
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label01 = tk.ttk.Label(self.top, text="Discussion Report I:", style='Label1.TLabel')
		self.Label01.place(relx=0.16, rely=0.16, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.ButtonCasted = tk.ttk.Button(self.top, text="Casted", command=self.command_view_report, style="CommandView.TButton")
		self.ButtonCasted.place(relx=0.5, rely=0.15, relwidth=0.18, relheight=0.06)

		self.ButtonRecieved = tk.ttk.Button(self.top, text="Recieved", command=self.command_view_report_recieved, style="CommandView.TButton")
		self.ButtonRecieved.place(relx=0.7, rely=0.15, relwidth=0.18, relheight=0.06)

		# Row 0: Complaint I Casted
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label0 = tk.ttk.Label(self.top, text="Complaint I Casted:", style='Label1.TLabel')
		self.Label0.place(relx=0.16, rely=0.26, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.ButtonView = tk.ttk.Button(self.top, text="View", command=self.command_view_complaint, style="CommandView.TButton")
		self.ButtonView.place(relx=0.7, rely=0.25, relwidth=0.18, relheight=0.06)

		# Row 1: Complain:
		self.Label1 = tk.ttk.Label(self.top, text="Complain:", style='Label1.TLabel')
		self.Label1.place(relx=0.16, rely=0.365, relwidth=0.4, relheight=0.062)

		self.Combo1List1 = ["Store Clerk", "Delivery Company", "Purchased Item"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.49, rely=0.365, relwidth=0.4, relheight=0.06)
		self.Combo1.set(self.Combo1List1[0])

		# Row 2: Complained Email
		self.Label2 = tk.ttk.Label(self.top, text="Complained Email:", style='Label1.TLabel')
		self.Label2.place(relx=0.16, rely=0.465, relwidth=0.4, relheight=0.062)

		self.Text2Var = tk.StringVar()
		self.Text2 = tk.ttk.Entry(self.top, textvariable=self.Text2Var, font=("Helvetica",11))
		self.Text2.place(relx=0.49, rely=0.465, relwidth=0.4, relheight=0.06)

		# Row 3 Details of the complaint
		self.Label3 = tk.ttk.Label(self.top, text="Details\nof the complaint:", style='Label1.TLabel')
		self.Label3.place(relx=0.16, rely=0.5725, relwidth=0.33, relheight=0.1)

		self.Text3 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.Text3.place(relx=0.49, rely=0.583, relwidth=0.4, relheight=0.2)

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.25, rely=0.88, relwidth=0.19, relheight=0.07)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Back", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.88, relwidth=0.19, relheight=0.07)

	def command_view_report(self):
		self.top.destroy()
		report_table.report_table(self.name, self.id, self.username, "casted")

	def command_view_report_recieved(self):
		self.top.destroy()
		report_table.report_table(self.name, self.id, self.username, "recieved")

	def command_view_complaint(self):
		self.top.destroy()
		complaint_table.complaint_table(self.name, self.id, self.username)

	def get_combo1(self, event):
		if self.Combo1.get() == "Purchased Item":
			# Row 2: Order ID
			self.Label2.destroy()
			self.Label2 = tk.ttk.Label(self.top, text="Order ID:", style='Label1.TLabel')
			self.Label2.place(relx=0.16, rely=0.465, relwidth=0.2, relheight=0.062)
		else:
			# Row 2: Complained Email
			self.Label2.destroy()
			self.Label2 = tk.ttk.Label(self.top, text="Complained Email:", style='Label1.TLabel')
			self.Label2.place(relx=0.16, rely=0.465, relwidth=0.3, relheight=0.062)

	def command_confirm(self):

		# Check if email is empty
		complained_email = self.Text2.get()
		if complained_email.strip() != "":
			flag_email_valid = True
		else:
			flag_email_valid = False
			tk.messagebox.showerror("Error", "Complained Email or Order ID cannot be empty")

		# Check if detail of complaint is empty
		complaint_detail = self.Text3.get("1.0", "end")
		if complaint_detail.strip() != "":
			flag_detail_valid = True
		else:
			flag_detail_valid = False
			tk.messagebox.showerror("Error", "Details of the complaint cannot be empty")

		# Check if complained email exist!!! TODO: the order ID is left unfinished
		df = pd.read_excel("csv_files/privileged_users.xlsx")
		df = df[df['Status'] == 'active']
		complained_party_type = self.Combo1.get()
		if complained_party_type == "Store Clerk" and flag_email_valid:
			df_clerk = df[df['Type_user'] == 'clerk']
			if complained_email in list(df_clerk['Username']):
				flag_email_exist = True
			else:
				flag_email_exist = False
		elif complained_party_type == "Delivery Company" and flag_email_valid:
			df_clerk = df[df['Type_user'] == 'delivery']
			if complained_email in list(df_clerk['Username']):
				flag_email_exist = True
			else:
				flag_email_exist = False
		elif complained_party_type == "Purchased Item" and flag_email_valid:
			#TODO: finish this
			# In orders file, fetch out all processing or assigned orders of this user
			df_order = pd.read_excel("csv_files/orders.xlsx")
			df_processing = df_order[df_order['Order_Status'].isin(['processing', 'assigned'])]
			df_me = df_processing[df_processing['Username'] == self.username]
			if int(complained_email) in list(df_me['Order_Id']):
				flag_email_exist = True

				# fetch out the computer name
				df_order_row = df_me[df_me['Order_Id'] == int(complained_email)]
				computer_name = str(df_order_row['Item_Name'].iloc[-1])

				# fetch out the assigned computer company in items file for this computer 
				df_item = pd.read_excel("csv_files/items.xlsx")
				df_computer_row = df_item[df_item['Name'] == computer_name]

				# add a complaint order id in complaint details
				complaint_detail = 'Complained Order ID: ' + str(complained_email) + '\t\t\t\t\t\t\t\t\t\t\t' + complaint_detail

				# change complained_email to computer company assigned
				complained_email = str(df_computer_row['Computer Company'].iloc[-1])
			else:
				flag_email_exist = False

		if not flag_email_exist:
			tk.messagebox.showerror("Error", "Complained Email or Order ID doesn't exist")

		# write to the dataframe
		df_complaint = pd.read_excel("csv_files/complaints.xlsx")

		now = datetime.datetime.now()
		date_time = now.strftime("%y-%m-%d %H:%M")

		satisfaction = "pending"
		complained_party_response = "pending"
		time_response = "pending"
		status = "pending"
		manager_justification = "pending"

		if len(df_complaint) == 0:
			Id = 0
		else:
			Id = int(df_complaint['ID'].iloc[-1])
			Id = Id+1
		tempo = pd.DataFrame([[Id, self.username.lower(), complained_party_type, complained_email, complaint_detail, satisfaction, 
								date_time, complained_party_response, time_response, status, manager_justification]], 
									columns=['ID', 'Complainant', 'Complained Party Type', 'Complained Party Email', 'Complained Details', 'Satisfaction',
											 'Time Complained', 'Complained Party Response', 'Time Response', 'Status', 'Manager Justification'])
		df_complaint = df_complaint.append(tempo)

		# write to the file
		if flag_email_valid and flag_email_exist and flag_detail_valid:
			# Check if suspended
			df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
			df_suspend_user = df_suspend[df_suspend['Type_user'] == self.type_user]
			if self.username.lower() in list(df_suspend_user['Username']):
				tk.messagebox.showerror("Error", "You can't make any complaint because you are suspended")
			else:
				df_complaint.to_excel("csv_files/complaints.xlsx", index=False)
				tk.messagebox.showinfo("Success", "New complaint casted")

				# refresh text boxes'
				self.Text2Var = tk.StringVar()
				self.Text2 = tk.ttk.Entry(self.top, textvariable=self.Text2Var, font=("Helvetica",11))
				self.Text2.place(relx=0.49, rely=0.465, relwidth=0.4, relheight=0.06)

				self.Text3 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
				self.Text3.place(relx=0.49, rely=0.583, relwidth=0.4, relheight=0.2)




	def command_cancel(self):
		self.top.destroy()
		setting_account.setting_account(self.name, self.id, self.username)

