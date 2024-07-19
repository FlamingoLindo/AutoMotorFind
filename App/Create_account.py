import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options())

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_create_account(self) -> None:
        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="motorfind"]'))
        )
        el.click()

        register_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Cadastrar"]'))
        ).click()

        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. José Santos"]'))
        )
        name.send_keys("Nome")

        email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Ex. nome@email.com"]'))
        )
        email.send_keys("email@gmail.com")

        phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
        )
        phone.send_keys("11987456321")

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Próximo"]/android.view.ViewGroup/android.view.View'))
        )
    
        next_btn.click()

        time.sleep(1.5)
        
        cpf = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="000.000.000-00"]'))
        )
        cpf.send_keys()  
        
        cnpj = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00.000.000/0000-00"]'))
        )
        cnpj.send_keys()  
        
        phone2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
        )
        phone2.send_keys()
        
        next_btn.click()

        time.sleep(1.5)
        
        cep = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00000-000"]'))
        )
        cep.send_keys()
        
        num = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Número"]'))
        )
        num.send_keys()
        
        next_btn.click()
        
        password1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[1]'))
        )
        password1.send_keys('Aa12345678!')
        
        password2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[2]'))
        )
        password2.send_keys('Aa12345678!')
        
        next_btn.click()
        
        

if __name__ == '__main__':
    unittest.main()