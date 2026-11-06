import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class JIO_SAAVAN_HOMEPAGE:
    music='//a[text()="Music"]'
    new_releases='//a[text()="New Releases"]'

    def __init__(self,driver):
        self.driver = driver

    def click_music(self):
        self.driver.find_element_by_xpath(self.music).click()
        time.sleep(3)


    def click_new_releases(self):
        self.driver.find_element_by_xpath(self.new_releases).click()
        time.sleep(3)