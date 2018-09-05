import pandas as pd
import numpy as np
from fractions import Fraction

df = pd.read_csv("data/yellow_tripdata_2017-01.csv")

"""
    fraction of payments under $5 use a credit card
"""

"""fraction_under_5_credit = str(Fraction(df.query("total_amount < 5 & payment_type == 1").shape[0], df.shape[0]))

with open("Q1_under5_creditcard.txt", "w") as text_file:
    print(f"fraction of payments under $ 5 use a credit card : {fraction_under_5_credit}", file=text_file)"""


"""
    Number of Credit Card payments under $5 and a list sorted highest to lowest
"""

"""num_under_5_credit = df[(df.total_amount < 5) & (df.payment_type == 1)]

num_under_5_credit.sort_values(by="total_amount", ascending=0)

# save_as_new_csv and sorted
file_name = "Q2_number_under_$5_credit_card.csv"
num_under_5_credit.to_csv(file_name, sep=",", encoding="utf-8")
print("saved" + file_name)

str(num_under_5_credit.shape[0])
with open("Q2_number_under_$5_credit_card.txt", "w") as text_file:
    print(f"Number of Credit Card payments under $5  {num_under_5_credit}", file=text_file)"""


"""
    fraction of payments over $50 use a credit card
"""
"""fraction_over_50_credit = str(
        Fraction(df.query("total_amount > 50 & payment_type == 1").shape[0], df.shape[0]))

with open("Q3_fraction_over_50_creditcard.txt", "w") as text_file:
    print(f"fraction of payments over $ 50 use a credit card :  {fraction_over_50_credit}", file=text_file)"""


"""
    Number of credit card payments over $50
"""
"""num_over_50_credit = str(df.query("total_amount > 50 & payment_type == 1").shape[0])

with open("Q4_number_over_50_creditcard.txt", "w") as text_file:
    print(f"Number of credit card payments over $50 :  {num_over_50_credit}", file=text_file)"""


"""
    the mean fare per minute driven # bug data...
"""

"""df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], format='%Y-%m-%d %H:%M:%S')
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], format='%Y-%m-%d %H:%M:%S')
df["time_diff"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
df['time_diff'] = df['time_diff'].astype('timedelta64[s]') /60
print("Min : " , df['time_diff'].min()) # data has bug ...
print("Max : ",df['time_diff'].max() )
quer = df.query("time_diff < 0")
print(quer.head())
df["fare_per_min"] = df["fare_amount"] / df["time_diff"]
print("the mean fare per minute driven :" + str( df["fare_per_min"].mean()))

fare_per_min_mean = str( df["fare_per_min"].mean())
with open("Q5_mean_fare_per_min_driven.txt", "w") as text_file:
    print(f"the mean fare per minute driven :  {fare_per_min_mean}", file=text_file)"""

"""
    the median of the taxi's fare per mile driven #
"""
"""df["fare_per_mile"] = df["fare_amount"] / df["trip_distance"]
print("the median of the taxi's fare per mile driven : " + str(df["fare_per_mile"].median()) )

median_fare_per_mile_driven = str(df["fare_per_mile"].median())
with open("Q6_median_fare_per_mile_driven.txt", "w") as text_file:
    print(f"the median of the taxi's fare per mile driven :  {median_fare_per_mile_driven}", file=text_file)
"""

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

quantile_95th = df.speed.quantile(0.95)

with open("Q7_95th_avg_speed_miles_per_hour.txt", "w") as text_file:
    print(f"the 95 percentile of the taxi's average driving speed in miles per hour :  {quantile_95th}", file=text_file)"""


"""
    the average ratio of the distance between the pickup and drop-off divided by the distance driven
"""

"""from geopy.geocoders import Nominatim
from geopy.distance import vincenty
geolocator = Nominatim()

taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")
df_clean = df[['trip_distance','PULocationID','DOLocationID']]
add_begloc = pd.merge(df_clean,taxi_zone_df, left_on="PULocationID", right_on="LocationID",how='left')
add_begloc["Zone"] = add_begloc["Zone"] +"," +add_begloc["Borough"]
add_begloc = add_begloc.rename(columns={'Zone':'begZone'})
add_begloc = add_begloc.drop(['service_zone', 'Borough'], axis=1)
add_begloc['beg_geocode'] = add_begloc['begZone'].apply(geolocator.geocode)
print(add_begloc.head())


add_endloc = pd.merge(add_begloc, taxi_zone_df, left_on="DOLocationID", right_on="LocationID",how='left')
add_endloc["Zone"] = add_endloc["Zone"] +"," +add_endloc["Borough"]
add_endloc = add_endloc.rename(columns={'Zone':'endZone'})
add_endloc = add_endloc.drop(['service_zone','Borough'], axis=1)
add_endloc['end_geocode'] = add_endloc['endZone'].apply(geolocator.geocode)

add_endloc['beg_end_distance']= add_endloc.apply((lambda row: vincenty(add_endloc['endZone'],add_endloc['begZone']).miles),axis=1)

add_endloc['distance_diff'] = add_endloc['beg_end_distance']/add_endloc['trip_distance']

print(add_endloc['distance_diff'].mean())
avg_beg_end_distance_divided_distance_driven = add_endloc['distance_diff'].mean()
with open("Q8_avg_beg_end_distance_divided_distance_driven.txt", "w") as text_file:
    print(f"the average ratio of the distance between the pickup and drop-off divided by the distance driven :  {avg_beg_end_distance_divided_distance_driven}", file=text_file)"""


"""
    the average tip for rides from JFK
"""
"""taxi_zone_df = pd.read_csv("data/taxi _zone_lookup.csv")
merge_loc_df = pd.merge(df,taxi_zone_df, left_on="PULocationID", right_on="LocationID",how='left')
jfk= merge_loc_df.loc[merge_loc_df['Zone'] == 'JFK Airport']
avg_tip = str(jfk['tip_amount'].mean())

with open("Q9_avg_tip_JFK.txt", "w") as text_file:
    print(f"the average tip for rides from JFK  :  {avg_tip}", file=text_file)"""


"""
    the median March revenue of a taxi driver
"""
"""march_yellow_2017 = pd.read_csv("data/yellow_tripdata_2017-03.csv")

march_yellow_2017["rev"] = march_yellow_2017['total_amount'] - march_yellow_2017['tolls_amount']

# print("the median March revenue of a taxi driver :"+str(march_yellow_2017["rev"].median()))

median_March_revenue = str(march_yellow_2017["rev"].median())
with open("Q10_median_March_revenue.txt", "w") as text_file:
    print(f"the median March revenue of a taxi driver  :  {median_March_revenue}", file=text_file)
"""
