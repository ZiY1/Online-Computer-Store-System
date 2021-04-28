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
import discussion_page
import generalized_item
import setting_account

# TODO: line 113
class discussion_table(tk.Frame):

	# Pass username as None if in guest page
	def __init__(self, coming_from, item_name, customer_name, 
                     customer_Id, customer_username, discussion_type, df, master=None): 
		tk.Frame.__init__(self, master)

		self.coming_from = coming_from
		self.item_name = item_name
		self.customer_name = customer_name
		self.customer_Id = customer_Id
		self.customer_username = customer_username
		self.discussion_type = discussion_type
		self.df = df

		self.master.title("View Discussion Page")
		self.master.geometry("740x800")
		self.master.configure( background = "light blue" )

		
		self.create_widgets()

	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.top.title("View Discussion Page")

		self.style = tk.ttk.Style()
		self.style.configure("LabelSeg.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.style.configure("LabelType.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.style.configure("LabelTime.TLabel",anchor="w", font=("Helvetica",11), background = "light blue")
		self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.style.configure("LabelContent.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.style.configure("ButtonReport.TButton", font=("Helvetica", 14))
		self.view_table(self.df)		

	def view_table(self, df):

		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

		self.MyFrame = tk.Frame(self.Canvas, bg="light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		df_rows = df.to_numpy().tolist()
		counter = 0
		for row in df_rows:

			# Row 0
			if self.discussion_type == "All":
				self.Text1Var = tk.StringVar(value="Enter a comment id")
				self.Text1 = tk.ttk.Entry(self.MyFrame, textvariable=self.Text1Var, font=("Helvetica",11))
				self.Text1.grid(sticky="W", row=0, column=0, padx=0, pady=10)

			# Row 1
			if self.discussion_type == "All":
				self.LabelReport = tk.ttk.Button(self.MyFrame, text="Report", command=self.report, style="ButtonReport.TButton")
				self.LabelReport.grid(sticky="W", row=1, column=0, padx=0, pady=5)

			self.Back = tk.ttk.Button(self.MyFrame, text="Back", command=self.command_back, style="ButtonReport.TButton")
			self.Back.grid(sticky="W", row=1, column=1, padx=0, pady=5)

			# Row 2

			self.LabelSeg = tk.ttk.Label(self.MyFrame, text="------------------------------------------------------------------------------------------------", style="LabelSeg.TLabel")
			self.LabelSeg.grid(sticky="W", row=2+counter, column=0, padx=0, pady=15)

			self.LabelID = tk.ttk.Label(self.MyFrame, text="Coment ID: " + str(row[0]), style="LabelType.TLabel")
			self.LabelID.grid(sticky="W", row=3+counter, column=0, padx=0, pady=10)

			if self.discussion_type == "Me All":
				self.LabelComputer = tk.ttk.Label(self.MyFrame, text="Computer Name: " + row[4], style="LabelType.TLabel")
				self.LabelComputer.grid(sticky="W", row=4+counter, column=0, padx=0, pady=5)

			self.LabelType = tk.ttk.Label(self.MyFrame, text=row[1] + ": " + row[3], style="LabelType.TLabel")
			self.LabelType.grid(sticky="W", row=5+counter, column=0, padx=0, pady=5)

			self.LabelVote = tk.ttk.Label(self.MyFrame, text=self.rate_text(row[5]),  foreground="#DAA520", style="LabelTime.TLabel")
			self.LabelVote.grid(sticky="W", row=6+counter, column=0, padx=0, pady=5)

			self.LabelTime = tk.ttk.Label(self.MyFrame, text="Reviewed on " + row[8], style="LabelTime.TLabel")
			self.LabelTime.grid(sticky="W", row=7+counter, column=0, padx=0, pady=10)

			self.LabelHeadline = tk.ttk.Label(self.MyFrame, text=row[6], style="LabelHeadline.TLabel")
			self.LabelHeadline.grid(sticky="W", row=8+counter, column=0, padx=0, pady=5)

			row[7] = self.wrap(row[7])
			self.LabelContent = tk.ttk.Label(self.MyFrame, text=row[7], style="LabelContent.TLabel")
			self.LabelContent.grid(sticky="W", row=9+counter, column=0, padx=0, pady=10)

			counter = counter+8

	def command_back(self):
		if self.coming_from == "discussion_page":
			self.top.destroy()
			#TODO: finish the args
			discussion_page.discussion_page()
		elif self.coming_from == "setting_account":
			self.top.destroy()
			setting_account.setting_account(self.customer_name, self.customer_Id, self.customer_username)
		else:
			self.top.destroy()
			generalized_item.generalized_item(self.coming_from, self.item_name, self.customer_name, self.customer_Id, self.customer_username)


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

	def report(self):
		answer = askyesno(title='agreement', message='Report only if you find violating words/sentences/attitud\n' + 
							'Your report will be examined by the manager, you will get penalty if your report is untrue\n' +
							'Do you agree?')

		if answer:
			# Check if comment id valid
			df = pd.read_excel("csv_files/discussions.xlsx")
			df_discussion = df[df['Status'] == "Non-Violated"]
			comment_id = int(self.Text1.get())
			flag_reportId_valid = False
			if comment_id in list(df_discussion['ID']):
				flag_reportId_valid = True

			#Check if comment is already reported
			df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
			flag_already_report = False
			if comment_id in list(df_report['Reported Comment ID']):
				flag_already_report = True

			now = datetime.datetime.now()
			DataTime = now.strftime("%y-%m-%d %H:%M")
			Status = "pending"
			ManagerJustification = "pending"
			if len(df_report) == 0:
				Id = 0
			else:
				Id = int(df_report['ID'].iloc[-1])
				Id = Id+1
			tempo = pd.DataFrame([[Id, self.customer_username, comment_id, DataTime, Status, ManagerJustification]], 
									columns=['ID', 'Reporter', 'Reported Comment ID', 'Reported Time', 'Status', 'Manager Justification'])
			df_report = df_report.append(tempo)

			if flag_reportId_valid and not flag_already_report:
				df_report.to_excel("csv_files/discussion_reports.xlsx", index=False)
				tk.messagebox.showinfo("Success", "Report Submit")
			elif not flag_reportId_valid:
				tk.messagebox.showerror("Error", "Comment ID invalid")
			else:
				tk.messagebox.showerror("Error", "Comment ID already reported")


	# Test Only
#---------------------Main----------
if __name__ == "__main__":
    top = tk.Tk()
    discussion_table(top).mainloop()   
			

	# def view_table(self, df):
	# 	self.style1 = tk.ttk.Style()
	# 	self.style1.theme_use("default")
	# 	self.style1.configure("Treeview", rowheight=40)
	# 	self.style1.map("Treeview",background=[('selected', 'light blue')])

	# 	self.tree = ttk.Treeview(self.top)
	# 	self.tree["columns"] = ("ID", "Type User", "Name", "Comment", "Posted Time")
	# 	self.tree.column("ID", width=70)
	# 	self.tree.column("Type User", width=100)
	# 	self.tree.column("Name", width=100)
	# 	self.tree.column("Comment", width=300)
	# 	self.tree.column("Posted Time", width=150)

	# 	self.tree.heading("ID", text="ID")
	# 	self.tree.heading("Type User", text="Type User")
	# 	self.tree.heading("Name", text="Name")
	# 	self.tree.heading("Comment", text="Comment")
	# 	self.tree.heading("Posted Time", text="Posted Time")

	# 	df.drop(labels='Username', axis='columns', inplace=True)
	# 	df.drop(labels='Computer Name', axis='columns', inplace=True)

	# 	df_rows = df.to_numpy().tolist()
	# 	for row in df_rows:
	# 		row[3] = self.wrap(row[3])
	# 		self.tree.insert("", "end", value=row)

	# 	self.tree.pack()

	# def wrap(self, string, lenght=45):
	# 	return '\n'.join(textwrap.wrap(string, lenght))
