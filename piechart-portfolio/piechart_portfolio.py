import sys
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
# aggregate assets by macro category with pie chart 
path_file = sys.path[0]
df = pd.read_csv( path_file + "/investments.csv")
data = df.groupby("type")["value"].sum()
plt.pie( data , labels = data.index)
plt.show()

