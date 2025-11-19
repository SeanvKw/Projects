from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

TARGET_ACCOUNT = "yourtargetaccount"
EMAIL = "youremail"
PASSWORD = "yourpassword"


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        sleep(4.2)

        decline_cookie_xpath = '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'
        cookie_warning = self.driver.find_elements(
            By.XPATH, decline_cookie_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)

        sleep(2)
        password_input.send_keys(Keys.ENTER)

        sleep(15)
        save_login_prompt = self.driver.find_element(
            By.XPATH, value="//div[contains(text(), 'Nie teraz')]")
        if save_login_prompt:
            save_login_prompt.click()

        sleep(8)
        try:
            notification_prompt = self.driver.find_element(
                By.XPATH, value="// button[contains(text(), 'Nie teraz')]")
            if notification_prompt:
                notification_prompt.click()
        except:
            print("No notification prompt appeared.")

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        sleep(5)
        followers_link = self.driver.find_element(
            By.PARTIAL_LINK_TEXT, "obserwujących")
        followers_link.click()
        sleep(7)
        scroll = self.driver.find_element(
            By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
            sleep(2)

    def follow(self):
        xpath_follow_btns = ("//div[@role='dialog']//button["
                             ".//div[contains(normalize-space(),'Obserwuj')]"
                             " or contains(normalize-space(),'Follow')"
                             " or normalize-space()='Obserwuj'"
                             " or normalize-space()='Follow']")
        follow_buttons = self.driver.find_elements(
            By.XPATH, xpath_follow_btns)
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(
                    by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
