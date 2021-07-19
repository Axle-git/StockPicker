from stockFunctions import *

# for ticker in TECH_TICKER_URLS:
#     print(getTickerNumb(TECH_TICKER_URLS[ticker]))

prices = []         
for stock in TECH_TICKER_URLS:                                  #   initialize 2D array, each row represents a stock and the values starting are stock prices (to be normalized later)
    prices.append([getTickerNumb(TECH_TICKER_URLS[stock])])     #   it's worth noting that this does not differentiate between stocks at all as far as name goes

iteration = 1
while True:
    row = 0       # row-index, denotes the current stock we're looking at in the prices 2D array

    for stock in TECH_TICKER_URLS:      #   probably takes values every ~40 seconds
        prices[row].append(getTickerNumb(TECH_TICKER_URLS[stock]))
        row += 1

    if iteration % 3 == 0: #   gives update on values every ~30 minutes
        updateTxt(prices)

    if iteration % 200 == 0:   #   every 200th interation
        prices = normalize(prices)

        stockToBuy(prices)

        prices = []                                             #   reset for next cycle
        for stock in TECH_TICKER_URLS:
            prices.append([getTickerNumb(TECH_TICKER_URLS[stock])])
        iteration = 0

    print("Iteration ", iteration, " done")

    time.sleep(30)
    iteration += 1