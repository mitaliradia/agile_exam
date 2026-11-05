from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)

try:
    file_path=Path("login.html").resolve().as_uri()
    driver.get(file_path)
    time.sleep(2)

    driver.find_element(By.ID,"username").send_keys("admin")
    time.sleep(2)

    driver.find_element(By.ID,"password").send_keys("123")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)

   