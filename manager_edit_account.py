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
import manager_view_account as mva


class edit_account_page(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.admin_name = name
		self.admin_username = username

		self.master.title("Edit Account Page")
		self.master.geometry("463x425")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Edit Account Information ", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.079)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="Modify:", style='Label1.TLabel')
		self.Label1.place(relx=0.12, rely=0.123, relwidth=0.4, relheight=0.062)

		self.Combo1List1 = ["Store Clerk", "Computer Company", "Delivery Company", "Customer"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.4, rely=0.123, relwidth=0.4, relheight=0.068)
		self.Combo1.set(self.Combo1List1[0])

		# Row 2
		self.Label2 = tk.ttk.Label(self.top, text="Operations:", style='Label1.TLabel')
		self.Label2.place(relx=0.12, rely=0.215, relwidth=0.4, relheight=0.062)
		self.Combo1List2 = ["Create", "Suspend"]
		self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List2, font=("Helvetica",11))
		self.Combo2.bind("<<ComboboxSelected>>", self.get_combo2)
		self.Combo2.place(relx=0.4, rely=0.215, relwidth=0.4, relheight=0.068)
		self.Combo2.set(self.Combo1List2[0])

		# Row 3 Name
		self.Label3 = tk.ttk.Label(self.top, text="Name:", style='Label1.TLabel')
		self.Label3.place(relx=0.12, rely=0.307, relwidth=0.4, relheight=0.062)

		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11))
		self.Text3.place(relx=0.4, rely=0.307, relwidth=0.4, relheight=0.068)

		# Row 4 User Name
		self.Label4 = tk.ttk.Label(self.top, text="User Name:", style='Label1.TLabel')
		self.Label4.place(relx=0.12, rely=0.399, relwidth=0.4, relheight=0.062)

		self.Text4Var = tk.StringVar(value="Please enter email")
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11))
		self.Text4.place(relx=0.4, rely=0.399, relwidth=0.4, relheight=0.068)

		# Row 5 Password
		self.Label5 = tk.ttk.Label(self.top, text="Password:", style='Label1.TLabel')
		self.Label5.place(relx=0.12, rely=0.491, relwidth=0.4, relheight=0.062)

		self.Text5Var = tk.StringVar()
		self.Text5 = tk.ttk.Entry(self.top, textvariable=self.Text5Var, font=("Helvetica",11))
		self.Text5.place(relx=0.4, rely=0.491, relwidth=0.4, relheight=0.068)

		# Row 6 Suspend Reason
		self.Label6 = tk.ttk.Label(self.top, text="Suspend \nJustification:", style='Label1.TLabel')
		self.Label6.place(relx=0.12, rely=0.56, relwidth=0.4, relheight=0.162)

		self.Text6 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD, state="disable")
		self.Text6.place(relx=0.4, rely=0.583, relwidth=0.4, relheight=0.22)

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.43, rely=0.86, relwidth=0.19, relheight=0.09)

		# View account Buttton
		self.CommandView = tk.ttk.Button(self.top, text="View Accounts", command=self.command_view, style="CommandConfirm.TButton")
		self.CommandView.place(relx=0.07, rely=0.86, relwidth=0.29, relheight=0.09)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Back", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.72, rely=0.86, relwidth=0.19, relheight=0.09)

	def get_combo1(self, event):
		if self.Combo1.get() == "Customer":
			self.Combo1List2 = ["Suspend"]
			self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List2, font=("Helvetica",11))
			self.Combo2.bind("<<ComboboxSelected>>", self.get_combo2)
			self.Combo2.place(relx=0.4, rely=0.215, relwidth=0.4, relheight=0.068)
		else:
			self.Combo1List2 = ["Create", "Suspend"]
			self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List2, font=("Helvetica",11))
			self.Combo2.bind("<<ComboboxSelected>>", self.get_combo2)
			self.Combo2.place(relx=0.4, rely=0.215, relwidth=0.4, relheight=0.068)
		self.create_refresh_textbox()

	def get_combo2(self, event):
		if self.Combo2.get() == "Suspend":
			self.suspend_refresh_textbox()

		else:
			self.create_refresh_textbox()


	def command_view(self):
		self.top.destroy()
		mva.view_account_page(self.admin_name, self.admin_username)

	def command_confirm(self, event=None):

		if self.Combo1.get() == "Store Clerk" and self.Combo2.get() == "Create":
			type_user = "clerk"
			self.create_staff(type_user)

		elif self.Combo1.get() == "Computer Company" and self.Combo2.get() == "Create":
			type_user = "computer_company"
			self.create_staff(type_user)

		elif self.Combo1.get() == "Delivery Company" and self.Combo2.get() == "Create":
			type_user = "delivery"
			self.create_staff(type_user)

		elif self.Combo1.get() == "Store Clerk" and self.Combo2.get() == "Suspend":
			type_user = "clerk"
			self.suspend_user(type_user)

		elif self.Combo1.get() == "Computer Company" and self.Combo2.get() == "Suspend":
			type_user = "computer_company"
			self.suspend_user(type_user)

		elif self.Combo1.get() == "Delivery Company" and self.Combo2.get() == "Suspend":
			type_user = "delivery"
			self.suspend_user(type_user)

		else:
			type_user = "customer"
			self.suspend_user(type_user)

		if self.Combo2.get() == "Suspend":
			self.suspend_refresh_textbox()

		else:
			self.create_refresh_textbox()

	def command_cancel(self, event=None):
		self.top.destroy()
		mmp.manager_management_page(self.admin_name, self.admin_username)

	def create_staff(self, type_user):
		Name = self.Text3.get()
		Username = self.Text4.get().lower()
		Password = self.Text5.get()


    	#----------------Check if the username is a working email----------------

		regex = "[A-Za-z0-9_]+[@]\w+[.]\w{2,3}$"
		if(  re.fullmatch(regex, Username) ):
			flag_valid_email = True
		else:
			flag_valid_email = False
			tk.messagebox.showerror( "Error", "invalid email username" )
    	#-------------------------------------------------------------------------

    	#---------------------check if the password is valid(no empty)-----------------------
		if Password != "":
			flag_password_valid = True
		else:
			tk.messagebox.showerror( "Error", "invalid password" )
			flag_password_valid = False

    	#-----------------------------------------------------------------------

    	#--------------Check if the username is already registered------------
		flag_suspended = self.is_suspended(type_user, Username)
		if not flag_suspended:
			df = pd.read_excel("csv_files/privileged_users.xlsx")
			Id = int(df['ID'].iloc[-1])
			Id = Id+1
			flag_duplicates = False
			warning = 0
			income = 0
			status = 'active'
			df_user = df[df['Type_user'] == type_user ]
			df_user_active = df_user[df_user['Status'] == 'active']
			if Username in list(df_user_active['Username']):
				# We have duplicates accounts
				flag_duplicates = True
				tk.messagebox.showerror("Error", "Username is taken")
			else:
				tempo = pd.DataFrame([[str(Id), type_user, Username, Password, Name, warning, income, status]], 
					columns=['ID','Type_user', 'Username', 'Password', 'Name', 'Warnings', 'Income', 'Status'])
				df = df.append(tempo)
		else:
			tk.messagebox.showerror( "Error", "Username has been suspended")

		#----------------------------------------------------------------------------------
		if (not flag_duplicates) and (not flag_suspended) and flag_valid_email and flag_password_valid:
			df.to_excel("csv_files/privileged_users.xlsx", index=False)
			tk.messagebox.showinfo("Success", "New " + type_user + " " + Username +" created")
		

	def suspend_user(self, type_user):
		Username = self.Text4.get().lower()
		SuspendReason = self.Text6.get("1.0", "end")
		#----------Check if username exist actively------------------------------------
		if type_user == "customer":
			df = pd.read_excel("csv_files/registered_customers.xlsx")
			df = df[df['Status'] == 'active']
			DenyNotify = 1
			if Username.lower() in list(df['Username']):
				flag_username_exist = True
				# Get his/her Password, Name, Warnings
				df_user_row = df[df['Username'] == Username]
				Password = str(df_user_row['Password'].iloc[-1])
				Name = df_user_row['Name'].iloc[-1]
				CurrentWarning = df_user_row['Warnings'].iloc[-1]
			else:
				flag_username_exist = False
				tk.messagebox.showerror("Error", "No such active username exist")
		else:
			df = pd.read_excel("csv_files/privileged_users.xlsx")
			df_user = df[ df['Type_user'] == type_user ]
			df_user = df_user[df_user['Status'] == 'active']
			DenyNotify = 0
			if Username.lower() in list(df_user['Username']):
				flag_username_exist = True
				# Get his/her Password, Name, Warnings
				df_user_row = df[df['Username'] == Username]
				Password = str(df_user_row['Password'].iloc[-1])
				Name = df_user_row['Name'].iloc[-1]
				CurrentWarning = df_user_row['Warnings'].iloc[-1]
			else:
				flag_username_exist = False
				tk.messagebox.showerror("Error", "No such active username exist")
		#--------------------------------------------------------------------------

		#----------Check if suspend reason is empty---------------------------------
		if SuspendReason.strip() != "":
			flag_suspend_valid = True
			SuspendReason = self.wrap(SuspendReason)
		else:
			flag_suspend_valid = False
			tk.messagebox.showerror("Error", "Suspend justification cannot be empty")
		#-------------------------------------------------------------------------------

		#------------Check if username is already suspended ----------------------------
		df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
		df_suspend_type = df_suspend[df_suspend['Type_user'] == type_user]
		flag_suspend_duplicates = False
		ChanceLogin = 1

		if len(df_suspend) == 0 and flag_username_exist:
			Id = 0
			tempo = pd.DataFrame([[Id, type_user, Username.lower(), Password, Name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
				columns=['ID', 'Type_user', 'Username', 'Password', 'Name','Current_warnings', 'Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
			df_suspend = df_suspend.append(tempo)

		else:
			if not flag_username_exist and Username.lower() in list(df_suspend_type['Username']):
				flag_suspend_duplicates = True
				tk.messagebox.showerror("Error", "Username has been suspended already")
			elif flag_username_exist:
				Id = int(df_suspend['ID'].iloc[-1])
				Id = Id+1
				tempo = pd.DataFrame([[Id, type_user, Username.lower(), Password, Name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
					columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
				df_suspend = df_suspend.append(tempo)
		#--------------------------------------------------------------------------------
		#------------Update the corresponding csv file------------------------------------
		if (not flag_suspend_duplicates) and flag_suspend_valid and flag_username_exist:
			#df_suspend.drop("Unnamed: 9", axis=1)
			df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
			tk.messagebox.showinfo("Success", "Username: " + Username + " is suspended")
			# Update status to 'suspended' from customers or privileged users file
			if type_user == "customer":
				df = pd.read_excel("csv_files/registered_customers.xlsx")
				df.loc[df['Username'] == Username, 'Status'] = 'suspended'
				df.to_excel("csv_files/registered_customers.xlsx", index=False)
			else:
				df = pd.read_excel("csv_files/privileged_users.xlsx")
				df.loc[df['Username'] == Username, 'Status'] = 'suspended'
				df.to_excel("csv_files/privileged_users.xlsx", index=False)


	def is_suspended(self, type_user, username):
		df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
		df_suspend_user = df_suspend[df_suspend['Type_user'] == type_user]
		flag_suspended = False
		if username.lower() in list(df_suspend_user['Username']):
			flag_suspended = True
		return flag_suspended

	def wrap(self, string, lenght=55):
		return '\n'.join(textwrap.wrap(string, lenght))

	def create_refresh_textbox(self):
		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11))
		self.Text3.place(relx=0.4, rely=0.307, relwidth=0.4, relheight=0.068)

		self.Text4Var = tk.StringVar(value="Pleasr enter email")
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11))
		self.Text4.place(relx=0.4, rely=0.399, relwidth=0.4, relheight=0.068)

		self.Text5Var = tk.StringVar()
		self.Text5 = tk.ttk.Entry(self.top, textvariable=self.Text5Var, font=("Helvetica",11))
		self.Text5.place(relx=0.4, rely=0.491, relwidth=0.4, relheight=0.068)

		self.Text6 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD, state="disable")
		self.Text6.place(relx=0.4, rely=0.583, relwidth=0.4, relheight=0.22)

	def suspend_refresh_textbox(self):
		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11), state="disable")
		self.Text3.place(relx=0.4, rely=0.307, relwidth=0.4, relheight=0.068)

		self.Text4Var = tk.StringVar(value="Pleasr enter email")
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11))
		self.Text4.place(relx=0.4, rely=0.399, relwidth=0.4, relheight=0.068)

		self.Text5Var = tk.StringVar()
		self.Text5 = tk.ttk.Entry(self.top, textvariable=self.Text5Var, font=("Helvetica",11), state="disable")
		self.Text5.place(relx=0.4, rely=0.491, relwidth=0.4, relheight=0.068)

		self.Text6 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.Text6.place(relx=0.4, rely=0.583, relwidth=0.4, relheight=0.22)
