import pandas as pd
import numpy as np
import geocoder


geo_df = pd.read_csv("zone_geocode.csv")

# clean by hand for this time
# geo_df["city_coord"] = [geo_df["city_coord"].fillna(geocoder.google(x).latlng for x in geo_df.Zone)]


geo_df["city_coord"] = geo_df.city_coord.apply(lambda x: x.replace('[','').replace(']',''))

geo_df['lat'], geo_df['lng'] = geo_df["city_coord"].str.split(',',1).str

geo_df = geo_df.drop('city_coord', 1)

print(geo_df.head())

file_name = "v2_zone_geocode.csv"
geo_df.to_csv(file_name, sep=",", encoding="utf-8")