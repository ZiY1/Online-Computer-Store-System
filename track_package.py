import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import requests
import json
import io
from PIL import ImageTk, Image

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
		self.Fetch_Data()

	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()

     	# ---------------------------------Title----------------------------------------

		self.style.configure(
                            "LabelTitle.TLabel",
                            anchor="N",
                            font=("Helvetica", 23),
                            background='#49A',
                            foreground="black"
                     )
		self.LabelTitle = tk.ttk.Label(self.top,
                                      text="Package Status",
                                      style="LabelTitle.TLabel"
                                    )
		self.LabelTitle.place(relx=0.25, rely=0.100, relwidth=0.572, relheight=0.095)
		# ---------------------------Go Back Button---------------------------------------

		self.style.configure("Command_Go_Back.TButton", font=("Helvetica", 16),
                                background="green",   foreground="black")
		self.CommandExit = tk.ttk.Button(
			self.top,
			text="Go Back",
			command=self.Command_Go_Back,
			style="Command_Go_Back.TButton")

		self.CommandExit.place(relx=0.873, rely=0.88,
		                       relwidth=0.119, relheight=0.065)

		#-----------------------------------------------------------
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
				self.map_image.place( x = 150, y = 180)
			else:
				print("Static_map: " + str(status_code))
				# Will need to change to a pop-up window
		except Exception as e:
			print(e)
			# Will need to change to a pop-up window

	def Fetch_Data(self):
		api_url_direction = "http://www.mapquestapi.com/directions/v2/route"
		api_key = "sI6vhp36vLAPPlC3hKEWgAI1aj2efRAC"

		delivery_name = "FedEx" # Clerk needs to assign a delivery company

		# Get customer's address
		df = pd.read_excel("csv_files/registered_customers.xlsx")
		customer_info = df[df['Username'] == self.customer_username]
		customer_address = customer_info['Address'].iloc[-1]

		# Get delivery company's address
		df = pd.read_excel('csv_files/privileged_users.xlsx')
		delivery_info = df[df['Name'] == delivery_name]
		delivery_address = delivery_info['Address'].iloc[-1]

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
									font = ("Helvetica", 18), 
									background = '#49A')
				self.LabelTitle = tk.ttk.Label(self.top, 
						text = "Order Number: \n\nDistance: " + str(distance) + "miles \nTime: " + str(time) + " minutes", 
						style = "LabelTitle.TLabel")
				self.LabelTitle.place( relx = 0.55, rely = 0.400, relwidth = 0.300, relheight = 0.300)
				self.Fetch_Static_Map(api_key, delivery_address, customer_address)
			else:
				print("Fetch_Data: " + str(status_code))
				# Will need to change to a pop-up window
		except Exception as e:
			print("Fetch_Data: Please check your internet connection.")
			# Will need to change to a pop-up window


	def Command_Go_Back(self):
		self.top.destroy()
		setting_account.setting_account(customer_name=self.customer_name,
        customer_username=self.customer_username, customer_Id=self.customer_Id)
