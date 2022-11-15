from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time
import packaging

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi?mobilelogin=1")

driver.find_element(By.NAME,'proceed').click()
time.sleep(3)

alert=driver.switch_to.alert
print(alert.text)
alert.accept()

driver.switch_to.default_content()

time.sleep(3)
driver.quit()