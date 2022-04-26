import pandas as pd

# read in the training set
df = pd.read_csv('train.csv')

# check out missingness and dtypes
df.isnull().sum()
df.info(null_counts=False)
df.describe()

