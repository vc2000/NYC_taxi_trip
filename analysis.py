import pandas as pd
import numpy as np
from fractions import Fraction

df = pd.read_csv("data/yellow_tripdata_2017-01.csv")

"""
    fraction of payments under $5 use a credit card
"""
"""print(
    "fraction of payments under $ 5 use a credit card : "
    + str(
        Fraction(df.query("total_amount < 5 & payment_type == 1").shape[0], df.shape[0])
    )
)"""

"""
    Credit Card payments under $5 and a list sorted highest to lowest
"""

"""under_5_credit_df = df[(df.total_amount < 5) & (df.payment_type == 1)]

under_5_credit_df.sort_values(by="total_amount", ascending=0)

# save_as_new_csv
file_name = "under_$5_credit_card.csv"
under_5_credit_df.to_csv(file_name, sep="\t", encoding="utf-8")
print("saved" + file_name)"""

"""
    fraction of payments over $50 use a credit card
"""
"""print(
    "fraction of payments over $ 50 use a credit card : "
    + str(
        Fraction(
            df.query("total_amount > 50 & payment_type == 1").shape[0], df.shape[0]
        )
    )
)"""

"""
    Number of credit card payments over $50
"""

"""print(
    "Number of credit card payments over $50 "
    + str(df.query("total_amount > 50 & payment_type == 1").shape[0])
)"""


"""
    the mean fare per minute driven
"""

"""df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], format='%Y-%m-%d %H:%M:%S')
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], format='%Y-%m-%d %H:%M:%S')
df["time_diff"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
df['time_diff'] = df['time_diff'].astype('timedelta64[s]') /60
print("Min : " , df['time_diff'].min()) # data has bug ... 
print("Max : ",df['time_diff'].max() )
df = df.query("time_diff < 0")
print(df.head())
df["fare_per_min"] = df["fare_amount"] / df["time_diff"]
print("the mean fare per minute driven :" + str( df["fare_per_min"].mean()))"""


"""
    the median of the taxi's fare per mile driven
"""
"""df["fare_per_mile"] = df["fare_amount"] / df["trip_distance"]
print("the median of the taxi's fare per mile driven : " + str(df["fare_per_mile"].median()) )"""


"""
    the 95 percentile of the taxi's average driving speed in miles per hour ???
"""

"""df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], format='%Y-%m-%d %H:%M:%S')
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], format='%Y-%m-%d %H:%M:%S')
df["time_diff"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
# per hour
df['time_diff_hour'] = df['time_diff'].astype('timedelta64[s]') /3600
# distance / time = speed
df['speed'] = df['trip_distance'] / df['time_diff_hour']


#need to sort


print(df.head())"""

"""
    the average ratio of the distance between the pickup and drop-off divided by the distance driven
"""
"""from geopy.geocoders import Nominatim
geolocator = Nominatim()

taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")
df_clean = df[['trip_distance','PULocationID','DOLocationID']]
add_begloc = pd.merge(df_clean,taxi_zone_df, left_on="PULocationID", right_on="LocationID",how='left')
add_begloc["Zone"] = add_begloc["Zone"] +"," +add_begloc["Borough"] 
add_begloc = add_begloc.rename(columns={'Zone':'begZone'})
add_begloc = add_begloc.drop(['service_zone', 'Borough'], axis=1)
add_begloc['beg_geocode'] = add_begloc['begZone'].apply(geolocator.geocode)


add_endloc = pd.merge(add_begloc, taxi_zone_df, left_on="DOLocationID", right_on="LocationID",how='left')
add_endloc["Zone"] = add_endloc["Zone"] +"," +add_endloc["Borough"] 
add_endloc = add_endloc.rename(columns={'Zone':'endZone'})
add_endloc = add_endloc.drop(['service_zone','Borough'], axis=1)
add_endloc['end_geocode'] = add_endloc['endZone'].apply(geolocator.geocode)

add_endloc['beg_end_distance']= add_endloc.apply(lambda row: vincenty(
        (add_endloc['endZone'],add_endloc['begZone']).miles),axis=1)

add_endloc['distance_diff'] = add_endloc['beg_end_distance']/add_endloc['trip_distance']

print(add_endloc.mean())"""


"""
    the average tip for rides from JFK
"""
"""taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")
merge_loc_df = pd.merge(df,taxi_zone_df, left_on="PULocationID", right_on="LocationID",how='left')
jfk= merge_loc_df.loc[merge_loc_df['Zone'] == 'JFK Airport']
#jfk = merge_loc_df[merge_loc_df['Zone'].str.contains("JFK Airport")]
print("the average tip for rides from JFK :"+str(jfk['tip_amount'].mean()))"""

"""
    the median March revenue of a taxi driver
"""
"""march_yellow_2017 = pd.read_csv("yellow_tripdata_2017-03.csv")

march_yellow_2017["rev"] = march_yellow_2017['total_amount'] - march_yellow_2017['tolls_amount']

# print("the median March revenue of a taxi driver :"+str(march_yellow_2017["rev"].median()))"""
