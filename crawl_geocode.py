import pandas as pd
import geocoder

taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")

#lat_lng = geocoder.google(x).latlng for x in taxi_zone_df.Zone

taxi_zone_df["city_coord"] =[geocoder.google(x).latlng for x in taxi_zone_df.Zone]


file_name = "zone_geocode.csv"
taxi_zone_df.to_csv(file_name, sep=",", encoding="utf-8")
