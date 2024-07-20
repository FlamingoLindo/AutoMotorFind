import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import time
from Functions.cpf import gera_e_valida_cpf
from Functions.cnpj import gera_cnpj

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
)


appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

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
        ).click()

        time.sleep(1.5)
        
        cpf = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="000.000.000-00"]'))
        )
        cpf.send_keys(gera_e_valida_cpf())  
        
        cnpj = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00.000.000/0000-00"]'))
        )
        cnpj.send_keys(gera_cnpj())  
        
        phone2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="(00) 9 1234-56789"]'))
        )
        phone2.send_keys('11923847569')
        
        next_btn2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
        ).click()
        time.sleep(1.5)
        
        cep = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="00000-000"]'))
        )
        cep.send_keys('39408197')
        
        num = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Número"]'))
        )
        num.send_keys('1')
        
        actions = TouchAction(self.driver)
        actions.press(x=500, y=1500).move_to(x=500, y=500).release().perform()

        next_btn3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View")'))
        ).click()
        
        password1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[1]'))
        )
        password1.send_keys('Aa12345678!')
        
        password2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.EditText[@text="Senha@!23"])[2]'))
        )
        password2.send_keys('Aa12345678!')
        
        next_btn4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
        ).click()
        
        car = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Carros"]/android.view.View'))
        ).click()

        classic = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Classicos"]/android.view.View'))
        ).click()

        restored = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Restaurados OEM"]/android.view.View'))
        ).click()

        lane = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Pista"]/android.view.View'))
        ).click()

        race = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Race"]/android.view.View'))
        ).click()

        bikes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Motos"]/android.view.View'))
        ).click()
        
        drift = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Drift"]/android.view.View'))
        ).click()

        black = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Placa preta"]/android.view.View'))
        ).click()

        next_btn5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)'))
        ).click()

        agree = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup'))
        ).click()

        done_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, '00000000-0000-0256-ffff-ffff000002ef'))
        ).click()

if __name__ == '__main__':
    unittest.main()