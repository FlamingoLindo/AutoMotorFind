from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/carhome/news')

cars_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gFOhXd')))

min_stores_select = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[8]/div[3]')
min_stores_select.click()

time.sleep(10) 