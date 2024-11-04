from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/partshome/news')

service_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.jGYlfK')))

min_price = driver.find_element(By.ID, 'min_price')
min_price.send_keys(1)

max_price = driver.find_element(By.ID, 'max_price')
max_price.send_keys(1)

time.sleep(10)

driver.quit()