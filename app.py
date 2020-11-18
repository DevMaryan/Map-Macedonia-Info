import folium
import pandas

# Import Macedonia CSV file
data = pandas.read_csv('Macedonia.csv')

lon = list(data["LON"])
lat = list(data["LAT"])
grad = list(data["CITY"])
elev = list(data["ELEV"])
pop = list(data["POP"])

# Function for ELEVATION COLOR
def ColorElev(elevation,popul):
    if (elevation < 1000) and (popul < 50000):
        return 'green'
    elif (1000 <= elevation < 3000) and (50000 <= popul < 300000):
        return 'orange'
    else:
        return 'red'




map = folium.Map(location = [41.6086, 21.7453], tiles = 'CartoDB dark_matter')

fg = folium.FeatureGroup(name = 'My Map')

for lt, ln, el, gr, po in zip(lat, lon, elev, grad, pop):
    fg.add_child(folium.Marker(location=[lt, ln], popup = folium.Popup(str(el)+ 'm'+'\n'+str(gr) + ' Град,' +'\n'+str(po) + '\n Популација', parse_html = True), icon = folium.Icon(color = ColorElev(el,po))))

map.add_child(fg)


map.save('Macedonia4.html')