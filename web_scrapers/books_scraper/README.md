## Books Scraper

This python project scraps books from a public page builded for practice purpose, 
"books.toscrape.com".

## What it does

- Fetches static HTML content using requests
- Extracts the title, price and availability of each book, using BeautifulSoup 
  (adds default values if missing) 
- Store the book in a list with incremental number
- Saves the results in a .csv file and into the MySQL data base.

## Tech used

- Beautifouls Soup 4
- MySQL
- CSV

## Special Logic

- Price strings are cleaned of special characters before saving
- Database fields are adjusted to accept the correct types, varchar, int, float

## How to run

- Clone the repository and navigate in the directory
- pip install beautifulsoup4
- Execute python books_scraper.py

## Output 

- .csv file with the scraped boooks
- books_list table in the database with the same data

## Database setup

CREATE DATABASE books_db;
USE books_db;
CREATE TABLE books_list (
    book_nr INT PRIMARY KEY,
    title VARCHAR(255),
    price VARCHAR(20),
    availability VARCHAR(50)
);
