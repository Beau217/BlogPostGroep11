#!/usr/bin/env python
# coding: utf-8

# # Import packages
# 
# 

# In[2]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st


# # Load data 

# In[3]:


##https://www.kaggle.com/arjunprasadsarkhel/2021-olympics-in-tokyo
athletes = pd.read_excel('Athletes.xlsx')
coaches = pd.read_excel('Coaches.xlsx')
entries_gender = pd.read_excel('EntriesGender.xlsx')
medals = pd.read_excel('Medals.xlsx')
teams = pd.read_excel('Teams.xlsx')


# # Barplot with dropdown
# 

# In[4]:


fig = go.Figure()
for medal in ['Gold','Silver', 'Bronze']:
    fig.add_trace(go.Bar(x = medals['Team/NOC'], y = medals[medal]))
dropdown_buttons = [
    {'label':'Gold medals','method':'update', 'args':[{'visible':[True, False, False]},{'title':'Gold medals'}]},
    {'label':'Silver medals', 'method':'update','args':[{'visible':[False,True,False]},{'title': 'Silver medals'}]},
    {'label':'Bronze medals', 'method':'update','args':[{'visible':[False,False,True]},{'title': 'Bronze medals'}]}]
fig.update_layout({'updatemenus':[{'type':'dropdown','x':1.3, 'y':0.5, 'showactive':True, 'active':0, 
                                   'buttons': dropdown_buttons}]})

st.plotly_chart(fig)


# # Histogram 

# In[ ]:


fig = px.histogram(athletes,title="Number of participants per discipline", x="Discipline", 
                   color='Discipline',animation_frame="NOC", 
                   animation_group="Discipline").update_xaxes(categoryorder='total descending')
fig.update_layout(height=800, width=1000, bargap=0.1, bargroupgap=0.1, xaxis = dict(
tickfont = dict(size=13)),yaxis = dict(
tickfont = dict(size=13)))
fig["layout"].pop("updatemenus")
st.plotly_chart(fig)


# In[ ]:





# In[ ]:


fig = px.histogram(athletes, x='Discipline', color='Discipline', labels={'x':'total_bill', 'y':'count'})



fig.update_layout(title='Discipline', title_x=0.5)
st.plotly_chart(fig)


# In[ ]:


coaches_NOC = coaches.groupby('NOC')['Discipline'].count()


# In[ ]:





# In[ ]:


#Figuur maken
fig = go.Figure(data=go.Choropleth(
locations = coaches_NOC.keys(),
locationmode = 'country names',
z = coaches_NOC,
text = coaches_NOC.keys(),
colorscale = 'viridis',
autocolorscale=False,
reversescale=True,
marker_line_color='darkgray',
marker_line_width=0.5,
colorbar_title = 'Disciplines',
))#Het figuur een titel geven en de grootte aanpassen
fig.update_layout(title = 'The amount of Coaches every country participated in ', title_x = 0.5,)
st.plotly_chart(fig)



# In[ ]:





# In[ ]:


#Maak een kopie van de dataframe
teams_temp = teams.copy()


# In[ ]:


#verwijder rijen met dezelfde Discipline en NOC
teams_data = teams_temp.drop_duplicates(subset=['Discipline', 'NOC'])


# In[ ]:


#Groepeer per disicipline de NOC en tel die bij elkaar op
teams_Dis_Noc = teams_data.groupby('Discipline')['NOC'].count()


# In[ ]:


#Figuur maken
fig = px.bar(teams_Dis_Noc)



#Een titel en yas label toevoegen
fig.update_layout(title = 'The amount of countries participating in each Discipline', title_x = 0.5,
yaxis_title = 'Countries', showlegend=False
)
st.plotly_chart(fig)


# In[ ]:


#Groepeer per NOC de Discipline en tel die bij elkaar op
teams_Noc_Dis = teams_data.groupby('NOC')['Discipline'].count()


# In[ ]:


#Figuur maken
fig = go.Figure(data=go.Choropleth(
locations = teams_Noc_Dis.keys(),
locationmode = 'country names',
z = teams_Noc_Dis,
text = teams_Noc_Dis.keys(),
colorscale = 'viridis',
autocolorscale=False,
reversescale=True,
marker_line_color='darkgray',
marker_line_width=0.5,
colorbar_title = 'Disciplines',
))#Het figuur een titel geven en de grootte aanpassen
fig.update_layout(title = 'The amount of Disciplines every country participated in ', title_x = 0.5,
)
st.plotly_chart(fig)


# In[ ]:





# In[ ]:





# In[ ]:


st.title('Medals')
check = st.checkbox('Total medals')
if check:
    fig = px.pie(medals, values = 'Total', names = 'Team/NOC', title = 'Total of medals for every country')
    fig.update_traces(textposition = 'inside', textinfo = 'percent+label' )
    st.plotly_chart(fig)

check2 = st.checkbox('Gold medals')
if check2:
    fig = px.pie(medals, values = 'Gold', names = 'Team/NOC', title = 'Gold of medals for every country')
    fig.update_traces(textposition = 'inside', textinfo = 'percent+label' )
    st.plotly_chart(fig)
          
check3 = st.checkbox('Silver medals')
if check3:
    fig = px.pie(medals, values = 'Silver', names = 'Team/NOC', title = 'Silver of medals for every country')
    fig.update_traces(textposition = 'inside', textinfo = 'percent+label' )
    st.plotly_chart(fig)
    
check4 = st.checkbox('Bronze medals')
if check4:
    fig = px.pie(medals, values = 'Total', names = 'Team/NOC', title = 'Bronze of medals for every country')
    fig.update_traces(textposition = 'inside', textinfo = 'percent+label' )
    st.plotly_chart(fig)

