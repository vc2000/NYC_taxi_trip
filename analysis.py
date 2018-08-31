import pandas as pd
import numpy as np
from fractions import Fraction

df = pd.read_csv("yellow_tripdata_2017-01.csv")

print(
    "fraction of payments under $ 5 use a credit card : "
    + str(
        Fraction(df.query("total_amount < 5 & payment_type == 1").shape[0], df.shape[0])
    )
)
