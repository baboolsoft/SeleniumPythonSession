from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://www.orangehrm.com/contact-sales/")
print(driver.title)

driver.execute_script("window.scrollBy(0,710)", "")

Fullname = driver.find_element(By.ID, 'Form_getForm_FullName')
phoneno = driver.find_element(By.ID, 'Form_getForm_Contact')
email = driver.find_element(By.ID, 'Form_getForm_Email')
submit = driver.find_element(By.ID, 'Form_getForm_action_submitForm')

Fullname.send_keys("angapparaja")
phoneno.send_keys("9384929444")
email.send_keys("angapparaja494@gmail.com")
submit.click()

#Css selector
#driver.find_element(By.CSS_SELECTOR, '#username').send_keys("angapparaja494@gmail.com")

#ClassName
#driver.find_element(By.CLASS_NAME, 'login-email').send_keys("angapparaja494@gmail.com")

#Xpath
#driver.find_element(By.XPATH, "//input[@class='form-control private-form__control login-email']").send_keys("angapparaja494@gmail.com")

#partial link Text
#driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').send_keys("angapparaja494@gmail.com")

#tagname
# headerelement = driver.find_element(By.TAG_NAME, 'h1')
# headerelement.click()

time.sleep(5)
driver.close()
