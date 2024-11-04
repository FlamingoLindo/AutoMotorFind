from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/partshome/news')

service_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.jGYlfK')))

name_input = driver.find_element(By.NAME, 'name')
name_input.send_keys('Teste')

order_select = driver.find_element(By.CSS_SELECTOR, '.fUluAi')
order_select.click()

high = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]')
high.click()

min_price = driver.find_element(By.ID, 'min_price')
min_price.send_keys(1)

max_price = driver.find_element(By.ID, 'max_price')
max_price.send_keys(1)

subcategory = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[3]/div[1]')
subcategory.click()

all_stores = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[4]/div[1]')
all_stores.click()

time.sleep(10)

driver.quit()