import pandas as pd
import matplotlib.pyplot as plt
import Name
data = pd.read_csv("Dataset.csv")
relative_data  = pd.DataFrame()
for i in  range(Name.del_day+1,len(data)):
    relative_data.append((data.iloc[i,2:] - data.iloc[i-Name.del_day,2:])/100)
    
print(relative_data)