import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
import textwrap

# python scripts 
import manager_management_page as mmp

class edit_discussion_page(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.admin_name = name
		self.admin_username = username

		self.master.title("Edit Discussion Report Page")
		self.master.geometry("663x955")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Edit Discussion Report ", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.252, rely=0.015, relwidth=0.52, relheight=0.043)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.195, rely=0.09, relwidth=0.3, relheight=0.026)

		self.Combo1List1 = ["All Discussion Report", "Pending Discussion Report"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.49, rely=0.09, relwidth=0.35, relheight=0.032)
		self.Combo1.set(self.Combo1List1[0])

		# Treeview
		df_report = pd.read_excel("csv_files/discussion_reports.xlsx")

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.08, rely=0.15, relwidth=0.85, relheight=0.2)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		#self.tree["column"] = list(df_report.columns)
		self.tree["columns"] = ("ID", "Reporter", "Reported Comment ID", "Reported Time", "Status")
		self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		self.tree.column("Reporter", anchor=tk.W, width=230, stretch=tk.NO)
		self.tree.column("Reported Comment ID", anchor=tk.W, width=130, stretch=tk.NO)
		self.tree.column("Reported Time", anchor=tk.W, width=95, stretch=tk.NO)
		self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		# for column in self.tree["column"]:
		# 	self.tree.heading(column, text=column, anchor=tk.W)
		self.tree.heading("ID", text="ID", anchor=tk.W)
		self.tree.heading("Reporter", text="Reporter", anchor=tk.W)
		self.tree.heading("Reported Comment ID", text="Reported Comment ID", anchor=tk.W)
		self.tree.heading("Reported Time", text="Reported Time", anchor=tk.W)
		self.tree.heading("Status", text="Status", anchor=tk.W)

		df_rows = df_report.to_numpy().tolist()
		for row in df_rows:
			self.tree.insert("", "end", value=row)

		# Reported Comment Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Reported Comment Content", style='LabelHead.TLabel')
		self.LabelHead.place(relx=0.34, rely=0.36, relwidth=0.35, relheight=0.04)

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

		self.LabelID = tk.ttk.Label(self.MyFrame, text="", style="LabelType.TLabel")
		self.LabelID.grid(sticky="W", row=0, column=0, padx=0, pady=5)

		self.LabelComputer = tk.ttk.Label(self.MyFrame, text="", style="LabelType.TLabel")
		self.LabelComputer.grid(sticky="W", row=1, column=0, padx=0, pady=10)

		self.LabelType = tk.ttk.Label(self.MyFrame, text="" ,style="LabelType.TLabel")
		self.LabelType.grid(sticky="W", row=2, column=0, padx=0, pady=5)

		self.LabelVote = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelVote.grid(sticky="W", row=3, column=0, padx=0, pady=3)

		self.LabelTime = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelTime.grid(sticky="W", row=4, column=0, padx=0, pady=10)

		self.LabelHeadline = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelHeadline.grid(sticky="W", row=5, column=0, padx=0, pady=5)

		self.LabelContent = tk.ttk.Label(self.MyFrame, text="", style="LabelContent.TLabel")
		self.LabelContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

		# Manager Justification
		self.LabelJustification = tk.ttk.Label(self.top, text="Manager Justification:", style='LabelHead.TLabel')
		self.LabelJustification.place(relx=0.36, rely=0.765, relwidth=0.35, relheight=0.04)

		self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
		self.Text.configure(state="disabled")


		# Violated Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonViolated = tk.ttk.Button(self.top, text="Violated", state="disabled", command=self.violated, style="ButtonAll.TButton")
		self.ButtonViolated.place(relx=0.125, rely=0.92, relwidth=0.15, relheight=0.045)

		# Non-Violated Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonNonViolated = tk.ttk.Button(self.top, text="Non-Violated", state="disabled", command=self.non_violated, style="ButtonAll.TButton")
		self.ButtonNonViolated.place(relx=0.415, rely=0.92, relwidth=0.2, relheight=0.045)

		# Back Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.735, rely=0.92, relwidth=0.15, relheight=0.045)


	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()
		# Disable button and text untile the next selection
		self.ButtonViolated.configure(state="disabled")
		self.ButtonNonViolated.configure(state="disabled")
		self.Text.configure(state="disabled")

	def selected_item(self, event):
		get_all = self.tree.item(self.tree.selection())
		list_row = get_all.get("values")
		if list_row != "":
			self.ID = list_row[0]
			self.Reporter = list_row[1]
			self.ReportedCommentID = list_row[2]
			self.ReportedTime = list_row[3]
			self.Status = list_row[4]
			self.Justification = list_row[5]


			if self.Status == "pending":
				# Enable button and text
				self.ButtonViolated = tk.ttk.Button(self.top, text="Violated", command=self.violated, style="ButtonAll.TButton")
				self.ButtonViolated.place(relx=0.125, rely=0.92, relwidth=0.15, relheight=0.05)

				self.ButtonNonViolated = tk.ttk.Button(self.top, text="Non-Violated", command=self.non_violated, style="ButtonAll.TButton")
				self.ButtonNonViolated.place(relx=0.415, rely=0.92, relwidth=0.2, relheight=0.05)

				self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
				self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)


			df_discussion = pd.read_excel("csv_files/discussions.xlsx")
			df_row = df_discussion[df_discussion['ID'] == self.ReportedCommentID]
			df_row_list = df_row.to_numpy().tolist()
			self.CommentID = df_row_list[0][0]
			self.TypeUser = df_row_list[0][1]
			self.ReportedUserName = df_row_list[0][2]
			self.ComputerName = df_row_list[0][4]
			self.Vote = df_row_list[0][5]
			self.Headline = df_row_list[0][6]
			self.Comment = df_row_list[0][7]
			self.Time = df_row_list[0][8]

			# Refresh
			self.refresh()

			# Display the selected reported comment
			self.LabelID = tk.ttk.Label(self.MyFrame, text="Coment ID: " + str(self.CommentID), style="LabelType.TLabel")
			self.LabelID.grid(sticky="W", row=0, column=0, padx=0, pady=5)

			self.LabelComputer = tk.ttk.Label(self.MyFrame, text="Computer: " + self.ComputerName, style="LabelType.TLabel")
			self.LabelComputer.grid(sticky="W", row=1, column=0, padx=0, pady=10)

			self.LabelType = tk.ttk.Label(self.MyFrame, text=self.TypeUser + ": " + self.ReportedUserName, style="LabelType.TLabel")
			self.LabelType.grid(sticky="W", row=2, column=0, padx=0, pady=5)

			self.LabelVote = tk.ttk.Label(self.MyFrame, text=self.rate_text(self.Vote), foreground="#DAA520", style="LabelTime.TLabel")
			self.LabelVote.grid(sticky="W", row=3, column=0, padx=0, pady=3)

			self.LabelTime = tk.ttk.Label(self.MyFrame, text="Reviewed on " + self.Time, style="LabelTime.TLabel")
			self.LabelTime.grid(sticky="W", row=4, column=0, padx=0, pady=10)

			self.LabelHeadline = tk.ttk.Label(self.MyFrame, text=self.Headline, style="LabelHeadline.TLabel")
			self.LabelHeadline.grid(sticky="W", row=5, column=0, padx=0, pady=5)

			self.Comment = self.wrap(self.Comment)
			self.LabelContent = tk.ttk.Label(self.MyFrame, text=self.Comment, style="LabelContent.TLabel")
			self.LabelContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

			if self.Status == "stay":
				self.LabelNotice = tk.ttk.Label(self.MyFrame, text="NOTICE: This comment is violated and will not be shown to customers", style="LabelType.TLabel")
				self.LabelNotice.grid(sticky="W", row=7, column=0, padx=0, pady=10)

				self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="Manager Justification:", style="LabelType.TLabel")
				self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=5)

				self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text=self.Justification, style="LabelContent.TLabel")
				self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=5)

			elif self.Status == "reverse":
				self.LabelNotice = tk.ttk.Label(self.MyFrame, text="NOTICE: This comment is non-violated", style="LabelType.TLabel")
				self.LabelNotice.grid(sticky="W", row=7, column=0, padx=0, pady=10)

				self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="Manager Justification:", style="LabelType.TLabel")
				self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=5)

				self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text=self.Justification, style="LabelContent.TLabel")
				self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=5)

	def refresh(self):
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=1, relheight=0.355)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.4, relheight=0.355, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		self.LabelID.destroy()
		self.LabelComputer.destroy()
		self.LabelType.destroy()
		self.LabelVote.destroy()
		self.LabelTime.destroy()
		self.LabelHeadline.destroy()
		self.LabelContent.destroy()

	def violated(self):
		# Check if the manager justification is valid (not empty)
		ManagerJustification = self.Text.get("1.0", "end")
		if ManagerJustification.strip() != "":
			ManagerJustification = self.wrap(ManagerJustification)
			# In discussion_report file, change the status to stay, change the manager justification to entered text
			df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report.loc[df_report['ID'] == self.ID, 'Status'] = 'stay'
			df_report.loc[df_report['ID'] == self.ID, 'Manager Justification'] = ManagerJustification
			df_report.to_excel("csv_files/discussion_reports.xlsx", index=False)

			# Change the status in discussion to violated
			df_discussion = pd.read_excel("csv_files/discussions.xlsx")
			#df_discussion.drop(df_discussion.index[(df_discussion['ID'] == self.CommentID)], axis=0, inplace=True)
			df_discussion.loc[df_discussion['ID'] == self.CommentID, 'Status'] = "Violated"
			df_discussion.to_excel("csv_files/discussions.xlsx", index=False)

			# Update the treeview
			self.update_treeview()

			# Refresh the comment body
			self.refresh()

			# Reported username get penalty
			self.update_warning(self.ReportedUserName)

			# Disable button untile the next selection
			self.ButtonViolated.configure(state="disabled")
			self.ButtonNonViolated.configure(state="disabled")

			self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
			self.Text.configure(state="disabled")
		else:
			tk.messagebox.showerror("Error", "Manager Justification cannot be empty")


	def non_violated(self):
		# Check if the manager justification is valid (not empty)
		ManagerJustification = self.Text.get("1.0", "end")
		if ManagerJustification.strip() != "":
			ManagerJustification = self.wrap(ManagerJustification)
			# In discussion_report file, change the status to change the manager justification to entered text
			df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report.loc[df_report['ID'] == self.ID, 'Status'] = 'reverse'
			df_report.loc[df_report['ID'] == self.ID, 'Manager Justification'] = ManagerJustification
			df_report.to_excel("csv_files/discussion_reports.xlsx", index=False)

			# Update the treeview
			self.update_treeview()

			# Refresh the comment body
			self.refresh()

			# Reporter get penalty
			self.update_warning(self.Reporter)

			# Disable button untile the next selection
			self.ButtonViolated.configure(state="disabled")
			self.ButtonNonViolated.configure(state="disabled")

			self.Text = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.Text.place(relx=0.049, rely=0.8, relwidth=0.9, relheight=0.09)
			self.Text.configure(state="disabled")
		else:
			tk.messagebox.showerror("Error", "Manager Justification cannot be empty")


	def back(self):
		self.top.destroy()
		mmp.manager_management_page(self.admin_name, self.admin_username)

	def rate_text(self, rate):
		if str(rate) == "1":
			return "★☆☆☆☆"
		elif str(rate) == "2":
			return "★★☆☆☆"
		elif str(rate) == "3":
			return "★★★☆☆"
		elif str(rate) == "4":
			return "★★★★☆"
		else:
			return "★★★★★"

	def wrap(self, string, lenght=55):
		return '\n'.join(textwrap.wrap(string, lenght))

	def update_treeview(self):
		if self.Combo1.get() == "All Discussion Report":
			df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
		else:
			df =  pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report = df[df["Status"] == "pending"]
		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.08, rely=0.15, relwidth=0.85, relheight=0.2)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		self.tree["columns"] = ("ID", "Reporter", "Reported Comment ID", "Reported Time", "Status")
		self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		self.tree.column("Reporter", anchor=tk.W, width=230, stretch=tk.NO)
		self.tree.column("Reported Comment ID", anchor=tk.W, width=130, stretch=tk.NO)
		self.tree.column("Reported Time", anchor=tk.W, width=95, stretch=tk.NO)
		self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		self.tree.heading("ID", text="ID", anchor=tk.W)
		self.tree.heading("Reporter", text="Reporter", anchor=tk.W)
		self.tree.heading("Reported Comment ID", text="Reported Comment ID", anchor=tk.W)
		self.tree.heading("Reported Time", text="Reported Time", anchor=tk.W)
		self.tree.heading("Status", text="Status", anchor=tk.W)

		df_rows = df_report.to_numpy().tolist()
		for row in df_rows:
			self.tree.insert("", "end", value=row)

	def update_warning(self, username):
		df = pd.read_excel("csv_files/registered_customers.xlsx")
		df_active = df[df['Status'] == "active"]
		if username.lower() in list(df_active['Username']):
			df_user_row = df[df['Username'] == username]
			df_row_list = df_user_row.to_numpy().tolist()
			type_user = "customer"
			name = df_row_list[0][1]
			password = df_row_list[0][3]

			CurrentWarning = int(df_user_row['Warnings'].iloc[-1])
			# Update the warning if taboo word found
			if CurrentWarning < 3:
				CurrentWarning = CurrentWarning + 1
				df.loc[df['Username'] == username, 'Warnings'] = CurrentWarning
				df.to_excel("csv_files/registered_customers.xlsx", index=False)
			# Auto suspend if Warning == 3
			if CurrentWarning >= 3:
				df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
				df_suspend_type = df_suspend[df_suspend['Type_user'] == type_user]
				ChanceLogin = 1
				DenyNotify = 1
				SuspendReason = "3 standing warnings"
				if len(df_suspend) == 0:
					Id = 0
					tempo = pd.DataFrame([[str(Id), type_user, username.lower(), password, name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
						columns=['ID', 'Type_user', 'Username', 'Password', 'Name','Current_warnings', 'Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
					df_suspend = df_suspend.append(tempo)

				else:
					if not username.lower() in list(df_suspend_type['Username']):
						Id = int(df_suspend['ID'].iloc[-1])
						Id = Id+1
						tempo = pd.DataFrame([[str(Id), type_user, username.lower(), password, name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
							columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
						df_suspend = df_suspend.append(tempo)
				# update suspend_user file and customers file
				df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
				df_cus = pd.read_excel("csv_files/registered_customers.xlsx")
				df_cus.loc[df_cus['Username'] == username, 'Status'] = 'suspended'
				df_cus.to_excel("csv_files/registered_customers.xlsx", index=False)

		else:
			tk.messagebox.showerror("Erorr", "Customer username not found, this may occurred when the customer is already suspended, failed to update the warning")


