import pandas as pd
import folium
from gmplot import gmplot

df = pd.read_csv("data/yellow_tripdata_2017-01.csv")

location_df = pd.read_csv("v2_zone_geocode.csv")
location_df = location_df.drop(["Unnamed: 0"], axis=1)

#drop other column
# df['DOLocationID'].value_counts().reset_index().to_csv('destination_count.csv')

# merging two df

lat_lng_count_df = pd.merge(df,location_df,left_on='DOLocationID', right_on="LocationID",how='left')
print(lat_lng_count_df.shape[0])

# NYC
# random 300000 data - gmplot cannot handle
data = lat_lng_count_df.head(n=300000)
gmap = gmplot.GoogleMapPlotter(40.758896, -73.985130, 9)

# Overlay our datapoints onto the map
gmap.heatmap(data['lat'], data['lng'])
gmap.draw("heatmap.html")
#map = folium.Map(location=[40.758896, -73.985130], tiles="Stamen Terrain", zoom_start=13)
#map.add_children(plugins.HeatMap(stationArr, radius=15))
