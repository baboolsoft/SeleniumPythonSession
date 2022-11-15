from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
#driver.implicitly_wait(10)
#time_out = 10
#dynamic_wait
#imp_wait will be applied for all the webElements
#global_wait
#find_element
#find_elements
#only for web elements

driver.get('https://app.hubspot.com/login')
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("test@gmail.com")
