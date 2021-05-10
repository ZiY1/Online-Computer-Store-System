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
import manager_management_page

class manager_view_suspicious_bidding(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username

		self.master.title("View Suspicious Bidding Page")
		self.master.geometry("1590x955")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text='View Suspicious Bidding', style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.36, rely=0.015, relwidth=0.26, relheight=0.047)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.35, rely=0.09, relwidth=0.13, relheight=0.026)

		# Ongoing means the status is 'processing', Closed means the status is 'assigned'
		self.Combo1List1 = ["All Suspicious Bidding"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.54, rely=0.09, relwidth=0.16, relheight=0.032)
		self.Combo1.set(self.Combo1List1[0])


		# Back Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.863, rely=0.92, relwidth=0.06, relheight=0.045)

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

			self.create_right_frame_content()
		

					
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
    				image_tempo = Image.open( f"images/computer_parts/{item_name}.png" )
    
			image_tempo = image_tempo.resize((220,160), Image.ANTIALIAS)

			self.images.append(None)
			self.images[i] = ImageTk.PhotoImage( image_tempo )
			tk.ttk.Label( self.MyFrame, image = self.images[i], style="Label_imag.TLabel").grid(sticky="W", row=4+counter, column=1, padx=0, pady = 25, rowspan=3)
			counter = counter + 3

		tk.ttk.Label(self.MyFrame, text="Subtotal: " + "$ {:,.2f}".format(self.subtotal) ,style="LabelHeadline.TLabel").grid(sticky="W", row=5+len(self.order_ids)*3, column=0, padx=0, pady=20)


	def create_right_frame_content(self):
		# Fome bidding file, get all biider of the selected tracking order number
		df = pd.read_excel("csv_files/biddings.xlsx")
		df_bidder = df[df['Bidding Tracking Order'] == self.tracking_order]
		df_bidder_list = df_bidder.to_numpy().tolist()

		self.bidding_ids = list()
		self.bidder_names = list()
		self.bidder_emails = list()
		self.bidder_prices = list()
		self.wins_loses = list()
		self.assigned_by = df_bidder_list[0][6]
		self.assigned_on = df_bidder_list[0][7]
		self.justification = df_bidder_list[0][8]

		for row in df_bidder_list:
			self.bidding_ids.append(row[0])
			self.bidder_names.append(row[2])
			self.bidder_emails.append(row[3])
			self.bidder_prices.append(row[4])
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

		

			win_lose = self.wins_loses[i]
			tk.ttk.Label(self.MyFrame2, text=win_lose, style="LabelHeadline.TLabel").grid(sticky="W", row=1+counter, column=2)


			if i in self.min_index_list and len(self.bidder_names) > 1:
				tk.ttk.Label(self.MyFrame2, text="Lowest!" ,style="LabelHeadline.TLabel").grid(sticky="W", row=2+counter, column=2)
				
			counter = counter+4

		tk.ttk.Label(self.MyFrame2, text="", style="LabelHeadline.TLabel").grid(sticky="W", row=1+len(self.bidder_names)*counter, column=0, padx=0, pady=15)
		tk.ttk.Label(self.MyFrame2, text="Assigned By Clerk: "+self.assigned_by ,
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
		manager_management_page.manager_management_page(self.name, self.username) #self.name, self.username

	def update_treeview(self):

		# get the assigned and delivered orders in orders file
		df = pd.read_excel("csv_files/orders.xlsx")
		df_orders = df[df['Order_Status'].isin(['assigned', 'delivered'])]

		# get the suspicous orders in tracking_orders file
		df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
		df_sus = df_tracking[df_tracking['Suspicious'] == 'yes']
		list_sus_bidding = list(df_sus['Tracking Order Number'])

		# get the corresponding orders
		df2 = df_orders[df_orders['Tracking Order'].isin(list_sus_bidding)]


		df3 = df2.sort_values(by='Tracking Order')
		df_order = df3[['Tracking Order', 'Username', 'Date order processed', 'Order_Status', 'Order_Id', 'Item_Name', 'Customized',
						'Item_Price', 'Home address', 'Delivery_Company_Assigned']]

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.2)
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
