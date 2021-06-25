#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import pickle
import sys
sys.path.append("scripts")
from PreProcessingRawData import *
#import PreProcessingRawData
from flask import Flask, render_template, request,json,jsonify

modelName = "./scripts/trainedModel.pkl"  
with open(modelName, 'rb') as file:  
    pipe = pickle.load(file)
	
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

#Read the request GET params
def readParams(request):
	
	BLUE_LEVEL_10 = int(request.args.get('BLUE_LEVEL_10'))
	BLUE_LEVEL_15 = int(request.args.get('BLUE_LEVEL_15'))
	BLUE_CURR_GOLD_10=int(request.args.get('BLUE_CURR_GOLD_10'))
	BLUE_CURR_GOLD_15=int(request.args.get('BLUE_CURR_GOLD_15'))
	BLUE_TOT_GOLD_10=int(request.args.get('BLUE_TOT_GOLD_10'))
	BLUE_TOT_GOLD_15=int(request.args.get('BLUE_TOT_GOLD_15'))
	BLUE_TOT_MINIONS_10=int(request.args.get('BLUE_TOT_MINIONS_10'))
	BLUE_TOT_MINIONS_15=int(request.args.get('BLUE_TOT_MINIONS_15'))
	BLUE_TOTJNG_MINIONS_10=int(request.args.get('BLUE_TOTJNG_MINIONS_10'))
	BLUE_TOTJNG_MINIONS_15=int(request.args.get('BLUE_TOTJNG_MINIONS_15'))
	BLUE_DRAGONS_10=int(request.args.get('BLUE_DRAGONS_10'))
	BLUE_DRAGONS_15=int(request.args.get('BLUE_DRAGONS_15'))
	BLUE_HERALDS_10=int(request.args.get('BLUE_HERALDS_10'))
	BLUE_HERALDS_15=int(request.args.get('BLUE_HERALDS_15'))
	BLUE_inhibitors_10=int(request.args.get('BLUE_inhibitors_10'))
	BLUE_inhibitors_15=int(request.args.get('BLUE_inhibitors_15'))
	BLUE_TOT_KILLS_10=int(request.args.get('BLUE_TOT_KILLS_10'))
	BLUE_TOT_KILLS_15=int(request.args.get('BLUE_TOT_KILLS_15'))
	BLUE_TOT_DEATH_10=int(request.args.get('BLUE_TOT_DEATH_10'))
	BLUE_TOT_DEATH_15=int(request.args.get('BLUE_TOT_DEATH_15'))
	BLUE_TOT_ASSIST_10=int(request.args.get('BLUE_TOT_ASSIST_10'))
	BLUE_TOT_ASSIST_15=int(request.args.get('BLUE_TOT_ASSIST_15'))
	BLUE_towers_10=int(request.args.get('BLUE_towers_10'))
	BLUE_towers_15=int(request.args.get('BLUE_towers_15'))
	BLUE_WARD_PLACED_10=int(request.args.get('BLUE_WARD_PLACED_10'))
	BLUE_WARD_PLACED_15=int(request.args.get('BLUE_WARD_PLACED_15'))
	BLUE_WARD_DESTR_10=int(request.args.get('BLUE_WARD_DESTR_10'))
	BLUE_WARD_DESTR_15=int(request.args.get('BLUE_WARD_DESTR_15'))
	BLUE_firstKill=int(request.args.get('BLUE_firstKill'))
	BLUE_firstTower10=int(request.args.get('BLUE_firstTower10'))
	BLUE_firstTower15=int(request.args.get('BLUE_firstTower15'))
	BLUE_firstDragon10=int(request.args.get('BLUE_firstDragon10'))
	BLUE_firstDragon15=int(request.args.get('BLUE_firstDragon15'))
	BLUE_firstInhibitor=int(request.args.get('BLUE_firstInhibitor'))
	BLUE_firstTowerLane=request.args.get('BLUE_firstTowerLane')
	
	RED_LEVEL_10=int(request.args.get('RED_LEVEL_10'))
	RED_LEVEL_15=int(request.args.get('RED_LEVEL_15'))
	RED_CURR_GOLD_10=int(request.args.get('RED_CURR_GOLD_10'))
	RED_CURR_GOLD_15=int(request.args.get('RED_CURR_GOLD_15'))
	RED_TOT_GOLD_10=int(request.args.get('RED_TOT_GOLD_10'))
	RED_TOT_GOLD_15=int(request.args.get('RED_TOT_GOLD_15'))
	RED_TOT_MINIONS_10=int(request.args.get('RED_TOT_MINIONS_10'))
	RED_TOT_MINIONS_15=int(request.args.get('RED_TOT_MINIONS_15'))
	RED_TOTJNG_MINIONS_10=int(request.args.get('RED_TOTJNG_MINIONS_10'))
	RED_TOTJNG_MINIONS_15=int(request.args.get('RED_TOTJNG_MINIONS_15'))
	RED_DRAGONS_10=int(request.args.get('RED_DRAGONS_10'))
	RED_DRAGONS_15=int(request.args.get('RED_DRAGONS_15'))
	RED_HERALDS_10=int(request.args.get('RED_HERALDS_10'))
	RED_HERALDS_15=int(request.args.get('RED_HERALDS_15'))
	RED_inhibitors_10=int(request.args.get('RED_inhibitors_10'))
	RED_inhibitors_15=int(request.args.get('RED_inhibitors_15'))
	RED_TOT_KILLS_10=int(request.args.get('RED_TOT_KILLS_10'))
	RED_TOT_KILLS_15=int(request.args.get('RED_TOT_KILLS_15'))
	RED_TOT_DEATH_10=int(request.args.get('RED_TOT_DEATH_10'))
	RED_TOT_DEATH_15=int(request.args.get('RED_TOT_DEATH_15'))
	RED_TOT_ASSIST_10=int(request.args.get('RED_TOT_ASSIST_10'))
	RED_TOT_ASSIST_15=int(request.args.get('RED_TOT_ASSIST_15'))
	RED_towers_10=int(request.args.get('RED_towers_10'))
	RED_towers_15=int(request.args.get('RED_towers_15'))
	RED_WARD_PLACED_10=int(request.args.get('RED_WARD_PLACED_10'))
	RED_WARD_PLACED_15=int(request.args.get('RED_WARD_PLACED_15'))
	RED_WARD_DESTR_10=int(request.args.get('RED_WARD_DESTR_10'))
	RED_WARD_DESTR_15=int(request.args.get('RED_WARD_DESTR_15'))
	RED_firstKill=int(request.args.get('RED_firstKill'))
	RED_firstTower10=int(request.args.get('RED_firstTower10'))
	RED_firstTower15=int(request.args.get('RED_firstTower15'))
	RED_firstDragon10=int(request.args.get('RED_firstDragon10'))
	RED_firstDragon15=int(request.args.get('RED_firstDragon15'))
	RED_firstInhibitor=int(request.args.get('RED_firstInhibitor'))
	RED_firstTowerLane=request.args.get('RED_firstTowerLane')
	
	matches=[]
	matches.append({"gameId":"000",
					"BLUE_WIN":"?","RED_WIN":"?",
					"BLUE_10Min_totLevel": BLUE_LEVEL_10 , "BLUE_15Min_totLevel": BLUE_LEVEL_15,"RED_10Min_totLevel":RED_LEVEL_10,"RED_15Min_totLevel":RED_LEVEL_15,
					"BLUE_10Min_totMinionsKilled":BLUE_TOT_MINIONS_10,"BLUE_15Min_totMinionsKilled":BLUE_TOT_MINIONS_15,"RED_10Min_totMinionsKilled":RED_TOT_MINIONS_10,"RED_15Min_totMinionsKilled":RED_TOT_MINIONS_15,
					"BLUE_10Min_totJnglMinionsKilled":BLUE_TOTJNG_MINIONS_10,"BLUE_15Min_totJnglMinionsKilled":BLUE_TOTJNG_MINIONS_15, "RED_10Min_totJnglMinionsKilled":RED_TOTJNG_MINIONS_10,"RED_15Min_totJnglMinionsKilled":RED_TOTJNG_MINIONS_15,
					"BLUE_10Min_kill":BLUE_TOT_KILLS_10,"BLUE_15Min_kill":BLUE_TOT_KILLS_15,"RED_10Min_kill":RED_TOT_KILLS_10,"RED_15Min_kill":RED_TOT_KILLS_15,
					"BLUE_10Min_assist":BLUE_TOT_ASSIST_10,"BLUE_15Min_assist":BLUE_TOT_ASSIST_15,"RED_10Min_assist":RED_TOT_ASSIST_10,"RED_15Min_assist":RED_TOT_ASSIST_15,
					"BLUE_10Min_death":BLUE_TOT_DEATH_10,"BLUE_15Min_death":BLUE_TOT_DEATH_15,"RED_10Min_death":RED_TOT_DEATH_10,"RED_15Min_death":RED_TOT_DEATH_15,
					"BLUE_10Min_towerKills":BLUE_towers_10,"BLUE_15Min_towerKills":BLUE_towers_15,"RED_10Min_towerKills":RED_towers_10,"RED_15Min_towerKills":RED_towers_15,
					"BLUE_10Min_inhibitors":BLUE_inhibitors_10,"BLUE_15Min_inhibitors":BLUE_inhibitors_15,"RED_10Min_inhibitors":RED_inhibitors_10,"RED_15Min_inhibitors":RED_inhibitors_15,
					"BLUE_10Min_dragons":BLUE_DRAGONS_10,"BLUE_15Min_dragons":BLUE_DRAGONS_15,"RED_10Min_dragons":RED_DRAGONS_10,"RED_15Min_dragons":RED_DRAGONS_15,
					"BLUE_10Min_riftHeralds":BLUE_HERALDS_10,"BLUE_15Min_riftHeralds":BLUE_HERALDS_15,"RED_10Min_riftHeralds":RED_HERALDS_10,"RED_15Min_riftHeralds":RED_HERALDS_15,
					"BLUE_10Min_wardPlaced":BLUE_WARD_PLACED_10,"BLUE_15Min_wardPlaced":BLUE_WARD_PLACED_15,"RED_10Min_wardPlaced":RED_WARD_PLACED_10,"RED_15Min_wardPlaced":RED_WARD_PLACED_15,
					"BLUE_10Min_wardKill":BLUE_WARD_DESTR_10,"BLUE_15Min_wardKill":BLUE_WARD_DESTR_15,"RED_10Min_wardKill":RED_WARD_DESTR_10,"RED_15Min_wardKill":RED_WARD_DESTR_15,
					"BLUE_10Min_totalGold":BLUE_TOT_GOLD_10,"BLUE_15Min_totalGold":BLUE_TOT_GOLD_15,"RED_10Min_totalGold":RED_TOT_GOLD_10,"RED_15Min_totalGold":RED_TOT_GOLD_15,
					"BLUE_10Min_currentGold":BLUE_CURR_GOLD_10,"BLUE_15Min_currentGold":BLUE_CURR_GOLD_15,"RED_10Min_currentGold":RED_CURR_GOLD_10,"RED_15Min_currentGold":RED_CURR_GOLD_15,
					"BLUE_10Min_firstKill":BLUE_firstKill,"BLUE_15Min_firstKill":BLUE_firstKill,"RED_10Min_firstKill":RED_firstKill,"RED_15Min_firstKill":RED_firstKill,"BLUE_10Min_firstTower":BLUE_firstTower10,"RED_10Min_firstTower":RED_firstTower10,
					"BLUE_15Min_firstTower":BLUE_firstTower15,"RED_15Min_firstTower":RED_firstTower15,
					"BLUE_10Min_firstInhibitor":BLUE_firstInhibitor,"BLUE_15Min_firstInhibitor":BLUE_firstInhibitor,"RED_10Min_firstInhibitor":RED_firstInhibitor,"RED_15Min_firstInhibitor":RED_firstInhibitor,
					"BLUE_10Min_firstDragon":BLUE_firstDragon10,"BLUE_15Min_firstDragon":BLUE_firstDragon15,"RED_10Min_firstDragon":RED_firstDragon10,"RED_15Min_firstDragon":RED_firstDragon15,
					"BLUE_10Min_firstTowerLane":BLUE_firstTowerLane,"BLUE_15Min_firstTowerLane":BLUE_firstTowerLane,"RED_10Min_firstTowerLane":RED_firstTowerLane,"RED_15Min_firstTowerLane":RED_firstTowerLane}
					)
	totDataFrame=pd.DataFrame(matches)
	
	totDataFrame = totDataFrame[['gameId','BLUE_WIN','BLUE_10Min_currentGold','BLUE_10Min_totalGold','BLUE_10Min_totLevel','BLUE_10Min_totMinionsKilled','BLUE_10Min_totJnglMinionsKilled','BLUE_10Min_firstKill','BLUE_10Min_kill','BLUE_10Min_death','BLUE_10Min_assist','BLUE_10Min_wardPlaced','BLUE_10Min_wardKill','BLUE_10Min_firstTower','BLUE_10Min_firstInhibitor','BLUE_10Min_firstTowerLane','BLUE_10Min_towerKills','BLUE_10Min_inhibitors','BLUE_10Min_firstDragon','BLUE_10Min_dragons','BLUE_10Min_riftHeralds','BLUE_15Min_currentGold','BLUE_15Min_totalGold','BLUE_15Min_totLevel','BLUE_15Min_totMinionsKilled','BLUE_15Min_totJnglMinionsKilled','BLUE_15Min_firstKill','BLUE_15Min_kill','BLUE_15Min_death','BLUE_15Min_assist','BLUE_15Min_wardPlaced','BLUE_15Min_wardKill','BLUE_15Min_firstTower','BLUE_15Min_firstInhibitor','BLUE_15Min_firstTowerLane','BLUE_15Min_towerKills','BLUE_15Min_inhibitors','BLUE_15Min_firstDragon','BLUE_15Min_dragons','BLUE_15Min_riftHeralds','RED_WIN','RED_10Min_currentGold','RED_10Min_totalGold','RED_10Min_totLevel','RED_10Min_totMinionsKilled','RED_10Min_totJnglMinionsKilled','RED_10Min_firstKill','RED_10Min_kill','RED_10Min_death','RED_10Min_assist','RED_10Min_wardPlaced','RED_10Min_wardKill','RED_10Min_firstTower','RED_10Min_firstInhibitor','RED_10Min_firstTowerLane','RED_10Min_towerKills','RED_10Min_inhibitors','RED_10Min_firstDragon','RED_10Min_dragons','RED_10Min_riftHeralds','RED_15Min_currentGold','RED_15Min_totalGold','RED_15Min_totLevel','RED_15Min_totMinionsKilled','RED_15Min_totJnglMinionsKilled','RED_15Min_firstKill','RED_15Min_kill','RED_15Min_death','RED_15Min_assist','RED_15Min_wardPlaced','RED_15Min_wardKill','RED_15Min_firstTower','RED_15Min_firstInhibitor','RED_15Min_firstTowerLane','RED_15Min_towerKills','RED_15Min_inhibitors','RED_15Min_firstDragon','RED_15Min_dragons','RED_15Min_riftHeralds']]
	
	print(totDataFrame.dtypes)
	
	totDataFrame.set_index("gameId")
	totDataFrame.to_csv('rowInstance.csv',index=False)
	
	return totDataFrame





# "http://127.0.0.1:5000/makePrediction?&
@app.route('/makePrediction',methods=['GET'])
def makePrediction():

	newRowInstance=readParams(request)
	newInstance=preProcess(newRowInstance)
	newInstance.to_csv('preProcessedInstance.csv',index=False)
	
	newInstance=pd.read_csv('preProcessedInstance.csv')
	
	X_DataTest=newInstance.loc[:, 'diffLevel':]
	
	yResult=pipe.predict(X_DataTest)
	print("Result: "+str(yResult[0]))
	if (yResult[0]==0):
		answer={"winner":"BLUE"}
	else:
		answer={"winner":"RED"}

	return jsonify(answer)

if __name__ == "__main__":
    app.run()
    





