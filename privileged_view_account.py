import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts
import clerk_management_page
import delivery_company_management_page
import computer_company_management_page

class privileged_view_account(tk.Frame):

	def __init__(self, type_user, name, username, master=None): #type_user, name, username,
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username
		self.type_user = type_user

		df_privilege_user = pd.read_excel('csv_files/privileged_users.xlsx')
		df_user_row = df_privilege_user[(df_privilege_user['Type_user'] == self.type_user) & (df_privilege_user['Username'] == self.username)]
		self.password = str(df_user_row['Password'].iloc[-1])
		self.income = "$ {:,.2f}".format(df_user_row['Income'].iloc[-1])
		self.warning = str(df_user_row['Warnings'].iloc[-1])
		self.status = str(df_user_row['Status'].iloc[-1])

		self.master.title("View Account Info Page")
		self.master.geometry("560x555")
		self.master.configure( background = "light blue" )

		self.create_widgets()


	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text='View My Account Information', style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.19, rely=0.015, relwidth=0.62, relheight=0.079)

		# Row 0 Name
		self.style.configure("LabelSub.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.LabelName = tk.ttk.Label(self.top, text = 'Name:', style='LabelSub.TLabel')
		self.LabelName.place(relx=0.145, rely=0.15, relwidth=0.8, relheight=0.079)

		self.Text0Var = tk.StringVar(value=self.name)
		self.Text0 = tk.ttk.Entry(self.top, textvariable=self.Text0Var, font=("Helvetica",11), state='readonly')
		self.Text0.place(relx=0.45, rely=0.15, relwidth=0.4, relheight=0.064)

		# Row 1 Username
		self.LabelUsername = tk.ttk.Label(self.top, text = 'Username:', style='LabelSub.TLabel')
		self.LabelUsername.place(relx=0.145, rely=0.28, relwidth=0.8, relheight=0.079)

		self.Text1Var = tk.StringVar(value=self.username)
		self.Text1 = tk.ttk.Entry(self.top, textvariable=self.Text1Var, font=("Helvetica",11), state='readonly')
		self.Text1.place(relx=0.45, rely=0.28, relwidth=0.4, relheight=0.064)

		# Row 2 Password
		self.LabelPassword = tk.ttk.Label(self.top, text = 'Password:', style='LabelSub.TLabel')
		self.LabelPassword.place(relx=0.145, rely=0.41, relwidth=0.8, relheight=0.079)

		self.Text2Var = tk.StringVar(value=self.password)
		self.Text2 = tk.ttk.Entry(self.top, textvariable=self.Text2Var, font=("Helvetica",11), state='readonly')
		self.Text2.place(relx=0.45, rely=0.41, relwidth=0.4, relheight=0.064)

		# Row 3 Income
		self.LabelIncome = tk.ttk.Label(self.top, text = 'Income:', style='LabelSub.TLabel')
		self.LabelIncome.place(relx=0.145, rely=0.54, relwidth=0.8, relheight=0.079)

		self.Text3Var = tk.StringVar(value=self.income)
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11), state='readonly')
		self.Text3.place(relx=0.45, rely=0.54, relwidth=0.4, relheight=0.064)

		# Row 4 Warning
		self.LabelWarning = tk.ttk.Label(self.top, text = 'Waring:', style='LabelSub.TLabel')
		self.LabelWarning.place(relx=0.145, rely=0.67, relwidth=0.8, relheight=0.079)

		self.Text4Var = tk.StringVar(value=self.warning)
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11), state='readonly')
		self.Text4.place(relx=0.45, rely=0.67, relwidth=0.4, relheight=0.064)

		# Row 5 Status
		self.LabelStatus = tk.ttk.Label(self.top, text = 'Status:', style='LabelSub.TLabel')
		self.LabelStatus.place(relx=0.145, rely=0.8, relwidth=0.8, relheight=0.079)

		self.Text5Var = tk.StringVar(value=self.status)
		self.Text5 = tk.ttk.Entry(self.top, textvariable=self.Text5Var, font=("Helvetica",11), state='readonly')
		self.Text5.place(relx=0.45, rely=0.8, relwidth=0.4, relheight=0.064)

		# Back Button
		self.style.configure("CommandBack.TButton", font=("Helvetica",14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.command_back, style="CommandBack.TButton")
		self.ButtonBack.place(relx=0.77, rely=0.925, relwidth=0.19, relheight=0.066)

	def command_back(self):
		self.top.destroy()
		if self.type_user == 'clerk':
			clerk_management_page.clerk_management_page(self.name, self.username)
		elif self.type_user == 'delivery':
			delivery_company_management_page.delivery_company_management_page(self.name, self.username)
		else:
			computer_company_management_page.computer_company_management_page(self.name, self.username)



# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    privileged_view_account(top).mainloop()   
