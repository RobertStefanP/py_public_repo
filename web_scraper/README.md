# GG.Deals Game Scraper

This project scrapes PC game deals from [gg.deals](https://gg.deals/games/pc/), collecting titles, prices, discounts, and game IDs.

## What It Does

- Opens the PC games section using Selenium
- Extracts:
  - Game ID
  - Title
  - Price (`Free` games handled correctly)
  - Discount
- Saves results to:
  - A local `games.csv` file
  - A MySQL database (`games_list` table)

## Tech Used

- Python
- Selenium
- MySQL (via connection pooling)
- ChromeDriver
- CSV

## Special Logic

- If a game is listed as `"Free"`:
  - The price is stored as the string `"Free"` (not float)
- Numeric prices are cleaned (`"52,41"` → `52.41`)
- Discounts are stripped of `%` and stored as integers

##  Setup

1. Install requirements:
   ```bash
   pip install selenium mysql-connector-python

##  Data Base table

CREATE DATABASE games_db;
USE games_db;
CREATE TABLE games_list (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    price VARCHAR(20),
    discount INT
);
