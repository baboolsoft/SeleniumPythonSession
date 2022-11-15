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
driver.get("https://www.amazon.in/")
print(driver.title)

#Scraping links
linktest = driver.find_elements(By.TAG_NAME, 'a')
print(len(linktest))
for ele in linktest:
    link_text = ele.text
    print(link_text)
    print(ele.get_attribute('href'))

#scraping images
linkImg=driver.find_elements(By.TAG_NAME, 'img')
print(len(linkImg))

for ele in linkImg:
    print(ele.get_attribute('src'))