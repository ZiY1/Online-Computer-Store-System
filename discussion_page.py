import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
from string import punctuation
import datetime

# python scripts 
import discussion_table
import main as home

# TODO: 191
class discussion_page(tk.Frame):

	def __init__(self, master=None): #type_user, username, password, name, computer_name
		tk.Frame.__init__(self, master)

		self.type_user = 'customer'
		self.username = 'ziyi@gmail.com'
		self.password = 123
		self.name = 'Ziyi Huang'
		#self.computer_name = 'Lenovo ThinkPad X390 Yoga Laptop'
		self.computer_name = 'Lenovo Chromebook S330'

		self.master.title("Comments & Vote Page")
		self.master.geometry("563x625")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Comments & Votes", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.077)

		# Sub title: computer name
		self.style.configure("LabelSub.TLabel",anchor="w", font=("Helvetica",17), background = "light blue")
		self.LabelSub = tk.ttk.Label(self.top, text="Computer:", style='LabelSub.TLabel')
		self.LabelSub.place(relx=0.06, rely=0.115, relwidth=0.3, relheight=0.058)

		self.LabelName = tk.ttk.Label(self.top, text=self.computer_name, style='LabelSub.TLabel')
		self.LabelName.place(relx=0.27, rely=0.115, relwidth=0.8, relheight=0.058)

		# Row 0
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label0 = tk.ttk.Label(self.top, text="Comments of This Computer:", style='Label1.TLabel')
		self.Label0.place(relx=0.16, rely=0.22, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_comment("All"), style="CommandView.TButton")
		self.CommandView.place(relx=0.7, rely=0.21, relwidth=0.18, relheight=0.06)

		# Row 0.5
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.Label01 = tk.ttk.Label(self.top, text="Comments I Casted:", style='Label1.TLabel')
		self.Label01.place(relx=0.16, rely=0.32, relwidth=0.6, relheight=0.058)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView1 = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_comment("Me"), style="CommandView.TButton")
		self.CommandView1.place(relx=0.7, rely=0.31, relwidth=0.18, relheight=0.06)

		# Row 1
		self.Label1 = tk.ttk.Label(self.top, text="Overall Rating:", style='Label1.TLabel')
		self.Label1.place(relx=0.16, rely=0.425, relwidth=0.4, relheight=0.062)

		self.Combo1List1 = ["1", "2", "3", "4", "5"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.place(relx=0.49, rely=0.425, relwidth=0.4, relheight=0.06)

		# Row 2
		self.Label2 = tk.ttk.Label(self.top, text="Add a Headline", style='Label1.TLabel')
		self.Label2.place(relx=0.16, rely=0.525, relwidth=0.33, relheight=0.062)

		self.Text1Var = tk.StringVar()
		self.Text1 = tk.ttk.Entry(self.top, textvariable=self.Text1Var, font=("Helvetica",11))
		self.Text1.place(relx=0.49, rely=0.510, relwidth=0.4, relheight=0.06)

		# Row 3 Write a comment
		self.Label3 = tk.ttk.Label(self.top, text="Write a Comment:", style='Label1.TLabel')
		self.Label3.place(relx=0.16, rely=0.605, relwidth=0.33, relheight=0.062)

		self.Text3 = tk.Text(self.top, font=("Helvetica",11))
		self.Text3.place(relx=0.49, rely=0.613, relwidth=0.4, relheight=0.2)

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.25, rely=0.88, relwidth=0.19, relheight=0.07)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Cancel", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.88, relwidth=0.19, relheight=0.07)


	def command_view_comment(self, discussion_type):
		# 3 discussion_type: "All" "Me" "Guest" "Me All"
		if discussion_type == "All":
			df = pd.read_excel( "csv_files/discussions.xlsx" )
			df_no_violated = df[df['Status'] == "Non-Violated"]
			df_computer = df_no_violated[df_no_violated['Computer Name'] == self.computer_name]
			if len(df_computer) == 0:
				tk.messagebox.showinfo("Info", "No comment of this computer posted")
			else:
				self.top.destroy()
				discussion_table.discussion_table("discussion_page", self.computer_name, None, None, self.username, discussion_type, df_computer)
		elif discussion_type == "Me":
			df = pd.read_excel( "csv_files/discussions.xlsx" )
			df_no_violated = df[df['Status'] == "Non-Violated"]
			df_me = df_no_violated[df_no_violated['Username'] == self.username]
			df_me_computer = df_me[df_me['Computer Name'] == self.computer_name]
			if len(df_me_computer) == 0:
				tk.messagebox.showinfo("Info", "You haven't posted any comment of this computer posted")
			else:
				self.top.destroy()
				discussion_table.discussion_table("discussion_page", self.computer_name, None, None, self.username, discussion_type, df_me_computer)

	def command_confirm(self):
		# Rating
		self.Rating = int(self.Combo1.get())
		if self.Combo1.get() != "":
			self.flag_vote_valid = True
		else:
			self.flag_vote_valid = False
			tk.messagebox.showerror("Error", "Please select a rating")

		# Headline
		self.Headline, self.flag_taboo_headline = self.replace_bad_words(self.Text1.get())

		if self.Headline.strip() != "":
			self.flag_headline_valid = True
		else:
			self.flag_headline_valid = False
			tk.messagebox.showerror("Error", "Headline cannot be empty")
			

		self.TextComment, self.flag_taboo_content = self.replace_bad_words(self.Text3.get("1.0", "end"))
		self.now = datetime.datetime.now()
		self.DataTime = self.now.strftime("%y-%m-%d %H:%M")

		Status = "Non-Violated"

		if self.TextComment.strip() != "":
			self.flag_comment_valid = True
		else:
			self.flag_comment_valid = False
			tk.messagebox.showerror("Error", "Comment cannot be empty")

		df = pd.read_excel("csv_files/discussions.xlsx")

		if len(df) == 0:
			Id = 0
			tempo = pd.DataFrame([[Id, self.type_user, self.username.lower(), self.name, self.computer_name, self.Rating, self.Headline, self.TextComment, self.DataTime, Status]], 
									columns=['ID', 'Type User', 'Username', 'Name', 'Computer Name', 'Vote', 'Headline','Comment', 'Timestamp', 'Status'])
			df = df.append(tempo)
		else:
			Id = int(df['ID'].iloc[-1])
			Id = Id+1
			tempo = pd.DataFrame([[Id, self.type_user, self.username.lower(), self.name, self.computer_name, self.Rating, self.Headline, self.TextComment, self.DataTime, Status]], 
									columns=['ID', 'Type User', 'Username', 'Name', 'Computer Name', 'Vote', 'Headline', 'Comment', 'Timestamp', 'Status'])
			df = df.append(tempo)

		if self.flag_headline_valid and self.flag_comment_valid and self.flag_vote_valid:
			# Check if suspended
			df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
			df_suspend_user = df_suspend[df_suspend['Type_user'] == self.type_user]
			if self.username.lower() in list(df_suspend_user['Username']):
				tk.messagebox.showerror("Error", "You can't write any comment because you are suspended")
			else:
				if self.flag_taboo_headline or self.flag_taboo_content:
					df_customers = pd.read_excel("csv_files/registered_customers.xlsx")
					self.update_warning(df_customers)
				tk.messagebox.showinfo("Success", "New comment posted")
				df.to_excel("csv_files/discussions.xlsx", index=False)
				# Udate overall review for this computer
				df_item = pd.read_excel( "csv_files/items.xlsx" )
				df_computer = df_item[df_item['Name'] == self.computer_name]
				current_rating = int(df_computer['overall review'].iloc[-1])
				if current_rating == 0:
					df_item.loc[df_item['Name'] == self.computer_name, 'overall review'] = self.Rating
					df_item.to_excel("csv_files/items.xlsx", index=False)
				else:
					df_item.loc[df_item['Name'] == self.computer_name, 'overall review'] = (self.Rating+current_rating)/2
					df_item.to_excel("csv_files/items.xlsx", index=False)

	def command_cancel(self):
		pass

	def replace_bad_words(self, my_str):
		flag_taboo_word = False
		df_taboo = pd.read_excel("csv_files/taboo_list.xlsx")
		string = str(my_str)
		r = re.compile(r'[\s{}]+'.format(re.escape(punctuation)))
		my_list = r.split(string)
		my_string = " "
		my_string = my_string.join(my_list)
		for word in my_list:
			if word.lower() in list(df_taboo['Taboo Words']):
				my_string = my_string.replace(word, "*")
				flag_taboo_word = True

		return my_string, flag_taboo_word

	def update_warning(self, df):
		df_user_row = df[df['Username'] == self.username]
		CurrentWarning = int(df_user_row['Warnings'].iloc[-1])
		# Update the warning if taboo word found
		if CurrentWarning < 3:
			CurrentWarning = CurrentWarning + 1
			df.loc[df['Username'] == self.username, 'Warnings'] = CurrentWarning
			df.to_excel("csv_files/registered_customers.xlsx", index=False)
		# Auto suspend if Warning == 3
		if CurrentWarning >= 3:
			df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
			df_suspend_type = df_suspend[df_suspend['Type_user'] == self.type_user]
			ChanceLogin = 1
			DenyNotify = 1
			SuspendReason = "3 standing warnings"
			if len(df_suspend) == 0:
				Id = 0
				tempo = pd.DataFrame([[str(Id), self.type_user, self.username.lower(), self.password, self.name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
					columns=['ID', 'Type_user', 'Username', 'Password', 'Name','Current_warnings', 'Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
				df_suspend = df_suspend.append(tempo)

			else:
				if self.username.lower() in list(df_suspend_type['Username']):
					self.top.destroy()
					home.HomePage()
					tk.messagebox.showerror("Error", "Sorry, you are suspended")
				else:
					Id = int(df_suspend['ID'].iloc[-1])
					Id = Id+1
					tempo = pd.DataFrame([[str(Id), self.type_user, self.username.lower(), self.password, self.name, CurrentWarning, SuspendReason, ChanceLogin, DenyNotify]], 
						columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
					df_suspend = df_suspend.append(tempo)
			# update suspend_user file and customers file
			df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
			df_cus = pd.read_excel("csv_files/registered_customers.xlsx")
			df_cus.loc[df_cus['Username'] == self.username, 'Status'] = 'suspended'
			df_cus.to_excel("csv_files/registered_customers.xlsx", index=False)

			self.top.destroy()
			home.HomePage()
			tk.messagebox.showerror("Error", "Sorry, you are suspended")












# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    discussion_page(top).mainloop()   