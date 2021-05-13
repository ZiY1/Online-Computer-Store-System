import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts 
import manager_management_page as mmp
import manager_view_account as mva


class view_account_table(tk.Frame):

	def __init__(self, type_user, my_geometry, username, master=None): 
		tk.Frame.__init__(self, master)

		self.type_user = type_user
		self.my_geometry = my_geometry
		self.username = username

		self.master.title("View Account Page")
		self.master.geometry(self.my_geometry)
		#self.master.configure( background = "light blue" )
		self.create_widgets()

	def create_widgets(self):
		self.top = tk.Toplevel()		
		self.top.title("User Accounts Info Page")
		#self.top.geometry('700x500')

		if self.type_user == 'clerk' or self.type_user == 'computer_company' or self.type_user == 'delivery':
			df = pd.read_excel( "csv_files/privileged_users.xlsx" )
			df_user = df[df['Type_user'] == self.type_user]
			self.users_table(df_user)
		elif self.type_user == 'customer':
			df = pd.read_excel( "csv_files/registered_customers.xlsx" )
			self.users_table(df)
		elif self.type_user == 'suspend':
			df = pd.read_excel( "csv_files/suspend_users.xlsx" )
			self.users_table(df)
		elif self.type_user == 'suggested_systems':
			df = pd.read_excel( "csv_files/suggested_systems.xlsx" )
			self.users_table(df)
		elif self.type_user == 'taboo_list':
			df = pd.read_excel( "csv_files/taboo_list.xlsx" )
			self.users_table(df)
		elif self.type_user == 'all_items':
			df = pd.read_excel( "csv_files/items.xlsx" )
			df_droped = df.drop(['Features', 'CPU cores', 'Graphic Card', 'Screen Resolution'], axis=1)
			self.users_table(df_droped)
		elif self.type_user == 'my_items':
			df = pd.read_excel( "csv_files/items.xlsx" )
			df_droped = df.drop(['Features', 'CPU cores', 'Graphic Card', 'Screen Resolution'], axis=1)
			df_droped_me = df_droped[df_droped['Computer Company'] == self.username]
			self.users_table(df_droped_me)

	def users_table(self, df):

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.pack()#place(relx=0.06, rely=0.15, relwidth=0.9, relheight=0.2)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
		

		self.style1 = tk.ttk.Style()
		self.style1.configure("Treeview",
		 	background="white",
		 	foreground="black",
			rowheight=25,
			filedbackground="silver" )
		self.style1.map("Treeview",background=[('selected', 'dark blue')])



		self.tree = tk.ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree_scroll.config(command=self.tree.yview)


		# Set up new treeview
		self.tree["columns"] = list(df.columns)
		self.tree["show"] = "headings"

		# Loop through column list for headers
		for column in self.tree["column"]:
			self.tree.heading(column, text=column, anchor=tk.W)
			self.tree.column(column, width=170, anchor=tk.W, stretch=tk.NO)

		# Put data in treeview
		self.tree.tag_configure('oddrow', background='white')
		self.tree.tag_configure('evenrow', background='light blue')
		global count
		count=0
		df_rows = df.to_numpy().tolist()
		for row in df_rows:
			if count % 2 == 0:
				self.tree.insert("", "end", value=row, tags=('evenrow',))
			else:
				self.tree.insert("", "end", value=row, tags=('oddrow',))
			count += 1

		self.tree.pack()