import statistics
import pandas

#read the entire csv file into a pandas dataframe
df=pandas.read_csv("shopping.csv")

#filter out the column,value_eur
player_values=df["amt_1"]
print(player_values)

