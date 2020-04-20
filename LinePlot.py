''' Line Plot- Death And Recovered '''



import matplotlib.pyplot as plt 
import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise'])
covid19_dfnew=covid19_df.drop(covid19_df.index[[0]])
plt.figure(figsize = (12, 7))
statecode=covid19_dfnew['statecode']
recovered=covid19_dfnew['recovered']
deaths=covid19_dfnew['deaths']
plt.plot(statecode, recovered, label='covid-19')
plt.plot(statecode, deaths, label='covid-19')