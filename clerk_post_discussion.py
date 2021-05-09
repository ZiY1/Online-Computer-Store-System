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
import clerk_management_page
import main




# TODO: 191
class clerk_post_discussion(tk.Frame):

	def __init__(self, name, username, master=None): #
		tk.Frame.__init__(self, master)

		self.type_user = 'clerk'

		# User-info account
		self.name = name
		self.username = username
		
		df_privileged_users = pd.read_excel("csv_files/privileged_users.xlsx")
		
		df_info_user = df_privileged_users[ (df_privileged_users['Type_user'] == self.type_user) & (df_privileged_users["Username"] == self.username)]
		
		if len(df_info_user) != 0 :
			self.password = df_info_user['Password'].iloc[-1]
			self.id = df_info_user['ID'].iloc[-1]

		self.master.title("Clerk Post Discussion Page")
		self.master.geometry("563x725")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()


		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="Clerk Post Discussion", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.22, rely=0.015, relwidth=0.62, relheight=0.066)

		# Row 0 view computer types
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.LabelComputerTypes = tk.ttk.Label(self.top, text="Computer Types:", style='Label1.TLabel')
		self.LabelComputerTypes.place(relx=0.16, rely=0.12, relwidth=0.4, relheight=0.051)

		self.Combo1List1 = ["Laptop", "Desktop", "Workstation", "Mainframe", "Server", "Computer Part"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.49, rely=0.12, relwidth=0.4, relheight=0.049)
		self.Combo1.set(self.Combo1List1[0])

		# Row 1 view computer names
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.LabelComputerNames = tk.ttk.Label(self.top, text="Computer Names:", style='Label1.TLabel')
		self.LabelComputerNames.place(relx=0.16, rely=0.22, relwidth=0.4, relheight=0.051)

		df_items = pd.read_excel("csv_files/items.xlsx")
		df_laptop = df_items[df_items['Type'] == 'Laptop']
		list_laptop = list(df_laptop['Name'])
		self.Combo2List1 = list_laptop
		self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo2List1, font=("Helvetica",11))
		self.Combo2.place(relx=0.49, rely=0.22, relwidth=0.4, relheight=0.049)
		self.Combo2.set(self.Combo2List1[0])

		# Row 2
		self.LabelComment = tk.ttk.Label(self.top, text="Comments of this Item:", style='Label1.TLabel')
		self.LabelComment.place(relx=0.16, rely=0.32, relwidth=0.6, relheight=0.051)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_comment("All"), style="CommandView.TButton")
		self.CommandView.place(relx=0.7, rely=0.31, relwidth=0.18, relheight=0.053)

		# Row 3
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.LabelDiscussion = tk.ttk.Label(self.top, text="Discussion I Posted:", style='Label1.TLabel')
		self.LabelDiscussion.place(relx=0.16, rely=0.42, relwidth=0.6, relheight=0.051)

		self.style.configure("CommandView.TButton", font=("Helvetica",14))
		self.CommandView1 = tk.ttk.Button(self.top, text="View", command=lambda: self.command_view_comment("Me"), style="CommandView.TButton")
		self.CommandView1.place(relx=0.7, rely=0.41, relwidth=0.18, relheight=0.053)

		# Row 4
		self.Label2 = tk.ttk.Label(self.top, text="Add a Headline", style='Label1.TLabel')
		self.Label2.place(relx=0.16, rely=0.51, relwidth=0.33, relheight=0.054)

		self.Text1Var = tk.StringVar()
		self.Text1 = tk.ttk.Entry(self.top, textvariable=self.Text1Var, font=("Helvetica",11))
		self.Text1.place(relx=0.49, rely=0.510, relwidth=0.4, relheight=0.052)

		# Row 3 Write a comment
		self.Label3 = tk.ttk.Label(self.top, text="Write a Comment:", style='Label1.TLabel')
		self.Label3.place(relx=0.16, rely=0.60, relwidth=0.33, relheight=0.054)

		self.Text3 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.Text3.place(relx=0.49, rely=0.613, relwidth=0.4, relheight=0.2)

		# Confirm Button
		self.style.configure("CommandConfirm.TButton", font=("Helvetica",14))
		self.CommandConfirm = tk.ttk.Button(self.top, text="Confirm", command=self.command_confirm, style="CommandConfirm.TButton")
		self.CommandConfirm.place(relx=0.25, rely=0.88, relwidth=0.19, relheight=0.07)

		# Cancel Button
		self.CommandCancel = tk.ttk.Button(self.top, text="Cancel", command=self.command_cancel, style="CommandConfirm.TButton")
		self.CommandCancel.place(relx=0.57, rely=0.88, relwidth=0.19, relheight=0.07)

	def get_combo1(self, event):  
		#["Laptop", "Desktop", "Workstation", "Mainframe", "Server", "Computer Part"]
		df_items = pd.read_excel("csv_files/items.xlsx")
		if self.Combo1.get() == 'Laptop': 
			df_computer = df_items[df_items['Type'] == 'Laptop']
			list_computer = list(df_computer['Name'])
		elif self.Combo1.get() == 'Desktop':
			df_computer = df_items[df_items['Type'] == 'Desktop']
			list_computer = list(df_computer['Name'])
		elif self.Combo1.get() == 'Workstation':
			df_computer = df_items[df_items['Type'] == 'workstation']
			list_computer = list(df_computer['Name'])
		elif self.Combo1.get() == 'Mainframe':
			df_computer = df_items[df_items['Type'] == 'mainframe']
			list_computer = list(df_computer['Name'])
		elif self.Combo1.get() == 'Server':
			df_computer = df_items[df_items['Type'] == 'server']
			list_computer = list(df_computer['Name'])
		else:
			df_computer = df_items[df_items['Type'] == 'Computer Part']
			list_computer = list(df_computer['Name'])

		self.Combo2List1 = list_computer
		self.Combo2 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo2List1, font=("Helvetica",11))
		self.Combo2.place(relx=0.49, rely=0.22, relwidth=0.4, relheight=0.049)
		self.Combo2.set(self.Combo2List1[0])


	def command_view_comment(self, discussion_type):
		# 3 discussion_type: "All" "Me" "Guest" "Me All"
		item_name = self.Combo2.get()
		coming_from_page = 'clerk_post_discussion'
		if discussion_type == "All":
			df = pd.read_excel( "csv_files/discussions.xlsx" )
			df_no_violated = df[df['Status'] == "Non-Violated"]
			df_item = df_no_violated[df_no_violated['Computer Name'] == item_name]
			if len(df_item) == 0:
				tk.messagebox.showinfo("Info", "No comment of this item posted")
			else:
				self.top.destroy()
				discussion_table.discussion_table( coming_from = None,
				coming_from_discuss = coming_from_page, 
				item_name = item_name, 
				customer_name = self.name, customer_Id = self.id, 
				customer_username = self.username, 
				discussion_type = discussion_type, df = df_item)
				
		elif discussion_type == "Me":
			df = pd.read_excel( "csv_files/discussions.xlsx" )
			df_no_violated = df[df['Status'] == "Non-Violated"]
			df_me = df_no_violated[df_no_violated['Username'] == self.username]
			df_me_item = df_me[df_me['Computer Name'] == item_name]
			if len(df_me_item) == 0:
				tk.messagebox.showinfo("Info", "You haven't posted any comment on this item")
			else:
				self.top.destroy()
				discussion_table.discussion_table( coming_from = None,
				coming_from_discuss = coming_from_page,
				item_name = item_name, customer_name = self.name,
				customer_Id = self.id, customer_username = self.username,
				discussion_type = discussion_type, df = df_me_item )

				
	def command_confirm(self):
		# Get computer name
		item_name = self.Combo2.get()
		rating = str('empty')

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

		if self.flag_headline_valid and self.flag_comment_valid:
    			
			df = pd.read_excel("csv_files/discussions.xlsx")

			if len(df) == 0:
				Id = 0
				tempo = pd.DataFrame([[Id, self.type_user, self.username.lower(), self.name, item_name, rating, self.Headline, self.TextComment, self.DataTime, Status]], 
										columns=['ID', 'Type User', 'Username', 'Name', 'Computer Name', 'Vote', 'Headline','Comment', 'Timestamp', 'Status'])
				df = df.append(tempo)
			else:
				Id = int(df['ID'].iloc[-1])
				Id = Id+1
				tempo = pd.DataFrame([[Id, self.type_user, self.username.lower(), self.name, item_name, rating, self.Headline, self.TextComment, self.DataTime, Status]], 
										columns=['ID', 'Type User', 'Username', 'Name', 'Computer Name', 'Vote', 'Headline', 'Comment', 'Timestamp', 'Status'])
				df = df.append(tempo)
		
			# Check if suspended
			df_suspend = pd.read_excel( "csv_files/suspend_users.xlsx" )
			df_suspend_user = df_suspend[df_suspend['Type_user'] == self.type_user]
			if self.username.lower() in list(df_suspend_user['Username']):
				tk.messagebox.showerror("Error", "You can't write any comment because you are suspended")
			else:
				tk.messagebox.showinfo("Success","New comment posted")
				
				# refresh the text entered
				self.Text1Var = tk.StringVar()
				self.Text1 = tk.ttk.Entry(self.top, textvariable=self.Text1Var, font=("Helvetica",11))
				self.Text1.place(relx=0.49, rely=0.510, relwidth=0.4, relheight=0.06)

				self.Text3 = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
				self.Text3.place(relx=0.49, rely=0.613, relwidth=0.4, relheight=0.2)

				if self.flag_taboo_headline or self.flag_taboo_content:
					df_privileged_users = pd.read_excel("csv_files/privileged_users.xlsx")
					self.update_warning(df_privileged_users, 'clerk')
					tk.messagebox.showwarning("Warning","You just got one warning because the comment you just posted contains taboo word(s)")

				df.to_excel("csv_files/discussions.xlsx", index=False)




	def command_cancel(self):
		self.top.destroy()
		clerk_management_page.clerk_management_page(self.name, self.username)



	def replace_bad_words(self, my_str):
		flag_taboo_word = False
		df_taboo = pd.read_excel("csv_files/taboo_list.xlsx")
		string = str(my_str)

		punctuation_ = ""

		for letter in re.escape( punctuation):
    			if letter not in "#$!.'\"?%:&":
    					punctuation_ += letter

		r = re.compile(r'[\s{}]+'.format(re.escape(punctuation_)))
		my_list = r.split(string)
		my_string = " "
		my_string = my_string.join(my_list)
		
		for word in my_list:
			if word.lower() in list(df_taboo['Taboo Words']):
    			#Change it to *****
				number_of_star = len(word)

				my_string = my_string.replace(word, "*"*number_of_star )
				flag_taboo_word = True

		return my_string, flag_taboo_word

	def update_warning(self, df, type_user):
		df = pd.read_excel("csv_files/privileged_users.xlsx")
		df2 = df[df['Type_user'] == type_user]
		df_privileged_active = df2[df2['Status'] == "active"]
		if self.username.lower() in list(df_privileged_active['Username']):
			flag_username_exist = True
			df_user_row = df[df['Username'] == self.username]
			df_row_list = df_user_row.to_numpy().tolist()
			name = df_row_list[0][1]
			password = df_row_list[0][3]
			current_warning = int(df_user_row['Warnings'].iloc[-1])

			chance_login = 1
			deny_notify = 0
		else:
			flag_username_exist = False
		
		if flag_username_exist:
			# Update the warning (+1)
			if current_warning < 3:
				current_warning = current_warning + 1
				df['Warnings'] = np.where((df['Username'] == self.username) & (df['Type_user'] == type_user), current_warning, df.Warnings)
				df.to_excel("csv_files/privileged_users.xlsx", index=False)

			# Auto suspend if Warning == 3
			if current_warning >= 3:
				df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
				df_suspend_type = df_suspend[df_suspend['Type_user'] == type_user]
				suspend_reason = "3 standing warnings"
				if len(df_suspend) == 0:
					Id = 0
					tempo = pd.DataFrame([[str(Id), type_user, self.username.lower(), password, name, current_warning, suspend_reason, chance_login, deny_notify]], 
						columns=['ID', 'Type_user', 'Username', 'Password', 'Name','Current_warnings', 'Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
					df_suspend = df_suspend.append(tempo)

				else:
					if not username.lower() in list(df_suspend_type['Username']):
						Id = int(df_suspend['ID'].iloc[-1])
						Id = Id+1
						tempo = pd.DataFrame([[str(Id), type_user, self.username.lower(), password, name, current_warning, suspend_reason, chance_login, deny_notify]], 
							columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
						df_suspend = df_suspend.append(tempo)

				# update suspend_user file and customers file
				df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
				df_privileged = pd.read_excel("csv_files/privileged_users.xlsx")
				df_privileged['Status'] = np.where((df_privileged['Username'] == self.username) & (df_privileged['Type_user'] == type_user), 'suspended', df_privileged.Status)
				#df_privileged.loc[df_privileged['Username'] == username, 'Status'] = 'suspended'
				df_privileged.to_excel("csv_files/privileged_users.xlsx", index=False)

				self.top.destroy()
				main.HomePage()
				tk.messagebox.showerror("Error", "Sorry, you are suspended")






# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    clerk_post_discussion(top).mainloop()    
