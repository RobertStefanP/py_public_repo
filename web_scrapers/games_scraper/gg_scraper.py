from h11 import Connection
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import mysql.connector
import csv
import time


from db_connection import Connection


def start_browser():
    """Setup and launch browser."""
    options = Options()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.add_argument("--start-maximized")
    time.sleep(3)
    
    service = Service(r"C:\Users\Robert\all_python\py_public_repo\web_scraper\chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://gg.deals/games/pc/") 
    return driver

def scrape_games(driver):
    """Load page and extract data."""
    games = []                                         
    game_block = driver.find_elements("css selector", "div.game-item")   
    for block in game_block:  
        try:                                                
            game_id = block.find_element("css selector", "button.game-options-trigger-btn").get_attribute("data-game-id")
            if not game_id:
                continue
        except:
            continue        
        title = block.find_element("css selector", "button.game-options-trigger-btn").get_attribute("data-game-title")
        try:
            price = block.find_element("css selector", "span.price-inner").text.strip("~€") 
        except:
            price = 0                   
        try:
            discount = block.find_element("css selector", "span.discount.label").text.strip("%")
        except:
            discount = 0                           
        games.append({"game_id": game_id, "title": title, "price": price, "discount": discount})      
    return games

def save_to_csv(games):
    """Save games list to CSV."""
    with open("games.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["game_id", "title", "price", "discount"])
        writer.writeheader()
        writer.writerows(games)

def save_to_mysql(games):
    """Connecting to MySQL data base and save the fetched data."""
    connection = None
    insert = "INSERT INTO games_list(id, title, price, discount) VALUES(%s, %s, %s, %s)"
    try:
        connect = Connection.obtain_connection()
        cursor = connect.cursor()        
        for game in games: 
            game_id = game['game_id']
            title = game['title']
            
            raw_price = str(game['price'])
            if raw_price == "Free":
                price = "Free"
                print(f"Price = {price}")               
            else:
                clean_price = raw_price.replace(",", ".")
                price = float(clean_price)
                                           
            raw_discount = str(game['discount'])
            clean_discount = raw_discount.replace(",", ".")
            discount = int(raw_discount)
                       
            values = (game_id, title, price, discount)
            cursor.execute(insert, values)
            print(f"Game inserted succesfully: {title}")
            connect.commit()
        return cursor.rowcount                
    except Exception as e:
        print(f"Error trying to update data_base: {e}")
    finally:
        if connection is not None:
            cursor.close()
            connect.release_connection()

if __name__ == "__main__":
    driver = start_browser()
    games = scrape_games(driver)
    save_to_csv(games)
    game_inserted = save_to_mysql(games)        
    driver.quit()
        