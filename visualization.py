import pandas as pd
import folium
from folium import IFrame

df = pd.read_csv("data/yellow_tripdata_2017-01.csv")

location_df = pd.read_csv("v2_zone_geocode.csv")
location_df = location_df.drop(["Unnamed: 0"], axis=1)

# saved destination count as csv
# df['DOLocationID'].value_counts().reset_index().to_csv('destination_count.csv')

# cleaning data
destination_count_df = pd.read_csv("destination_count.csv")
destination_count_df = destination_count_df.rename(
    columns={"index": "LocationID", "DOLocationID": "count"}
)
destination_count_df = destination_count_df.drop(["Unnamed: 0"], axis=1)

# merging two df
lat_lng_count_df = pd.merge(destination_count_df,location_df,on="LocationID",how='left')

# NYC
map = folium.Map(location=[40.758896, -73.985130], tiles="Stamen Terrain", zoom_start=13)

color_list = [
    "red",
    "blue",
    "green",
    "purple",
    "orange",
    "darkred",
    "lightred",
    "beige",
    "darkblue",
    "darkgreen",
    "cadetblue",
    "darkpurple",
    "white",
    "pink",
    "lightblue",
    "lightgreen",
    "gray",
    "black",
    "lightgray",
]
count = 0
while count < 10:
    map.add_child(
        folium.Marker(
            location=[lat_lng_count_df.iloc[count]["lat"], lat_lng_count_df.iloc[count]["lng"]],
            popup="No. " + str(count +1)+ " destination is " + str(lat_lng_count_df.iloc[count]["Zone"]) + " : " + str(lat_lng_count_df.iloc[count]["count"]),
            icon=folium.Icon(color=color_list[count]),
        )
    )
    count += 1

map.save("NYC_destination_count.html")