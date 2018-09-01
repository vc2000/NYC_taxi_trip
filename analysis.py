import pandas as pd
import numpy as np
from fractions import Fraction

df = pd.read_csv("yellow_tripdata_2017-01.csv")

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
"""

"""
    Number of credit card payments over $50
"""

"""print(
    "Number of credit card payments over $50 "
    + str(df.query("total_amount > 50 & payment_type == 1").shape[0])
)"""


"""
    the mean fare per minute driven  ?????problem??????
    how to convert min to float
"""
#df["time_diff"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]

"""df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["time_diff"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]

df["fare_per_min"] = df["fare_amount"] / df["time_diff"]
print(df.head())"""

#print("the mean fare per minute driven :" + str( df["fare_per_min"].mean()))


"""
    the median of the taxi's fare per mile driven
"""
"""print(df.head())

df["fare_per_mile"] = df["fare_amount"] / df["trip_distance"]

print("the median of the taxi's fare per mile driven : " + str(df["fare_per_mile"].median()) )"""


"""
    the 95 percentile of the taxi's average driving speed in miles per hour ??
"""

"""
    the average ratio of the distance between the pickup and drop-off divided by the distance driven???
"""

"""
    the average tip for rides from JFK
"""

"""JFK_avg = df[(df.RatecodeID = 2)

print(JFK_avg.tip_amount.mean())"""

"""
    the median March revenue of a taxi driver
"""
"""march_yellow_2017 = pd.read_csv("yellow_tripdata_2017-03.csv")

march_yellow_2017["rev"] = march_yellow_2017['total_amount'] - march_yellow_2017['tolls_amount']
print(march_yellow_2017.groupby(['VendorID'])['rev'].sum())"""
