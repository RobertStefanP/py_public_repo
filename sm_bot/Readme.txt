	Here i have a stock market bot which is connecting to Interactive Broker API 
during active trading hours. We are trading MES future contracts.

    The logic behind it is to enter a long position if the last 5 min bar closed 
above EMA 10 and SMA 20, short if below, or waiting till the next signal check 
if none.
	The bot will run constantly as long as the trading hours are valid, entering
in a sleep mode if not, and waiting till the market hours are valid again.
	At start up, it checks if we have open orders/positions and it will enter in 
a monitoring mode if yes, checking every 30 seconds if the orders are filled. When 
filled, a print info will be displayed highlightning the filled order in a bright 
color, then it will wait till minute 5 and 8 second to check for signals. 

	The bot will check for bar close value and compare it with the values of EMA 
and SMA. If a signal is detected, a trade will be executed depending of the type 
of signal, short or long(if its a bullish signal, a green print will be 
printed with the details of the trade, if is a bearish signal, the prints will 
be red printing the details of the trade). A bracket order will be placed and 
the bot will enter in a monitoring open orders/positions, checking every 30 
seconds if is still active.

    The event handler will be triggered if any of the orders will be 
filled. Since the orders/position are checked every 30 seconds, when detecting
that none are opened, the bot will start checking again for signals and placing 
trades till the active hours are not valid anymore. 
	Some prints are connected to a telegram bot which will send messages 
to a private channel with info purpose. 
   