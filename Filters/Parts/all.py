from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/partshome/news')

parts_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.eGwSYG')))

name_input = driver.find_element(By.NAME, 'name')
name_input.send_keys('Rodas')

view_order = driver.find_element(By.CSS_SELECTOR, '.iGtWIt')
view_order.click()

high = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/span')))
high.click()

lower = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[3]/span')))
lower.click()

relevant = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[1]/span')))
relevant.click()

view_order = driver.find_element(By.CSS_SELECTOR, '.iGtWIt')
view_order.click()

min_price = driver.find_element(By.ID, 'min_price')
min_price.send_keys(1)

max_price = driver.find_element(By.ID, 'max_price')
max_price.send_keys(100000)

brand = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[3]/div/div')
brand.click()

component = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[4]/div/div')
component.click()

new = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[5]/div[1]')
new.click()

used = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[5]/div[2]')
used.click()

min_milage = driver.find_element(By.ID, 'min_km')
min_milage.send_keys(0)

max_milage = driver.find_element(By.ID, 'max_km')
max_milage.send_keys(1000000)

color = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[8]/div[1]/div[17]')
color.click()

all_stores = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[9]/div[1]')
all_stores.click()

time.sleep(10)
driver.quit()