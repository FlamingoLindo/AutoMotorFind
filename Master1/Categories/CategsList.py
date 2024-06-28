import pandas as pd
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

def register_category():
    catg_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                       )
                            ).send_keys(row['title'])
    
    catg_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')
                                                      )
                           ).send_keys(row['description'])
    
    register = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/form/div[2]/button[2]')
                                                     )
                          ).click()
    
    done = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/button')
                                                 )
                      ).click()

# Load the Excel file
df = pd.read_excel(r'C:\Users\josef\Desktop\AfterLifeDeath\MotorFind\AutoMotorFind\Files\CategoriesList.xlsx')
print(df)

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

# Dictionary to map each type to its corresponding XPath
type_to_xpath = {
    "Carros": '/html/body/main/div/div/div[2]/div[1]/div[1]/div[2]',
    "Motos": '/html/body/main/div/div/div[2]/div[2]/div[1]/div[2]',
    "Trucks": '/html/body/main/div/div/div[2]/div[3]/div[1]/div[2]',
    "Race": '/html/body/main/div/div/div[2]/div[4]/div[1]/div[2]',
    "Drag": '/html/body/main/div/div/div[2]/div[5]/div[1]/div[2]',
    "Peças": '/html/body/main/div/div/div[2]/div[6]/div[1]/div[2]',
    "Serviços": '/html/body/main/div/div/div[2]/div[7]/div[1]/div[2]',
    "Clássicos": '/html/body/main/div/div/div[2]/div[8]/div[1]/div[2]'
}

type_to_num = {
    "Carros": 1,
    "Motos": 2,
    "Trucks": 3,
    "Race": 4,
    "Drag": 5,
    "Peças": 6,
    "Serviços": 7,
    "Clássicos": 8
}

# Loop through the DataFrame and process each row
for index, row in df.iterrows():
    # Show what index it's currently inputting (Just for debugging)
    print(index)
    
    if row['type'] in type_to_xpath:
        num = type_to_num[row['type']]
        xpath_register = f'/html/body/main/div/div/div[2]/div[{num}]/div[2]/div[1]'
        
        xpath = type_to_xpath[row['type']]
        
        catg = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        catg.click()
        
        register = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_register)
                                                         )
                              ).click() 

        time.sleep(1)

        register_category()
        
        catg.click()


# Close the browser
driver.quit()
