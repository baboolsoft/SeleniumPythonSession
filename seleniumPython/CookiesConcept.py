from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.reddit.com/')
print(driver.get_cookies())  #dictionary value (hashtable) key value pair

driver.add_cookie({"name": "AnguPython", "domain": "reddit.com", "value": "python"})

#print(driver.get_cookies())

cookies = driver.get_cookies()

for cook in cookies:
    print(cook)

time.sleep(3)
