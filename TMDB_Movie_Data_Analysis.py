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