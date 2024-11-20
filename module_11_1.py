import pandas as pd
import numpy as np
test = pd.read_csv('pandas_tutorial_read.csv', delimiter=';',
	    names=['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])
print(test)

print(test.tail())
print(test.sample(5))

print(test[['user_id', 'country']])
print(test.user_id)
print(test[test.source == 'SEO'])
print(test.head()[['user_id', 'country']])
print(test[['user_id', 'country']].head())
print(test[test.country == 'country_2'][['user_id', 'country', 'topic']].head())
print(test.groupby('source').count()[['user_id']])
print(test[test.country == 'country_2'][['topic']].count())
print(test[test.country == 'country_2'][['source']].count())
print(test[test.country == 'country_2'].groupby(['source', 'topic']).count())


zoo = pd.read_csv('animals.csv', delimiter=',')
print(zoo)
print(zoo[['animal']].count())
print(zoo.animal.count())
print(zoo[['weight']].sum())
print(zoo.weight.sum())
print(zoo[['age']].max(),'\n', zoo[['age']].min(),'\n', zoo[['age']].mean(),'\n', zoo[['age']].median())
print(zoo.groupby('animal').median())
print(zoo.groupby('animal').mean().weight)