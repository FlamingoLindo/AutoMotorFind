from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/carhome/news')

cars_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gFOhXd')))

min_milage = driver.find_element(By.ID,'min_km')
min_milage.send_keys(1)

max_milage = driver.find_element(By.ID,'max_km')
max_milage.send_keys(1000)


time.sleep(10)
driver.quit()
