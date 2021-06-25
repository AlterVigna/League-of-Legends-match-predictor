#!/usr/bin/env python
# coding: utf-8

# In[9]:


#This method has been implemented to avoid to have missing categorical values during the prediction.
def OneHotEncoding(dfTot,prefix,listOfValues):
    row=dfTot.iloc[0]
    # Adding a duplicate row for each possibile categorical value
    for val in listOfValues:
         dfTot=dfTot.append(row,ignore_index=True)
   
    #Assign to each new row the possible value
    i=0
    for val in listOfValues:
        i=i+1
        dfTot.iloc[len(dfTot.index)-i,dfTot.columns.get_loc(prefix)]=val
        
    # Splitting the columns for each possibile combination
    y = pd.get_dummies(dfTot[prefix], prefix=prefix)
    
    #Assigning to the original Dataframe.
    for val in listOfValues:
        dfTot[prefix+'_'+val]=y[prefix+'_'+val]
        
    #Removing the added dummy rows.    
    for val in listOfValues:
        dfTot = dfTot[:-1]
    return dfTot


# In[10]:


def featureCostruction(dfTot):
    #Diff Domination Ratio 
    dfTot['BLUE_10MinDomRatio']=((2*dfTot.BLUE_10Min_kill)+dfTot.BLUE_10Min_assist)/(3*dfTot.BLUE_10Min_death).replace({ 0 : 1 })
    dfTot['BLUE_15MinDomRatio']=((2*dfTot.BLUE_15Min_kill)+dfTot.BLUE_15Min_assist)/(3*dfTot.BLUE_15Min_death).replace({ 0 : 1 })
    dfTot['RED_10MinDomRatio']=((2*dfTot.RED_10Min_kill)+dfTot.RED_10Min_assist)/(3*dfTot.RED_10Min_death).replace({ 0 : 1 })
    dfTot['RED_15MinDomRatio']=((2*dfTot.RED_15Min_kill)+dfTot.RED_15Min_assist)/(3*dfTot.RED_15Min_death).replace({ 0 : 1 })
    
    #Diff Ward score
    dfTot['BLUE_diffWardPlaced']=(dfTot['BLUE_15Min_wardPlaced']-dfTot['RED_15Min_wardKill'])-(dfTot['BLUE_10Min_wardPlaced']-dfTot['RED_10Min_wardKill'])
    dfTot['RED_diffWardPlaced']=(dfTot['RED_15Min_wardPlaced']-dfTot['BLUE_15Min_wardKill'])-(dfTot['RED_10Min_wardPlaced']-dfTot['BLUE_10Min_wardKill'])
    return dfTot


# In[11]:


