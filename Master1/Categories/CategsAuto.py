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
import sys
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

banana = 1

def register_catg():
    catg_title = f"Subcategoria {banana} {type}" 
    catg_info = f"Texto informativo {banana} para {type}"

    car_catg_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(catg_title)

    car_catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                    )
                        ).send_keys(catg_info)

    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/button[2]')
                                                    )
                        ).click()   
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                    )
                        ).click() 
    
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

email_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')
                                                    )
                         ).send_keys(os.getenv("MASTER_LOGIN"))

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')
                                                       )
                            ).send_keys(os.getenv("MASTER_PASSWORD"))

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

catgs_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[4]')
                                                  )
                       ).click()

time.sleep(0.5)

categ_type = 8

category_map = {
    1: "Carros",
    2: "Motos",
    3: "Trucks",
    4: "Race",
    5: "Drag",
    6: "Peças",
    7: "Serviços",
    8: "Clássicos"
}

type = category_map.get(categ_type)

categ_amount_str = get_user_input("How many categories?")
categ_amount_int = int(categ_amount_str)
 
open_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[1]/div[2]')
                                                )
                    ).click()

for _ in range(categ_amount_int):   
    
    add_categ = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{categ_type}]/div[2]/div[1]')
                                                    )
                        ).click()

    register_catg()
    
    banana += 1
    
    time.sleep(0.5)
    

# Close the browser
driver.quit()
