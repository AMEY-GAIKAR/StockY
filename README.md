StockY 

Introduction:
This project aims to create a stable trading algorithm with implementation of the Bollinger Bands indicator.
This algorithm evaluates intraday trades and longer trades seperately.
This algorithm aims to recursively capitalized on minor changes in the stock market in order to increase the overall return on investment.
This algorithm performs exceptionally well on executing intraday trades as the trends observed exhibit regression to the mean.
This algorithm is backtested with stocks from the S&P 500 list.


Architecture:
Fetch data --> Initialise object --> Evaluate
Data is fetched through an API call.
This data is stored in a csv file.
This file is used to create a pandas.DataFrame object which is the core attribute of the 'Entity' object.
Bollinger Bands are plotted to determine the opening and closing points.
These trades are evaluated to calculate the ROI.


Algorithm:
OHLCV data is fetched per stock.
This data is passed into an object that creates bollinger bands.
Long trades are opened when the close value intersects the lower bollinger band.
Long trades are closed when the close value intersects the middle bollinger band.
Short trades are opened when the close value intersects the upper bollinger band.
Short trades are closed when the close value intersects the middle bollinger band.
These trades are evaluated and ROI is calculated as the performance measure.

Software:
This project is written in python. 
Processing and evaluation are all done in python.
Data is processed as a pandas.DataFrame instance, while matplotlib is used to create plots.

Results:
ROI is used as the performance measure.
The results of individual trades or the cumalative results can be viewd as statistical plots.

Future Work:
The current strategy bases itself on the Bollinger Bands indicator.
This provides a narrow perspective of the bigger picture of the non-deterministic stock market.
Additional indicators and analysis of market sentiment can be used to create a more refined algorithm.