def featureExtraction(dfTot):
    
    # Diff level
    dfTot['BLUE_diffLevel'] = dfTot['BLUE_15Min_totLevel'] - dfTot['BLUE_10Min_totLevel']
    dfTot['RED_diffLevel'] = dfTot['RED_15Min_totLevel'] - dfTot['RED_10Min_totLevel']
    dfTot['diffLevel']=dfTot['RED_diffLevel']-dfTot['BLUE_diffLevel']

    # Diff minions
    dfTot['BLUE_diffMinions'] = dfTot['BLUE_15Min_totMinionsKilled'] - dfTot['BLUE_10Min_totMinionsKilled']
    dfTot['RED_diffMinions'] = dfTot['RED_15Min_totMinionsKilled'] - dfTot['RED_10Min_totMinionsKilled']
    dfTot['diffMinions']=dfTot['RED_diffMinions']-dfTot['BLUE_diffMinions']

    # Diff jungle minions
    dfTot['BLUE_diffJglMinions'] = dfTot['BLUE_15Min_totJnglMinionsKilled'] - dfTot['BLUE_10Min_totJnglMinionsKilled']
    dfTot['RED_diffJglMinions'] = dfTot['RED_15Min_totJnglMinionsKilled'] - dfTot['RED_10Min_totJnglMinionsKilled']
    dfTot['diffJglMinions']=dfTot['RED_diffJglMinions']-dfTot['BLUE_diffJglMinions']
    
    #Diff DomRation
    dfTot['BLUE_diffDomRatio']=dfTot['BLUE_15MinDomRatio']-dfTot['BLUE_10MinDomRatio']
    dfTot['RED_diffDomRatio']=dfTot['RED_15MinDomRatio']-dfTot['RED_10MinDomRatio']
    dfTot['diffDomRatio']=dfTot['RED_diffDomRatio']-dfTot['BLUE_diffDomRatio']

    #Diff tower kills
    dfTot['BLUE_diffTowers']=dfTot['BLUE_15Min_towerKills'] - dfTot['BLUE_10Min_towerKills']
    dfTot['RED_diffTowers']=dfTot['RED_15Min_towerKills'] - dfTot['RED_10Min_towerKills']
    dfTot['diffTowers']=dfTot['RED_diffTowers']-dfTot['BLUE_diffTowers']

    #Diff Hinibitor
    dfTot['diffInhibitors15']=dfTot['RED_15Min_inhibitors'] - dfTot['BLUE_15Min_inhibitors']
    
    #Diff Dragons
    dfTot['BLUE_diffDragons']=dfTot['BLUE_15Min_dragons']-dfTot['BLUE_10Min_dragons']
    dfTot['RED_diffDragons']=dfTot['RED_15Min_dragons']-dfTot['RED_10Min_dragons']
    dfTot['diffDragons']=dfTot['RED_diffDragons']-dfTot['BLUE_diffDragons']

    #Diff RifthHeralds
    dfTot['BLUE_diffHeralds']=dfTot['BLUE_15Min_riftHeralds']-dfTot['BLUE_10Min_riftHeralds']
    dfTot['RED_diffHeralds']=dfTot['RED_15Min_riftHeralds']-dfTot['RED_10Min_riftHeralds']
    dfTot['diffHeralds']=dfTot['RED_diffHeralds']-dfTot['BLUE_diffHeralds']
    
    #Diff total gold earned
    dfTot['BLUE_diffTotGold']=dfTot['BLUE_15Min_totalGold']-dfTot['BLUE_10Min_totalGold']
    dfTot['RED_diffTotGold']=dfTot['RED_15Min_totalGold']-dfTot['RED_10Min_totalGold']
    dfTot['diffTotGold']=dfTot['RED_diffTotGold']-dfTot['BLUE_diffTotGold']

    #Diff gold available
    dfTot['BLUE_diffTotGoldAvailable']=dfTot['BLUE_15Min_currentGold']-dfTot['BLUE_10Min_currentGold']
    dfTot['RED_diffTotGoldAvailable']=dfTot['RED_15Min_currentGold']-dfTot['RED_10Min_currentGold']
    dfTot['diffTotGoldAvailable']=dfTot['RED_diffTotGoldAvailable']-dfTot['BLUE_diffTotGoldAvailable']
    
    #diff Ward Vision
    dfTot['diffWardVision']=dfTot['RED_diffWardPlaced']-dfTot['BLUE_diffWardPlaced']
    return dfTot


# In[12]:


def featureTransformation(dfTot):
    
    #First kill
    dfTot["firstKill15"]=(((dfTot["BLUE_15Min_firstKill"]-dfTot["RED_15Min_firstKill"]).astype(int)).replace({-1 : 2})).astype(str)

    #First tower
    dfTot["firstTower10"]=(((dfTot["BLUE_10Min_firstTower"]-dfTot["RED_10Min_firstTower"]).astype(int)).replace({-1 : 2})).astype(str)
    dfTot["firstTower15"]=(((dfTot["BLUE_15Min_firstTower"]-dfTot["RED_15Min_firstTower"]).astype(int)).replace({-1 : 2})).astype(str)

    #First Inhibitor
    dfTot["firstInhibitor"]=(((dfTot["BLUE_15Min_firstInhibitor"]-dfTot["RED_15Min_firstInhibitor"]).astype(int)).replace({-1 : 2})).astype(str)

    #First Dragon
    dfTot["firstDragon10"]=(((dfTot["BLUE_10Min_firstDragon"]-dfTot["RED_10Min_firstDragon"]).astype(int)).replace({-1 : 2})).astype(str)
    dfTot["firstDragon15"]=(((dfTot["BLUE_15Min_firstDragon"]-dfTot["RED_15Min_firstDragon"]).astype(int)).replace({-1 : 2})).astype(str)
    
    #First Tower lane
    dfTot["BLUE_firstTowerLane"]=dfTot["BLUE_15Min_firstTowerLane"]
    dfTot["RED_firstTowerLane"]=dfTot["RED_15Min_firstTowerLane"]
    
    #Treat nominal data
    dfTot=OneHotEncoding(dfTot,"firstKill15",["1","2"])
    dfTot=OneHotEncoding(dfTot,"firstTower10",["0","1","2"])
    dfTot=OneHotEncoding(dfTot,"firstTower15",["0","1","2"])
    dfTot=OneHotEncoding(dfTot,"firstInhibitor",["0","1","2"])
    dfTot=OneHotEncoding(dfTot,"firstDragon10",["0","1","2"])
    dfTot=OneHotEncoding(dfTot,"firstDragon15",["0","1","2"])
    dfTot=OneHotEncoding(dfTot,"BLUE_firstTowerLane",["NONE","BOT_LANE","MID_LANE","TOP_LANE"])
    dfTot=OneHotEncoding(dfTot,"RED_firstTowerLane",["NONE","BOT_LANE","MID_LANE","TOP_LANE"])
    return dfTot


# In[13]:


