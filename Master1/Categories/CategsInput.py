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
import sys
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def gera_parcela():
    return str(random.randint(1, 999999999))

def gera_aviso():
    return str(random.randint(1, 29))

# Create the register category function
def register_catg():
    car_catg_title_input = get_user_input("Category name       ")
    car_catg_info_input = get_user_input("Category info        ")

    car_catg_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(car_catg_title_input)

    car_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(car_catg_info_input)

    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/button[2]')
                                                    )
                        ).click()   
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                    )
                        ).click() 

# Driver stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

# Email input
email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

# Password input
password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

# Clicks at the login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Opens categories page
catgs_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[4]')
                                                  )
                       ).click()

time.sleep(0.5)

# Ask the category type
categ_type = get_user_input("(Carros, Motos, Trucks, Race, Drag, Peças, Serviços, Clássicos").title()

# Ask how many categories are going to be created
categ_amount_str = get_user_input("How many categories?")
categ_amount_int = int(categ_amount_str)

category_map = {
    "Carros": 1,
    "Motos": 2,
    "Trucks": 3,
    "Race": 4,
    "Drag": 5,
    "Peças": 6,
    "Serviços": 7,
    "Clássicos": 8
}

num = category_map.get(categ_type)

# Open the random category
open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num}]/div[1]/div[2]')
                                                )
                    ).click()

for _ in range(categ_amount_int):   
    
    # Opens the category creation modal
    add_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{num}]/div[2]/div[1]')
                                                    )
                        ).click()

    register_catg()
    
    time.sleep(0.5)

get_user_input("DONE")
# Close the browser
driver.quit()
