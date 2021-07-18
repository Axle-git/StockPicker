import requests
from Constants import *
import re

def getTickerNumb(url):
    page = requests.get(url).text

    page = page.partition(YAHOO_TICKER_NUMB)[2]     #get rid of characters before number
    page = page[:page.index("<")]                   #get rid of after
    page = float(page.replace(',','')) #   remove commas + convert to float
    return page

