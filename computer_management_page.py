import tkinter as tk 
import tkinter.ttk as ttk


# python files
import main as home

class computer_management_page(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.master.title("Computer Management Page")
		self.master.geometry( "1350x676")
		self.create_widgets()

	def create_widgets(self):
		self.top = self.winfo_toplevel()
		self.style = tk.ttk.Style()
