import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_duckduckgo_search():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://duckduckgo.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("XO Health QA")
    search.submit()
    time.sleep(3)

    assert "XO Health" in driver.page_source

    driver.quit()