from sklearn.preprocessing import LabelEncoder
def classEncoding(dfTot):
    dfTot['Team_Win']="0"
    dfTot.loc[dfTot['BLUE_WIN'] == 1,['Team_Win']]="1"
    dfTot.loc[dfTot['RED_WIN'] == 1,['Team_Win']]="2"
    
    labelencoder = LabelEncoder()
    dfTot['Team_Win'] = labelencoder.fit_transform(dfTot['Team_Win'])
    return dfTot


# In[14]:


def featureReduction(dfTot):
    dfTot=dfTot.drop(columns=['BLUE_WIN','RED_WIN','BLUE_diffLevel','RED_diffLevel','BLUE_15Min_totLevel','BLUE_10Min_totLevel','RED_diffLevel','RED_15Min_totLevel','RED_10Min_totLevel',
                             'BLUE_15Min_totMinionsKilled','BLUE_10Min_totMinionsKilled','BLUE_diffMinions','RED_15Min_totMinionsKilled','RED_10Min_totMinionsKilled','BLUE_diffMinions','RED_diffMinions',
                             'BLUE_15Min_totJnglMinionsKilled','BLUE_10Min_totJnglMinionsKilled','RED_15Min_totJnglMinionsKilled','RED_10Min_totJnglMinionsKilled','BLUE_diffJglMinions','RED_diffJglMinions',
                             'BLUE_10Min_kill','BLUE_10Min_assist','BLUE_10Min_death','BLUE_15Min_kill','BLUE_15Min_assist','BLUE_15Min_death','RED_10Min_kill','RED_10Min_assist','RED_10Min_death',
                             'RED_15Min_kill','RED_15Min_assist','RED_15Min_death',
                             'BLUE_10MinDomRatio','BLUE_15MinDomRatio','RED_10MinDomRatio','RED_15MinDomRatio','BLUE_diffDomRatio','RED_diffDomRatio',
                             'BLUE_10Min_firstKill','RED_10Min_firstKill','BLUE_15Min_firstKill','RED_15Min_firstKill',
                             'BLUE_10Min_firstTower','BLUE_15Min_firstTower','RED_10Min_firstTower','RED_15Min_firstTower',
                             'BLUE_10Min_firstInhibitor','RED_10Min_firstInhibitor','BLUE_15Min_firstInhibitor','RED_15Min_firstInhibitor',
                             'BLUE_10Min_firstDragon','RED_10Min_firstDragon','BLUE_15Min_firstDragon','RED_15Min_firstDragon',
                             'BLUE_10Min_towerKills','RED_10Min_towerKills','BLUE_15Min_towerKills','RED_15Min_towerKills','BLUE_diffTowers','RED_diffTowers',
                             'BLUE_10Min_inhibitors','BLUE_15Min_inhibitors','RED_10Min_inhibitors','RED_15Min_inhibitors',
                             'BLUE_10Min_dragons','RED_10Min_dragons','BLUE_15Min_dragons','RED_15Min_dragons','BLUE_diffDragons','RED_diffDragons',
                             'BLUE_10Min_riftHeralds','RED_10Min_riftHeralds','BLUE_15Min_riftHeralds','RED_15Min_riftHeralds','BLUE_diffHeralds','RED_diffHeralds',
                             'BLUE_15Min_wardPlaced','RED_15Min_wardKill','BLUE_10Min_wardPlaced','RED_10Min_wardKill','RED_15Min_wardPlaced','BLUE_15Min_wardKill','RED_10Min_wardPlaced','BLUE_10Min_wardKill','BLUE_diffWardPlaced','RED_diffWardPlaced',
                             'BLUE_15Min_totalGold','BLUE_10Min_totalGold','RED_10Min_totalGold','RED_15Min_totalGold','BLUE_diffTotGold','RED_diffTotGold',
                             'BLUE_15Min_currentGold','BLUE_10Min_currentGold','RED_15Min_currentGold','RED_10Min_currentGold','BLUE_diffTotGoldAvailable','RED_diffTotGoldAvailable',
                             'BLUE_10Min_firstTowerLane','BLUE_15Min_firstTowerLane','RED_10Min_firstTowerLane','RED_15Min_firstTowerLane',
                             'gameId','firstKill15','firstTower10','firstTower15','firstInhibitor','firstDragon10','firstDragon15','BLUE_firstTowerLane','RED_firstTowerLane'             
                             ])
    return dfTot


# In[15]:


import numpy as np
import pandas as pd

#Get the RawDataset as parameter and trasform it in appropriate form.
def preProcess(dfTot):
    dfTot=classEncoding(dfTot)
    dfTot=featureCostruction(dfTot)
    dfTot=featureExtraction(dfTot)
    dfTot=featureTransformation(dfTot)
    dfTot=featureReduction(dfTot)
    return dfTot


# In[ ]:




