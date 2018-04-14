
# coding: utf-8

# In[1]:


#1. 這是一個利用中央氣象局API查詢天氣預報資訊，並將其利用plotly等資料視覺化套件呈現出來的小程式

#-- coding:utf-8 -
#import numpy as np
#import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
#import json
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#plotly的授權
plotly.tools.set_credentials_file(username='MilkyWay', api_key='aIM09UL0mIrMkoSvrpMY')

url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
pdata=pd.read_json(url)

#nameindex是縣市對照index的一維串列
nameindex=[]
for j in range(0,21):
    nameindex.append(pdata.records.locations[0]['location'][j]['locationName'])

#依城市名稱查詢編號(含臺字的縣市要使用繁體的臺)
def query(city):
    for i in range(0,21):
        if city==nameindex[i]:
            return i
        else:
            continue
    print('您查詢的城市名稱錯誤，預設顯示臺北市的預報')
    return 9

#讓使用者輸入要查詢的城市，並轉換成編號
p=input('請輸入您要查詢的縣市')
pp=query(p)

#使用氣象局api查詢所需的資料
date=[]
htemp=[]
ltemp=[]
weather=[]
for i in range(0,14):
    date.append(pdata.records.locations[0]['location'][pp]['weatherElement'][1]['time'][i]['endTime'])
    htemp.append(pdata.records.locations[0]['location'][pp]['weatherElement'][12]['time'][i]['elementValue'][0]['value'])
    ltemp.append(pdata.records.locations[0]['location'][pp]['weatherElement'][8]['time'][i]['elementValue'][0]['value'])
    weather.append(pdata.records.locations[0]['location'][pp]['weatherElement'][6]['time'][i]['elementValue'][0]['value'])

#製作軌跡
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

#合併資料並繪圖
data=[trace1,trace2]
py.iplot(data,filename='basic_line')

