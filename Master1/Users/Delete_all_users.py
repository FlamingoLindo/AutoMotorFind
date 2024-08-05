import customtkinter as tk
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
import pyautogui
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

# Input email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Input password
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Click the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens the clients page
users_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[6]')
                                                  )
                       ).click()

time.sleep(1)

# Finds amount of eye icons there are on the page
eye_icons = driver.find_elements(By.CSS_SELECTOR, '.guehBu')

# Loop for the amount of icons found
for _ in range(len(eye_icons)):
    
    # Click at the eye icon
    eye_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.HPyke')
                                                  )
                       ).click()
    
    # Click at the trash icon
    trash_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bbTOtk')
                                                  )
                       ).click()
    
    # Inputs deletion reason
    reason = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ciUGNx')
                                                  )
                       ).send_keys("Auto Delete")
    
    # Click at the delte button
    delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ceWOoL')
                                                  )
                       ).click()
    
    # Click at the continue button
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.kVnpAj')
                                                  )
                       ).click()
    
    time.sleep(0.6)
    
get_user_input("DONE")
# Close the browser
driver.quit()