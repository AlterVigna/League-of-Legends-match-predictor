#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Scraping the RIOT Developer Portal starting from a gold level account in ranked matches.
#requestsCount, variabile containg the sent requests.

#RIOT - RATE LIMITS
#20 requests every 1 seconds(s)
#100 requests every 2 minutes(s)

import time
import requests
import json

listMatchID=[]
listAccountPlayer=["Ag-e1UJDjtlodgBfqw1yXw5gFtw8eL_B66VTFHWswvK64Jk"]
requestsCount=0
idxAccountViewed=0
MAX_NUM_MATCH_ID=26000

API_KEY=input('Insert the Riot API-KEY: ')
NUM_MATCH=input('How many match do you want to scrape (default 26000): ')

if (NUM_MATCH != "" and NUM_MATCH.isnumeric() ):
    MAX_NUM_MATCH_ID=int(NUM_MATCH)
print ("Starting extraction procedure...")
while (idxAccountViewed<len(listAccountPlayer) and (len(listMatchID)<MAX_NUM_MATCH_ID)):
   
    #For each account in the list, search all the match's id.
    appMatchIdList=[]
    while (idxAccountViewed<len(listAccountPlayer) and (len(listMatchID)<MAX_NUM_MATCH_ID)):
        if (requestsCount>=100):
                print ("Waiting 2 minutes for Riot's Rate Limit")
                time.sleep(120) 
                requestsCount=0 
        resp=requests.get("https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"+listAccountPlayer[idxAccountViewed]+"?api_key="+API_KEY+"&queue=420")
        jsonMatches=resp.json()
        idxAccountViewed+=1
        requestsCount+=1
        for elem in jsonMatches["matches"]:
            if (elem["gameId"] not in listMatchID):
                listMatchID.append(elem["gameId"])
                appMatchIdList.append(elem["gameId"])

    #For each new matchId found, search the other account's id participating.
    if (len(listMatchID)<MAX_NUM_MATCH_ID):
        for idMatch in appMatchIdList:
            print("Sending request for idMatch: "+str(idMatch))
            if (requestsCount>=100):
                print ("Waiting 2 minutes for Riot's Rate Limit")
                time.sleep(120) 
                requestsCount=0 
            ris=requests.get("https://euw1.api.riotgames.com/lol/match/v4/matches/"+str(idMatch)+"?api_key="+API_KEY)
            requestsCount+=1
            script=ris.json()
            try:
                for partecipant in script["participantIdentities"]:
                        if (partecipant["player"]["accountId"] not in listAccountPlayer):
                            listAccountPlayer.append(partecipant["player"]["accountId"])
            except:
                print("Error executing extraction accounts match id:"+str(idMatch))
print("Match id are succesifully extracted!")
with open('listMatchId.txt', 'w') as filehandle:
    json.dump(listMatchID, filehandle)
                    

