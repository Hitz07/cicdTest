from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("XO Health QA")
    search.submit()
    time.sleep(2)
    assert "XO Health" in driver.page_source
    driver.quit()