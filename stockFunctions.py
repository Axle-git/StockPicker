import requests
from Constants import *
import re
import time
import datetime

def getTickerNumb(url):
    page = requests.get(url).text

    page = page.partition(YAHOO_TICKER_NUMB)[2]     #get rid of characters before number
    page = page[:page.index("<")]                   #get rid of after
    page = float(page.replace(',','')) #   remove commas + convert to float
    return page

def normalize(prices):

    stockIndex = 0

    for stock in prices:
        norm = [float(i)/sum(stock) for i in stock] #normalized so values sum to 1
        prices[stockIndex] = norm

        stockIndex += 1


    return prices

####        TO DO       ####
def stockToBuy(prices):

    return
####                    ####

def getSlopes(prices):
    allSlopes = []
    aveSlopes = []

    for stock in prices:    #   fills allSlopes with lists of slopes from each normalized stock
        slopes = []
        for i in range(len(stock) - 1):
            slopes.append(stock[i + 1] - stock[i])
        allSlopes.append(slopes)
    
    for i in len(allSlopes[0]):
        slopeSum = 0
        for j in allSlopes:
            slopeSum += j[i]
        aveSlopes.append(slopeSum/len(prices))

    return aveSlopes

def updateTxt(prices):
    open("stockValues.txt","w").close() #   clears text file
    f = open("stockValues.txt","w")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    x = 0 # indexer for prices
    for stock in TECH_TICKER_URLS:
        f.write(stock)
        f.write("\t: ")
        f.write(str(prices[x]))
        f.write("\n")
        x += 1
        
    f.close()

    return
