#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Inizialization of the team's variable
def initScore(teams,prefix):
    for keyteam in teams:
        if ((keyteam =="team1") or (keyteam =="team2")):
            team=teams[keyteam]
            team[prefix]={}
            team[prefix]["currentGold"]=0
            team[prefix]["totalGold"]=0
            team[prefix]["totLevel"]=0
            team[prefix]["totMinionsKilled"]=0
            team[prefix]["totJnglMinionsKilled"]=0
            team[prefix]["firstKill"]=0
            team[prefix]["kill"]=0
            team[prefix]["death"]=0
            team[prefix]["assist"]=0
            team[prefix]["wardPlaced"]=0
            team[prefix]["wardKill"]=0
            team[prefix]["firstTower"]=0
            team[prefix]["firstInhibitor"]=0
            team[prefix]["firstTowerLane"]='NONE'
            team[prefix]["towerKills"]=0
            team[prefix]["inhibitors"]=0
            team[prefix]["firstDragon"]=0
            team[prefix]["dragons"]=0
            team[prefix]["riftHeralds"]=0
            team[prefix]["firstTowerFlag"]=False 


# In[ ]:


# Retrive information abouts who has partecipated to a match, what his/her id is and the duration in terms of millis.
# If the variable winOrLose is set to true, then even the match esit will be retrived.
def getTeamBasicInfo(script,scriptTIMELINE,teams,winOrLose):
    for player in script['participants']:
        teamId=player["teamId"]
        if teams.get(teamId)== None:
            obj={}
            obj["idPlayers"]=[player["participantId"]]
            obj["teamId"]=teamId
            teams[teamId]=obj
        else:
            teams[teamId].get("idPlayers").append(player["participantId"])
  
    for team in script["teams"]:
        teamId=team["teamId"]
        if (winOrLose == True):
            result=team["win"]
            teams[teamId]["win"]= 1 if result == "Win" else 0
        else:
            teams[teamId]["win"]="?"          
    res = list(teams.keys())[0]
    teams['team1'] = teams.pop(list(teams.keys())[0])
    teams['team2'] = teams.pop(list(teams.keys())[0])
    teams["gameId"]=script["gameId"]
    teams["gameDuration"]=scriptTIMELINE["frames"][-1]["timestamp"] 


# In[ ]:


#Extraciton of following information in the timeline game:
#FirstBlood,Kill,Death,Assist,WardPlaced,WardKills,FirstTower,FirstInhibitor,FirstTowerLane,TowerKills,Inhibitor,FirstDragon,Dragon,RiftHeralds
#rangeAtMillis indicates the number of milliseconds from the beginning to be considered. It represents the max time to stop the elaboration.
def extractTimelineInfo(teams,script,rangeAtMillis,prefix):
    firstKill=False
    firstTower=False
    firstInhibitor=False
    firstDragon=False
    for frame in script["frames"]:
            if (frame["timestamp"]<rangeAtMillis):
                for event in frame["events"]:

                    #Kill event
                    if (event["type"] == "CHAMPION_KILL"):
                        killer=event["killerId"]
                        killed=event["victimId"]
                        teamKiller={}
                        teamKilled={}
                        if (killer in teams.get("team1").get("idPlayers")):
                            teamKiller=teams.get('team1')
                            teamKilled=teams.get('team2')
                        if (killer in teams.get("team2").get("idPlayers")):
                            teamKiller=teams.get('team2')
                            teamKilled=teams.get('team1')
                        
                        #Tower neutral kill (Suicide champ)
                        if (killer == 0):
                            if (killed in teams.get("team1").get("idPlayers")):
                                teamKiller=teams.get('team2')
                                teamKilled=teams.get('team1')
                            if (killed in teams.get("team2").get("idPlayers")):
                                teamKiller=teams.get('team1')
                                teamKilled=teams.get('team2')
                            
                        teamKiller[prefix]["kill"]+=1
                        teamKilled[prefix]["death"]+=1
                        #Setting the number of assists
                        if (event["assistingParticipantIds"] !=None):
                            teamKiller[prefix]["assist"]+=len(event["assistingParticipantIds"])
                        #Setting the first kill
                        if (firstKill == False):
                            firstKill=True
                            teamKiller[prefix]["firstKill"]=1
                            teamKilled[prefix]["firstKill"]=0
                            
                    #Ward placed event     
                    if( event["type"] == "WARD_PLACED" ):
                        if (event["wardType"] != "UNDEFINED"):
                            team={}
                            player=event["creatorId"]
                            if (player in teams.get("team1").get("idPlayers")):
                                team=teams.get('team1')
                            if (player in teams.get("team2").get("idPlayers")):
                                team=teams.get('team2')
                            team[prefix]["wardPlaced"]+=1
                    
                    #Enemy Ward killed event
                    if (event["type"] == "WARD_KILL"):
                        team={}
                        player=event["killerId"]
                        if (player in teams.get("team1").get("idPlayers")):
                            team=teams.get('team1')
                        if (player in teams.get("team2").get("idPlayers")):
                            team=teams.get('team2')
                        team[prefix]["wardKill"]+=1
                    
                    #Enemy Building killed event
                    if (event["type"] == "BUILDING_KILL"):
                        
                        team={}
                        player=event["killerId"]
                        if (player in teams.get("team1").get("idPlayers")):
                            team=teams.get('team1')
                        if (player in teams.get("team2").get("idPlayers")):
                            team=teams.get('team2')
                            
                        #Da finire casistica kill con player vuoto.  
                        if (player == 0):
                           
                            teamId=event["teamId"]
                            if (teams.get("team1").get("teamId") == teamId):
                                team=teams.get("team2")
                            if (teams.get("team2").get("teamId") == teamId):
                                team=teams.get("team1")
                        
                        # Tower Killed
                        if (event["buildingType"] == "TOWER_BUILDING"):
                            team[prefix]["towerKills"]+=1
                            
                            if(firstTower == False):
                                firstTower=True
                                team[prefix]["firstTower"]=1
                                
                            if (team[prefix]["firstTowerFlag"] == False):
                                team[prefix]["firstTowerFlag"]=True
                                team[prefix]["firstTowerLane"]=event["laneType"]
                                
                        
                        #Inhibitor Kills
                        if (event["buildingType"] == "INHIBITOR_BUILDING"):
                            team[prefix]["inhibitors"]+=1
                            if (firstInhibitor == False):
                                firstInhibitor=True
                                team[prefix]["firstInhibitor"]=1
                        
                    #Elite Monster Kills
                    if (event["type"]=="ELITE_MONSTER_KILL"):   
                        team={}
                        player=event["killerId"]
                        if (player in teams.get("team1").get("idPlayers")):
                            team=teams.get('team1')
                        if (player in teams.get("team2").get("idPlayers")):
                            team=teams.get('team2')
                        
                        if (player != 0):
                            #Specific RiftHerald
                            if (event["monsterType"] == "RIFTHERALD"):
                                team[prefix]["riftHeralds"]+=1
                                
                            if (event["monsterType"] == "DRAGON"):
                                team[prefix]["dragons"]+=1

                                if (firstDragon == False):
                                    firstDragon=True
                                    team[prefix]["firstDragon"]=1  
    teams["team1"][prefix].pop('firstTowerFlag', None)
    teams["team2"][prefix].pop('firstTowerFlag', None)


