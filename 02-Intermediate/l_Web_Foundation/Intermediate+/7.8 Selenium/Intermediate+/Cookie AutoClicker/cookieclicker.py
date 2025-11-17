from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time
CLICKER_URL = "https://ozh.github.io/cookieclicker"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(CLICKER_URL)

# Wait for the page to load
sleep(3)

try:
    language_select = driver.find_element(
        By.XPATH, value='//*[@id="langSelect-EN"]')
    language_select.click()
except NoSuchElementException:
    print("Language selection not found, continuing...")
sleep(2)  # Wait for the main game to load

# Find the big cookie to click
cookie = driver.find_element(by=By.ID, value="bigCookie")

# Set timers
wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes

while True:
    cookie.click()

    # Every 5 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        can_buy = driver.find_elements(By.CSS_SELECTOR,
                                       value="#products .enabled")
        can_buy_upgrades = driver.find_elements(By.CSS_SELECTOR,
                                                value="#upgrades .enabled")
        for item in can_buy:
            item.click()
            sleep(0.1)
        timeout = time() + wait_time
