def bestTimeToBuyAndSellStocks(input):
    minPrice=input[0]
    start=0
    maxProfit=float('-inf') #let start with worst profit

    for i in range (1, len(input)):
        if input[i-1] < minPrice:
            minPrice= input[i-1]
            start=i-1
        profit = input[i]- minPrice
        if profit > maxProfit:
            maxProfit=profit
            end=i

    return  (maxProfit, start, end) #it will return profit and start position and end position

def main():
    prices = [7, 1, 5, 3, 6, 4]
    profit = bestTimeToBuyAndSellStocks(prices)
    print("profit " + str(profit))


main()