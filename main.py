import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import readchar

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
res_items = driver.find_elements(By.CSS_SELECTOR, ".resItemBox a")


# Extract the text and corresponding href from each <a> element
links = [(index, item.text, item.get_attribute('href')) for index, item in enumerate(res_items)]
print(links)
# Display the texts to the user
print("Select an item by pressing the corresponding number key:")
for index, (text, href) in enumerate(links):
    print(f"{index + 1}: {text}")

# Prompt the user to select an item using the keyboard
while True:
    key = readchar.readkey()
    if key.isdigit():
        selected_index = int(key) - 1
        if 0 <= selected_index < len(links):
            break
    print("Invalid selection. Please try again.")

# Get the selected link
selected_text, selected_href = links[selected_index][1], links[selected_index][2]
print(f"You selected: {selected_text} - {selected_href}")

# Optionally, navigate to the selected link
driver.get(selected_href)

# Close the browser
driver.quit()
