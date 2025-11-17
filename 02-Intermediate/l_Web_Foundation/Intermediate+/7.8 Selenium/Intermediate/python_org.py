from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events_dict = {}

for n in range(0, (len(event_times))):
    events_dict[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events_dict)
driver.quit()
