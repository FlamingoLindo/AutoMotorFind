from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/partshome/news')

parts_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.eGwSYG')))

min_milage = driver.find_element(By.ID, 'min_km')
min_milage.send_keys(0)


time.sleep(10)
driver.quit()