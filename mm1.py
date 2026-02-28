import numpy as np
import pandas as pd
from scipy import stats

data=[5,7,10,10,10,12,15]
series=pd.Series(data)
mean_val=series.mean()
median_val=series.median()
mode_val=series.mode()
print("Data:",data)
print("Mean:",mean_val)
print("Median:",median_val)
print("Mode:",mode_val)