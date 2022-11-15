from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Chrome(executable_path=GeckoDriverManager().install(), options=options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
print(driver.title)
time.sleep(3)
