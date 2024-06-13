import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.menu_interface import display_menu


def main():
    parser = argparse.ArgumentParser(description='Search query')
    parser.add_argument('query', type=str, help='search query on z-library')
    args = parser.parse_args()

    # Setup Chrome options (optional)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
    chrome_options.add_argument("--disable-infobars")  # Disabling infobars
    chrome_options.add_argument("--disable-extensions")  # Disabling extensions
    chrome_options.add_argument("--disable-gpu")  # applicable to windows os only
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the URL
    driver.get(f"https://singlelogin.re/s/{args.query}")

    # Wait for a few seconds to view the page
    # time.sleep(5)

    # Find all <a> elements inside elements with the class .resItem
    res_items = driver.find_elements(By.CSS_SELECTOR, ".resItemBox h3 a")
    page_size = 10

    # Extract the text and corresponding href from each <a> element
    links = [(index, item.text, item.get_attribute('href')) for index, item in enumerate(res_items)][0:page_size]

    selected_index = display_menu(links)
    
    # Optionally, navigate to the selected link

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()