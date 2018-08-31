import pandas as pd
import numpy as np
from fractions import Fraction

df = pd.read_csv("yellow_tripdata_2017-01.csv")

"""
    fraction of payments under $5 use a credit card
"""
print(
    "fraction of payments under $ 5 use a credit card : "
    + str(
        Fraction(df.query("total_amount < 5 & payment_type == 1").shape[0], df.shape[0])
    )
)

"""
    Credit Card payments under $5 and a list sorted highest to lowest
"""

under_5_credit_df =df[(df.total_amount < 5) & (df.payment_type == 1)]

under_5_credit_df.sort_values(by='total_amount', ascending=0)

# print(under_5_credit_df.head())

"""
    fraction of payments over $50 use a credit card
"""
print(
    "fraction of payments over $ 50 use a credit card : "
    + str(
        Fraction(df.query("total_amount > 50 & payment_type == 1").shape[0], df.shape[0])
    )
)

"""
    Number of credit card payments over $50
"""
print(
    "Number of credit card payments over $50 "
    + str( df.query("total_amount > 50 & payment_type == 1").shape[0])
    )
)

