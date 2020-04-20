import matplotlib.pyplot as plt

import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise'])
print("Total Confirmed Cases: "+str(covid19_df[covid19_df.state == "Total"]['confirmed']))
print("Total Active Cases: "+str(covid19_df[covid19_df.state == "Total"]['active']))
print("Total Recovered Cases: "+str(covid19_df[covid19_df.state == "Total"]['recovered']))
print("Total Deceased Cases: "+str(covid19_df[covid19_df.state == "Total"]['deaths']))
print(covid19_df[['state','confirmed','active','recovered','deaths']].sort_values(by="confirmed", ascending=False))