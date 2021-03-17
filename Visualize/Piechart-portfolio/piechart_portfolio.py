import pandas as pd
import matplotlib.pyplot as plt
import sys
%matplotlib inline
path_file = sys.path[0]
df_investimenti = pd.read_csv(path_file+"/investiments.csv")
df_investimenti.head()
data = df_investimenti.groupby("type")["value"].sum()
data.plot.pie()
