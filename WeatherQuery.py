
# coding: utf-8
#1. This is a mini program to query weather forecast data from Central Weather Bureau API and use plotly to visualize the data


#import numpy as np
#import json
#import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

#plotly username and plotly
plotly.tools.set_credentials_file(username='your_username', api_key='your_api_key')

#CWB api key
url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=your_api_key'
pdata=pd.read_json(url)

#nameindex is used to convert cityname to the index in json data from CWB API
nameindex=[]
for j in range(0,21):
    nameindex.append(pdata.records.locations[0]['location'][j]['locationName'])

#use cityname to query index(which cityname include '台' must use '臺' to substitute.
#Cityname can only use Traditional Chinese to Query currently. English Query may upload in a short period
def query(city):
    for i in range(0,21):
        if city==nameindex[i]:
            return i
        else:
            continue
    print('The cityname is incorrect, showing Taipei City forecast data substitute')
    return 9

#Let user to enter cityname and convert to the index
p=input('Please enter the cityname that you want to query')
pp=query(p)

#Use CWB_API to Query data
date=[]
htemp=[]
ltemp=[]
weather=[]
for i in range(0,14):
    date.append(pdata.records.locations[0]['location'][pp]['weatherElement'][1]['time'][i]['endTime'])
    htemp.append(pdata.records.locations[0]['location'][pp]['weatherElement'][12]['time'][i]['elementValue'][0]['value'])
    ltemp.append(pdata.records.locations[0]['location'][pp]['weatherElement'][8]['time'][i]['elementValue'][0]['value'])
    weather.append(pdata.records.locations[0]['location'][pp]['weatherElement'][6]['time'][i]['elementValue'][0]['value'])

#constructing traces
trace1=go.Scatter(
    x=date,
    y=htemp,
    mode='lines+markers',
    name='高溫',
    marker=dict(
        color='red'
    )
)
trace2=go.Scatter(
    x=date,
    y=ltemp,
    mode='lines+markers',
    name='低溫',
    marker=dict(
        color='blue'
    )
)

#conbine data and output the figure
data=[trace1,trace2]
py.iplot(data,filename='basic_line')

