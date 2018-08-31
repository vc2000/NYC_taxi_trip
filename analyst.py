import pandas as pd
df = pd.read_csv('yellow_tripdata_2017-01.csv', sep=',')
# print(df.head())
#print(df.count())
print(df.total_amount > 5)

#https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe
