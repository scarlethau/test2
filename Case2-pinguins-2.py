#!/usr/bin/env python
# coding: utf-8

# # Blogpost case team 10

# In[66]:


#GROUPMEMBERS
#Yswar Gokoel     (500786750)
#Billy Uzel       (500828005)
#Scarlet Hau      (500817271)
#Daan Bouwmeester (500826025)


# # Schiphol API

# In[67]:


import pandas as pd
import requests
import json


# In[68]:


i = 0 
data = []
for i in range(5) :
    
    url = "https://api.schiphol.nl/public-flights/flights?includedelays=false&page=" + str(i) + "&sort=%2BscheduleTime&fromDateTime=2020-12-01T00%3A00%3A00&toDateTime=2020-12-03T00%3A00%3A00&searchDateTimeField=estimatedLandingTime"
    i = i + 1
     
    r = requests.get(url)
    headers = headers = {
      'accept': 'application/json',
	  'resourceversion': 'v4',
      'app_id': '6ec7ae49',
	  'app_key': '0b7a8784dc9b7bd1e7b12d927ff3fab9'}
    response = requests.request('GET', url, headers=headers)
    datatxt = response.text
    dataspl = json.loads(datatxt)
    data = response.json()


# In[69]:


df = pd.DataFrame.from_dict(data['flights'], orient='columns')


# In[70]:


df.head()


# In[71]:


df['aircraftType']


# In[72]:


part1 = pd.DataFrame(dataspl)


# In[73]:


part1.head()


# # Penguins dataset

# ### Importing data and packages

# In[90]:



import matplotlib.pyplot as plt
get_ipython().system('pip install plotly==5.3.1')
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[75]:


#Dataset afkomstig van Datacamp
penguins = pd.read_csv('penguins.csv')


# ### Inspecting data

# In[76]:


penguins.head()


# In[77]:


penguins.info()


# In[78]:


penguins.nunique()


# In[88]:


penguins['Island'].value_counts(normalize = True).sort_index()


# In[94]:


penguins['Sex'].value_counts(normalize = True).sort_index()


# In[80]:


#penguins.dropna(inplace=True)
#penguins.info()


# In[81]:


penguins.describe()


# #### Conclusion of data inspection

# ### Analyzing data true visuals

# #### Culmen ratio

# In[98]:


penguins['CulmenRatio'] = penguins['Culmen Length (mm)'] / penguins['Culmen Depth (mm)']


# In[99]:


penguins['CulmenRatio'].mean()


# In[100]:


fig, axes = plt.subplots()
sns.boxplot(x="Island", y="CulmenRatio", data=penguins).set(title="Relation between CulmenRatio and Island")


# #### Correlation in a heatmap

# In[86]:


penguins[["Body Mass (g)", "Culmen Length (mm)", 'Culmen Depth (mm)', 'Flipper Length (mm)']].corr()


# In[93]:


sns.heatmap(penguins[["Body Mass (g)", "Culmen Length (mm)", 'Culmen Depth (mm)', 'Flipper Length (mm)']].corr(), annot=True, cmap = 'Greens')
plt.show()


# #### Slider

# In[107]:


fig = go.Figure()
for island in ['Torgersen', 'Biscoe', 'Dream']:
    df = penguins[penguins.Island == island]
    fig.add_trace(go.Scatter(
        x=df["Culmen Length (mm)"],
        y=df["Culmen Depth (mm)"],
        mode='markers',
        name=island))

    
sliders = [
    {'steps':[
    {'method': 'update', 'label': 'Torgensen', 'args': [{'visible': [True, False, False]}]},
    {'method': 'update', 'label': 'Biscoe', 'args': [{'visible': [False, True, False]}]},
    {'method': 'update', 'label': 'Dream', 'args': [{'visible': [False, False, True]}]}]}]
fig.data[0].visible=False
fig.data[1].visible=False
fig.update_layout({'sliders': sliders},
                   xaxis_title='Culmen Length (mm)',
                   yaxis_title="Culmen Depth (mm)",
                   title = 'Relation between culmen length and depth')
fig.show()


# #### Dropdown menu

# In[83]:


fig = go.Figure()
for island in ['Torgensen', 'Biscoe', 'Dream']:    
    df = penguins[penguins.Island == island]    
    fig.add_trace(go.Scatter(
        x=df["Culmen Length (mm)"], 
        y=df["Culmen Depth (mm)"],
        mode='markers',
        name=island))
    
dropdown_buttons = [  
    {'label': 'Torgensen', 'method': 'update',
     'args': [{'visible': [True, False, False]},           
        {'title': 'Torgensen'}]},  
    {'label': 'Biscoe', 'method': 'update',
     'args': [{'visible': [False, True, False]},          
        {'title': 'Biscoe'}]},  
    {'label': "Dream", 'method': "update",
     'args': [{"visible": [False, False, True]},          
        {'title': 'Dream'}]}]


fig.update_layout({
    'updatemenus':[{
        'type': "dropdown",
        'x': 1.3,'y': 0.5,
        'showactive': True,
        'active': 0,
        'buttons': dropdown_buttons}]})

fig.show()


# #### Checkboxes

# In[84]:


fig = px.scatter(data_frame=penguins, x='Species', y='Flipper Length (mm)', color='Species')

my_buttons = [{'label': "Scatterplot", 'method': "update", 'args': [{"type": 'scatter'}]},
  {'label': "Boxplot", 'method': "update", 'args': [{"type": 'box', 'mode': 'markers'}]}]

fig.update_layout({
    'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]})
fig.show()


# #### Relation between weight and flipperlength

# In[85]:


fig = px.scatter(data_frame=penguins,
                x='Body Mass (g)',
                y='Flipper Length (mm)',
                color='Species',
                trendline='ols',
                labels={'species':'Pinguïnsoort', 'body_mass_g':'Gewicht in gram (g)', 'flipper_length_mm':'Vleugel lengte in milimeter (mm)'}, 
                height=600,
                width=1000, 
                title='Relatie tussen gewicht en vleugel grootte per pinguïnsoort')
                
fig.show()


# #### Conclusion of data analysis

# ### Predictive model
