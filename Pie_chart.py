import matplotlib.pyplot as plt 
import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise']) 
active=covid19_df['active'][0]
confirmed=covid19_df['confirmed'][0]
deltaconfirmed=covid19_df['deltaconfirmed'][0]
deaths=covid19_df['deaths'][0]
deltadeaths=covid19_df['deltadeaths'][0]
recovered=covid19_df['recovered'][0]
deltarecovered=covid19_df['deltarecovered'][0]


labels=['death','Deltadeaths','Recoverd','TotalRecovered']
sizes=[deaths,deltadeaths,recovered,deltarecovered]
explode=[0.2,0.3,0,0]
colors = ['orange','red','lightblue','pink']
plt.figure(figsize = (10, 7))
plt.pie(sizes,labels=labels,colors=colors,shadow='true',autopct='%1.1f%%',explode=explode,startangle=90)