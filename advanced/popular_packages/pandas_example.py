import pandas as pd
import numpy as np

list = pd.Series([1,2,3,4,5])
print(list)

dataframe = pd.DataFrame({
    'column1': [1,2,3,4,5],
    'column2': [6,7,8,9,10]
})
print(dataframe)

# creating random dates
dates = np.random.choice(pd.date_range('20250101', periods=90), 90)

# creating dataframes with random number and dates
df = pd.DataFrame(np.random.randn(90,4), index=dates, columns=['column1', 'column2', 'column3', 'column4'])
print(df)

# print first 5 rows
print(df.head())


