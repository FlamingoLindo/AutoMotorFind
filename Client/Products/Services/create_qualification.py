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
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz')
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
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fAJeQq')
                                                        )
                            ).click()  
except Exception as e:
    print('There has been an error on the login')
    print(e)

try:
    count = 1
    
    time.sleep(2)
    
    # Click sales
    sales = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz')
                                                        )
                            ).click() 
    
    amount_str = get_user_input("How many?")
    amount_int = int(amount_str)
    for i in range(amount_int):
        
        # Click add product button
        add_service_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/button[1]')
                                                            )
                                ).click()

        # Click add product button 2
        add_prod_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/button[2]')
                                                            )
                                ).click()
        
        #
        name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                            )
                                ).send_keys(f'Auto Qualification Eduardo {count}')
        
        #
        rand_duration = random.randint(1,99)
        duration = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="duration"]')
                                                            )
                                ).send_keys(rand_duration)
        
        #
        time_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div/div/div')
                                                            )
                                ).click()
        
        #
        rand_time = random.randint(0,1)
        time_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-2-option-{rand_time}"]')
                                                            )
                                ).click()
        
        #
        sub_category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/div/div[1]')
                                                            )
                                ).click()
        
        # 
        quali_sub_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-3-option-1"]')
                                                            )
                                ).click()
        
        #
        quali_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/div/div')
                                                            )
                                ).click()
        
        #
        rand_quali = random.randint(0,2)
        quali_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-6-option-{rand_quali}"]')
                                                            )
                                ).click()
        
        #
        quali_lvl_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[5]/div/div[1]')
                                                            )
                                ).click()
        
        #
        rand_lvl = random.randint(0,2)
        quali_type_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-7-option-{rand_quali}"]')
                                                            )
                                ).click()
        
        #
        quali_lang_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[6]/div/div')
                                                            )
                                ).click()
        
        #
        rand_lang = random.randint(0,2)
        quali_lang_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-8-option-{rand_lang}"]')
                                                            )
                                ).click()
        
        #
        rand_value = random.randint(1,999)
        value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="value"]')
                                                            )
                                ).send_keys(rand_value)
        
        #
        highlight_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[8]/div/div')
                                                            )
                                ).click()
        
        # 
        rand_high = random.randint(0,1)
        highlight_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-select-4-option-{rand_high}']")
                                                            )
                                ).click()
        
        # 
        address_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[2]/div[3]/div[1]/div/div')
                                                            )
                                ).click()
        
        # 
        adress_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-5-option-0"]')
                                                            )
                                ).click()
        
        # Sets images path
        vehicles_paths_string  = os.getenv('CAR_IMAGES')
        vehicles_image_paths = vehicles_paths_string.split(',')
        
        for _ in range(3):
            #
            image = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[9]/div[2]/label/img')
                                                                )
                                    ).click()
            
            rand_img = random.choice(vehicles_image_paths)
            
            time.sleep(1)
            
            pyautogui.write(rand_img)
            
            time.sleep(1)
            
            pyautogui.press('enter')
            
            time.sleep(0.5)
            
        #
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link"]')
                                                            )
                                ).send_keys('https://motorfind-client.netlify.app/manageproduct/add')
        
        #
        desc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="description"]')
                                                            )
                                ).send_keys(f'AUTOMATIC DESCRIPTION {count}')
        
        #
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/button[1]")
                                                            )
                                ).click()
        
        time.sleep(4)
        
        pyautogui.press('f5')
        
        time.sleep(2)
        
        count += 1
except Exception as e:
    print('There has been an error opening products creation page')
    print(e)


get_user_input("DONE")
# Close the browser
driver.quit()
