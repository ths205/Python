
#This program produces the chart of the stock Apple
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

start_date = '2023-1-1' #This stands for January 1, 2023

end_date = '2024-1-1' #This stands for January 1, 2024

#The line below downloads the stock information
apple = yf.download(tickers ="AAPL", start = start_date , end = end_date)

plt.figure(figsize=(14, 6) )
sns.set_style("ticks")
sns.lineplot(data = apple, x = "Date", y ='Close',color= 'purple')
sns.despine()
plt.title("The Stock Price of Apple", size ='x-large', color = 'blue')

plt.show()
