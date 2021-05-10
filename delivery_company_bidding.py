import tkinter as tk  
import tkinter.ttk as ttk 
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter.messagebox import *

import pandas as pd 
import numpy as np 
import re

# python scripts 
import delivery_company_management_page

class delivery_company_bidding(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username

		self.master.title("Delivery Company Bidding Page")
		self.master.geometry("890x955")
		self.master.configure( background = "light blue" )

		self.create_widgets()


	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 16), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text='Delivery Company Bidding', style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.296, rely=0.015, relwidth=0.4, relheight=0.043)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.235, rely=0.09, relwidth=0.18, relheight=0.026)

		# Ongoing means the status is 'processing', Closed means the status is 'assigned' or 'delivered'
		self.Combo1List1 = ["Processing Order","Ongoing Bidding", "Closed Bidding"]
		self.Combo1 = tk.ttk.Combobox(self.top, state="readonly",values=self.Combo1List1, font=("Helvetica",11))
		self.Combo1.bind("<<ComboboxSelected>>", self.get_combo1)
		self.Combo1.place(relx=0.53, rely=0.09, relwidth=0.35, relheight=0.032)
		self.Combo1.set(self.Combo1List1[0])

		# Treeview
		self.update_treeview()

		# Order details Head
		self.style.configure("LabelHead.TLabel",anchor="w", font=("Helvetica",13), background = "light blue")
		self.LabelHead = tk.ttk.Label(self.top, text="Order Details", style='LabelHead.TLabel')
		self.LabelHead.place(relx=0.45, rely=0.355, relwidth=0.35, relheight=0.04)

		# Order details Body
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=1, relheight=0.355)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.4, relheight=0.355, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

		self.style.configure("LabelTime.TLabel",anchor="w", font=("Helvetica",11), background = "light blue")
		self.style.configure("LabelHeadline.TLabel",anchor="w", font=("Helvetica",15), background = "light blue")
		self.style.configure("LabelBidding.TLabel",anchor="w", font=("Helvetica",16), background = "light blue")

		# Make a bid
		self.LabelBid = tk.ttk.Label(self.top, text="Bidding Price:  $", style='LabelBidding.TLabel')
		self.LabelBid.place(relx=0.175, rely=0.83, relwidth=0.2, relheight=0.04)

		self.TextVar = tk.StringVar(value="Format: X.XX")
		self.Text = tk.ttk.Entry(self.top, textvariable=self.TextVar, font=("Helvetica",14))
		self.Text.place(relx=0.389, rely=0.83, relwidth=0.15, relheight=0.038)
		self.Text.configure(state="disabled")

		# Bid Button
		self.style.configure("ButtonAll.TButton", font=("Helvetica", 14))
		self.ButtonBid = tk.ttk.Button(self.top, text="Make Bid", command=self.make_bid, style="ButtonAll.TButton")
		self.ButtonBid.place(relx=0.628, rely=0.83, relwidth=0.15, relheight=0.041)
		self.ButtonBid.configure(state="disabled")

		# A bid info
		self.LabelInfo = tk.ttk.Label(self.top, text="", style='LabelTime.TLabel')
		self.LabelInfo.place(relx=0.295, rely=0.78, relwidth=0.8, relheight=0.04)

		# Back Button
		self.ButtonBack = tk.ttk.Button(self.top, text="Back", command=self.back, style="ButtonAll.TButton")
		self.ButtonBack.place(relx=0.735, rely=0.92, relwidth=0.15, relheight=0.045)


	def get_combo1(self, event):
		self.update_treeview()
		self.refresh()

		self.ButtonBid.configure(state="disabled")

		self.TextVar = tk.StringVar(value="Format: X.XX")
		self.Text = tk.ttk.Entry(self.top, textvariable=self.TextVar, font=("Helvetica",14))
		self.Text.place(relx=0.389, rely=0.83, relwidth=0.15, relheight=0.038)
		self.Text.configure(state="disabled")

		self.LabelInfo = tk.ttk.Label(self.top, text="", style='LabelTime.TLabel')
		self.LabelInfo.place(relx=0.295, rely=0.78, relwidth=0.8, relheight=0.04)

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
			
			# put items of the same tracking order in a list
			self.order_ids = list()
			self.item_names = list()
			self.item_prices = list()
			self.images = list()
			self.is_customized = list()

			# get all orders of the same tracking order number, !drop the cancelled and in cart
			self.df = pd.read_excel("csv_files/orders.xlsx")
			self.df.drop( self.df.index[(self.df['Order_Status'] == 'cancelled')], axis=0, inplace = True)
			self.df.drop( self.df.index[(self.df['Order_Status'] == 'in cart')], axis=0, inplace = True)
			df2 = self.df.sort_values(by='Tracking Order')
			df_order = df2[['Tracking Order', 'Username', 'Date order processed', 'Order_Status', 'Order_Id', 'Item_Name', 'Customized',
							'Item_Price', 'Home address', 'Delivery_Company_Assigned']]
			df_a_tracking_order = df_order[df_order['Tracking Order'] == self.tracking_order]
			self.subtotal = df_a_tracking_order['Item_Price'].sum()
			df_a_tracking_order_list = df_a_tracking_order.to_numpy().tolist()
			#print(df_a_tracking_order_list)
			for row in df_a_tracking_order_list:
				self.order_ids.append(row[4])
				self.item_names.append(row[5])
				self.is_customized.append(row[6])
				self.item_prices.append(float(row[7]))

			# get info of each computer, for displaying the image
			df_items = pd.read_excel( "csv_files/items.xlsx" )
			
			# Refresh
			self.refresh()

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

			if self.order_status == "processing":
				self.check_bidding()
			elif self.order_status == "bidding":
				self.check_bidding()
			else:
				self.ButtonBid.configure(state="disabled")

				self.TextVar = tk.StringVar(value="Format: X.XX")
				self.Text = tk.ttk.Entry(self.top, textvariable=self.TextVar, font=("Helvetica",14))
				self.Text.place(relx=0.389, rely=0.83, relwidth=0.15, relheight=0.038)
				self.Text.configure(state="disabled")

				self.LabelInfo = tk.ttk.Label(self.top, text="Delivery company have already been assigned for this order", style='LabelTime.TLabel')
				self.LabelInfo.place(relx=0.335, rely=0.78, relwidth=0.4, relheight=0.04)


	def refresh(self):
		self.Canvas = tk.Canvas(self.top, bg="light blue")
		self.Canvas.place(relx=0, rely=0.4, relwidth=1, relheight=0.355)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=1, rely=0.4, relheight=0.355, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

	def make_bid(self):
		bidding_price = self.Text.get()

		# Check if biiding price enetered valid
		flag_price_invalid = False
		if len( bidding_price.split(".") ) == 2:
			if len(bidding_price.split(".")[1]) != 2: # We need the format $ X.XX e.g 3.03 3.16 3.00
				flag_price_invalid = True  
		else: # The user did not provide the cent part
			flag_price_invalid = True

		try: 
			bidding_price = float(bidding_price)
			if bidding_price < 0:
				flag_price_invalid = True
		except:
			flag_price_invalid = True


		if flag_price_invalid:
			tk.messagebox.showerror("Error", "Bidding price invalid")
		elif bidding_price > float(self.subtotal*0.3):
			tk.messagebox.showerror("Error", "Bidding price cannot greater than the 30 percent of the subtotal")
		else: 
			# write to bidding csv file
			df_bidding = pd.read_excel("csv_files/biddings.xlsx")
			status = 'bidding' # Status includes bidding, win, lose
			assigned_by = 'pending'
			assigned_on = 'pending'
			clerk_jutification = ''
			if len(df_bidding) == 0:
				Id = 0
				tempo = pd.DataFrame([[Id, self.tracking_order, self.name, self.username, bidding_price, status, assigned_by, assigned_on, clerk_jutification]], 
				columns=['Bidding ID', 'Bidding Tracking Order', 'Delivery Company Name','Delivery Company Email', 'Price Offered', 'Status', 'Assigned_by', 'Assigned_on', 'Clerk_justification'])
				df_bidding = df_bidding.append(tempo)

			else:
				Id = int(df_bidding['Bidding ID'].iloc[-1])
				Id = Id+1
				tempo = pd.DataFrame([[Id, self.tracking_order, self.name, self.username, bidding_price, status, assigned_by, assigned_on, clerk_jutification]], 
				columns=['Bidding ID', 'Bidding Tracking Order', 'Delivery Company Name','Delivery Company Email', 'Price Offered', 'Status', 'Assigned_by', 'Assigned_on', 'Clerk_justification'])
				df_bidding = df_bidding.append(tempo)

			df_bidding.to_excel("csv_files/biddings.xlsx", index=False)
			tk.messagebox.showinfo("Success", "Bidding Made!")

			# change the order status to 'bidding' in orders file
			df = pd.read_excel("csv_files/orders.xlsx")
			df['Order_Status'] = np.where((df['Tracking Order'] == self.tracking_order) & (df['Order_Status'] == 'processing'), 'bidding', df.Order_Status)
			df.to_excel("csv_files/orders.xlsx", index=False)
			# Disable buttons until the next selection, and update treeview
			self.check_bidding()
			self.update_treeview()


	def back(self):
		self.top.destroy()
		delivery_company_management_page.delivery_company_management_page(self.name, self.username) 

	def update_treeview(self):
		combo1 = self.Combo1.get()
		df = pd.read_excel("csv_files/orders.xlsx")
		if combo1 == 'Processing Order':
			df2 = df[df['Order_Status'] == 'processing']
		elif combo1 == 'Ongoing Bidding':
			df2 = df[df['Order_Status'] == 'bidding']
		else:
			df2 = df[df['Order_Status'].isin(['assigned', 'delivered'])]

		df3 = df2.sort_values(by='Tracking Order')
		df_order = df3[['Tracking Order', 'Username', 'Date order processed', 'Order_Status', 'Order_Id', 'Item_Name', 'Customized',
						'Item_Price', 'Home address', 'Delivery_Company_Assigned']]

		self.tree_frame = tk.Frame(self.top)
		self.tree_frame.place(relx=0.06, rely=0.15, relwidth=0.9, relheight=0.2)
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


	def check_bidding(self):
		# Check if delivery company has bidded already
		df_bidding = pd.read_excel( "csv_files/biddings.xlsx" )
		df_my_bidding = df_bidding[df_bidding['Delivery Company Email'] == self.username]
		if self.tracking_order in list(df_my_bidding['Bidding Tracking Order']):
			self.ButtonBid.configure(state="disabled")

			self.TextVar = tk.StringVar(value="Format: X.XX")
			self.Text = tk.ttk.Entry(self.top, textvariable=self.TextVar, font=("Helvetica",14))
			self.Text.place(relx=0.389, rely=0.83, relwidth=0.15, relheight=0.038)
			self.Text.configure(state="disabled")

			self.LabelInfo = tk.ttk.Label(self.top, text="You've already made the bid on this order", style='LabelTime.TLabel')
			self.LabelInfo.place(relx=0.365, rely=0.78, relwidth=0.4, relheight=0.04)
		else:
			self.ButtonBid.configure(state="normal")
			self.Text.configure(state="normal")
			self.LabelInfo = tk.ttk.Label(self.top, text="", style='LabelTime.TLabel')
			self.LabelInfo.place(relx=0.195, rely=0.78, relwidth=0.8, relheight=0.04)