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
load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window

    user_input = simpledialog.askstring("Input", prompt)

    return user_input

# Drive stuff
driver_path = './chromedriver.exe'
s = Service(driver_path)
driver = webdriver.Chrome(service=s)  

driver.get(os.getenv('MASTER_URL'))

wait = WebDriverWait(driver, 5)

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

# Opesn the plans page
plans_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/aside/nav/a[3]')
                                                  )
                       ).click()

categ_type = int(get_user_input('Escolha a categoria: [1]Carros, [2]Motos, [3]Trucks, [4]Race, [5]Drag, [6]Peças, [7]Serviços, [8]Clássicos'))

# Ask how many plans are going to be created
plan_amount = int(get_user_input("How many?"))

count = 1

for _ in range(plan_amount):
    
    # Opens the plan creation modal
    add_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button'))).click()
    
    # Click at the category dropdown
    categ_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[1]/div')
                                                    )
                        ).click()
    
    # Randonmly choose the category
    #categ_choose = random.randint(1, 8)  
    
    # Click at the choosen category
    categ_option_click = wait.until(EC.presence_of_element_located
                            ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[3]/div[1]/div[2]/div[{categ_type}]")
                                )
                            ).click()
    
    # Opens the subcategory dropdown
    subcateg_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/div[2]/div')
                                                    )
                        ).click()
    
    # Randonmly choose the subcategory
    subcateg_choose = random.randint(1, 4)
    
    # Click the choosen category
    subcateg_option_click = wait.until(EC.presence_of_element_located
                            ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[3]/div[2]/div[2]/div[{subcateg_choose}]")
                                )
                            ).click()
    
    # Set up names
    name = ""
    if categ_type == 1:
        name = "Carros"
    elif categ_type ==2:
        name = "Motos"
    elif categ_type ==3:
        name = "Trucks"
    elif categ_type ==4:
        name = "Race"
    elif categ_type ==5:
        name = "Drag"
    elif categ_type ==6:
        name = "Peças"
    elif categ_type ==7:
        name = "Serviços"
    elif categ_type ==8:
        name = "Clássicos"
    
    # Inputs the plan name 
    plan_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]')
                                                    )
                        ).send_keys(f"Automatic Plan {name} {count}")
    
    # Randonmly generate fee value
    sub_fee_input = random.randint(1,9999999)
    
    # Inputs the random fee value
    sub_fee = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subscriptionFeeValue"]')
                                                    )
                        ).send_keys(sub_fee_input)

    # Randonmly generate charge value
    charge_input = random.randint(1,9999999)
    
    # Inputs the charge value
    charge = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="chargingValue"]')
                                                    )
                        ).send_keys(charge_input)
    
    # Opens the time dropdown
    time_drop_down = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[4]/form/div[5]/div/div/div')
                                                           )
                                ).click()
    
    # Randonmly choose the time type
    time_input = random.randint(2, 3)

    # Choose the choosen time type
    time_option_click = wait.until(EC.presence_of_element_located
                            ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[5]/div/div[2]/div[2]/div[{time_input}]")
                                )
                            ).click()
    
    # Randonmly choose the comission 
    comission_input = random.randint(1, 3)
    print(comission_input)

    # Condions according to the comission type
    if comission_input == 1:
        pass
    elif comission_input == 2:
        
        # Opens the comission dropdown
        comission_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[6]/div/div/div')
                                                            )
                                    ).click()
        
        time.sleep(0.5)
        
        # Click the choosen comission type
        comission_option_click = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[6]/div[1]/div/div[2]/div[{comission_input}]")
                                    )).click()
        
        random_percentage = random.randint(1,100)
        percentage = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='commissionValue']")
                                                    )
                        ).send_keys(random_percentage)
    elif comission_input == 3:
        # Opens the comission dropdown
        comission_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[6]/div/div/div')
                                                            )
                                    ).click()
        
        time.sleep(0.5)
        
        # Click the choosen comission type
        comission_option_click = wait.until(EC.element_to_be_clickable
                                ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[6]/div[1]/div/div[2]/div[{comission_input}]")
                                    )).click()
        
        random_value2 = random.randint(1,999999)
        value = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='valuePerSale']")
                                                    )
                        ).send_keys(random_value2)
    
    # Random stock 
    random_stock = random.randint(1,99999)
    
    # Input random stock
    stock = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='stock']")
                                                    )
                        ).send_keys(random_stock)
    
    # Random feature value
    random_feature = random.randint(1,99999)
    
    # Inputs feature value
    feature = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='featuredProducts']")
                                                    )
                        ).send_keys(random_feature)
    
    # Input description
    description = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='description']")
                                                    )
                        ).send_keys(f"Description {count}")
    
    # Click at done button
    done = wait.until(EC.presence_of_element_located
                            ((By.XPATH, f"/html/body/main/div/div/div[4]/form/div[1]/div/button[2]")
                                )
                            ).click()
    
    # Confirm the creation button
    done2 = wait.until(EC.presence_of_element_located
                            ((By.XPATH, f"/html/body/main/div/div/div[4]/div/button")
                                )
                            ).click()

    count += 1
    
    
    
get_user_input("DONE")
# Close the browser
driver.quit()
