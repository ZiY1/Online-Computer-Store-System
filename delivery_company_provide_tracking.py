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
import delivery_company_management_page

class delivery_company_provide_tracking(tk.Frame):

	def __init__(self, name, username, master=None): 
		tk.Frame.__init__(self, master)

		self.name = name
		self.username = username

		self.master.title("Delivery Company Provide Tracking Page")
		self.master.geometry("1590x955")
		self.master.configure( background = "light blue" )

		self.create_widgets()



	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

		# Titles
		self.style.configure("LabelTitle.TLabel", relief=tk.SUNKEN, anchor="center", font=("Helvetica", 17), background = "#49A")
		self.LabelTitle = tk.ttk.Label(self.top, text='Provide Tracking Information', style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.36, rely=0.015, relwidth=0.26, relheight=0.047)

		# Row 1
		self.style.configure("Label1.TLabel",anchor="w", font=("Helvetica",14), background = "light blue")
		self.Label1 = tk.ttk.Label(self.top, text="View:", style='Label1.TLabel')
		self.Label1.place(relx=0.35, rely=0.09, relwidth=0.13, relheight=0.026)

		# Waiting For Shpping means 'assigned', shipping means 'shipping', delivered means 'delivered' in tracking orders file(Delivery_status)
		self.Combo1List1 = ["Waiting For Shipping Orders","Shipping Orders", "Delivered Orders"]
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
		self.Canvas.place(relx=0, rely=0.4, relwidth=0.495, relheight=0.43)

		self.MyFrame = tk.Frame(self.Canvas, bg = "light blue")
		self.MyFrame.bind('<Configure>', lambda e: self.Canvas.configure(scrollregion=self.Canvas.bbox('all')))

		self.Canvas.create_window(0, 0, window=self.MyFrame)

		self.Scrolly = tk.Scrollbar(self.top, command=self.Canvas.yview)
		self.Scrolly.place(relx=0.495, rely=0.4, relheight=0.43, anchor='ne')
		self.Canvas.configure(yscrollcommand=self.Scrolly.set)

	def create_right_frame(self):
		# Delivery Details
		self.LabelHead2 = tk.ttk.Label(self.top, text="Delivery Details", style='LabelHead.TLabel')
		self.LabelHead2.place(relx=0.71, rely=0.355, relwidth=0.35, relheight=0.04)

		# Shipping Details Body
		self.Canvas2 = tk.Canvas(self.top, bg="light blue")
		self.Canvas2.place(relx=0.505, rely=0.4, relwidth=0.494, relheight=0.43)

		# self.MyFrame2 = tk.Frame(self.Canvas2, bg = "light blue")
		# self.MyFrame2.bind('<Configure>', lambda e: self.Canvas2.configure(scrollregion=self.Canvas2.bbox('all')))

		# self.Canvas2.create_window(0, 0, window=self.MyFrame2)

		# self.Scrolly2 = tk.Scrollbar(self.top, command=self.Canvas2.yview)
		# self.Scrolly2.place(relx=1, rely=0.4, relheight=0.385, anchor='ne')
		# self.Canvas2.configure(yscrollcommand=self.Scrolly2.set)

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
		df2 = df[df['Order_Status'] == "bidding"]
		df2 = df.sort_values(by='Tracking Order')
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
    
			image_tempo = image_tempo.resize((220,160), Image.ANTIALIAS)

			self.images.append(None)
			self.images[i] = ImageTk.PhotoImage( image_tempo )
			tk.ttk.Label( self.MyFrame, image = self.images[i], style="Label_imag.TLabel").grid(sticky="W", row=4+counter, column=1, padx=0, pady = 25, rowspan=3)
			counter = counter + 3

		tk.ttk.Label(self.MyFrame, text="Subtotal: " + "$ {:,.2f}".format(self.subtotal) ,style="LabelHeadline.TLabel").grid(sticky="W", row=5+len(self.order_ids)*3, column=0, padx=0, pady=20)


	def create_right_frame_content(self):
		# Fome bidding file, get all bidder of the selected tracking order number
		df = pd.read_excel("csv_files/biddings.xlsx")
		df_win = df[df['Status'] == 'win']
		df_bidder = df_win[df_win['Bidding Tracking Order'] == self.tracking_order] #only one row
		#print(df_bidder)
		df_bidder_list = df_bidder.to_numpy().tolist()
		# bidding_id = df_bidder_list[0][0]
		# bidder_name = df_bidder_list[0][2]
		# bidder_email = df_bidder_list[0][3]
		bidder_price = "$ {:,.2f}".format(df_bidder_list[0][4])
		assigned_on = df_bidder_list[0][7]

		df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
		df_row = df_tracking[df_tracking['Tracking Order Number'] == self.tracking_order]
		df_row_list = df_row.to_numpy().tolist()

		current_location = df_row_list[0][3]
		updated_time = df_row_list[0][4]
		if current_location == 'pending':
			current_location = 'Waiting For Shipping'
			updated_time = ''

		# Refresh
		self.create_right_frame()

		tk.ttk.Label(self.top, text="Tracking Order Number: " + self.tracking_order, style="LabelHeadline.TLabel").place(relx=0.51, rely=0.405, relwidth=0.35, relheight=0.04)
		tk.ttk.Label(self.top, text="My Price Offered: " + bidder_price ,style="LabelHeadline.TLabel").place(relx=0.51, rely=0.455, relwidth=0.35, relheight=0.04)
		tk.ttk.Label(self.top, text="Assigned On: " + assigned_on ,style="LabelHeadline.TLabel").place(relx=0.51, rely=0.505, relwidth=0.35, relheight=0.04)
		tk.ttk.Label(self.top, text="Current Package Location: " + current_location ,style="LabelHeadline.TLabel").place(relx=0.51, rely=0.555, relwidth=0.35, relheight=0.04)
		tk.ttk.Label(self.top, text="Updated On: " + updated_time ,style="LabelHeadline.TLabel").place(relx=0.51, rely=0.605, relwidth=0.35, relheight=0.04)

		# Display 3 buttons: started shipping, update delivery location, arrived

		# started shipping
		self.style.configure("Button2.TButton", font=("Helvetica", 14))
		self.ButtonStart = tk.ttk.Button(self.top, text="Started Shipping", command=self.start, style="Button2.TButton")
		self.ButtonStart.place(relx=0.51, rely=0.655, relwidth=0.15, relheight=0.042)

		self.LocationVar1 = tk.StringVar(value="Pleasr enter the initial package location")
		self.TextLocation1 =  tk.Entry(self.top, textvariable = self.LocationVar1 ) 
		self.TextLocation1.place( relx=0.7, rely=0.658, relwidth=0.2, relheight=0.035 )

        # update delivery location
		self.ButtonShipping = tk.ttk.Button(self.top, text="Update Delivery Location", command=self.shipping, style="Button2.TButton")
		self.ButtonShipping.place(relx=0.51, rely=0.715, relwidth=0.15, relheight=0.042)

		self.LocationVar2 = tk.StringVar(value="Pleasr enter the current package location")
		self.TextLocation2 =  tk.Entry(self.top, textvariable = self.LocationVar2 ) 
		self.TextLocation2.place( relx=0.7, rely=0.718, relwidth=0.2, relheight=0.035 )

		# arrived
		self.ButtonArrive = tk.ttk.Button(self.top, text="Arrived", command=self.arrive, style="Button2.TButton")
		self.ButtonArrive.place(relx=0.51, rely=0.775, relwidth=0.15, relheight=0.042)

		combo1 = self.Combo1.get()
		if combo1 == 'Waiting For Shipping Orders':
			self.ButtonStart.configure(state='normal')
			self.TextLocation1.configure(state='normal')
			self.ButtonShipping.configure(state='disabled')
			self.TextLocation2.configure(state='disabled')
			self.ButtonArrive.configure(state='disabled')

		elif combo1 == 'Shipping Orders':
			self.ButtonStart.configure(state='disabled')
			self.TextLocation1.configure(state='disabled')
			self.ButtonShipping.configure(state='normal')
			self.TextLocation2.configure(state='normal')
			self.ButtonArrive.configure(state='normal')

		else:
			self.ButtonStart.configure(state='disabled')
			self.TextLocation1.configure(state='disabled')
			self.ButtonShipping.configure(state='disabled')
			self.TextLocation2.configure(state='disabled')
			self.ButtonArrive.configure(state='disabled')


	def refresh(self):
		self.create_left_frame()
		self.create_right_frame()

	def back(self):
		self.top.destroy()
		delivery_company_management_page.delivery_company_management_page(self.name, self.username) #self.name, self.username

	def update_treeview(self):
		combo1 = self.Combo1.get()
		# Get all the assigned orders in orders file
		df = pd.read_excel("csv_files/orders.xlsx")
		df_order = df[df['Order_Status'].isin(['assigned', 'delivered'])]
		# Get all the wining bidding for this delivery company
		df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
		df_delivery = df_tracking[df_tracking['Delivery Company Assigned Email'] == self.username]

		# if len(df_delivery) == 0:
		# 	tk.messagebox.showinfo("Notice", "You don't have any wining delivry order at this time")

		if combo1 == 'Waiting For Shipping Orders':
			df_tracking_status = df_delivery[df_delivery['Delivery_status'] == 'assigned']
		elif combo1 == 'Shipping Orders':
			df_tracking_status = df_delivery[df_delivery['Delivery_status'] == 'shipping']
		else: # combo1 == 'Delivered Orders'
			df_tracking_status = df_delivery[df_delivery['Delivery_status'] == 'delivered']
			
		df2 = df_order[df_order['Tracking Order'].isin(list(df_tracking_status['Tracking Order Number']))]
		

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

	def start(self):
		# Get the current time
		now = datetime.datetime.now()
		my_datetime = now.strftime("%y-%m-%d %H:%M")

		# Get the entered location
		initial_location = self.TextLocation1.get()
		if initial_location.strip() == '':
			tk.messagebox.showerror("Error","Location cannot be empty")
		else:
			answer = askyesno(title='Confirm?', message='Please double check the address entered. \n\nConfirm?')
			if answer:
				# update file
				df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
				df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Current_Location'] = initial_location
				df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Updated_time'] = my_datetime
				df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Delivery_status'] = 'shipping'

				df_tracking.to_excel("csv_files/tracking_orders.xlsx", index=False)
				tk.messagebox.showinfo("Success","Update tracking information success")

				self.update_treeview()
				self.refresh()


	def shipping(self):
		# Get the current time
		now = datetime.datetime.now()
		my_datetime = now.strftime("%y-%m-%d %H:%M")

		# Get the entered location
		current_location = self.TextLocation2.get()
		if current_location.strip() == '':
			tk.messagebox.showerror("Error","Location cannot be empty")
		else:
			answer = askyesno(title='Confirm?', message='Please double check the address entered. \n\nConfirm?')
			if answer:
				# update file
				df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
				df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Current_Location'] = current_location
				df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Updated_time'] = my_datetime

				df_tracking.to_excel("csv_files/tracking_orders.xlsx", index=False)
				tk.messagebox.showinfo("Success","Update tracking information success")

				self.update_treeview()
				self.refresh()

	def arrive(self):
		# Get the current time
		now = datetime.datetime.now()
		my_datetime = now.strftime("%y-%m-%d %H:%M")
		
		answer = askyesno(title='Confirm?', message='Please double check the package is arrived. \n\nConfirm?')
		if answer:
			# update file
			df_tracking = pd.read_excel("csv_files/tracking_orders.xlsx")
			df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Current_Location'] = self.home_address
			df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Updated_time'] = my_datetime
			df_tracking.loc[df_tracking['Tracking Order Number'] == self.tracking_order, 'Delivery_status'] = 'delivered'

			df_order = pd.read_excel("csv_files/orders.xlsx")
			df_order['Order_Status'] = np.where((df_order['Tracking Order'] == self.tracking_order) & (df_order['Order_Status'] == 'assigned'), 'delivered', df_order.Order_Status)


			df_tracking.to_excel("csv_files/tracking_orders.xlsx", index=False)
			df_order.to_excel("csv_files/orders.xlsx", index=False)
			tk.messagebox.showinfo("Success","Update tracking information success")

			self.update_treeview()
			self.refresh()