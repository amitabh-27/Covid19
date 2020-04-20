''' Visualize By Pie-Chart
State wise total confirm percentage '''


import matplotlib.pyplot as plt 
import requests 
from pandas.io.json import json_normalize 
URL = "https://api.covid19india.org/data.json" 
data = requests.get(url=URL).json() 
covid19_df = json_normalize(data['statewise']) 
T='This graph is showing which States of india is affected by what percentage' 
labels=covid19_df['state'][covid19_df["state"]!='Total']  
fig = plt.figure(figsize=(26,25))  
size=covid19_df['confirmed'][covid19_df["state"]!='Total'] 
plt.pie(size, labels=labels, autopct='%1.1f%%',shadow=True,startangle=43) 
plt.legend(labels, loc="best",shadow=True) 
plt.axis('equal') 
plt.title(T,bbox={'facecolor':'0.6', 'pad':10}) 
plt.show()