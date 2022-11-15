import document as document
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import packaging

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.reddit.com/')
time.sleep(1)
#driver.get_screenshot_as_file('reddit_1.png');

''' full screenshot'''
#make sure that you are running in headless mode

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element(By.TAG_NAME, 'body').screenshot('reddit_full_1.png')
driver.quit()
