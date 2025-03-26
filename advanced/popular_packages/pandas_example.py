import pandas as pd
import numpy as np

list = pd.Series([1,2,3,4,5])
print(list)

dataframe = pd.DataFrame({
    'column1': [1,2,3,4,5],
    'column2': [6,7,8,9,10]
})
print(dataframe)




df = pd.DataFrame(np.random.randint(0,100, (10,10)))

