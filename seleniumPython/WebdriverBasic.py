from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\\Users\\angap\\OneDrive\\Desktop\\python selenium program\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("stock market india")
optionList=driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li div.wM6W7d span')
print(len(optionList))
for ele in optionList:
    print(ele.text)
    if ele.text =='stock market india live':
        ele.click()
        break

time.sleep(5)
driver.quit()