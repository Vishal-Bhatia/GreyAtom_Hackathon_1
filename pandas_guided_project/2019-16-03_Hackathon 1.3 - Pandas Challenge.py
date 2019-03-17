#Team 3::: Pandas Challenge

#%%
##Importing classes
import os
from datetime import datetime as dt
from collections import Counter
import random as rd
import math as mt
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pyplt
import seaborn as sb
import requests


#%%
##Loading the CSV file onto a Pandas DataFrame
path = "C:\\Users\\CitizenVish\\OneDrive\\DataScience\\ProjectSpaces\\Hackathon_1\\pandas_guided_project\\data\\excel-comp-data.csv"
df = pd.read_csv(path)
##Lower-casing all values in the "state" column
df["state"] = df["state"].str.lower()
##Creating a new column "total" to capture quarterly amount per record
df["Total"] = df["Jan"] + df["Feb"] + df["Mar"]

#%%
##Computing the sums of the Jan, Feb, Mar, and Total variables
sum_Jan = df["Jan"].sum()
sum_Feb = df["Feb"].sum()
sum_Mar = df["Mar"].sum()
sum_Total = df["Total"].sum()
##Adding the monthly and quarterly sums as a new row to the existing dataframe
df_final = df.append([{"Jan" : sum_Feb,"Feb" : sum_Feb, "Mar" : sum_Mar, "Total" : sum_Total}], ignore_index = True)

#%%
##Loading the state-abbreviations data on a Wiki page onto a DataFrame
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
###Using the "requests" module to get the url and store it in variable called "response"
response = requests.get(url)
##Creating a DataFrame from the above variable
df1 = pd.read_html(response.content)[0]
##Dropping the first 11 rows from the above DataFrame, as these contain irrelevant text
df1.drop(df.head(11).index, inplace = True)

#%%
##Creating a dictionary of a zip object that combines the state names and abbreviations of the URL DataFrame
mapping = dict(zip(df1[0].str.lower(), df1[5]))
##Using the above dictionary variable to create a new column of abbreviations
df_final["abbr"] = pd.Series(df_final["state"]).map(mapping)

#%%
##Replacing the NaN values for mississipi and tennesse with "MS" and "TN", respectively
df_final["abbr"][df_final.state == "mississipi"] = "MS"
df_final["abbr"][df_final.state == "tenessee"] = "TN"

#%%
##Using groupby to calculate state-wise data
###Creating a pivot table will NOT work here as all records have unique states
df_sub = pd.DataFrame(df_final.groupby("abbr")["Jan", "Feb", "Mar", "Total"].sum())
##Adding the dollar symbol before all amounts
formatted_df = df_sub.applymap("${0:.2f}".format)

#%%
##Computing the monthly and quarterly amounts for all accounts, and applying the dollar symbol to monetary records
sum_row = pd.DataFrame(df_sub[["Jan", "Feb", "Mar", "Total"]].sum())
df_sub_sum = sum_row.applymap("${0:.2f}".format)

#%%
##Storing the final amount as a variable
df_sub_total = df_sub["Total"].sum()

#%%
##Creating a pie-chart of the state-wise quarterly amounts
fig = pyplt.figure(figsize = (8, 5))
ax = pyplt.pie(df_sub["Total"], labels = df_sub.index, autopct = "%.2f")
pyplt.title("State-Wise Quarterly Amounts")
pyplt.legend(df_sub.index, loc = "upper right")
pyplt.show()