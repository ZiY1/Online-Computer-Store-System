import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
import textwrap
import datetime

# python scripts 
import complaint_page
import manager_management_page as mmp
import clerk_management_page
import delivery_company_management_page
import computer_company_management_page

# TODO: at line 66, 207, 263, 339, 425 (finished)
class edit_complaint_page(tk.Frame):

	def __init__(self, type_privileged_user, name, username, master=None): 
		tk.Frame.__init__(self, master)

		# type_privileged_user includes 'manager', 'delivery', 'clerk', 'computer_company'
		self.type_privileged_user = type_privileged_user
		self.name = name
		self.username = username

		self.master.title("Edit Complaints Page")
		self.master.geometry("890x855")
		self.master.configure( background = "light blue" )

		if self.type_privileged_user == "manager":
			self.title = "Edit Complaints"
			self.response_title = "Manager Justification:"
		else:
			self.title = "Handle Complaints Recieved"
			self.response_title = "Complained Party Response:"

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text=self.title, style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.296, rely=0.015, relwidth=0.4, relheight=0.043)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.235, rely=0.09, relwidth=0.18, relheight=0.026)

		self.Combo1List1 = ["All Complaints", "Pending Complaints", "Closed Complaints & Pending Satisfaction", "Closed Complaints & Satisfied", "Closed Complaints & Dissatisfied","Stay Complaints", "Reverse Complaints"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.53, rely=0.09, relwidth=0.35, relheight=0.032)
		self.Combo1.set(self.Combo1List1[0])

		self.update_treeview()

		# Reported Comment Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Complaint details and feedbacks", style='LabelHead.TLabel')
		self.LabelHead.place(relx=0.36, rely=0.355, relwidth=0.35, relheight=0.04)

		# Reported Comment Body
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=1, relheight=0.355)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.4, relheight=0.355, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		# Display reported comment
		self.style.configure("LabelType.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.style.configure("LabelTime.TLabel",anchor="w", font=("Helvetica",11), background = "light blue")
		self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.style.configure("LabelContent.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")

		self.LabelMyTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelMyTitle.grid(sticky="W", row=0, column=0, padx=0, pady=5)

		self.LabelMyTime = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelMyTime.grid(sticky="W", row=1, column=0, padx=0, pady=5)

		self.LabelMyContent = tk.ttk.Label(self.MyFrame, text="" ,style="LabelContent.TLabel")
		self.LabelMyContent.grid(sticky="W", row=2, column=0, padx=0, pady=10)

		self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="" ,
									  style="LabelContent.TLabel")
		self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

		self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

		self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

		self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text="", style="LabelContent.TLabel")
		self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

		self.LabelSeg2 = tk.ttk.Label(self.MyFrame, text="" ,
									  style="LabelContent.TLabel")
		self.LabelSeg2.grid(sticky="W", row=7, column=0, padx=0, pady=10)

		self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=0)

		self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text="", style="LabelContent.TLabel")
		self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=10)

		# Manager Justification OR Complained Party Response
		self.LabelJustification = tk.ttk.Label(self.top, text=self.response_title, style='LabelHead.TLabel')
		self.LabelJustification.place(relx=0.375, rely=0.765, relwidth=0.35, relheight=0.04)

		self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
		self.Text.configure(state="disabled")


		if self.type_privileged_user == "manager":
			# Violated Button
			self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
			self.ButtonViolated = tk.ttk.Button(self.top, text="Stay", state="disabled", command=self.violated, style="ButtonAll.TButton")
			self.ButtonViolated.place(relx=0.125, rely=0.92, relwidth=0.15, relheight=0.045)

			# Non-Violated Button
			self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
			self.ButtonNonViolated = tk.ttk.Button(self.top, text="Reverse", state="disabled", command=self.non_violated, style="ButtonAll.TButton")
			self.ButtonNonViolated.place(relx=0.415, rely=0.92, relwidth=0.2, relheight=0.045)
		else:
			# Submit Button
			self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
			self.ButtonSubmit = tk.ttk.Button(self.top, text="Submit", state="disabled", command=self.submit, style="ButtonAll.TButton")
			self.ButtonSubmit.place(relx=0.125, rely=0.92, relwidth=0.15, relheight=0.045)

		# Back Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.735, rely=0.92, relwidth=0.15, relheight=0.045)


	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()
		if self.type_privileged_user == "manager":
			self.ButtonViolated.configure(state="disabled")
			self.ButtonNonViolated.configure(state="disabled")
		else:
			self.ButtonSubmit.configure(state="disabled")
		self.Text.configure(state="disabled")

	def selected_item(self, event):
		get_all = self.tree.item(self.tree.selection())
		list_row = get_all.get("values")
		if list_row != "":
			self.id = list_row[0]
			self.complainant = list_row[1]
			self.complained_party_type = list_row[2]
			if self.complained_party_type == "Purchased Item":
				self.complained_party_email = list_row[3]
				self.type_user = "computer_company"
			elif self.complained_party_type == "Store Clerk":
				self.complained_party_email = list_row[3]
				self.type_user = "clerk"
			else:
				self.complained_party_email = list_row[3]
				self.type_user = "delivery"

			complaint_time = list_row[5]
			complaint_detail = self.wrap(list_row[7])
			satisfaction = list_row[4]
			complained_party_response_time = list_row[9]
			complained_party_response = self.wrap(list_row[8])
			manager_justification = self.wrap(list_row[10])
			status = list_row[6]
			# Refresh
			self.refresh()


			self.LabelMyTitle = tk.ttk.Label(self.MyFrame, text="Details of Customer Conplaint:", style="LabelHeadline.TLabel")
			self.LabelMyTitle.grid(sticky="W", row=0, column=0, padx=0, pady=5)

			self.LabelMyTime = tk.ttk.Label(self.MyFrame, text="Conplained on " + complaint_time, style="LabelTime.TLabel")
			self.LabelMyTime.grid(sticky="W", row=1, column=0, padx=0, pady=5)

			self.LabelMyContent = tk.ttk.Label(self.MyFrame, text=complaint_detail ,style="LabelContent.TLabel")
			self.LabelMyContent.grid(sticky="W", row=2, column=0, padx=0, pady=10)
			# Case 1: status = "pending", complained party hasn't responsed yet, show my complaint, disable satisfaction
			if status == "pending":
				if self.type_privileged_user == "manager":
					self.ButtonViolated.configure(state="disabled")
					self.ButtonNonViolated.configure(state="disabled")
					self.Text.configure(state="disabled")
				else:
					self.ButtonSubmit.configure(state="normal")
					self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
					self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)

			# Case 1: status = "pending" and satisfaction = "pending" complained party has responsed, 
			# you need to responed, show my complaint and party response, enable satisfaction
			elif status == "closed":
				self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

				self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="Complained Party Response:", style="LabelHeadline.TLabel")
				self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

				self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="Responsed on " + complained_party_response_time, style="LabelTime.TLabel")
				self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

				self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text=complained_party_response, style="LabelContent.TLabel")
				self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)
				if satisfaction == "dissatisfied":
					if self.type_privileged_user == "manager":
						self.ButtonViolated.configure(state="normal")
						self.ButtonNonViolated.configure(state="normal")
						self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
						self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
					else:
						self.ButtonSubmit.configure(state="disabled")
						self.Text.configure(state="disabled")
				else:
					if self.type_privileged_user == "manager":
						self.ButtonViolated.configure(state="disabled")
						self.ButtonNonViolated.configure(state="disabled")
					else:
						self.ButtonSubmit.configure(state="disabled")
					self.Text.configure(state="disabled")

			# Case 3: Manager decided stay or reverse
			else:
				self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

				self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="Complained Party Response:", style="LabelHeadline.TLabel")
				self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

				self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="Responsed on " + complained_party_response_time, style="LabelTime.TLabel")
				self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

				self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text=complained_party_response, style="LabelContent.TLabel")
				self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

				self.LabelSeg2 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg2.grid(sticky="W", row=7, column=0, padx=0, pady=10)

				self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="Manager Justification:", style="LabelHeadline.TLabel")
				self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=0)

				self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text=manager_justification, style="LabelContent.TLabel")
				self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=10)

				if self.type_privileged_user == "manager":
					self.ButtonViolated.configure(state="disabled")
					self.ButtonNonViolated.configure(state="disabled")
				else:
					self.ButtonSubmit.configure(state="disabled")
				self.Text.configure(state="disabled")


	def refresh(self):
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=1, relheight=0.355)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.4, relheight=0.355, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		self.LabelMyTitle.destroy()
		self.LabelMyTime.destroy()
		self.LabelMyContent.destroy()
		self.LabelSeg1.destroy()
		self.LabelPartyTitle.destroy()
		self.LabelPartyTime.destroy()
		self.LabelPartyContent.destroy()
		self.LabelSeg2.destroy()
		self.LabelManagerTitle.destroy()
		self.LabelManagerContent.destroy()

	def violated(self):
		# Check if the manager justification is valid (not empty)
		manager_justification = self.Text.get("1.0", "end")
		if manager_justification.strip() != "":
			manager_justification = self.wrap(manager_justification)
			# In complaint file, change the status to stay, change the manager justification to entered text
			df_complaint = pd.read_excel("csv_files/complaints.xlsx")
			df_complaint.loc[df_complaint['ID'] == self.id, 'Status'] = 'stay'
			df_complaint.loc[df_complaint['ID'] == self.id, 'Manager Justification'] = manager_justification
			df_complaint.to_excel("csv_files/complaints.xlsx", index=False)

			# Update the treeview
			self.update_treeview()

			# Refresh the comment body
			self.refresh()

			# Complained Party get penalty
			self.update_warning(self.type_user, self.complained_party_email)

			# Disable button untile the next selection
			self.ButtonViolated.configure(state="disabled")
			self.ButtonNonViolated.configure(state="disabled")
			self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
			self.Text.configure(state="disabled")

			tk.messagebox.showinfo("Success", "The complaint is stayed and " + self.complained_party_email + " gets one warning")
		else:
			tk.messagebox.showerror("Error", "Manager Justification cannot be empty")

	def non_violated(self):
		# Check if the manager justification is valid (not empty)
		manager_justification = self.Text.get("1.0", "end")
		if manager_justification.strip() != "":
			manager_justification = self.wrap(manager_justification)
			# In complaint file, change the status to stay, change the manager justification to entered text
			df_complaint = pd.read_excel("csv_files/complaints.xlsx")
			df_complaint.loc[df_complaint['ID'] == self.id, 'Status'] = 'reverse'
			df_complaint.loc[df_complaint['ID'] == self.id, 'Manager Justification'] = manager_justification
			df_complaint.to_excel("csv_files/complaints.xlsx", index=False)

			# Update the treeview
			self.update_treeview()

			# Refresh the comment body
			self.refresh()

			# Complainant get penalty
			self.update_warning("customer", self.complainant)

			# Disable button untile the next selection
			self.ButtonViolated.configure(state="disabled")
			self.ButtonNonViolated.configure(state="disabled")
			self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
			self.Text.configure(state="disabled")

			tk.messagebox.showinfo("Success", "The complaint is reversed and " + self.complainant + " gets one warning")
		else:
			tk.messagebox.showerror("Error", "Manager Justification cannot be empty")

	# For clerk, delivery, and computer company
	def submit(self):
		# Check if the manager justification is valid (not empty)
		complained_party_response = self.Text.get("1.0", "end")
		if complained_party_response.strip() != "":
			complained_party_response = self.wrap(complained_party_response)

			now = datetime.datetime.now()
			date_time = now.strftime("%y-%m-%d %H:%M")
			# In complaints file, change the status closed, change the Complained Party Response to entered text
			df_complaint = pd.read_excel("csv_files/complaints.xlsx")
			df_complaint.loc[df_complaint['ID'] == self.id, 'Status'] = 'closed'
			df_complaint.loc[df_complaint['ID'] == self.id, 'Complained Party Response'] = complained_party_response
			df_complaint.loc[df_complaint['ID'] == self.id, 'Time Response'] = date_time
			df_complaint.to_excel("csv_files/complaints.xlsx", index=False)

			# Update the treeview
			self.update_treeview()

			# Refresh the comment body
			self.refresh()

			# Disable button untile the next selection
			self.ButtonSubmit.configure(state="disabled")
			self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
			self.Text.configure(state="disabled")

			tk.messagebox.showinfo("Success", "Response submitted")
		else:
			tk.messagebox.showerror("Error", "Complained Party Response cannot be empty")

	def back(self):
		if self.type_privileged_user == 'manager':
			self.top.destroy()
			mmp.manager_management_page(self.name, self.username)
		elif self.type_privileged_user == 'clerk':
			self.top.destroy()
			clerk_management_page.clerk_management_page(self.name, self.username)
		elif self.type_privileged_user == 'delivery':
			self.top.destroy()
			delivery_company_management_page.delivery_company_management_page(self.name, self.username)
		else:
			self.top.destroy()
			computer_company_management_page.computer_company_management_page(self.name, self.username)


	def wrap(self, string, lenght=70):
		return '\n'.join(textwrap.wrap(string, lenght))

	def update_treeview(self):
		combo1 = self.Combo1.get()
		df = pd.read_excel("csv_files/complaints.xlsx")
		if combo1 == "All Complaints":
			df_complaint = df
		elif combo1 == "Pending Complaints":
			df_complaint = df[df['Status'] == 'pending']
		elif combo1 == "Closed Complaints & Pending Satisfaction":
			df_complaint = df[df['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'pending']
		elif combo1 == "Closed Complaints & Satisfied":
			df_complaint = df[df['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'satisfied']
		elif combo1 == "Closed Complaints & Dissatisfied":
			df_complaint = df[df['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'dissatisfied']
		elif combo1 == "Stay Complaints":
			df_complaint = df[df['Status'] == 'stay']
		else:
			df_complaint = df[df['Status'] == 'reverse']

		df_complaint = df_complaint[['ID', 'Complainant', 'Complained Party Type', 'Complained Party Email', 'Satisfaction','Time Complained', 
									 'Status', 'Complained Details', 'Complained Party Response', 'Time Response', 'Manager Justification']]
		if self.type_privileged_user == 'clerk' or self.type_privileged_user == 'delivery':
			df_complaint = df_complaint[df_complaint['Complained Party Email'] == self.username]
		elif self.type_privileged_user == 'computer_company':
			df_complaint = df_complaint[df_complaint['Complained Party Email'] == self.username]

			
		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.06, rely=0.15, relwidth=0.9, relheight=0.2)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		self.tree["column"] = ("ID", "Complainant", "Complained Party Type", "Complained Party Email", "Satisfaction", "Time Complained", "Status")
		self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		self.tree.column("Complainant", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Complained Party Type", anchor=tk.W, width=140, stretch=tk.NO)
		self.tree.column("Complained Party Email", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Satisfaction", anchor=tk.W, width=85, stretch=tk.NO)
		self.tree.column("Time Complained", anchor=tk.W, width=105, stretch=tk.NO)
		self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		self.tree.heading("ID", text="ID", anchor=tk.W)
		self.tree.heading("Complainant", text="Complainant", anchor=tk.W)
		self.tree.heading("Complained Party Type", text="Complained Party Type", anchor=tk.W)
		self.tree.heading("Complained Party Email", text="Complained Party Email", anchor=tk.W)
		self.tree.heading("Satisfaction", text="Satisfaction", anchor=tk.W)
		self.tree.heading("Time Complained", text="Time Complained", anchor=tk.W)
		self.tree.heading("Status", text="Status", anchor=tk.W)

		df_rows = df_complaint.to_numpy().tolist()

		for row in df_rows:
			self.tree.insert("", "end", value=row)

	def update_warning(self, type_user, username):
		if type_user == "customer":
			df = pd.read_excel("csv_files/registered_customers.xlsx")
			df_cus_active = df[df['Status'] == "active"]
			if username.lower() in list(df_cus_active['Username']):
				flag_username_exist = True
				df_user_row = df[df['Username'] == username]
				df_row_list = df_user_row.to_numpy().tolist()
				name = df_row_list[0][4]
				password = df_row_list[0][3]
				current_warning = int(df_user_row['Warnings'].iloc[-1])

				chance_login = 1
				deny_notify = 1
			else:
				flag_username_exist = False
				tk.messagebox.showerror("Erorr", "Username not found, this may occurred when the username is already suspended, failed to update the warning")

		else:
			df = pd.read_excel("csv_files/privileged_users.xlsx")
			df2 = df[df['Type_user'] == type_user]
			df_privileged_active = df2[df2['Status'] == "active"]
			if username.lower() in list(df_privileged_active['Username']):
				flag_username_exist = True
				df_user_row = df[df['Username'] == username]
				df_row_list = df_user_row.to_numpy().tolist()
				name = df_row_list[0][1]
				password = df_row_list[0][3]
				current_warning = int(df_user_row['Warnings'].iloc[-1])

				chance_login = 1
				deny_notify = 0
			else:
				flag_username_exist = False
				tk.messagebox.showerror("Erorr", "Username not found, this may occurred when the username is already suspended, failed to update the warning")

		if flag_username_exist:
			# Update the warning (+1)
			if current_warning < 3:
				current_warning = current_warning + 1
				if type_user == "customer":
					df.loc[df['Username'] == username, 'Warnings'] = current_warning
					df.to_excel("csv_files/registered_customers.xlsx", index=False)
				else:
					df['Warnings'] = np.where((df['Username'] == username) & (df['Type_user'] == type_user), current_warning, df.Warnings)
					df.to_excel("csv_files/privileged_users.xlsx", index=False)

			# Auto suspend if Warning == 3
			if current_warning >= 3:
				df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
				df_suspend_type = df_suspend[df_suspend['Type_user'] == type_user]
				suspend_reason = "3 standing warnings"
				if len(df_suspend) == 0:
					Id = 0
					tempo = pd.DataFrame([[str(Id), type_user, username.lower(), password, name, current_warning, suspend_reason, chance_login, deny_notify]], 
						columns=['ID', 'Type_user', 'Username', 'Password', 'Name','Current_warnings', 'Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
					df_suspend = df_suspend.append(tempo)

				else:
					if not username.lower() in list(df_suspend_type['Username']):
						Id = int(df_suspend['ID'].iloc[-1])
						Id = Id+1
						tempo = pd.DataFrame([[str(Id), type_user, username.lower(), password, name, current_warning, suspend_reason, chance_login, deny_notify]], 
							columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
						df_suspend = df_suspend.append(tempo)

				# update suspend_user file and customers file
				df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
				if type_user == "customer":
					df_cus = pd.read_excel("csv_files/registered_customers.xlsx")
					df_cus.loc[df_cus['Username'] == username, 'Status'] = 'suspended'
					df_cus.to_excel("csv_files/registered_customers.xlsx", index=False)
				else:
					df_privileged = pd.read_excel("csv_files/privileged_users.xlsx")
					df_privileged['Status'] = np.where((df_privileged['Username'] == username) & (df_privileged['Type_user'] == type_user), 'suspended', df_privileged.Status)
					#df_privileged.loc[df_privileged['Username'] == username, 'Status'] = 'suspended'
					df_privileged.to_excel("csv_files/privileged_users.xlsx", index=False)

