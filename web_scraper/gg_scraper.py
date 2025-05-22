from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


def start_browser():
    """Setup and launch browser."""
    options = Options()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.add_argument("--start-maximized")
    
    service = Service(r"C:\Users\Robert\all_python\py_public_repo\web_scraper\chrome_driver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://gg.deals/")
    sleep(5)
    return driver

def scrape_games(driver):
    """Load page and extract data."""
    games = []
    game_element = driver.find_elements("css selector", "button.game-options-trigger-btn")
    
    for elemnt in game_element:
        title = elemnt.get_attribute("data-game-title")
        games.append({"title": title})        
    print(games)
    
    return games

def save_to_csv(games):
    """Save to CSV."""
    
    pass


def save_to_mysql(games):
    """Save to MySQL."""
    pass  # later: insert into DB


if __name__ == "__main__":
    driver = start_browser()
    games = scrape_games(driver)
    save_to_csv(games)
    save_to_mysql(games)        
    driver.quit()
        