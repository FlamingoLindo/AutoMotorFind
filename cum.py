import unittest
from appium import webdriver
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

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="motorfind"]')
        el.click()
        time.sleep(6)
        register_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Cadastrar"]').click()
        
        name = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Ex. José Santos"]')
        name.click()
        name.send_keys("Nome")
        
        email = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Ex. nome@email.com"]')
        email.click()
        email.send_keys("email@gmail.com")
        
        phone = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="(00) 9 1234-56789"]')
        phone.click()
        phone.send_keys("11987456321")
        
        next_btn = self.driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="Próximo"]/android.view.ViewGroup/android.view.View').click()
        
        time.sleep(12121212)
        
        

if __name__ == '__main__':
    unittest.main()