import folium

dhaka_xy = [23.751764, 90.362865]
poi_coordinates = [
                    [23.751764, 90.362865],
                    [23.797350, 90.449529],
                    [23.736914, 90.400971],
                    [23.762386, 90.378491],
                    [23.737461, 90.393924],
                    [23.732397, 90.416771],
                    [23.747888, 90.378671],]
poi_names = ['Basa', 'UIU', 'Ramna', 'Parliament', 'Museum', 'Motijheel', 'Lake']                 
map = folium.Map(location=dhaka_xy, zoom_start=6, tiles="Stamen Toner")
#print(dir(folium))
fg = folium.FeatureGroup(name='Map1')
i = 0
for cord,names in zip(poi_coordinates, poi_names):
    fg.add_child(folium.Marker(cord, popup=names,icon=folium.Icon(color='green')) )

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig'))) )

map.add_child(fg)



map.save("Home.html")