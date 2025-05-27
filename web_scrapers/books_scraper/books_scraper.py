from bs4 import BeautifulSoup
import requests
import csv

from db_connection import Connection


BASE_URL = "http://books.toscrape.com/"

def fetch_page(url):
    """Download page content."""
    response = requests.get(url)
    return response.text

def parse_books(html):
    """Extract book data (title, price, availability)."""
    soup = BeautifulSoup(html, "lxml")
    books = []
    book_nr = 0
    for book in soup.select("article.product_pod"):
        book_nr += 1
        title_tag = book.h3.a if book.h3 and book.h3.a else None
        title = title_tag["title"] if title_tag and "title" in title_tag.attrs else "N/A"
        
        price_tag = book.select_one("p.price_color")
        price = price_tag.text.strip("Â£") if price_tag else "N/A"
        
        availability_tag = book.select_one("p.instock")
        availability = availability_tag.text.strip() if availability_tag else "N/A"
        
        books.append({"book_nr": book_nr, "title": title, "price": price,"availability": availability})                 
    return books

def save_to_csv(books):
    """Save books to CSV file."""
    with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["book_nr", "title", "price", "availability"])
        writer.writeheader()
        writer.writerows(books)
        
def save_to_books_db(books):
    """Connecting and inserting books into MySQL database."""
    connection = None
    insert = "INSERT INTO books_list(book_nr, title, price, availability) VALUES(%s, %s, %s, %s)"
    try:
        connect = Connection.obtain_connection()
        cursor = connect.cursor()
        for book in books:
            book_nr = book["book_nr"]
            title = book['title']
            price = book['price']
            availability = book['availability']
            
            values = (book_nr, title, price, availability)
            cursor.execute(insert, values)
            print(f"Book inserted succesfully: {title}")
            connect.commit()
        return cursor.rowcount
    except Exception as e:
        print(f"Error tring to update the DB: {e}")
    finally:
        if connection is not None:
            cursor.close()
            connect.realese_connection()
    
if __name__ == "__main__":
    url = BASE_URL
    html = fetch_page(url)
    books = parse_books(html)
    save_to_csv(books)
    save_to_books_db(books)
