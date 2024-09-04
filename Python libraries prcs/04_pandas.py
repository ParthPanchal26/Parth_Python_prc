import pandas as pd
import numpy as np

# series = pd.Series([1, 3, 5, 7, 9, 11])
# print(series)

# key = ['firstname: ', 'lastname: ', 'age: ']
# values = ['parth', 'panchal', 19]
# obj = pd.Series(values, key)
# print(obj)


dates = pd.to_datetime("4th of sep, 2024")
index = dates + pd.to_timedelta(np.arange(5), unit='D')
data = [1, 2, 3, 4, 5]
timeSeries = pd.Series(data, index)
print(timeSeries)
