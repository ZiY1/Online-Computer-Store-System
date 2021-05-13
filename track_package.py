import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import requests
import json
import io
from tkinter.messagebox import *
from PIL import ImageTk, Image
from smartystreets import Client

# python script
import customer_page
import setting_account

class track_package(tk.Frame):

	def __init__(self, customer_name, customer_Id, customer_username, master=None):
		tk.Frame.__init__(self, master)
		self.master.title("Package Status")
		self.master.geometry("1350x676")
		self.master.configure(background="light blue")

		# User account info
		self.customer_name = customer_name
		self.customer_username = customer_username
		self.customer_Id = customer_Id
		
		self.create_widgets()

	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

     	# ---------------------------------Title----------------------------------------

		self.style.configure("LabelTitle.TLabel", anchor="N", font=("Helvetica", 23), background='#49A', foreground="black")
		self.LabelTitle = tk.ttk.Label(self.top, text="Package Status", style="LabelTitle.TLabel")
		self.LabelTitle.place(relx=0.25, rely=0.100, relwidth=0.572, relheight=0.095)

		# ---------------------------------Drop-down menu of tracking orders----------------------------------------

		self.style.configure("Combo.Label", font=("Helvetica", 12), background='#add8e6', foreground = "black")
		self.label = tk.ttk.Label(self.top, text = "Select a date of purchase and tracking number", style="Combo.Label")
		self.label.place(relx=0.35, rely=0.21)

		self.comboValues = self.verify_orders()
		self.TrackNumCombo = tk.ttk.Combobox(self.top, state="readonly", values=self.comboValues, font=("Helvetica",14))
		self.TrackNumCombo.bind("<<ComboboxSelected>>", self.combo_clicked)
		self.TrackNumCombo.place(relx=0.35, rely=0.24, relwidth=0.35, relheight=0.032)
		self.TrackNumCombo.set("Select a date of purchase and tracking number")

		# ---------------------------Go Back Button---------------------------------------

		self.style.configure("Command_Go_Back.TButton", font=("Helvetica", 16), background="green",   foreground="black")
		self.CommandExit = tk.ttk.Button(self.top, text="Go Back", command=self.Command_Go_Back, style="Command_Go_Back.TButton")
		self.CommandExit.place(relx=0.873, rely=0.88, relwidth=0.119, relheight=0.065)

		#-----------------------------------------------------------
	
	# Get a list of unique tracking orders of the user
	def verify_orders(self):
		df = pd.read_excel("csv_files/orders.xlsx")
		df = df[df['Username'] == self.customer_username]
		df = df.loc[df['Order_Status'] == 'assigned']
		df = df[['Date order processed', 'Tracking Order']]
		df = df.drop_duplicates()
		trackNum = df.values.tolist()
		if len(trackNum) == 0:
			tk.messagebox.showinfo("Info", "Please check purchase history for this order status")
			return
		else:
			return trackNum
		
	# Display tracking information if event is fired
	def combo_clicked(self, event):
		trackInfo = self.TrackNumCombo.get()
		
		# Date of purchased
		date1 = trackInfo.partition('}')[0]
		date = date1.replace('{','').replace('}','')
		
		# Tracking number
		trackNum1 = trackInfo.partition('}')[-1]
		trackNum = trackNum1.replace(' ', '')
		
		# Verify tracking status and information
		newdf = pd.read_excel("csv_files/tracking_orders.xlsx")
		newdf = newdf[newdf['Tracking Order Number'] == trackNum]
		newdf = newdf.loc[newdf['Delivery_status'] == 'shipping']
		if len(newdf) == 0:
			tk.messagebox.showinfo("Info", "Waiting for delivery company confirmation."\
				" Please check purchase history for more information.")
			return
		else:
			delivery_address = newdf['Current_Location'].iloc[-1]
			delivery_company = newdf['Delivery Company Assigned Name'].iloc[-1]
			delivery_email = newdf['Delivery Company Assigned Email'].iloc[-1]

		# Customer's address
		df = pd.read_excel("csv_files/registered_customers.xlsx")
		customer_info = df[df['Username'] == self.customer_username]
		customer_address = customer_info['Home Address'].iloc[-1]

		self.Fetch_Data(trackNum, customer_address, delivery_address, delivery_company, delivery_email, date)
		
	
	# Fetch the static map of the route between two address
	def Fetch_Static_Map(self, api, delivery, customer):
		api_url_map = "https://www.mapquestapi.com/staticmap/v5/map"
		params = {'key': api,
				'start': delivery,
				'end': customer}

		try: 
			static_map = requests.get(api_url_map, params=params, headers={"content-type": "image/png"})
			if static_map.status_code == 200:
				s_map = io.BytesIO(static_map.content)
				self.tracking_map = ImageTk.PhotoImage(Image.open(s_map))
				self.map_image = tk.Label( image = self.tracking_map)
				self.map_image.image = self.tracking_map
				self.map_image.place( x = 150, y = 195)
		except Exception as e:
			tk.messagebox.showerror("Error: ", e)

	# MAPQUEST api: fetch route
	def Fetch_Data(self, tracking_number, customer_address, delivery_address, delivery_company, delivery_email, dates):
		api_url_direction = "http://www.mapquestapi.com/directions/v2/route"
		api_key = "sI6vhp36vLAPPlC3hKEWgAI1aj2efRAC"

		params = {'key': api_key,
				'from': delivery_address,
				'to': customer_address}
		try: 
			r = requests.get(api_url_direction, params=params)
			if r.status_code == 200:
				response = r.json()
				distance = round((response["route"]["distance"]),2)		# default unit: miles
				time = round(((response["route"]["time"])/60), 2)		# default unit: seconds
				self.style.configure( "LabelTitle.TLabel", 
									anchor = "left", 
									font = ("Helvetica", 18, 'bold'), 
									background = '#49A')
				message = "Purchased on: " + str(dates) + "\n"\
						"Tracking number: " + str(tracking_number) +"\n\n"\
						"Please allow additional time for loading packages\nand order processing.\n\n"\
						"Delivery company: " + str(delivery_company) + "\n"\
						"Delivery company Email: " + str(delivery_email) + "\n\n"\
						"Current whereabout: " + str(delivery_address) + "\n"\
						"Distance: " + str(distance) + " miles \nDriving Time: " + str(time) + " minutes"
				self.LabelTitle = tk.ttk.Label(self.top, 
						text = message, 
						style = "LabelTitle.TLabel")
				self.LabelTitle.place( relx = 0.46, rely = 0.300, relwidth = 0.5, relheight = 0.57)
				self.Fetch_Static_Map(api_key, delivery_address, customer_address)
		except Exception as e:
			err_message = str(response["info"]["messages"]).replace('[', '').replace(']', '').replace('\'', '')
			tk.messagebox.showerror("Error", err_message)

	# Validate address - pass in address
	# This method only validates USA addresses
	# smartystreets api
	def validate_addr(self, address):
		AUTH_ID = "895de920-0f01-34e3-db12-a2b039ce11b7"
		AUTH_TOKEN = "2DMF7uiZczEX2wIhMF0o"
		client = Client(AUTH_ID, AUTH_TOKEN)
		try:
			addresss = client.street_address(address)
			if addresss.confirmed == True:
				return addresss.confirmed
		except Exception as e:
			return False
			#k.messagebox.showerror("Error", "Please re-enter a valid USA address")


	def Command_Go_Back(self):
		self.top.destroy()
		setting_account.setting_account(customer_name=self.customer_name,
        customer_username=self.customer_username, customer_Id=self.customer_Id)
