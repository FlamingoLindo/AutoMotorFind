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

# Sets image path
image_path = r'C:\Users\josef\Desktop\AfterLifeDeath\MotorFind\AutoMotorFind\Images\logo.svg'
banana = 1

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

# Opens the scnes page
users_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[6]')
                                                  )
                       ).click()

time.sleep(1)

eye_icons = driver.find_elements(By.CSS_SELECTOR, '.guehBu')
print(len(eye_icons))
for _ in range(len(eye_icons)):
    
    eye_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.HPyke')
                                                  )
                       ).click()
    
    trash_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bbTOtk')
                                                  )
                       ).click()
    
    reason = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ciUGNx')
                                                  )
                       ).send_keys("Auto Delete")
    
    delete_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ceWOoL')
                                                  )
                       ).click()
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.kVnpAj')
                                                  )
                       ).click()
    
    time.sleep(0.6)
    
get_user_input("DONE")
# Close the browser
driver.quit()