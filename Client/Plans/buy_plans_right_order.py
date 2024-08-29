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
import pyautogui
load_dotenv()

# Add the path to the directory containing the Functions module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..','..'))

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

def buy_plan_go_back():
    # Click 
    credit_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[4]/div[1]')
                                                        )
                            ).click() 
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/button')
                                                        )
                            ).click() 
    
    select_card = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[1]')
                                                        )
                            ).click()
    
    confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/button[2]')
                                                        )
                            ).click()
    
    time.sleep(6.2)
    
    see_all_plans = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
                                                        )
                            ).click()
    
try:
    # Drive stuff
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  

    driver.get(os.getenv('CLIENT_URL'))

    wait = WebDriverWait(driver, 5)
except Exception as e:
    print('There has been an error initialising the chrome driver')
    print(e)

try:
    # Click the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz')
                                                        )
                            ).click() 

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                        )
                            ).send_keys(get_user_input('Email'))

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                        )
                            ).send_keys(get_user_input('Password'))

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fAJeQq')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)
    
try:
    # Click options
    options = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.gzIVkm')
                                                        )
                            ).click() 

    # Click my profile option
    my_profile_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[4]')
                                                        )
                            ).click()

    # Click plans option
    plans_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/button[2]')
                                                        )
                            ).click()  
except Exception as e:
    print('There has been an error on the login')
    print(e)
    
try:
    # 
    car_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[7]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    bike_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[2]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    truck_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[8]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    race_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[4]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    drag_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[5]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    parts_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    classic_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div/div[6]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    service_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[1]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    # 
    qualification_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[3]/div/div[2]/button')
                                                        )
                            ).click() 
    
    buy_plan_go_back()
    
    

    
except Exception as e:
    print('There has been an error on the login')
    print(e)


 


get_user_input("DONE")
# Close the browser
driver.quit()
