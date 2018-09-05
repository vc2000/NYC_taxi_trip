import pandas as pd
import numpy as np

geo_df = pd.read_csv("zone_geocode.csv")
#geo_df["city_coord"] = 

#print(geo_df["city_coord"])

lat=[x[1] for x in np.asarray(geo_df["city_coord"])]

print(lat.head())
