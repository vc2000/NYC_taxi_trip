import pandas as pd
import numpy as np
import geocoder


geo_df = pd.read_csv("zone_geocode.csv")
geo_df["city_coord"] = [geo_df["city_coord"].fillna(geocoder.google(x).latlng for x in geo_df.Zone)]



print(geo_df.head())

file_name = "v2_zone_geocode.csv"
geo_df.to_csv(file_name, sep=",", encoding="utf-8")