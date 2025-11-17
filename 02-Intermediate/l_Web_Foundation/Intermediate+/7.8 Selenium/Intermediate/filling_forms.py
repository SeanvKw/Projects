from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

FORM_URL = "https://secure-retreat-92358.herokuapp.com"

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Adrian")
last_name.send_keys("Rączka")
email.send_keys("example@gmail.com")  # , Keys.ENTER if site accepts it

# Locate the "Sign up" Button. Then click it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
