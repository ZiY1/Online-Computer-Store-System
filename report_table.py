import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
import textwrap

# python scripts 
import complaint_page


class report_table(tk.Frame):

	def __init__(self, customer_name, customer_Id, customer_username, report_type, master=None): 
		tk.Frame.__init__(self, master)

		self.name = customer_name
		self.id = customer_Id
		self.username = customer_username
		self.report_type = report_type
		self.master.title("View My Report Page")
		self.master.geometry("663x855")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		if self.report_type == "casted":
			title = "View My Casted Report"
		else:
			title = "View My Receieved Report"
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text=title, style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.252, rely=0.015, relwidth=0.52, relheight=0.049)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.195, rely=0.125, relwidth=0.3, relheight=0.032)

		self.Combo1List1 = ["All Discussion Reports", "Pending Discussion Reports", "Stay Discussion Reports", "Reverse Discussion Reports"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.49, rely=0.125, relwidth=0.35, relheight=0.038)
		self.Combo1.set(self.Combo1List1[0])

		# Treeview Frame
		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.08, rely=0.2, relwidth=0.85, relheight=0.25)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		# Treeview details
		df = pd.read_excel("csv_files/discussion_reports.xlsx")
		if self.report_type == "casted":
			df_report = df[df['Reporter'] == self.username]
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
		else: # self.report_type == "receieved"
			df_discussion = pd.read_excel("csv_files/discussions.xlsx")
			df_posted_row = df_discussion[df_discussion['Username'] == self.username]
			id_list = list(df_posted_row['ID'])
			df_new = df.loc[df['Reported Comment ID'].isin(id_list)]
			cols = df_new.columns.tolist()
			cols = cols[2:] + cols[:2]
			df_new = df_new[cols]

			self.tree["columns"] = ("Reported Comment ID", "Reported Time", "Status")
			#self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
			#self.tree.column("Reporter", anchor=tk.W, width=230, stretch=tk.NO)
			self.tree.column("Reported Comment ID", anchor=tk.W, width=190, stretch=tk.NO)
			self.tree.column("Reported Time", anchor=tk.W, width=187, stretch=tk.NO)
			self.tree.column("Status", anchor=tk.W, width=167, stretch=tk.NO)
			self.tree.bind('<ButtonRelease-1>', self.selected_item)
			self.tree["show"] = "headings"
			#self.tree.heading("ID", text="ID", anchor=tk.W)
			#self.tree.heading("Reporter", text="Reporter", anchor=tk.W)
			self.tree.heading("Reported Comment ID", text="My Comment ID Receieved Report", anchor=tk.W)
			self.tree.heading("Reported Time", text="Reported Time", anchor=tk.W)
			self.tree.heading("Status", text="Status", anchor=tk.W)

			df_rows = df_new.to_numpy().tolist()
			for row in df_rows:
				self.tree.insert("", "end", value=row)

		# Reported Comment Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Reported Comment Content", style='LabelHead.TLabel')
		self.LabelHead.place(relx=0.34, rely=0.46, relwidth=0.35, relheight=0.04)

		# Reported Comment Body
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.5, relheight=0.4, anchor='ne')
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

		# Back Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.735, rely=0.92, relwidth=0.15, relheight=0.05)


	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()

	def selected_item(self, event):
		get_all = self.tree.item(self.tree.selection())
		list_row = get_all.get("values")
		if list_row != "":
			if self.report_type == "casted":
				self.ID = list_row[0]
				self.Reporter = list_row[1]
				self.ReportedCommentID = list_row[2]
				self.ReportedTime = list_row[3]
				self.Status = list_row[4]
				self.Justification = list_row[5]
			else:
				self.ID = list_row[4]
				self.Reporter = list_row[5]
				self.ReportedCommentID = list_row[0]
				self.ReportedTime = list_row[1]
				self.Status = list_row[2]
				self.Justification = list_row[3]


			df_discussion = pd.read_excel("csv_files/discussions.xlsx")
			df_row = df_discussion[df_discussion['ID'] == self.ReportedCommentID]
			df_row_list = df_row.to_numpy().tolist()
			self.CommentID = df_row_list[0][0]
			self.TypeUser = df_row_list[0][1]
			self.ReportedName = df_row_list[0][3]
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

			self.LabelType = tk.ttk.Label(self.MyFrame, text=self.TypeUser + ": " + self.ReportedName, style="LabelType.TLabel")
			self.LabelType.grid(sticky="W", row=2, column=0, padx=0, pady=5)

			self.LabelVote = tk.ttk.Label(self.MyFrame, text=self.rate_text(self.Vote),  foreground="#DAA520", style="LabelTime.TLabel")
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
		self.Canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.5, relheight=0.4, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		self.LabelID.destroy()
		self.LabelComputer.destroy()
		self.LabelType.destroy()
		self.LabelVote.destroy()
		self.LabelTime.destroy()
		self.LabelHeadline.destroy()
		self.LabelContent.destroy()


	def back(self):
		# Remember to pass args
		self.top.destroy()
		complaint_page.complaint_page(self.name, self.id, self.username)

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
		if self.Combo1.get() == "All Discussion Reports":
			df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
		elif self.Combo1.get() == "Pending Discussion Reports":
			df =  pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report = df[df["Status"] == "pending"]
		elif self.Combo1.get() == "Stay Discussion Reports":
			df =  pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report = df[df["Status"] == "stay"]
		else:
			df =  pd.read_excel("csv_files/discussion_reports.xlsx")
			df_report = df[df["Status"] == "reverse"]

		# Treeview
		#df_report.drop(labels='Manager Justification', axis='columns', inplace=True)

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.08, rely=0.2, relwidth=0.85, relheight=0.25)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		if self.report_type == "casted":
			df_report = df_report[df_report['Reporter'] == self.username]
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
		else: # self.report_type == "receieved"
			df_discussion = pd.read_excel("csv_files/discussions.xlsx")
			df_posted_row = df_discussion[df_discussion['Username'] == self.username]
			id_list = list(df_posted_row['ID'])
			df_new = df_report.loc[df_report['Reported Comment ID'].isin(id_list)]
			cols = df_new.columns.tolist()
			cols = cols[2:] + cols[:2]
			df_new = df_new[cols]

			self.tree["columns"] = ("Reported Comment ID", "Reported Time", "Status")
			#self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
			#self.tree.column("Reporter", anchor=tk.W, width=230, stretch=tk.NO)
			self.tree.column("Reported Comment ID", anchor=tk.W, width=190, stretch=tk.NO)
			self.tree.column("Reported Time", anchor=tk.W, width=187, stretch=tk.NO)
			self.tree.column("Status", anchor=tk.W, width=167, stretch=tk.NO)
			self.tree.bind('<ButtonRelease-1>', self.selected_item)
			self.tree["show"] = "headings"
			#self.tree.heading("ID", text="ID", anchor=tk.W)
			#self.tree.heading("Reporter", text="Reporter", anchor=tk.W)
			self.tree.heading("Reported Comment ID", text="My Comment ID Receieved Report", anchor=tk.W)
			self.tree.heading("Reported Time", text="Reported Time", anchor=tk.W)
			self.tree.heading("Status", text="Status", anchor=tk.W)

			df_rows = df_new.to_numpy().tolist()
			for row in df_rows:
				self.tree.insert("", "end", value=row)

		# self.tree["columns"] = ("ID", "Reporter", "Reported Comment ID", "Reported Time", "Status")
		# self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		# self.tree.column("Reporter", anchor=tk.W, width=230, stretch=tk.NO)
		# self.tree.column("Reported Comment ID", anchor=tk.W, width=130, stretch=tk.NO)
		# self.tree.column("Reported Time", anchor=tk.W, width=95, stretch=tk.NO)
		# self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		# self.tree.bind('<ButtonRelease-1>', self.selected_item)
		# self.tree["show"] = "headings"	
		# self.tree.heading("ID", text="ID", anchor=tk.W)
		# self.tree.heading("Reporter", text="Reporter", anchor=tk.W)
		# self.tree.heading("Reported Comment ID", text="Reported Comment ID", anchor=tk.W)
		# self.tree.heading("Reported Time", text="Reported Time", anchor=tk.W)
		# self.tree.heading("Status", text="Status", anchor=tk.W)
		# df_rows = df_report.to_numpy().tolist()
		# for row in df_rows:
		# 	self.tree.insert("", "end", value=row)