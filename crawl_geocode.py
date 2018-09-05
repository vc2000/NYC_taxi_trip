import pandas as pd
import geocoder

taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")

taxi_zone_df['address']=taxi_zone_df['Borough'] + " , " + taxi_zone_df['Zone']

lat_lng = geocoder.google(x).latlng for x in taxi_zone_df.Zone

taxi_zone_df["city_coord"] =[geocoder.google(x).latlng for x in taxi_zone_df.address]


file_name = "zone_geocode.csv"
taxi_zone_df.to_csv(file_name, sep=",", encoding="utf-8")
