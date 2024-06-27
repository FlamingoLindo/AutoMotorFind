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

driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

image_path = r'C:\Users\josef\Desktop\AfterLifeDeath\MotorFind\AutoMotorFind\Images\logo.svg'
banana = 1

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

scnes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[7]')
                                                  )
                       ).click()

scnes_amount_str = get_user_input("How many scenes?")
scnes_amount_int = int(scnes_amount_str)
for _ in range(scnes_amount_int):
    register_scene = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/div/button')
                                                  )
                       ).click()
    
    scene_image = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/label[2]')
                                                  )
                       ).click()
    time.sleep(1.3)
    
    pyautogui.write(image_path)
    pyautogui.press('enter')

    title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="title"]')
                                                  )
                       ).send_keys(f"Titulo {banana}")
    
    categ_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div')
                                                  )
                       ).click()
    
    categ_type = random.randint(1,8)
                                                                   
    categ_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[4]/div[2]/div[{categ_type}]')
                                                )
                    ).click()

    categ_close_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[4]/div[1]')
                                                  )
                       ).click()
    
    type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[6]/div/div')
                                                )
                    ).click()
    
    type_input = random.randint(1,3)
  
    type_select = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[3]/form/div[6]/div/div[2]/div[{type_input}]')
                                                )
                    ).click()

    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link"]')
                                                  )
                       ).send_keys("https://motorfind-master.netlify.app/scenarios")

    description = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')
                                                  )
                       ).send_keys(f"Descrição {banana}")
    
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[1]/div/button[2]')
                                                )
                    ).click()
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                )
                    ).click()
    
    open_scene_choise = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{type_input}]/div[1]')
                                                )
                    ).click()
    
    time.sleep(1)
    
    switch = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM')
                                                  )
                       ).click()
    
    time.sleep(1)
    
    close_scene_choise = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[{type_input}]/div[1]')
                                                )
                    ).click()
    
    banana += 1
    

# Close the browser
driver.quit()
