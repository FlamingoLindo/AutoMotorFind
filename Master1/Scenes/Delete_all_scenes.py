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
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

banana = 1

# DELETES ALL ACTIVE CATEGORIES!!!!!!!!!!!!!!

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

# Inputs email
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Password input
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Click the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens the scnes page
scnes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[7]')
                                                  )
                       ).click()

time.sleep(0.5)

# Ask the category type
categ_type = get_user_input("Eventos, Notícias, Vídeos cadastrados").title()

category_map = {
    "Eventos": 1,
    "Notícias": 2,
    "Vídeos cadastrados": 3
}

num = category_map.get(categ_type)

# Open the choosen category
open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num}]/div[1]')
                                                  )
                       ).click()

# Finds trash can icons
trash_icon = driver.find_elements(By.CSS_SELECTOR, '.jgxYQo')
count = 1
for _ in range(len(trash_icon)):
    time.sleep(0.6)
    # Click the trash icon
    click_trash = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[1]/div[2]/div[{count}]/div[2]/img[2]')
                                                    )
                        ).click()
    
    # Click the delete button
    delete = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/div/div/button[1]')
                                                    )
                        ).click()
    
    # Confirm the deletion
    done = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/div/button')
                                                    )
                        ).click()
    
    count += 1
    
    time.sleep(1)
    
get_user_input("DONE")
# Close the browser
driver.quit()
