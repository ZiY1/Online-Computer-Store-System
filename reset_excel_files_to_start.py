import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

''' We need to empty those files
1) registered_customers
2) suspend_users
3) emails
4) orders
5) complaints
6) discussion_reports
7) discussions
8) biddings
9) tracking_orders
'''

def empty_df(df, directory):

    df_tempo = pd.DataFrame( columns = df.columns)
    df_tempo.to_excel(directory, index = False)

files = [   "registered_customers", "suspend_users", "emails", "orders",
            "complaints", "discussion_reports", "discussions", "biddings",
            "tracking_orders" ]

df_customers = pd.read_excel("csv_files/registered_customers.xlsx")

for file in files:
    df_ = pd.read_excel( f"csv_files/{file}.xlsx" )
    empty_df( df = df_, directory = f"csv_files/{file}.xlsx" )


'''We need to modify but not empty them specially the item file
1) items
2) privileged_users
'''
df_items = pd.read_excel("csv_files/items.xlsx")
df_staffs = pd.read_excel("csv_files/privileged_users.xlsx")

df_items["Number of Sales"] = 0
df_items["overall review"] = 0 
df_items.to_excel("csv_files/items.xlsx", index  = False)



#tempo_df2 = df_staffs[ df_staffs["Type_user"] == "Super user"] 
tempo_df2 = df_staffs.iloc[0:11] # gather the default privileged users
tempo_df2['Income'] = 0.00  # reset their income 
tempo_df2['Status'] = 'active' # reset their status
tempo_df2['Warnings'] = 0 # reset their warnings
tempo_df2.to_excel("csv_files/privileged_users.xlsx",index = False)

