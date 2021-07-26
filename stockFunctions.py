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

def getSlopes(prices):  #   prices must already be normalized
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

def estGraph(priceSlopes,prices): # requires normalized prices

    points = []

    intercept = 0 # find start location
    for x in prices:
        intercept += x[0]
    intercept /= len(prices)
    points.append(intercept)

    previousPoint = 0
    for x in priceSlopes:
        points.append(x + points[previousPoint])
        previousPoint += 1

    return points

def leastSquaresByStock(points,prices): #   requires normalized prices and points from estGraph 

    leastSquares = []
    currentStock = 0

    for stock in prices:
        stockIndex = 0
        squareError = 0
        for point in points:
            squareError += pow(stock[stockIndex] - point,2)

            stockIndex += 1
        currentStock += 1

    return leastSquares

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
