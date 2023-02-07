import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
baseUrl = "https://valbury.co.id/campaign/trading-tools-acuity"

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_register_with_correct_name_email_and_phone_number_1(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"name").send_keys("Rika Meilani")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("rikamela@outlook.com")
        time.sleep(1)
        browser.find_element(By.ID,"telepon").send_keys("81705013973")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        title_page = browser.find_element(By.XPATH,"//h3[text()='Verifikasi']").text
        self.assertIn('Verifikasi', title_page)

    def test_a_test_a_failed_register_with_empty_name_2(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("sirdandy@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"telepon").send_keys("81905017120")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_error = browser.find_element(By.ID,"error-name").text
        self.assertEqual(alert_error, 'This field is required')
    
    def test_a_test_a_failed_register_with_empty_email_3(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"name").send_keys("Muhammad Ali")
        time.sleep(1)
        browser.find_element(By.ID,"telepon").send_keys("853555291")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_error = browser.find_element(By.ID,"error-email").text
        self.assertEqual(alert_error, 'This field is required')

    def test_a_test_a_failed_register_with_empty_phone_number_4(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"name").send_keys("Bagus Mulyawan")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("bagus15@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_error = browser.find_element(By.ID,"error-telepon").text
        self.assertEqual(alert_error, 'This field is required')

    def test_a_test_a_failed_register_with_empty_name_and_phone_number_5(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"email").send_keys("sandymulya@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_name = browser.find_element(By.ID,"error-name").text
        self.assertEqual(alert_name, 'This field is required')

        alert_phonenum = browser.find_element(By.ID,"error-telepon").text
        self.assertEqual(alert_phonenum, 'This field is required')

    def test_a_test_a_failed_register_with_empty_email_and_phone_number_6(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"name").send_keys("Hamdani")
        time.sleep(1)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_email = browser.find_element(By.ID,"error-email").text
        self.assertEqual(alert_email, 'This field is required')
        
        alert_phonenum = browser.find_element(By.ID,"error-telepon").text
        self.assertEqual(alert_phonenum, 'This field is required')
    
    def test_a_test_a_failed_register_with_all_empty_fields_7(self): 
        # steps
        browser = self.browser
        browser.get(baseUrl)
        time.sleep(3)
        browser.find_element(By.ID,"flexCheckChecked").click()
        time.sleep(1)
        browser.find_element(By.ID,"btn-daftar").click()
        time.sleep(1)

        # validasi
        alert_name = browser.find_element(By.ID,"error-name").text
        self.assertEqual(alert_name, 'This field is required')

        alert_email = browser.find_element(By.ID,"error-email").text
        self.assertEqual(alert_email, 'This field is required')
        
        alert_phonenum = browser.find_element(By.ID,"error-telepon").text
        self.assertEqual(alert_phonenum, 'This field is required')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()