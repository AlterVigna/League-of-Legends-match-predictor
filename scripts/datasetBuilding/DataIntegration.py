#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

print("For data integration:")
print("Be sure to put in the same folder of this script GoldMatchesDataset.csv and ChallengerMatchesDataset")

df1= pd.read_csv('GoldMatchesDataset.csv')
#Just to be scure
df1.drop_duplicates(subset=['gameId'])

df2= pd.read_csv('ChallengerMatchesDataset.csv')
df2.drop_duplicates(subset=['gameId'])

dfTot=pd.concat([df1, df2])
# #Shuffle the dataset
dfTot=dfTot.sample(frac=1)

#Remove some instances to have a balance dataset
win=dfTot[dfTot["BLUE_WIN"]==0]["BLUE_WIN"].count()
lose=dfTot[dfTot["BLUE_WIN"]==1]["BLUE_WIN"].count()

index = dfTot.index
if (win>lose):
    condition = (dfTot["BLUE_WIN"] == 0)
    diff=win-lose
else:
    condition = (dfTot["BLUE_WIN"] == 1)
    diff=lose-win

sel_indices = index[condition]

sel_indices_list = sel_indices.tolist()

rm_idx=sel_indices_list[-(diff+1):-1]
update_df = dfTot.drop(rm_idx)

print(update_df[update_df["BLUE_WIN"]==0]["BLUE_WIN"].count())
print(update_df[update_df["BLUE_WIN"]==1]["BLUE_WIN"].count())
update_df.to_csv('RawDataset.csv',index=False)


# In[54]:


dfTot["gameId"==4767097992]


# In[ ]:





# In[ ]:




