import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time

load_dotenv()

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chat_username = str(input("Enter the username you want to send the message to: "))
        self.chat_message = str(input("Enter the message you want to send to the user: "))
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def open(self):
        bot = self.bot
        bot.get('https://www.instagram.com')
        time.sleep(4)
    def login(self):
        bot = self.bot
        username = self.username
        password = self.password
        usernameField = bot.find_element_by_name('username')
        passwordField = bot.find_element_by_name('password')
        usernameField.clear()
        passwordField.clear()
        usernameField.send_keys(username)
        passwordField.send_keys(password)
        passwordField.send_keys(Keys.RETURN)
        time.sleep(6)
    def goToChat(self):
        bot = self.bot
        chat_username = self.chat_username
        chat_message = self.chat_message
        inputField = bot.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        inputField.send_keys(chat_username)
        time.sleep(5)
        inputField.send_keys(Keys.RETURN)
        inputField.send_keys(Keys.RETURN)
        time.sleep(8)
        messageButton = bot.find_element_by_xpath('//button[normalize-space()="Message"]')
        messageButton.click()
        time.sleep(5)
        notificationClose = bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notificationClose.click()
        messageField = bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        messageField.send_keys(chat_message)
        messageField.send_keys(Keys.RETURN)
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
toRun = InstagramBot(username, password)
toRun.open()
toRun.login()
toRun.goToChat()
