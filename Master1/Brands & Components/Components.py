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

# Sets images path
car_image_paths_string  = os.getenv('CAR_LOGOS')
car_image_paths = car_image_paths_string.split(',')

bike_image_paths_string  = os.getenv('BIKE_LOGOS')
bike_image_paths = bike_image_paths_string.split(',')

truck_image_paths_string  = os.getenv('TRUCK_LOGOS')
truck_image_paths = truck_image_paths_string.split(',')

race_image_paths_string  = os.getenv('RACE_LOGOS')
race_image_paths = race_image_paths_string.split(',')

drag_image_paths_string  = os.getenv('DRAG_LOGOS')
drag_image_paths = drag_image_paths_string.split(',')

part_image_paths_string  = os.getenv('PARTS_LOGOS')
part_image_paths = part_image_paths_string.split(',')

service_image_paths_string  = os.getenv('SERVICE_LOGOS')
service_image_paths = service_image_paths_string.split(',')

classic_image_paths_string  = os.getenv('CLASSIC_LOGOS')
classic_image_paths = classic_image_paths_string.split(',')

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

# Login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/form/fieldset/button')
                                                  )
                       ).click()

time.sleep(1)

# Open brands page 
brands_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[9]')
                                                  )
                       ).click()

#        
components_page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fyxKfL'))
                        ).click()
    
time.sleep(1)

count = 1

# Asks the amount of brands to be created
brand_input_str = get_user_input("How many?")
brand_input_int = int(brand_input_str)
for _ in range(brand_input_int):    
    
    #
    add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'.fsHaFl'))
                        ).click()
        
    #
    title = wait.until(EC.element_to_be_clickable((By.ID, 'title'))
                       ).send_keys(f"Component {count}")

    #
    register = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dskIoT'))
                        ).click()
    
    #
    sucess = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[5]/div/button'))
                        ).click()
    
    #
    activate = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.esbzDM'))
                           ).click()
    
    count += 1
    
    time.sleep(1)                         
get_user_input("DONE")
# Close the browser
driver.quit()
