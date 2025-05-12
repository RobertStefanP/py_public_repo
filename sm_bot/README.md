# Stock Market Trading Bot (MES Futures, IB API)

This bot connects to the **Interactive Brokers API** and trades **MES futures contracts** during active trading hours.

---

## What It Does

- Monitors the market in **5-minute intervals**
- Uses technical indicators to detect entry signals:
  - **Bullish crossover** → 10 EMA crosses above 20 SMA → triggers a **long position**
  - **Bearish crossover** → 10 EMA crosses below 20 SMA → triggers a **short position**
- Automatically sends **bracket orders** on signal detection
- Enters **monitoring mode** to track open orders and positions
- Sends key status updates to a **private Telegram channel**

---

## Market Hours Handling

- Runs continuously and checks if current time is within **trading hours**
- Sleeps when market is closed
- Wakes and resumes automatically when market reopens

---

## Logic Flow

1. **Startup check**:
   - If open orders or positions exist → enter monitoring mode
2. **Monitoring**:
   - Every 30 seconds, checks if orders are filled
   - Once filled, logs the order with colored terminal output (green for buy, red for sell)
3. **Signal detection**:
   - At minute `:05:08` of each 5-minute candle, checks for crossover signals
   - If no open positions, evaluates signal and executes trade accordingly
4. **Order tracking**:
   - After placing a trade, continuously monitors bracket orders until they are filled or canceled
5. **Looping**:
   - After order closure, resumes signal checking if market is still open

---

## Notifications

- Key trade events and updates are sent via a **Telegram bot** to a private channel for monitoring and alerts

---

## Requirements

- Interactive Brokers account
- IB API (TWS or IB Gateway)
- Python libraries:
  - `ib_insync`
  - `pandas`, `datetime`, `time`
  - `telegram` (or any other bot wrapper)

---

## Notes

- No GUI included — fully terminal-based
- Designed for **educational and testing purposes**
- Can be extended with logging, database storage, or advanced risk management

