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
import multiprocessing

load_dotenv()

def get_user_input(prompt):
    root = tk.CTk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", prompt)
    return user_input

def login(wait, email, password):
    # Click the login button
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eAOppz'))).click() 

    # Input login
    login_input = wait.until(EC.element_to_be_clickable((By.ID, 'email'))).send_keys(email)

    # Input password
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys(password)

    # Logs in 
    do_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fAJeQq'))).click()
    
def auto_messages(messages_amount, email, password):
    
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('CLIENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password)
    
    time.sleep(3)
    
    menu = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]'))).click()
        
    messages_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/span[3]'))).click() 
        
    time.sleep(1.3)
        
    second_chat = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]'))).click() 
        
    for _ in range(messages_amount):
        
        message_area = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fPlqIq')))
        
        message_area.send_keys('a a a a a a a a a a a a a a a a a a a a a a a a') 
        
        send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fKTyJf'))).click()
        
    driver.quit()
    
def main():
    messages_amount = int(get_user_input('How many messages?'))
    
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(target=auto_messages, args=(messages_amount, email, password))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
        
if __name__ == "__main__":
    main()
