import pandas as pd
import numpy as np
from fractions import Fraction
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
geolocator = Nominatim(timeout=3)

# df = pd.read_csv("data/yellow_tripdata_2017-01.csv")

taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")
taxi_zone_df["city_coord"] = taxi_zone_df['Zone'].apply(geolocator.geocode).apply(lambda x: (x.latitude, x.longitude))
#265
print(taxi_zone_df.head())