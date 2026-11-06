import time
from selenium import webdriver
from JIOSAAVAN.Jio_saavan_home_page import JioSavanHomePage
from selenium.webdriver import ActionChains
class JIO_SAAVAN_MUSIC:
    top_play_list='//h3[text()="Top Playlists"]'
    surprise_me='//a[text()="Surprise Me"]'
    dumdaar_hits='//a[text()="Dumdaar Hits"]'
    romantic_hits_hindi='//a[text()="Romantic Hits 2026 - Hindi"]'
    best_dance_hindi='//a[text()="Best Of Dance - Hindi"]'
    play_arjith_singh='//a[contains(text(), "Let\'s Play - Arijit Singh - Hindi")]'
    best_90s_pop='//a[text()="Best Of Pop - Hindi"]'
    best_90s_hindi='//a[text()="Best Of 90s - Hindi"]'
    retro_songs='//a[text()="Best Of Retro"]'
    lata_hits='//a[text()="Lata Mangeshkar"]'
    udit_hits='//a[text()="Udit Narayan"]'

    def __init__(self,driver):
        self.driver = driver

    def mouse_hover(self):
        pointer=ActionChains(self.driver)
        TopPlay=self.driver.find_element_by_xpath(self.top_play_list)
        time.sleep(3)
        RomanticPlay=self.driver.find_element_by_xpath(self.romantic_hits)
        time.sleep(3)
        pointer.move_to_element(TopPlay).move_to_element(RomanticPlay).perform()
        time.sleep(3)
        click_music()
        time.sleep(3)




