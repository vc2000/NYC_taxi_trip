import pandas as pd
from fractions import Fraction
from math import radians, cos, sin, asin, sqrt

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

print("Min : " , df['time_diff'].min())
print("Max : ",df['time_diff'].max() )
negtime = df.query("time_diff < 0")  # data has bug ...
negfare = df.query("fare_amount < 0") # data has bug ...

print(negtime.head())
print(negfare.head())


print("the mean fare per minute driven :" + str(sum(df["fare_amount"])/ sum(df["time_diff"])))

fare_per_min_mean = str(sum(df["fare_amount"])/ sum(df["time_diff"]))
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

taxi_zone_df = pd.read_csv("v2_zone_geocode.csv")
df_clean = df[['trip_distance','PULocationID','DOLocationID']]

PUlat = [ taxi_zone_df['lat'][taxi_zone_df['LocationID'] == df_clean['PULocationID'][x]] for x in range(0,(len(df.index)))]
PUlon = [ taxi_zone_df['lng'][taxi_zone_df['LocationID'] == df_clean['PULocationID'][x]] for x in range(0,(len(df.index)))]

DOlat = [ taxi_zone_df['lat'][taxi_zone_df['LocationID'] == df_clean['DOLocationID'][x]] for x in range(0,(len(df.index)))]
DOlon = [ taxi_zone_df['lng'][taxi_zone_df['LocationID'] == df_clean['DOLocationID'][x]] for x in range(0,(len(df.index)))]

import mpu
#km to mile
dist = [mpu.haversine_distance((float(PUlat[i]), float(PUlon[i])), (float(DOlat[i]), float(DOlon[i]))) * 0.621371 for i in range(0,(len(df.index)))]


distance_diff = sum(dist)/sum(df['trip_distance'])

with open("Q8_avg_beg_end_distance_divided_distance_driven.txt", "w") as text_file:
    print(f"the average ratio of the distance between the pickup and drop-off divided by the distance driven :  {distance_diff}", file=text_file)



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
