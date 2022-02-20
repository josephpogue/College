import pandas as pd 
import math
df = pd.read_csv('/Users/josephpogue/Desktop/College/Data Mining - CS470/data.csv')

new_data = []
for row in df:
    newlist = []
    for i in df[row]:
        for j in df[row]:
            if(row in ["age", "resting blood pressure", "serum cholesterol in mg/dl", "maximum heart rate achieved", "oldpeak = ST depression induced by exercise relative to rest"]):
                newlist.append(abs(i-j))
            else:
                if(i == j):
                     newlist.append(0)
                else: 
                    newlist.append(1)
new_data.append(newlist)