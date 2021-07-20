#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:07:29 2020

@author: edyta
"""
import folium
from folium.plugins import MarkerCluster

import pandas as pd
import urllib.request, json 
with urllib.request.urlopen("http://gbfs.urbansharing.com/bergenbysykkel.no/station_information.json") as url:
    data = json.loads(url.read().decode())
    
lon = []
lat = []
bysykkel= []
capacity = []
for item in data["data"]["stations"]:
      bysykkel.append(item["name"])
      lon.append(item["lon"])
      lat.append(item["lat"])
      capacity.append(item["capacity"])
      
      

data = pd.DataFrame({'name': bysykkel,'lon': lon,'lat': lat, 'capacity': capacity})

m = folium.Map(location=[60.3935, 5.325], zoom_start=14,  tiles='cartodbdark_matter') 
marker_cluster = MarkerCluster().add_to(m)

for row in data.itertuples():
    folium.Marker(location=[row.lat,row.lon],popup= (row.name, row.capacity) , icon=folium.Icon(color='blue')).add_to(marker_cluster)

m.save('sykker_bergen.html')
