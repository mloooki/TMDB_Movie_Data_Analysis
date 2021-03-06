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


#Now I will compare Revenue with vote_count.¶

p1=df_not_zero.plot(x='vote_count',y='revenue',kind="scatter",figsize=(15,8));
p1.set_title("Compare vote_count and Revenue", fontsize = 15)



# get the aveatge revenue for each group
less_than_2000 = df_not_zero.query('vote_count <=2000').mean()['revenue']
between_2000_4000 = df_not_zero.query('vote_count > 2000 and vote_count <=4000').mean()['revenue']
between_4000_6000 = df_not_zero.query('vote_count > 4000 and vote_count <=6000').mean()['revenue']
between_6000_8000 = df_not_zero.query('vote_count > 4000 and vote_count <=6000').mean()['revenue']
between_8000_10000 = df_not_zero.query('vote_count > 8000 and vote_count <=10000').mean()['revenue']


# bar chart
plt.figure(figsize=(15,8))
plt.bar(['>=2000','between_2000_4000','between_4000_6000','between_6000_8000','between_8000_10000'],[less_than_2000,between_2000_4000,between_4000_6000,between_6000_8000,between_8000_10000])
plt.title('Compare vote_count and Revenue')
plt.xlabel('Vote Count')
plt.ylabel('avg Revenue');


# Now I will compare Revenue with Votes?
p3=df_not_zero.plot(x='vote_average',y='revenue',kind="scatter",figsize=(15,8))
p3.set_title("Compare Vote_Avg and Revenue", fontsize = 15);


df_not_zero.vote_average.min() # get minimum of vote
df_not_zero.vote_average.max() # get maximum of vote

# get the aveatge revenue for each group
between_2_to_3= df_not_zero.query('vote_average >= 2.2 and 3.2>= vote_average').mean()['revenue']
between_3_to_4= df_not_zero.query('vote_average >= 3.3 and 4.2>= vote_average').mean()['revenue']
between_4_to_5= df_not_zero.query('vote_average >= 4.3 and 5.2>= vote_average').mean()['revenue']
between_5_to_6= df_not_zero.query('vote_average >= 5.3 and 6.2>= vote_average').mean()['revenue']
between_6_to_7= df_not_zero.query('vote_average >= 6.3 and 7.2>= vote_average').mean()['revenue']
between_7_to_8= df_not_zero.query('vote_average >= 7.3 and 8.5>= vote_average').mean()['revenue']

# bar chart
plt.figure(figsize=(15,8))
plt.bar(['2.2 to 3.2','3.3 to 4.2','4.3 to 5.2','5.3 to 6.2','6.3 to 7.2','7.3 to 8.5'],[between_2_to_3,between_3_to_4,between_4_to_5,between_5_to_6,between_6_to_7,between_7_to_8])
plt.title('Compare vote Avg and Revenue')
plt.xlabel('Vote')
plt.ylabel('avg Revenue');


#Now I will compare Revenue with the budget

df_not_zero.budget.median() # get the median of the budget

above=df.query('budget >= 24000000.0') # above or equal to the median
under=df.query('budget < 24000000.0') # under the median

above.revenue.mean() # get the average for the budget that above the median.

under.revenue.mean() # get the average for the budget that under the median.

# bar chart
plt.figure(figsize=(15,8))
plt.bar(['Above','Under'],[above.revenue.mean(),under.revenue.mean()])
plt.title('Compare Median Budget and avg Revenue')
plt.xlabel('Median Budget')
plt.ylabel('avg Revenue');


# what are the characteristics that make a movie has higher votes?

votes_median=df.vote_average.median() # get the median of votes
print(votes_median)


High_votes = df.query('vote_average >= 6.0')
Low_votes = df.query('vote_average < 6.0')
High_votes.budget.mean() # get budget average

Low_votes.budget.mean() # get budget average

plt.figure(figsize=(15,8))
plt.bar(['High_votes (more than or equal to 6.0)','Low_votes (Less than6.0)'],[High_votes.budget.mean(),Low_votes.budget.mean()])
plt.title('Compare Budget and votes')
plt.xlabel('Votes')
plt.ylabel('Budget Avg');


High_votes.revenue.mean() # get revenue average.
Low_votes.revenue.mean() # get revenue average.

plt.figure(figsize=(15,8))
plt.bar(['High_votes','Low_votes'],[High_votes.revenue.mean(),Low_votes.revenue.mean()])
plt.title('Compare Revenue and votes')
plt.xlabel('Votes')
plt.ylabel('Revenue Avg');

High_votes.popularity.mean()
Low_votes.popularity.mean()

plt.figure(figsize=(15,8))
plt.bar(['High_votes','Low_votes'],[High_votes.popularity.mean(),Low_votes.popularity.mean()])
plt.title('Compare Popularity and votes')
plt.xlabel('Votes')
plt.ylabel('Popularity');

#How the characteristics of the movie changed over time ?

df_not_zero.release_date.describe()

sum(df_not_zero.release_date.dt.year >=2021) # to get number of relase dates that not correct.
correct_dates_df= df_not_zero.query('release_date.dt.year <=2021') # to get only the movies with correct relase date.
correct_dates_df.release_date.describe()

# I save it to csv to use excel to calculate moving average for budget and revene
correct_dates_df.to_csv('add_moving_average.csv',index=False)

moving_avg_df = pd.read_csv('add_moving_average.csv') # load dataset after adding moving average..

p4 = moving_avg_df.plot(x='release_date',y='moving_budget',kind="line",figsize=(15,8));
p4.set_title("How Budget Changed Over The Time ?", fontsize = 15)
p4.set_xlabel("Realase Date");
p4.set_ylabel("Budget");

p5 = moving_avg_df.plot(x='release_date',y='moving_revenue',kind="line",figsize=(15,8));
p5.set_title("How Revenue Changed Over The Time ?", fontsize = 15)
p5.set_xlabel("Realase Date");
p5.set_ylabel("Revenue");