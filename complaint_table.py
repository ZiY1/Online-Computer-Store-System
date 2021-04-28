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

class complaint_table(tk.Frame):

	def __init__(self, customer_name, customer_Id, customer_username, master=None): 
		tk.Frame.__init__(self, master)

		self.name = customer_name
		self.id = customer_Id
		self.username = customer_username

		self.master.title("View My Complaint Page")
		self.master.geometry("890x855")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text="View My Complaint", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.296, rely=0.015, relwidth=0.4, relheight=0.049)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.235, rely=0.125, relwidth=0.18, relheight=0.032)

		self.Combo1List1 = ["All Complaints", "Pending Complaints", "Closed Complaints & Pending Satisfaction", "Closed Complaints & Satisfied", "Closed Complaints & Dissatisfied","Stay Complaints", "Reverse Complaints"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.53, rely=0.125, relwidth=0.35, relheight=0.038)
		self.Combo1.set(self.Combo1List1[0])

		# Treeview
		df = pd.read_excel("csv_files/complaints.xlsx")
		df_complaint = df[df['Complainant'] == self.username]
		df_complaint = df_complaint[['ID', 'Complainant', 'Complained Party Type', 'Complained Party Email', 'Satisfaction','Time Complained', 
									 'Status', 'Complained Details', 'Complained Party Response', 'Time Response', 'Manager Justification']]

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.06, rely=0.2, relwidth=0.9, relheight=0.25)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		self.tree["column"] = ("ID", "Complainant", "Complained Party Type", "Complained Party Email", "Satisfaction", "Time Complained", "Status")
		self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		self.tree.column("Complainant", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Complained Party Type", anchor=tk.W, width=140, stretch=tk.NO)
		self.tree.column("Complained Party Email", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Satisfaction", anchor=tk.W, width=85, stretch=tk.NO)
		self.tree.column("Time Complained", anchor=tk.W, width=105, stretch=tk.NO)
		self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		self.tree.heading("ID", text="ID", anchor=tk.W)
		self.tree.heading("Complainant", text="Complainant", anchor=tk.W)
		self.tree.heading("Complained Party Type", text="Complained Party Type", anchor=tk.W)
		self.tree.heading("Complained Party Email", text="Complained Party Email", anchor=tk.W)
		self.tree.heading("Satisfaction", text="Satisfaction", anchor=tk.W)
		self.tree.heading("Time Complained", text="Time Complained", anchor=tk.W)
		self.tree.heading("Status", text="Status", anchor=tk.W)

		df_rows = df_complaint.to_numpy().tolist()

		for row in df_rows:
			self.tree.insert("", "end", value=row)

		# Reported Comment Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Complaint details and feedbacks", style='LabelHead.TLabel')
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

		self.LabelMyTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelMyTitle.grid(sticky="W", row=0, column=0, padx=0, pady=5)

		self.LabelMyTime = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelMyTime.grid(sticky="W", row=1, column=0, padx=0, pady=5)

		self.LabelMyContent = tk.ttk.Label(self.MyFrame, text="" ,style="LabelContent.TLabel")
		self.LabelMyContent.grid(sticky="W", row=2, column=0, padx=0, pady=10)

		self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="" ,
									  style="LabelContent.TLabel")
		self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

		self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

		self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="", style="LabelTime.TLabel")
		self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

		self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text="", style="LabelContent.TLabel")
		self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

		self.LabelSeg2 = tk.ttk.Label(self.MyFrame, text="" ,
									  style="LabelContent.TLabel")
		self.LabelSeg2.grid(sticky="W", row=7, column=0, padx=0, pady=10)

		self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="", style="LabelHeadline.TLabel")
		self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=0)

		self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text="", style="LabelContent.TLabel")
		self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=10)

		# Satisfied Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonSatisfied = tk.ttk.Button(self.top, text="Satisfied", command=self.satisfied, style="ButtonAll.TButton")
		self.ButtonSatisfied.place(relx=0.135, rely=0.92, relwidth=0.12, relheight=0.05)
		self.ButtonSatisfied.configure(state="disabled")

		# dissatisfied Button
		self.ButtonDissatisfied = tk.ttk.Button(self.top, text="Dissatisfied", command=self.dissatisfied, style="ButtonAll.TButton")
		self.ButtonDissatisfied.place(relx=0.415, rely=0.92, relwidth=0.15, relheight=0.05)
		self.ButtonDissatisfied.configure(state="disabled")

		# Back Button
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.735, rely=0.92, relwidth=0.12, relheight=0.05)


	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()
		self.ButtonSatisfied.configure(state="disabled")
		self.ButtonDissatisfied.configure(state="disabled")

	def selected_item(self, event):
		get_all = self.tree.item(self.tree.selection())
		list_row = get_all.get("values")
		if list_row != "":
			self.id = list_row[0]
			complaint_time = list_row[5]
			complaint_detail = self.wrap(list_row[7])
			satisfaction = list_row[4]
			complained_party_response_time = list_row[9]
			complained_party_response = self.wrap(list_row[8])
			manager_justification = self.wrap(list_row[10])
			status = list_row[6]
			# Refresh
			self.refresh()


			self.LabelMyTitle = tk.ttk.Label(self.MyFrame, text="Details of My Conplaint:", style="LabelHeadline.TLabel")
			self.LabelMyTitle.grid(sticky="W", row=0, column=0, padx=0, pady=5)

			self.LabelMyTime = tk.ttk.Label(self.MyFrame, text="Conplained on " + complaint_time, style="LabelTime.TLabel")
			self.LabelMyTime.grid(sticky="W", row=1, column=0, padx=0, pady=5)

			self.LabelMyContent = tk.ttk.Label(self.MyFrame, text=complaint_detail ,style="LabelContent.TLabel")
			self.LabelMyContent.grid(sticky="W", row=2, column=0, padx=0, pady=10)
			# Case 1: status = "pending", complained party hasn't responsed yet, show my complaint, disable satisfaction
			if status == "pending":
				self.ButtonSatisfied.configure(state="disabled")
				self.ButtonDissatisfied.configure(state="disabled")

			# Case 1: status = "pending" and satisfaction = "pending" complained party has responsed, 
			# you need to responed, show my complaint and party response, enable satisfaction
			elif status == "closed":
				self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

				self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="Complained Party Response:", style="LabelHeadline.TLabel")
				self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

				self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="Responsed on " + complained_party_response_time, style="LabelTime.TLabel")
				self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

				self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text=complained_party_response, style="LabelContent.TLabel")
				self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)
				if satisfaction == "pending":
					self.ButtonSatisfied.configure(state="normal")
					self.ButtonDissatisfied.configure(state="normal")
				else:
					self.ButtonSatisfied.configure(state="disabled")
					self.ButtonDissatisfied.configure(state="disabled")

			# Case 3: Manager decided stay or reverse
			else:
				self.LabelSeg1 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg1.grid(sticky="W", row=3, column=0, padx=0, pady=10)

				self.LabelPartyTitle = tk.ttk.Label(self.MyFrame, text="Complained Party Response:", style="LabelHeadline.TLabel")
				self.LabelPartyTitle.grid(sticky="W", row=4, column=0, padx=0, pady=0)

				self.LabelPartyTime = tk.ttk.Label(self.MyFrame, text="Responsed on " + complained_party_response_time, style="LabelTime.TLabel")
				self.LabelPartyTime.grid(sticky="W", row=5, column=0, padx=0, pady=5)

				self.LabelPartyContent = tk.ttk.Label(self.MyFrame, text=complained_party_response, style="LabelContent.TLabel")
				self.LabelPartyContent.grid(sticky="W", row=6, column=0, padx=0, pady=10)

				self.LabelSeg2 = tk.ttk.Label(self.MyFrame, text="-------------------------------------------------------------------------------------------------------------------------------------------------" ,
									  style="LabelContent.TLabel")
				self.LabelSeg2.grid(sticky="W", row=7, column=0, padx=0, pady=10)

				self.LabelManagerTitle = tk.ttk.Label(self.MyFrame, text="Manager Justification:", style="LabelHeadline.TLabel")
				self.LabelManagerTitle.grid(sticky="W", row=8, column=0, padx=0, pady=0)

				self.LabelManagerContent = tk.ttk.Label(self.MyFrame, text=manager_justification, style="LabelContent.TLabel")
				self.LabelManagerContent.grid(sticky="W", row=9, column=0, padx=0, pady=10)

				self.ButtonSatisfied.configure(state="disabled")
				self.ButtonDissatisfied.configure(state="disabled")


	def refresh(self):
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.5, relheight=0.4, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		self.LabelMyTitle.destroy()
		self.LabelMyTime.destroy()
		self.LabelMyContent.destroy()
		self.LabelSeg1.destroy()
		self.LabelPartyTitle.destroy()
		self.LabelPartyTime.destroy()
		self.LabelPartyContent.destroy()
		self.LabelSeg2.destroy()
		self.LabelManagerTitle.destroy()
		self.LabelManagerContent.destroy()

	def satisfied(self):
		answer = askyesno(title='Notice', message='Do you confirm that you are satisfied with the complained party response?'+
							'\nSo no one will get penalty.')
		if answer:
			# change the satisfaction
			df_complaint = pd.read_excel("csv_files/complaints.xlsx")
			df_complaint.loc[df_complaint['ID'] == self.id, 'Satisfaction'] = 'satisfied'
			df_complaint.to_excel("csv_files/complaints.xlsx", index=False)
			# Update the treeview
			self.update_treeview()
			# Refresh the comment body
			self.refresh()
			# Disable the button untile the next selection
			self.ButtonSatisfied.configure(state="disabled")
			self.ButtonDissatisfied.configure(state="disabled")

	def dissatisfied(self):
		answer = askyesno(title='Notice', message='Do you confirm that you are dissatisfied with the complained party response?'+
							'\nSo the manager will look into it and decide who gets penalty.')
		if answer:
			# change the satisfaction
			df_complaint = pd.read_excel("csv_files/complaints.xlsx")
			df_complaint.loc[df_complaint['ID'] == self.id, 'Satisfaction'] = 'dissatisfied'
			df_complaint.to_excel("csv_files/complaints.xlsx", index=False)
			# Update the treeview
			self.update_treeview()
			# Refresh the comment body
			self.refresh()
			# Disable the button untile the next selection
			self.ButtonSatisfied.configure(state="disabled")
			self.ButtonDissatisfied.configure(state="disabled")

	def back(self):
		# Remember to pass args
		self.top.destroy()
		complaint_page.complaint_page(self.name, self.id, self.username)

	def wrap(self, string, lenght=70):
		return '\n'.join(textwrap.wrap(string, lenght))

	def update_treeview(self):
		combo1 = self.Combo1.get()
		df = pd.read_excel("csv_files/complaints.xlsx")
		if combo1 == "All Complaints":
			df_complaint = df[df['Complainant'] == self.username]
		elif combo1 == "Pending Complaints":
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'pending']
		elif combo1 == "Closed Complaints & Pending Satisfaction":
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'pending']
		elif combo1 == "Closed Complaints & Satisfied":
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'satisfied']
		elif combo1 == "Closed Complaints & Dissatisfied":
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'closed']
			df_complaint = df_complaint[df_complaint['Satisfaction'] == 'dissatisfied']
		elif combo1 == "Stay Complaints":
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'stay']
		else:
			df_complaint = df[df['Complainant'] == self.username]
			df_complaint = df_complaint[df_complaint['Status'] == 'reverse']

		df_complaint = df_complaint[['ID', 'Complainant', 'Complained Party Type', 'Complained Party Email', 'Satisfaction','Time Complained', 
									 'Status', 'Complained Details', 'Complained Party Response', 'Time Response', 'Manager Justification']]

			
		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.06, rely=0.2, relwidth=0.9, relheight=0.25)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		self.tree["column"] = ("ID", "Complainant", "Complained Party Type", "Complained Party Email", "Satisfaction", "Time Complained", "Status")
		self.tree.column("ID", anchor=tk.W, width=32, stretch=tk.NO)
		self.tree.column("Complainant", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Complained Party Type", anchor=tk.W, width=140, stretch=tk.NO)
		self.tree.column("Complained Party Email", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.column("Satisfaction", anchor=tk.W, width=85, stretch=tk.NO)
		self.tree.column("Time Complained", anchor=tk.W, width=105, stretch=tk.NO)
		self.tree.column("Status", anchor=tk.W, width=75, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		self.tree.heading("ID", text="ID", anchor=tk.W)
		self.tree.heading("Complainant", text="Complainant", anchor=tk.W)
		self.tree.heading("Complained Party Type", text="Complained Party Type", anchor=tk.W)
		self.tree.heading("Complained Party Email", text="Complained Party Email", anchor=tk.W)
		self.tree.heading("Satisfaction", text="Satisfaction", anchor=tk.W)
		self.tree.heading("Time Complained", text="Time Complained", anchor=tk.W)
		self.tree.heading("Status", text="Status", anchor=tk.W)

		df_rows = df_complaint.to_numpy().tolist()

		for row in df_rows:
			self.tree.insert("", "end", value=row)