# In[ ]:


#This method allows to capture specific information regurding the match: 
# - Summurization of gold,level,minions killed at specific minute, indicates as a range of milliseconds (rangeFromMillis)-(rangeAtMillis)
# - Retriving the other information of the match timeline until the rangeAtMillis.
def getAllMatchInformationAtMin(teams,script,rangeFromMillis,rangeAtMillis,prefix):

    initScore(teams,prefix)
    for frame in script["frames"]:
        if (frame["timestamp"]>rangeFromMillis and frame["timestamp"]<rangeAtMillis):
            print ('Find timeline at timestamp: ',frame["timestamp"])
            for key in frame["participantFrames"]:
                player=frame["participantFrames"].get(key)
                playerID=player.get("participantId")
                
                if (playerID in teams.get("team1").get("idPlayers")):
                    team=teams.get('team1')
                else:
                    team=teams.get('team2')

                c_gold=team[prefix].get("currentGold")
                if (player.get("currentGold") == None):
                    p_gold=0
                else :
                    p_gold=player.get("currentGold")

                c_gold+=p_gold
                team[prefix]["currentGold"]=c_gold

                t_gold=team[prefix].get("totalGold")
                if (player.get("totalGold")== None):
                    p_gold=0
                else:
                    p_gold=player.get("totalGold")

                t_gold+=p_gold
                team[prefix]["totalGold"]=t_gold

                t_lv=team[prefix].get("totLevel")
                if (player.get("level")== None):
                    p_lv=0
                else:
                    p_lv=player.get("level")
                t_lv+=p_lv
                team[prefix]["totLevel"]=t_lv
                
                t_mk=team[prefix].get("totMinionsKilled") 
                if (player.get("minionsKilled")== None):
                    p_mk=0
                else:
                    p_mk=player.get("minionsKilled")
                t_mk+=p_mk
                team[prefix]["totMinionsKilled"]=t_mk

                t_mkj=team[prefix].get("totJnglMinionsKilled")
                if (player.get("jungleMinionsKilled")== None):
                    p_mjk=0
                else:
                    p_mjk=player.get("jungleMinionsKilled")
                t_mkj+=p_mjk
                team[prefix]["totJnglMinionsKilled"]=t_mkj
    extractTimelineInfo(teams,script,rangeAtMillis,prefix) 


# In[ ]:


#Trasform a dict to one only row match, with all information of both teams (10Mins+15Mins)
def trasformInOneRowOnly(teams):
    singleDict={}
    singleDict["gameId"]=teams["gameId"]
    for key in teams["team1"]:
        if ( (key != "idPlayers") and (key!="teamId") and (key!="win")):
            for key2 in teams["team1"][key]:
                singleDict["BLUE"+"_"+key+"_"+key2]= teams["team1"][key][key2]
        if (key=="win"):
            singleDict["BLUE"+"_WIN"]=teams["team1"][key]

    for key in teams["team2"]:
        if ( (key != "idPlayers") and (key!="teamId") and (key!="win")):
            for key2 in teams["team1"][key]:
                singleDict["RED"+"_"+key+"_"+key2]= teams["team2"][key][key2]
        if (key=="win"):
            singleDict["RED"+"_WIN"]=teams["team2"][key]
    return singleDict

