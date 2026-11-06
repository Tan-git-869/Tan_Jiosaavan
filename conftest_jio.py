from selenium import pytest
@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(r"https://www.jiosaavn.com/")
    driver.maximize_window()
    yield driver
    time.sleep(3)
    driver.close()
