import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts 
import manager_management_page as mmp
import view_account_table as vat

class edit_system_page(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.admin_name = name
		self.admin_username = username

		self.master.title("Edit System Page")
		self.master.geometry("463x425")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Choose 3 Suggested Systems ", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.19, rely=0.015, relwidth=0.64, relheight=0.079)

		# Row 0
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label0 = tk.ttk.Label(self.top, text="Current Suggested Sys:", style='Label1.TLabel')
		self.Label0.place(relx=0.17, rely=0.2, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_list('suggested_systems'), style="CommandView.TButton")
		self.CommandView.place(relx=0.67, rely=0.185, relwidth=0.18, relheight=0.07)

		# Row 1
		self.Label1 = tk.ttk.Label(self.top, text="Option 1:", style='Label1.TLabel')
		self.Label1.place(relx=0.17, rely=0.315, relwidth=0.4, relheight=0.062)

		self.Combo1List1 = ["laptops", "mainframes", "servers", "desktops", "workstations"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		#self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.45, rely=0.315, relwidth=0.4, relheight=0.068)
		self.Combo1.set(self.Combo1List1[0])

		# Row 2
		self.Label2 = tk.ttk.Label(self.top, text="Option 2:", style='Label1.TLabel')
		self.Label2.place(relx=0.17, rely=0.43, relwidth=0.4, relheight=0.062)
		self.Combo1List2 = ["laptops", "mainframes", "servers", "desktops", "workstations"]
		self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List2, font=("Helvetica",11))
		#self.Combo2.bind("<<ComboboxSelected>>", self.get_combo2)
		self.Combo2.place(relx=0.45, rely=0.43, relwidth=0.4, relheight=0.068)
		self.Combo2.set(self.Combo1List2[4])

		# Row 3
		self.Label3 = tk.ttk.Label(self.top, text="Option 3:", style='Label1.TLabel')
		self.Label3.place(relx=0.17, rely=0.545, relwidth=0.4, relheight=0.062)
		self.Combo1List3 = ["laptops", "mainframes", "servers", "desktops", "workstations"]
		self.Combo3 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List3, font=("Helvetica",11))
		#self.Combo3.bind("<<ComboboxSelected>>", self.get_combo3)
		self.Combo3.place(relx=0.45, rely=0.545, relwidth=0.4, relheight=0.068)
		self.Combo3.set(self.Combo1List3[1])

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.25, rely=0.8, relwidth=0.19, relheight=0.09)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Cancel", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.8, relwidth=0.19, relheight=0.09)

	def command_confirm(self):
		if self.Combo1.get() == self.Combo2.get() or self.Combo1.get() == self.Combo3.get() or self.Combo2.get() == self.Combo3.get():
			tk.messagebox.showerror("Error", "You must choose 3 different systems")
		else:
			#guess_page.manager_system_inputs(self, self.Combo1.get(), self.Combo2.get(), self.Combo3.get(), False)
			System1 = self.Combo1.get()
			System2 = self.Combo2.get()
			System3 = self.Combo3.get()
			df = pd.read_excel( "csv_files/suggested_systems.xlsx" )
			NewSystems = [System1, System2, System3]
			df['Suggested System'] = NewSystems
			df.to_excel("csv_files/suggested_systems.xlsx", index=False)
			self.manager_system_inputs()
			tk.messagebox.showinfo("Success", "Reset 3 susgested systems\n" + 
									"\nSystem 1: " + System1 + 
									"\nSystem 2: " + System2 + 
									"\nSystem 2: " + System3)

	def command_cancel(self):
		self.top.destroy()
		mmp.manager_management_page(self.admin_name, self.admin_username)

	def command_view_list(self, type_csv):
		vat.view_account_table(type_csv, "463x425", self.admin_username)

	# For guest page and customer page 
	def manager_system_inputs(self):
		df = pd.read_excel( "csv_files/suggested_systems.xlsx" )
		System1 = str(df.iloc[0,0])
		System2 = str(df.iloc[1,0])
		System3 = str(df.iloc[2,0])
		return (System1, System2, System3)





# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    edit_system_page(top).mainloop()   