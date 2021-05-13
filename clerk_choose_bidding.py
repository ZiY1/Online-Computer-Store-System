import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re
import textwrap
import datetime

# python scripts 
import clerk_management_page

class clerk_choose_bidding(tk.Frame):

	def __init__(self,  name, username, master=None): #name, username,
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username

		self.master.title("Clerk Choose Bidding Page")
		self.master.geometry("1330x855")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text='Clerk Choose Bidding', style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.36, rely=0.015, relwidth=0.26, relheight=0.047)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.35, rely=0.09, relwidth=0.13, relheight=0.03)

		# Ongoing means the status is 'processing', Closed means the status is 'assigned'
		self.style.configure("LabelSub.TLabel",anchor="w", font=("Helvetica",10), background = "light blue")
		self.LabelSub = tk.ttk.Label(self.top, text="select the bidding status", style='LabelSub.TLabel')
		self.LabelSub.place(relx=0.54, rely=0.066, relwidth=0.18, relheight=0.026)
		self.Combo1List1 = ["Ongoing Bidding", "Closed Bidding"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.54, rely=0.09, relwidth=0.16, relheight=0.032)
		self.Combo1.set(self.Combo1List1[0])

		# Clerk Justification
		self.LabelClerkJusti = tk.ttk.Label(self.top, text="Clerk Justification:", style='Label1.TLabel')
		self.LabelClerkJusti.place(relx=0.59, rely=0.8, relwidth=0.13, relheight=0.03)

		self.TextJusti = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.TextJusti.place(relx=0.72, rely=0.8, relwidth=0.2, relheight=0.08)

		# Back Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.863, rely=0.93, relwidth=0.06, relheight=0.045)

		# Create left and right frame, create treeview
		self.update_treeview()
		self.create_left_frame()
		self.create_right_frame()

		# Some configuration
		self.style.configure("LabelTime.TLabel",anchor="w", font=("Helvetica",11), background = "light blue")
		self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.style.configure("LabelBidding.TLabel",anchor="w", font=("Helvetica",16), background = "light blue")

	def create_left_frame(self):
		# Order Details Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Order Details", style='LabelHead.TLabel')
		self.LabelHead.place(relx=0.21, rely=0.355, relwidth=0.35, relheight=0.04)

		# Order Details Body
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=0.495, relheight=0.385)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=0.495, rely=0.4, relheight=0.385, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

	def create_right_frame(self):
		# Bidder Details
		self.LabelHead2 = tk.ttk.Label(self.top, text="Bidder Details", style='LabelHead.TLabel')
		self.LabelHead2.place(relx=0.71, rely=0.355, relwidth=0.35, relheight=0.04)

		# Bidder Details Body
		self.Canvas2 = tk.Canvas(self.top, bg="light blue")
		self.Canvas2.place(relx=0.505, rely=0.4, relwidth=0.5, relheight=0.385)

		self.MyFrame2 = tk.Frame(self.Canvas2, bg = "light blue")
		self.MyFrame2.bind('<Configure>', lambda e: self.Canvas2.configure(scrollregion=self.Canvas2.bbox('all')))

		self.Canvas2.create_window(0, 0, window=self.MyFrame2)

		self.Scrolly2 = tk.Scrollbar(self.top, command=self.Canvas2.yview)
		self.Scrolly2.place(relx=1, rely=0.4, relheight=0.385, anchor='ne')
		self.Canvas2.configure(yscrollcommand=self.Scrolly2.set)

	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()
		# Refresh text
		self.TextJusti = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.TextJusti.place(relx=0.72, rely=0.8, relwidth=0.2, relheight=0.08)

	def selected_item(self, event):
		get_all = self.tree.item(self.tree.selection())
		list_row = get_all.get("values")
		if list_row != "":
			self.tracking_order = list_row[0]
			self.buyer_username = list_row[1]
			self.date_purchased = list_row[2]
			self.order_status = list_row[3]
			
			# get customers' home address in cutomer file
			df_cus = pd.read_excel("csv_files/registered_customers.xlsx")
			df_cus_row = df_cus[df_cus['Username'] == self.buyer_username]
			self.home_address = str(df_cus_row['Home Address'].iloc[-1])

			self.create_left_frame_content()

			if self.order_status == "bidding":
				self.create_right_frame_content("bidding")
			else: 
				# delivery company assigned
				# Display the wins and loses
				self.create_right_frame_content("assigned")

			# Refresh text
			self.TextJusti = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
			self.TextJusti.place(relx=0.72, rely=0.8, relwidth=0.2, relheight=0.08)

					
	def create_left_frame_content(self):
		# put items of the same tracking order in a list
		self.order_ids = list()
		self.item_names = list()
		self.item_prices = list()
		self.images = list()
		self.is_customized = list()

		# get all orders of the same tracking order number, !drop the cancelled and in cart
		df = pd.read_excel("csv_files/orders.xlsx")
		df.drop( df.index[(df['Order_Status'] == 'cancelled')], axis=0, inplace = True)
		df.drop( df.index[(df['Order_Status'] == 'in cart')], axis=0, inplace = True)
		df2 = df[df['Order_Status'].isin(["bidding", "assigned", "delivered"])]
		df2 = df2.sort_values(by='Tracking Order')
		df_order = df2[['Tracking Order', 'Username', 'Date order processed', 'Order_Status', 'Order_Id', 'Item_Name', 'Customized',
						'Item_Price', 'Home address', 'Delivery_Company_Assigned']]
		df_a_tracking_order = df_order[df_order['Tracking Order'] == self.tracking_order]
		self.subtotal = df_a_tracking_order['Item_Price'].sum()
		df_a_tracking_order_list = df_a_tracking_order.to_numpy().tolist()
		for row in df_a_tracking_order_list:
			self.order_ids.append(row[4])
			self.item_names.append(row[5])
			self.is_customized.append(row[6])
			self.item_prices.append(float(row[7]))

		# get info of each computer, for displaying the image
		df_items = pd.read_excel( "csv_files/items.xlsx" )
		
		# Refresh
		self.create_left_frame()

		self.style.configure( "Label_imag.TLabel",  background = 'light blue')

		self.LabelTrackingOrderNumber = tk.ttk.Label(self.MyFrame, text="Tracking Order Number: " + self.tracking_order, style="LabelHeadline.TLabel")
		self.LabelTrackingOrderNumber.grid(sticky="W", row=0, column=0, padx=0, pady=10)

		self.LabelBuyer = tk.ttk.Label(self.MyFrame, text="Buyer Username: " + self.buyer_username, style="LabelHeadline.TLabel")
		self.LabelBuyer.grid(sticky="W", row=1, column=0, padx=0, pady=10)

		self.LabelHomeAddress = tk.ttk.Label(self.MyFrame, text="Home Address: " + self.home_address ,style="LabelHeadline.TLabel")
		self.LabelHomeAddress.grid(sticky="W", row=2, column=0, padx=0, pady=10)

		self.LabelPurchaseTime = tk.ttk.Label(self.MyFrame, text="Purchased on: " + self.date_purchased ,style="LabelTime.TLabel")
		self.LabelPurchaseTime.grid(sticky="W", row=3, column=0, padx=0, pady=5)

		counter = 0
		for i in range(len(self.order_ids)):
			order_id = self.order_ids[i]
			item_name = self.item_names[i]
			item_price = "$ {:,.2f}".format(self.item_prices[i])
			customized = self.is_customized[i]

			# Display the order id, item_name, item_price
			tk.ttk.Label(self.MyFrame, text="Order Id: " + str(order_id) ,style="LabelHeadline.TLabel").grid(sticky="W", row=4+counter, column=0, padx=0, pady=5)
			if customized == 'Customized':
				tk.ttk.Label(self.MyFrame, text="Product: " + item_name + '(Customized)' ,style="LabelHeadline.TLabel").grid(sticky="W", row=5+counter, column=0, padx=0, pady=5)
			else:
				tk.ttk.Label(self.MyFrame, text="Product: " + item_name ,style="LabelHeadline.TLabel").grid(sticky="W", row=5+counter, column=0, padx=0, pady=5)
			tk.ttk.Label(self.MyFrame, text="Price: " + item_price ,style="LabelHeadline.TLabel").grid(sticky="W", row=6+counter, column=0, padx=0, pady=5)

			# Display the image
			item_type = df_items[df_items['Name'] == item_name ]['Type'].iloc[-1]
			if item_type == 'Desktop':
				image_tempo = Image.open( f"images/Lenovo_Desktops/{item_name}.png" )
			elif item_type == 'Laptop':
				image_tempo = Image.open( f"images/Lenovo_Laptops/{item_name}.png" )
			elif item_type == 'workstation':
				image_tempo = Image.open( f"images/workstations/{item_name}.png" )
			elif item_type == "server":
				image_tempo = Image.open( f"images/servers/{item_name}.png" )
			elif item_type == "mainframe":
				image_tempo = Image.open( f"images/mainframes/{item_name}.png" )
			elif item_type == "Computer Part":
    				image_tempo = Image.open( f"images/computer_parts/{item_name}.png")
    
			image_tempo = image_tempo.resize((220,160), Image.ANTIALIAS)

			self.images.append(None)
			self.images[i] = ImageTk.PhotoImage( image_tempo )
			tk.ttk.Label( self.MyFrame, image = self.images[i], style="Label_imag.TLabel").grid(sticky="W", row=7+counter, column=0, padx=0, pady = 5)
			counter = counter + 4

		tk.ttk.Label(self.MyFrame, text="Subtotal: " + "$ {:,.2f}".format(self.subtotal) ,style="LabelHeadline.TLabel").grid(sticky="W", row=5+len(self.order_ids)*4, column=0, padx=0, pady=30)


	def create_right_frame_content(self, status):
		# Fome bidding file, get all biider of the selected tracking order number
		df = pd.read_excel("csv_files/biddings.xlsx")
		df_bidder = df[df['Bidding Tracking Order'] == self.tracking_order]
		df_bidder_list = df_bidder.to_numpy().tolist()

		self.bidding_ids = list()
		self.bidder_names = list()
		self.bidder_emails = list()
		self.bidder_prices = list()
		if status == 'bidding':
			self.win_buttons = list()
		else:
			self.wins_loses = list()
			self.assigned_by = df_bidder_list[0][6]
			self.assigned_on = df_bidder_list[0][7]
			self.justification = df_bidder_list[0][8]

		for row in df_bidder_list:
			self.bidding_ids.append(row[0])
			self.bidder_names.append(row[2])
			self.bidder_emails.append(row[3])
			self.bidder_prices.append(row[4])
			if status == 'assigned':
				self.wins_loses.append(row[5])

		# Refresh
		self.create_right_frame()

		self.LabelTrackingOrderNumber = tk.ttk.Label(self.MyFrame2, text="Tracking Order Number: " + self.tracking_order, style="LabelHeadline.TLabel")
		self.LabelTrackingOrderNumber.grid(sticky="W", row=0, column=0, padx=0, pady=20)

		# get the the list index of the lowest price offered (1 or more)
		self.min_index_list = self.locate_min(self.bidder_prices)

		counter = 0
		for i in range(len(self.bidder_names)):
			bidding_id = self.bidding_ids[i]
			bidder_name = self.bidder_names[i]
			bidder_email = self.bidder_emails[i]
			bidder_price = "$ {:,.2f}".format(self.bidder_prices[i])


			# Display the bidding_id, bidder_name, bidder_email, price_offered
			tk.ttk.Label(self.MyFrame2, text="Biding ID: " + str(bidding_id) ,style="LabelHeadline.TLabel").grid(sticky="W", row=1+counter, column=0, padx=0, pady=10)
			tk.ttk.Label(self.MyFrame2, text="Bidder Company Name: " + bidder_name ,style="LabelHeadline.TLabel").grid(sticky="W", row=2+counter, column=0, padx=0, pady=10)
			tk.ttk.Label(self.MyFrame2, text="Bidder Company Email: " + bidder_email ,style="LabelHeadline.TLabel").grid(sticky="W", row=3+counter, column=0, padx=0, pady=10)
			tk.ttk.Label(self.MyFrame2, text="Price Offered: " + bidder_price ,style="LabelHeadline.TLabel").grid(sticky="W", row=4+counter, column=0, padx=0, pady=10)

			if status == 'bidding':
				self.win_buttons.append(None)
				self.win_buttons[i] = tk.Button(self.MyFrame2, text = "Win", command = lambda bid_index = i: self.bidding_win(bid_index))
				self.win_buttons[i].grid( row = 1+counter, column = 2)
			else: # status == 'assigned' or 'delivered'
				win_lose = self.wins_loses[i]
				tk.ttk.Label(self.MyFrame2, text=win_lose, style="LabelHeadline.TLabel").grid(sticky="W", row=1+counter, column=2)


			if i in self.min_index_list and len(self.bidder_names) > 1:
				tk.ttk.Label(self.MyFrame2, text="Lowest!" ,style="LabelHeadline.TLabel").grid(sticky="W", row=2+counter, column=2)
				
			counter = counter+4

		if status == 'assigned' or status == 'delivered':
			tk.ttk.Label(self.MyFrame2, text="", style="LabelHeadline.TLabel").grid(sticky="W", row=1+len(self.bidder_names)*counter, column=0, padx=0, pady=15)
			tk.ttk.Label(self.MyFrame2, text="Assigned By: "+self.assigned_by ,
				style="LabelHeadline.TLabel").grid(sticky="W", row=2+len(self.bidder_names)*counter, column=0, padx=0, pady=5)
			tk.ttk.Label(self.MyFrame2, text="Assigned On: "+self.assigned_on ,
				style="LabelHeadline.TLabel").grid(sticky="W", row=3+len(self.bidder_names)*counter, column=0, padx=0, pady=5)
			if str(self.justification) == "" or str(self.justification) == "nan":
				tk.ttk.Label(self.MyFrame2, text="Justification: No justification provided" ,
					style="LabelHeadline.TLabel").grid(sticky="W", row=4+len(self.bidder_names)*counter, column=0, padx=0, pady=5)
			else:
				tk.ttk.Label(self.MyFrame2, text="Justification: " + str(self.justification) ,
					style="LabelHeadline.TLabel").grid(sticky="W", row=4+len(self.bidder_names)*counter, column=0, padx=0, pady=5)

	def locate_min(self, my_list):
		smallest = min(my_list)
		return [index for index, element in enumerate(my_list) if smallest == element]

	def refresh(self):
		self.create_left_frame()
		self.create_right_frame()

	def back(self):
		self.top.destroy()
		clerk_management_page.clerk_management_page(self.name, self.username) #self.name, self.username

	def update_treeview(self):
		combo1 = self.Combo1.get()
		df = pd.read_excel("csv_files/orders.xlsx")
		if combo1 == 'Ongoing Bidding':
			df2 = df[df['Order_Status'] == 'bidding']
		else:
			df2 = df[df['Order_Status'].isin(['assigned', 'delivered'])]

		df3 = df2.sort_values(by='Tracking Order')
		df_order = df3[['Tracking Order', 'Username', 'Date order processed', 'Order_Status', 'Order_Id', 'Item_Name', 'Customized',
						'Item_Price', 'Home address', 'Delivery_Company_Assigned']]

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.2315, rely=0.15, relwidth=0.55, relheight=0.2)
		self.tree_scroll = tk.Scrollbar(self.tree_frame)
		self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

		self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set)
		self.tree.pack()

		self.tree_scroll.config(command=self.tree.yview)

		self.tree["column"] = ("Tracking Order", "Username", "Date order processed", "Order_Status")
		self.tree.column("Tracking Order", anchor=tk.W, width=230, stretch=tk.NO)
		self.tree.column("Username", anchor=tk.W, width=240, stretch=tk.NO)
		self.tree.column("Date order processed", anchor=tk.W, width=140, stretch=tk.NO)
		self.tree.column("Order_Status", anchor=tk.W, width=175, stretch=tk.NO)
		self.tree.bind('<ButtonRelease-1>', self.selected_item)
		self.tree["show"] = "headings"
		self.tree.heading("Tracking Order", text="Tracking Order Number", anchor=tk.W)
		self.tree.heading("Username", text="Buyer Username", anchor=tk.W)
		self.tree.heading("Date order processed", text="Date order placed", anchor=tk.W)
		self.tree.heading("Order_Status", text="Order Status", anchor=tk.W)

		df_rows = df_order.to_numpy().tolist()
		for row_num in range(len(df_rows)):
			if row_num == 0: 
				self.tree.insert("", "end", value=df_rows[row_num])
			else:
				if df_rows[row_num][0] == df_rows[row_num-1][0]:
					continue
				else:
					self.tree.insert("", "end", value=df_rows[row_num])

	def bidding_win(self, selected_index):

		# Check if clerk is suspended, if suspended, clerk can't choose the biddding
		df_suspend = pd.read_excel("csv_files/suspend_users.xlsx")
		df_suspend_type = df_suspend[df_suspend['Type_user'] == 'clerk']
		if self.username.lower() in list(df_suspend_type['Username']):
			flag_clerk_suspended = True
			tk.messagebox.showerror("Erorr", "You can't choose the wining delivery company because you are suspended")
		else:
			flag_clerk_suspended = False

		if not flag_clerk_suspended:
			# Check if there is at least two bidders
			if len(self.bidding_ids) < 2:
				flag_mutiple_bidder = False
				tk.messagebox.showerror("Error", "There are need to be at least 2 delivery companies bid on this order, please wait")
			else:
				flag_mutiple_bidder = True

			if flag_mutiple_bidder:
				# Get the current text entered
				self.clerk_justification = self.TextJusti.get("1.0", "end")
				if self.clerk_justification.strip() != "":
					flag_justi_not_null = True
					self.clerk_justification = self.wrap(self.clerk_justification)
				else:
					flag_justi_not_null = False

				# Get the current time
				now = datetime.datetime.now()
				self.DateTime = now.strftime("%y-%m-%d %H:%M")

				# Check if selected winner offered the lowest price
				flag_jutstification_needed = False

				if len(self.min_index_list) == 1:
					lowest_price_index = self.min_index_list[0]
					# only one lowest price, select the lowest
					if selected_index == lowest_price_index:
						flag_jutstification_needed = False

						self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)

					# only one lowest price, not select the lowest with no justification
					elif not flag_justi_not_null:
						answer = askyesno(title='Warning', message='The system detects that you are not selecting the only lowest price offered , and you are not providing your justification.'
						+' \n\nYou are strongly encouraged to provide justification. \nOtherwise, you will get one warning automatically.'
						+' \n\nDo you want to proceed without your justification?')
						if answer:

							flag_jutstification_needed = True
							self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)

					# only one lowest price, not select the lowest with justification
					else:

						flag_jutstification_needed = True
						self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)

				else: 
					# more than one lowest price, select one of the lowest with no justification
					if selected_index in self.min_index_list and (not flag_justi_not_null):
						answer = askyesno(title='Warning', message='The system detects that you are selecting one of the multiple lowest price offered , and you are not providing your justification.'
						+' \n\nYou are strongly encouraged to provide justification. \nOtherwise, you will get one warning automatically.'
						+' \n\nDo you want to proceed without your justification?')
						if answer:

							flag_jutstification_needed = True
							self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)
							
					# more than one lowest price, select neither of the lowest with no justification
					elif selected_index not in self.min_index_list and (not flag_justi_not_null):
						answer = askyesno(title='Warning', message='The system detects that you are not selecting the lowest price offered , and you are not providing your justification.'
						+' \n\nYou are strongly encouraged to provide justification. \nOtherwise, you will get one warning automatically.'
						+' \n\nDo you want to proceed without your justification?')
						if answer:
							flag_jutstification_needed = True
							self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)
					# more than one lowest price, select one with justification
					else:
						flag_jutstification_needed = True
						self.update_files(selected_index, flag_jutstification_needed, flag_justi_not_null)

	def update_files(self, selected_index, flag_jutstification_needed, flag_justi_not_null):
		delivery_company_assigned_name = self.bidder_names[selected_index]
		delivery_company_assigned_email = self.bidder_emails[selected_index]
		# change the status to assigned in orders file for the selected traking order number
		# change the company assigned to corresponding company in orders file for the selected traking order number
		df_order = pd.read_excel("csv_files/orders.xlsx")
		df_order['Order_Status'] = np.where((df_order['Tracking Order'] == self.tracking_order) & (df_order['Order_Status'] == 'bidding'), 'assigned', df_order.Order_Status)
		df_order['Delivery_Company_Assigned'] = np.where((df_order['Tracking Order'] == self.tracking_order) & (df_order['Order_Status'] == 'assigned'), delivery_company_assigned_email, df_order.Delivery_Company_Assigned)
		df_order.to_excel("csv_files/orders.xlsx", index=False)


		# In biddings file. 
		# For winner, change the status to 'win'. For losers, change the status to 'lose'; for the selected traking order number
		# Fill in Assigned_by and Assigned_on
		# Fill in Justification if needed
		# Update warning if needed
		df_bidding = pd.read_excel("csv_files/biddings.xlsx")
		for i in range(len(self.bidding_ids)):
			if i == selected_index:
				df_bidding['Status'] = np.where((df_bidding['Bidding Tracking Order'] == self.tracking_order) & (df_bidding['Bidding ID'] == self.bidding_ids[i]), 'win', df_bidding.Status)
			else:
				df_bidding['Status'] = np.where((df_bidding['Bidding Tracking Order'] == self.tracking_order) 
											 & (df_bidding['Bidding ID'] == self.bidding_ids[i]), 'lose', df_bidding.Status)
			df_bidding['Assigned_by'] = np.where((df_bidding['Bidding Tracking Order'] == self.tracking_order) 
							  			      & (df_bidding['Bidding ID'] == self.bidding_ids[i]), self.username, df_bidding.Assigned_by)
			df_bidding['Assigned_on'] = np.where((df_bidding['Bidding Tracking Order'] == self.tracking_order) 
											  & (df_bidding['Bidding ID'] == self.bidding_ids[i]), self.DateTime, df_bidding.Assigned_on)

			if flag_jutstification_needed and flag_justi_not_null:
				df_bidding['Clerk_justification'] = np.where((df_bidding['Bidding Tracking Order'] == self.tracking_order) 
													  	   & (df_bidding['Bidding ID'] == self.bidding_ids[i]), self.clerk_justification, df_bidding.Clerk_justification)


		if flag_jutstification_needed and not flag_justi_not_null:
			suspicious = 'yes'
			# Update Warning
			self.update_warning()
		elif flag_jutstification_needed and flag_justi_not_null:
			suspicious = 'yes'
		else:
			suspicious = 'no'

		df_bidding.to_excel("csv_files/biddings.xlsx", index=False)

		# Write to tracking file
		df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
		tempo = pd.DataFrame([[self.tracking_order, delivery_company_assigned_name, delivery_company_assigned_email, 'pending', self.DateTime, 'assigned', suspicious]], 
							columns=['Tracking Order Number', 'Delivery Company Assigned Name', 'Delivery Company Assigned Email', 'Current_Location','Updated_time', 'Delivery_status', 'Suspicious'])
		df_tracking = df_tracking.append(tempo)
		df_tracking.to_excel("csv_files/tracking_orders.xlsx", index = False)

		tk.messagebox.showinfo("Success", "Wining delivery company has assigned")

		# Transfer the money from manager to wining delivery company

		# get the winner price offered
		delivery_company_price = self.bidder_prices[selected_index]

		# get the manager current money, reduce by the amount of winner price offered
		df_privileged = pd.read_excel("csv_files/privileged_users.xlsx")
		df_manager_row = df_privileged[df_privileged['Type_user'] == 'Super user']
		manager_income = float(df_manager_row['Income'].iloc[-1])
		manager_income = manager_income - delivery_company_price
		df_privileged.loc[df_privileged['Type_user'] == 'Super user', 'Income'] = manager_income
		df_privileged.to_excel("csv_files/privileged_users.xlsx", index=False)

		# get the winning delivery company current money, increase by the amount he/she offered
		df_privileged2 = pd.read_excel("csv_files/privileged_users.xlsx")
		df_delivery = df_privileged2[df_privileged2['Type_user'] == 'delivery']
		df_delivery_row = df_delivery[df_delivery['Username'] == delivery_company_assigned_email.lower()]
		delivery_income = float(df_delivery_row['Income'].iloc[-1])
		delivery_income = delivery_income + delivery_company_price
		df_privileged2['Income'] = np.where((df_privileged2['Username'] == delivery_company_assigned_email.lower()) 
										 & (df_privileged['Type_user'] == 'delivery'), delivery_income, df_privileged2.Income)
		df_privileged2.to_excel("csv_files/privileged_users.xlsx", index=False)


		# Refesh things
		self.update_treeview()
		self.refresh()
		self.TextJusti = tk.Text(self.top, font=("Helvetica",11), wrap=tk.WORD)
		self.TextJusti.place(relx=0.72, rely=0.8, relwidth=0.2, relheight=0.08)

	def update_warning(self):
		type_user = 'clerk'
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
					if not self.username.lower() in list(df_suspend_type['Username']):
						Id = int(df_suspend['ID'].iloc[-1])
						Id = Id+1
						tempo = pd.DataFrame([[str(Id), type_user, self.username.lower(), password, name, current_warning, suspend_reason, chance_login, deny_notify]], 
							columns=['ID', 'Type_user', 'Username', 'Password', 'Name', 'Current_warnings','Suspend_reason', 'Chance_login', 'Customer_deny_notify'])
						df_suspend = df_suspend.append(tempo)

				# update suspend_user file and customers file
				df_suspend.to_excel("csv_files/suspend_users.xlsx", index=False)
				df_privileged = pd.read_excel("csv_files/privileged_users.xlsx")
				df_privileged['Status'] = np.where((df_privileged['Username'] == self.username) & (df_privileged['Type_user'] == type_user), 'suspended', df.Status)
				#df_privileged.loc[df_privileged['Username'] == username, 'Status'] = 'suspended'
				df_privileged.to_excel("csv_files/privileged_users.xlsx", index=False)


	def wrap(self, string, lenght=55):
		return '\n'.join(textwrap.wrap(string, lenght))



# #---------------------Main----------
# if __name__ == "__main__":
#     top = tk.Tk()
#     clerk_choose_bidding(top).mainloop()    


