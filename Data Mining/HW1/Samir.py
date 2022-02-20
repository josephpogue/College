import numpy as np
import pandas as pd
import scipy as sp
import csv

df = pd.read_csv('data.csv')
df = df.rename(columns={'person ID': 'id', 'chest pain type': 'cp', 'resting blood pressure': 'trestbps', 'serum cholesterol in mg/dl': 'chol', 
                  'fasting blood sugar > 120 mg/dl': 'fbs', 'resting electrocardiographic results': 'restecg', 'maximum heart rate achieved': 'thalach', 
                  'exercise induced angina': 'exang', 'oldpeak = ST depression induced by exercise relative to rest': 'oldpeak', 
                  'the slope of the peak exercise ST segment': 'slope', 'number of major vessels (0-3) colored by flourosopy': 'ca', 
                  'thal: 3 = normal; 6 = fixed defect; 7 = reversable defect': 'thal', 'Has heart disease?': 'target'})

# Generating pairs 
numRows = len(df.index)
pairs = []
for i in range(numRows):
    for j in range(i+1,numRows):
        pairs.append((str(i) + " " + str(j)))

# Calculating for distances
dAge = []
dGender = []
dChestPainType = []
dRestingBloodPressure = []
dChol = []
dFbs = []
dRestEcg = []
dThalach = []
dExang = []
dOldpeak = []
dSlope = []
dNumVessels = []
dThal = []
dHeart = []
for i in range(numRows):
    for j in range(i+1,numRows):
        # Age
        dAge.append(np.linalg.norm(df['age'][i] - df['age'][j]))
        
        # Gender
        dGender.append(int(df['gender'][i] != df['gender'][j]))
        
        # Chest Pain Type 
        dChestPainType.append(int(df['cp'][i] != df['cp'][j]))
        
        # Resting blood pressure
        dRestingBloodPressure.append(np.linalg.norm(df['trestbps'][i] - df['trestbps'][j]))
        
        # Serum cholesterol in mg/dl
        dChol.append(np.linalg.norm(df['chol'][i] - df['chol'][j]))
        
        # Fasting blood sugar > 120 mg/dl 
        dFbs.append(int(df['fbs'][i] != df['fbs'][j]))
        
        # Resting electrocardiographic result
        dRestEcg.append(int(df['restecg'][i] != df['restecg'][j]))
        
        # Maximum heart rate achieved 
        dThalach.append(np.linalg.norm(df['thalach'][i] - df['thalach'][j]))
        
        # Exercise induced angina
        dExang.append(int(df['exang'][i] != df['exang'][j]))
        
        # Oldpeak = ST depression induced by exercise relative to rest
        dOldpeak.append(np.linalg.norm(df['oldpeak'][i] - df['oldpeak'][j]))
        
        # the slope of peak exercise 
        dSlope.append(int(df['slope'][i] != df['slope'][j]))
        
        # number of major vessels (0-3) colored by flourosopy
        dNumVessels.append(np.linalg.norm(df['ca'][i] - df['ca'][j]))
        
        # thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
        dThal.append(int(df['thal'][i] != df['thal'][j]))
        
        # Has heart disease?
        dHeart.append(int(df['target'][i] != df['target'][j]))
        
# Converting to dataframe 
d = {'pairs': pairs, 'Age Distance': dAge, 'Gender Distance': dGender, 'Chest Pain Type Distance': dChestPainType, 
     'Resting Blood Pressure Distance': dRestingBloodPressure, 'Serum Cholesterol Distance': dChol, 'Fasting Blood Sugar Distance': dFbs,
     'Resting ECG Distance': dRestEcg, 'Max Heart Rate Distance': dThalach, 'Exercise Induced Angina Distance': dExang, 'Oldpeak Distance': dOldpeak, 
     'Slope Distance': dSlope, 'Number of Vessels Distance': dNumVessels, 'Thalassemia Distance': dThal, 'Heart Disease Distance': dHeart,}
t3 = pd.DataFrame(data=d)

# Task 3: Electric Boogaloo
t3Adj = pd.DataFrame(['age'])
agg = []
def normalize(i, df, attr):
    return (df[attr][i] - df[attr].min())/(df[attr].max()-df[attr].min())
    
for i in range(len(pairs)):
    res = 0
    
    # Age
    res += normalize(i,t3, 'Age Distance')
    
    # Gender
    res += t3['Gender Distance'][i]
    
    # Chest Pain Type Distance
    res += t3['Chest Pain Type Distance'][i]
    
    # Resting BP Distance
    res += normalize(i, t3, 'Resting Blood Pressure Distance')
    
    # Serum Chol Distance
    res += normalize(i, t3, 'Serum Cholesterol Distance')
    
    # FBS Distance
    res += t3['Fasting Blood Sugar Distance'][i]
   
    # Resting ECG Distance 
    res += t3['Resting ECG Distance'][i]
    
    # Max Heart Rate Distance 
    res += normalize(i, t3, 'Max Heart Rate Distance')
    
    # Exercise Induced Angina Distance
    res += t3['Exercise Induced Angina Distance'][i]
    
    # Old Peak Distance
    res += normalize(i, t3, 'Oldpeak Distance')
    
    # Slope Distance
    res += t3['Slope Distance'][i]

    # Number of Vessels Distance
    res += normalize(i, t3, 'Number of Vessels Distance')
    
    # Thalassemia Distance
    res += t3['Thalassemia Distance'][i]
    
    # Heart Disease Distance
    res += t3['Heart Disease Distance'][i]
    
    agg.append(res/14)

d = {'pairs': pairs, 'Aggregate Dissimilarity': agg}
t3Agg = pd.DataFrame(data=d)
t3Agg, t3Agg.min(axis=1)

t3Agg['Aggregate Dissimilarity'].idxmin(), t3Agg['Aggregate Dissimilarity'].idxmax()
t3.loc[3082].values

# Writing to CSV
t3.to_csv('t3p1.csv', index=False)
t3Agg.to_csv('t3p2.csv', index=False)