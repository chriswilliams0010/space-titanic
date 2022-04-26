import pandas as pd
import numpy as np
from sklearn import preprocessing

# -read in the training set
df = pd.read_csv('train.csv')

# -check out missingness and dtypes
df.isnull().sum()
df.info(null_counts=False)
df.describe()

# -begin data wrangling
# loop for splitting PassengerId into two and saving each split in a list
group = []  # group list initialized
ind = []  # individual list initialized
for pid in df['PassengerId']:
    group.append(pid.split("_")[0])
df['group'] = group  # add group column with first split

# prepare a dict with columns that need to change dtypes
change_dtype = {'group': 'int'}

# start a list of columns to drop
drop = ['PassengerId']

# add a column of value counts for group
df['alone'] = df['group'].map(df['group'].value_counts())
# change to binary
df['alone'] = np.where(df['alone'] == 1, 1, 0)

# change HomePlanet to factor
le_hp = preprocessing.LabelEncoder()
le_hp.fit(df['HomePlanet'])
df['home_planet'] = le_hp.transform(df['HomePlanet'])
drop.append('HomePlanet')

