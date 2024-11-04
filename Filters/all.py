from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/carhome/news')

cars_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gFOhXd')))

name_search = driver.find_element(By.ID, 'name')
name_search.click()
name_search.send_keys('Mustang')

viewing_order_dropdown = driver.find_element(By.CSS_SELECTOR, '.iGtBuh')
viewing_order_dropdown.click()

higher_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/span')))
higher_opt.click()

min_price = driver.find_element(By.ID,'min_price')
min_price.send_keys(6)

max_price = driver.find_element(By.ID,'max_price')
max_price.send_keys(10)

brand1 = driver.find_element(By.CSS_SELECTOR, '.huvIcB')
brand1.click()

new = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[4]/div[1]')
new.click()

min_milage = driver.find_element(By.ID,'min_km')
min_milage.send_keys(1)

max_milage = driver.find_element(By.ID,'max_km')
max_milage.send_keys(1000)

min_year = driver.find_element(By.ID,'min_year')
min_year.send_keys(2023)

max_year = driver.find_element(By.ID,'max_year')
max_year.send_keys(2024)

# Preto
color_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[7]/div[1]/div[19]')
color_select.click()

all_stores_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[8]/div[1]')
all_stores_select.click()


time.sleep(10)
