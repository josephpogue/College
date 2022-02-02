import pandas as pd 
df = pd.read_csv('/Users/josephpogue/Desktop/College/Data Mining - CS470/data.csv')
age_col = []
blood_col = []
cholesterol_col = []
heartrate_col = []
oldpeak_col = []

for (index, row) in df.iterrows():
    for(index2, row2) in df.iterrows():
        age_difference = row['age'] - row2['age']
        blood_difference = row['blood pressure'] - row2['blood pressure']
        cholesterol_difference = row['cholesterol'] - row2['cholesterol']
        heart_difference = row['heart rate'] - row2['heart rate']
        oldpeak_difference = row['oldpeak'] - row2['oldpeak']
        age_col.append(age_difference)
        blood_col.append(blood_difference)
        cholesterol_col.append(cholesterol_difference)
        heartrate_col.append(heart_difference)
        oldpeak_col.append(oldpeak_difference)
a = pd.Series(age_col, name="age")
b = pd.Series(blood_col, name="blood pressure")
c = pd.Series(cholesterol_col, name="cholesterol")
d = pd.Series(heartrate_col, name="heart rate")
e = pd.Series(oldpeak_col, name="oldpeak")
df_final = pd.concat([a,b,c,d,e],axis=1)
df_final.to_csv('step1.csv', index=True)


