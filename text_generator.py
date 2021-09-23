import folium

dhaka_xy = [23.751764, 90.362865]
map = folium.Map(location=dhaka_xy, zoom_start=6, tiles="Stamen Toner")
#print(dir(folium))

map.add_child(folium.Marker(dhaka_xy, popup="Amar Basa",icon=folium.Icon(color='green')) )




map.save("Home.html")