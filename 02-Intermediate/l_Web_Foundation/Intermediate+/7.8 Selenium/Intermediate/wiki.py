from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(WIKI_URL)

# article_num = driver.find_element(
#     By.CSS_SELECTOR, value='#articlecount a')
# article_num.click()

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" input by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)
