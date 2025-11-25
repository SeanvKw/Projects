import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdQ3BvqTz7UUFA_33uZoPASwdA0NMjjNzLxPyHi9rEygnN7Tg/viewform?usp=dialog"
SRACPE_URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(SRACPE_URL)

soup = BeautifulSoup(response.text, "html.parser")

all_prices = soup.find_all(
    name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_addresses = soup.find_all(
    name="address")
all_links = soup.find_all(
    name="a", class_="property-card-link")

prices_list = [price.getText().split("+")[0].split("/mo")[0]
               for price in all_prices]
addresses_list = [address.getText().strip() for address in all_addresses]
links_list = [links.get("href")for links in all_links]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)
address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
submit_xpath = "//span[contains(text(), 'Prześlij')]"

print(f"Fetching all necessary informations...")
sleep(2)
print(f"Found: {len(links_list)} localization/s")
for n in range(len(links_list)):
    sleep(1)

    addres_input = driver.find_element(By.XPATH, value=address_xpath)
    price_input = driver.find_element(By.XPATH, value=price_xpath)
    link_input = driver.find_element(By.XPATH, value=link_xpath)
    submit_button = driver.find_element(By.XPATH, value=submit_xpath)

    addres_input.send_keys(addresses_list[n])
    price_input.send_keys(prices_list[n])
    link_input.send_keys(links_list[n])  # type: ignore

    sleep(0.5)

    submit_button.click()

    sleep(1)

    return_button = driver.find_element(By.CSS_SELECTOR, value="div a")
    return_button.click()
