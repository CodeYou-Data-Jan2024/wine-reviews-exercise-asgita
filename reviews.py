import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

#print(df.head())

summary_df = df.groupby('country').agg({'title':'count','points' :'mean'}).round(1)

summary_df = summary_df.rename(columns = {'title' :'count'}).reset_index()

summary_df = summary_df.sort_values('count',ascending=False)

summary_df.to_csv('data/reviews-per-country.csv',index=False)




