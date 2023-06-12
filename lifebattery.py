import pandas as pd
import time
from datetime import datetime, date



    
def open_who_data(): 
  stats_path = './files/who_data.csv'
  with open(stats_path, 'r') as file:
        who_data = file.read()
        df = pd.read_csv(who_data)
        df = df[df["Unnamed: 1"] == "2019"] 
        return df
      

who_df = open_who_data()      





    
