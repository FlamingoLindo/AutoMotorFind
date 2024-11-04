from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get('https://motorfind-client.netlify.app/carhome/news')

cars_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.gFOhXd')))

viewing_order_dropdown = driver.find_element(By.CSS_SELECTOR, '.iGtBuh')
viewing_order_dropdown.click()

higher_opt = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/span')))
higher_opt.click()

time.sleep(10)
driver.quit()