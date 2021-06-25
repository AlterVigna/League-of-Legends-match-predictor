#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np 
import json

fileName=input('Insert file name to extract matchId: ')
#Download from link https://www.kaggle.com/fernandorubiogarcia/league-of-legends-high-elo-patch-1016
# fileName=10.16_LeagueOfLegends_Games.csv
dataSetExt1=pd.read_csv(fileName,sep = ';')

listMatchID=[]

for val in dataSetExt1["gameId"].values:
    listMatchID.append(int(val))
    

print("Match id are succesifully extracted!")
with open('listMatchId.txt', 'w') as filehandle:
    json.dump(listMatchID, filehandle)






