import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts 
import manager_management_page as mmp
import clerk_management_page
import view_account_table as vat

class edit_taboo_page(tk.Frame):

	def __init__(self, coming_from, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.coming_from = coming_from
		self.name = name
		self.username = username

		self.master.title("Edit Taboo Page")
		self.master.geometry("463x425")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Edit Taboo List", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.079)

		# Row 1 View taboo list button
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="Taboo list:", style='Label1.TLabel')
		self.Label1.place(relx=0.17, rely=0.2, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_list('taboo_list'), style="CommandView.TButton")
		self.CommandView.place(relx=0.67, rely=0.185, relwidth=0.18, relheight=0.07)

		# Row 2
		self.Label2 = tk.ttk.Label(self.top, text="Operations:", style='Label1.TLabel')
		self.Label2.place(relx=0.17, rely=0.315, relwidth=0.4, relheight=0.062)

		self.Combo1List1 = ["Create", "Delete"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.45, rely=0.315, relwidth=0.4, relheight=0.068)
		self.Combo1.set(self.Combo1List1[0])

		# Row 3
		self.Label3 = tk.ttk.Label(self.top, text="Word Id:", style='Label1.TLabel')
		self.Label3.place(relx=0.17, rely=0.430, relwidth=0.4, relheight=0.062)

		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11), state='disable')
		self.Text3.place(relx=0.45, rely=0.430, relwidth=0.4, relheight=0.068)

		# Row 4
		self.Label4 = tk.ttk.Label(self.top, text="Taboo Word:", style='Label1.TLabel')
		self.Label4.place(relx=0.17, rely=0.545, relwidth=0.4, relheight=0.062)

		self.Text4Var = tk.StringVar()
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11))
		self.Text4.place(relx=0.45, rely=0.545, relwidth=0.4, relheight=0.068)

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.25, rely=0.8, relwidth=0.19, relheight=0.09)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Cancel", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.8, relwidth=0.19, relheight=0.09)

	def command_view_list(self, type_user):
		vat.view_account_table(type_user, "463x425")

	def get_combo1(self, event):
		if self.Combo1.get() == 'Delete':
			self.delete_refresh()
		else:
			self.create_refresh()

	def command_cancel(self):
		if self.coming_from == 'manager_management_page':
			self.top.destroy()
			mmp.manager_management_page(self.name, self.username)
		else:
			self.top.destroy()
			clerk_management_page.clerk_management_page(self.name, self.username)


	def command_confirm(self):
		# Check if suspended
		df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
		if self.username.lower() in list(df_suspend['Username']):
			tk.messagebox.showerror("Error", "You can't edit the taboo list because you are suspended")
		else:
			if self.Combo1.get() == 'Create':
				TabooWord = self.Text4.get().lower()
				TabooWord = TabooWord.strip() # strip white spaces
				df = pd.read_excel("csv_files/taboo_list.xlsx")
				flag_duplicates = False # declare here avoid referenced before assignment
				
				
				# Check if the Taboo word entered is empty
				if TabooWord == "":
					flag_empty_word = True
					tk.messagebox.showerror("Error", "Taboo word cannot be empty")
				else:
					flag_empty_word = False

				# check if the input is a valid word
				
				regex_format_1 = "[a-zA-Z]+"
				regex_format_2 = "[a-zA-Z]+[\s][a-zA-Z]+"
				if(  re.fullmatch(regex_format_1, TabooWord) or re.fullmatch(regex_format_2, TabooWord) ):
	    				flag_valid_format = True
				else:
						flag_valid_format = False
						tk.messagebox.showerror( "Error", "Provide a valid word" )


				# Check if taboo list is an English word 
				if (len(df) == 0):
					tempo = pd.DataFrame([["0", TabooWord]], columns=['ID','Taboo Words'])
					df = df.append(tempo)
				else:
					if TabooWord in list(df['Taboo Words']):
						# We have duplicates accounts
						flag_duplicates = True
						tk.messagebox.showerror("Error", "Taboo word is already in the list")
					else:
						Id = int( df['ID'].iloc[-1] )
						Id += 1
						tempo = pd.DataFrame([[Id, TabooWord]], columns=['ID','Taboo Words'])
						df = df.append(tempo)

				if not flag_empty_word and not flag_duplicates and flag_valid_format:
					df.to_excel("csv_files/taboo_list.xlsx", index=False)
					tk.messagebox.showinfo("Success",  TabooWord + " added to the list")

					# refresh text entered
					self.create_refresh()

			else: # Delete Section 

				if str(self.Text3.get()).isdigit():	# first check if the ID is an integer
					WordId = int(self.Text3.get())
					df = pd.read_excel("csv_files/taboo_list.xlsx")
					
					if WordId in list(df['ID']):
						flag_id_exist = True
					else:
						flag_id_exist = False
						tk.messagebox.showerror("Error", "Invalid word Id")
					
					if flag_id_exist:
						df.drop(df.index[(df['ID'] == WordId)], axis=0, inplace=True)
						df.to_excel("csv_files/taboo_list.xlsx", index=False)
						tk.messagebox.showinfo("Success",  "Taboo word deleted")

						# refresh text entered
						self.delete_refresh()

				else:
	    				tk.messagebox.showerror("Error", "Invalid Id input provided.\n" + 
					        "Try an integer next time." )

	def create_refresh(self):
		# Disable Id
		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11), state='disable')
		self.Text3.place(relx=0.45, rely=0.430, relwidth=0.4, relheight=0.068)
		# Enable Word
		self.Text4Var = tk.StringVar()
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11))
		self.Text4.place(relx=0.45, rely=0.545, relwidth=0.4, relheight=0.068)

	def delete_refresh(self):
		# Enable Id
		self.Text3Var = tk.StringVar()
		self.Text3 = tk.ttk.Entry(self.top, textvariable=self.Text3Var, font=("Helvetica",11))
		self.Text3.place(relx=0.45, rely=0.430, relwidth=0.4, relheight=0.068)
		# Disable Word
		self.Text4Var = tk.StringVar()
		self.Text4 = tk.ttk.Entry(self.top, textvariable=self.Text4Var, font=("Helvetica",11), state='disable')
		self.Text4.place(relx=0.45, rely=0.545, relwidth=0.4, relheight=0.068)
				
