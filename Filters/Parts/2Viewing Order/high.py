from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/partshome/news')

parts_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.eGwSYG')))

view_order = driver.find_element(By.CSS_SELECTOR, '.iGtWIt')
view_order.click()

high = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/span')))
high.click()


time.sleep(10)
driver.quit()