import pytest
from JIOSAAVAN.Jio_saavan_home_page import JIO_SAAVAN_HOMEPAGE
from JIOSAAVAN.Jio_saavan_music_page import JIO_SAAVAN_MUSIC
import time
@pytest.mark.jiomarker1
def test_case3(setup1):
    driver = setup1
    H=JIO_SAAVAN_HOMEPAGE(driver)
    H.click_music()
    H.click_new_releases()
    