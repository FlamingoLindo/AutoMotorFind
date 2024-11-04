from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/carhome/news')

cars_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gFOhXd')))

min_price = driver.find_element(By.ID,'min_price')
min_price.send_keys(6)


time.sleep(10)
driver.quit()