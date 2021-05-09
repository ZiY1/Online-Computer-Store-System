import tkinter as tk  
import tkinter.ttk as ttk 
from PIL import ImageTk, Image
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
import clerk_post_discussion


class discussion_table(tk.Frame):

	# Pass username as None if in guest page
	def __init__(self, coming_from, coming_from_discuss,item_name, customer_name, 
                     customer_Id, customer_username, discussion_type, df, master=None): 
		tk.Frame.__init__(self, master)

		self.coming_from = coming_from
		self.coming_from_discuss = coming_from_discuss
		self.item_name = item_name
		
		#---Customer Info-------------
		self.Customer_Name = customer_name
		self.Customer_Id = customer_Id
		self.Customer_username = customer_username
		#-------------------------------
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
		self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",20, "bold"), background = "light blue")
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

		if self.coming_from_discuss != "setting_account":
			df_items = pd.read_excel("csv_files/items.xlsx")
			df_item_info = df_items[ df_items["Name"] == self.item_name]
			self.item_type = df_item_info['Type'].iloc[-1]
			
			if self.item_type == 'Desktop':
				image_tempo = Image.open( f"images/Lenovo_Desktops/{self.item_name}.png" )
			elif self.item_type == 'Laptop':
				image_tempo = Image.open( f"images/Lenovo_Laptops/{self.item_name}.png" )
			elif self.item_type == 'workstation':
				image_tempo = Image.open( f"images/workstations/{self.item_name}.png" )
			elif self.item_type == "server":
				image_tempo = Image.open( f"images/servers/{self.item_name}.png" )
			elif self.item_type == "mainframe":
				image_tempo = Image.open( f"images/mainframes/{self.item_name}.png" )
			elif self.item_type == "Computer Part":
				image_tempo = Image.open( f"images/computer_parts/{self.item_name}.png" )

			image_tempo = image_tempo.resize(  (220,160), Image.ANTIALIAS )
			self.item_image = ImageTk.PhotoImage( image_tempo )
			self.label_image = tk.Label( self.MyFrame, 
				text = f"{self.item_name}", image = self.item_image,
                        compound = tk.TOP,
                        font = "Bold").grid( row = 2, column = 0, pady = 10 )
            
			

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
			self.LabelSeg.grid(sticky="W", row = 3+counter, column=0, padx=0, pady=15)

			self.LabelID = tk.ttk.Label(self.MyFrame, text="Coment ID: " + str(row[0]), style="LabelType.TLabel")
			self.LabelID.grid(sticky="W", row = 4+counter, column=0, padx=0, pady=10)

			if self.discussion_type == "Me All":
				self.LabelComputer = tk.ttk.Label(self.MyFrame, text = "Item Name: " + row[4], style="LabelType.TLabel")
				self.LabelComputer.grid(sticky="W", row=5+counter, column=0, padx=0, pady=5)

			self.LabelType = tk.ttk.Label(self.MyFrame, text=row[1] + ": " + row[3], style="LabelType.TLabel")
			self.LabelType.grid(sticky="W", row=6+counter, column=0, padx=0, pady=5)

			if str(row[5]) != 'nan':
				self.LabelVote = tk.ttk.Label(self.MyFrame, text=self.rate_text(str(row[5])),  foreground="#DAA520", style="LabelTime.TLabel")
				self.LabelVote.grid(sticky="W", row=7+counter, column=0, padx=0, pady=5)
			else:
				self.LabelEmail = tk.ttk.Label(self.MyFrame, text='Email: ' + row[2], style="LabelType.TLabel")
				self.LabelEmail.grid(sticky="W", row=7+counter, column=0, padx=0, pady=5)

			self.LabelTime = tk.ttk.Label(self.MyFrame, text="Reviewed on " + row[8], style="LabelTime.TLabel")
			self.LabelTime.grid(sticky="W", row=8+counter, column=0, padx=0, pady=10)

			self.LabelHeadline = tk.ttk.Label(self.MyFrame, text=row[6], style="LabelHeadline.TLabel")
			self.LabelHeadline.grid(sticky="W", row=9+counter, column=0, padx=0, pady=5)

			row[7] = self.wrap(row[7])
			self.LabelContent = tk.ttk.Label(self.MyFrame, text=row[7], style="LabelContent.TLabel")
			self.LabelContent.grid(sticky="W", row=10+counter, column=0, padx=0, pady=10)

			counter = counter+10



	def command_back(self):
		if self.coming_from_discuss == "discussion_page":
			self.top.destroy()		
			discussion_page.discussion_page(
			        coming_from = self.coming_from, 
					item_name = self.item_name, customer_name = self.Customer_Name, 
                    customer_Id = self.Customer_Id, customer_username = self.Customer_username)
			
			'''
			generalized_item.generalized_item(coming_from = self.coming_from, 
			item_name = self.item_name, customer_name = self.Customer_Name, 
            customer_Id = self.Customer_Id, customer_username = self.Customer_username) 
            '''

		elif self.coming_from_discuss == "setting_account":
			self.top.destroy()
			setting_account.setting_account(customer_name = self.Customer_Name, 
			customer_Id = self.Customer_Id, customer_username = self.Customer_username)

		elif self.coming_from_discuss == "generalized_item":
			self.top.destroy()
			generalized_item.generalized_item(coming_from = self.coming_from, 
			item_name = self.item_name, customer_name = self.Customer_Name, 
            customer_Id = self.Customer_Id, customer_username = self.Customer_username)

		else: #self.coming_from_discuss == "clerk_post_discussion":
			self.top.destroy()
			clerk_post_discussion.clerk_post_discussion(self.Customer_Name, self.Customer_username) #

	def rate_text(self, rate):
		if str(rate) == "1.0":
			return "★☆☆☆☆"
		elif str(rate) == "2.0":
			return "★★☆☆☆"
		elif str(rate) == "3.0":
			return "★★★☆☆"
		elif str(rate) == "4.0":
			return "★★★★☆"
		elif str(rate) == "5.0":
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
			
		
			if str( self.Text1.get()).isdigit(): # Before casting check if we can convert it into integer
				comment_id = int(self.Text1.get())
				
				if comment_id in list(df_discussion['ID']):
					flag_reportId_valid = True
				else:
					flag_reportId_valid = False

				#----------------Check if comment is already reported---------------------
				df_report = pd.read_excel("csv_files/discussion_reports.xlsx")
				
				if comment_id in list(df_report['Reported Comment ID']):
						flag_already_report = True
				else:
    					flag_already_report = False
				#--------------------------------------------------------------------------

				now = datetime.datetime.now()
				DataTime = now.strftime("%y-%m-%d %H:%M")
				Status = "pending"
				ManagerJustification = "pending"
				
					
				Id = len(df_report) 
				tempo = pd.DataFrame([[Id, self.Customer_username, comment_id, DataTime, Status, ManagerJustification]], 
										columns=['ID', 'Reporter', 'Reported Comment ID', 'Reported Time', 'Status', 'Manager Justification'])
				df_report = df_report.append(tempo)

				if flag_reportId_valid and not flag_already_report:
					df_report.to_excel("csv_files/discussion_reports.xlsx", index=False)
					tk.messagebox.showinfo("Success", "Report Submitted")
				elif not flag_reportId_valid:
					tk.messagebox.showerror("Error", "Comment ID invalid")
				else:
					tk.messagebox.showerror("Error", "Comment ID already reported")

			else:
				tk.messagebox.showerror( "Error", "Invalid input provided.\n" +
					"Try an integer next time." )
		