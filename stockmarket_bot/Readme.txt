	Here i have a stock market bot which is connecting to Interactive Broker API 
during active trading hours. We are trading MES future contracts.

    The logic behind it is to enter a long position if is detecting a bull crossover,
10EMA crossing above 20 SMA, or short position if is detecting a bear crossover, 
10EMA is crossing below 20SMA, in a 5 minutes time period.

	The bot will run constantly as long as the trading hours are valid, entering
in a sleep mode if not, and waiting till the market hours are valid again.

	At start up, it checks if we have open orders/positions and it will enter in 
a monitoring mode if yes, checking every 30 seconds if the orders are filled. When 
filled, a print info will be displayed highlightning the filled order in a bright 
color, and then it will wait till minute 5 and 8 second to check for signals. 

	The bot will check for signals of crossver as long we don't have any open 
orders/positions for the currrent contract, else it will wait till filled, 
and constantly checking for their status. If a signal is detected, a trade 
will be executed depending of the type of signal, short or long(if its a buy 
signal, a green print will be displayed with the details of the trade, if is 
a sell signal, the prints will be red displaying the details of the trate). Also 
a bracket order will be placed and the bot will enter in a monitoring open 
orders/positions, checking every 30 seconds if the bracket/positions are still active. 
When the orders are filled/canceled, the bot will detect that none are opened, 
and it will start again checking for signals till the active hoours are not valid 
anymore. 

	Also, some prints are connected to a telegram bot which will send messages 
to a private channel with info purpose.    
