#import the libraries we need in this project.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("tmdb-movies.csv",parse_dates=['release_date']) #load dataset
df.head() # see first 5 rows from the dataset.

df.shape #to get number of records and columns

df.info()  # to get some info

df.drop(['id' , 'imdb_id' , 'original_title' , 'homepage', 'tagline' ,'director' , 'cast' ,'overview','production_companies','release_year','keywords','genres','budget_adj','revenue_adj'] ,axis=1, inplace=True)

df.head() # to see the data after drop.

df.hist(figsize=(10,8)); # histogram for all columns.

df.info()

df.describe()

df_zero=df.query('budget == 0 and revenue == 0 ') # to get the records that have budget and revenue = 0 
df_zero.shape

df_not_zero=df.query('budget != 0 and revenue != 0 ') # to get the records that doesn't have budget and revenue = 0 
df_not_zero.shape

#Now I will compare Revenue with Run Time
p=df_not_zero.plot(x='runtime',y='revenue',kind="scatter",figsize=(15,8)); 
p.set_title("Compare Run Time and Revenue", fontsize = 15)
p.set_xlabel("Run Time (Min)");
