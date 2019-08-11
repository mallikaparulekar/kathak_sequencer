import numpy as np
import math


#startBeat is the beat where the user wants the tihai to start
#taalName is the name of the taal
    #if the user enters a name not in the dictionary, it prints taal not in dictionary, pls add it
#half beat palla means that the palla needs to oeither be a whole number of beats or whole number + 0.5 beats long
#pallaMult and gapMult set user constraints for pallas and gaps
#pallaGgap means palla needs to be greater than the gap


def tihaiMath(startBeat, taalName, pallaMult = 0.5, gapMult = 0.25, pallaGgap = True ):
    taalDict = {"Daadra": 6,
                "Rupak": 7,
                "Keherva": 8,
                "Jhaptaal": 10,
                "Ektaal": 11,
                "Dhamaar": 14,
                "Teentaal": 16,
                }
    if taalName not in taalDict.keys():
        return ("Taal not in existing dictionary, please update dictionary")
    
    cycleBeats = taalDict[taalName]
    tihaiTotalBeats = (cycleBeats-startBeat)+1
    maxPalla = maxPallaCalc(tihaiTotalBeats)
    #print("maxPalla", maxPalla)
    pallaGapdict = {}
    
    currentPalla = 0.5
    count = 1

    while(currentPalla <= maxPalla):
        currentGap = gapCalculator(tihaiTotalBeats, currentPalla)
        #checks if gap is a multiple of 0.5
        #print("currentGap", currentGap)
        #print("currentPalla", currentPalla)
        if ((currentGap % gapMult)==0):
            #print("cond satisfied")
            if pallaGgap:
                if currentPalla > currentGap:
                    #print("gap is small enough")
                    pallaGapdict["combination{}".format(count)]= np.array([currentPalla,currentGap])
                    count +=1
            else:
                 pallaGapdict["combination{}".format(count)]= np.array([currentPalla,currentGap])
                 count+=1
        currentPalla += pallaMult

    return pallaGapdict


def gapCalculator (totalBeats, pallaLength):
    gap = (totalBeats - 3*pallaLength)/2
    return gap


#divides into 3 and then finds the nearest palla by rounding down to the nearest half beat
def maxPallaCalc(totalBeats):
    #divides into 3
    rawVal = totalBeats/3
    #print(rawVal)

    #finds floor, ceiling and middle
    fl = math.floor(rawVal)
    #print(fl)
    ce = math.ceil(rawVal)
    #print(ce)
    mid = (fl + ce)/2
    #print(mid)

    #checks if rawVal is a whole number
    if (ce == fl):
        return ce
    #checks if rawVal is less than the mid
    if (rawVal < mid):
        return fl

    else:
        return mid





    #finds floor and ceiling

#example print
print(tihaiMath(3, "Jhaptaal", pallaGgap=True))





