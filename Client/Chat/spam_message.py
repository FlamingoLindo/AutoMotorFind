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
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.hygPet')
                                                        )
                            ).click() 

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')
                                                        )
                            ).send_keys('caos@gmail.com')

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')
                                                        )
                            ).send_keys('12345678')

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eaqkjo')
                                                        )
                            ).click() 
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    
    time.sleep(3)
    
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]')
                                                        )
                            ).click()
        
    messages_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[3]')
                                                        )
                            ).click() 
        
    time.sleep(1.3)
        
    second_chat = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]')
                                                        )
                            ).click() 
        
    for _ in range(int(get_user_input('How many'))):
        
        message_area = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/textarea')
                                                            )
                                )
        message_area.click()
        message_area.send_keys('a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a aa a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a') 
        
        send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[3]/img')
                                                            )
                                ).click() 
    
except Exception as e:
    print('There has been an error opening products creation page')
    print(e)


get_user_input("DONE")
# Close the browser
driver.quit()
