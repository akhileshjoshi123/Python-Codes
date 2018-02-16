'''
Say you have an array for which the i th element is the price of a given stock on day i . If you
were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit

'''



def maximumProfit(stocks):
    
    minStock = float('inf')

    profit = 0
    transactions = 0
    
    for i in range(0,len(stocks)):
        if stocks[i] < minStock :
            minStock = stocks[i]
        if stocks[i] - minStock > profit :
            profit = stocks[i] - minStock
            transactions += 1
    
    return profit , transactions 


stocks = [7,6,4,3,1]

profit , transactions  = maximumProfit(stocks)
print("maximum profit is" , profit ,"with" , transactions , "transactions" )
