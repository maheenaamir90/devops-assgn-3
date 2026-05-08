
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://100.24.114.216:5000")

# Test Case 1
assert "DevOps Assignment Running Successfully" in driver.page_source

# Test Case 2
title = driver.title
assert title == ""

print("All Selenium Tests Passed")

driver.quit()
