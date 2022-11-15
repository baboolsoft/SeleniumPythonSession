from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.drivers.chrome import ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://www.amazon.in/")
time.sleep(2)
best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].click();", best_sellers) #javascript click method

title = driver.execute_script("return document.title;") #javascript get title method
print(title)

driver.execute_script("history.go(0);") #javascript refresh page

# driver.execute_script("alert('hello selenium');") #javascript create the alert popup
# time.sleep(3)

inner_text = driver.execute_script("return document.documentElement.innerText;") #javascript innertext method
print(inner_text)

time.sleep(3)

form_text = driver.find_element(By.LINK_TEXT, 'Best Sellers')
driver.execute_script("arguments[0].style.border = '3px solid red'", form_text)  #javascript text border

time.sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  #javascript scrolldown
time.sleep(3)

driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")  #javascript scrollUp
time.sleep(3)

Bestsellers = driver.find_element(By.XPATH, "//h3[text()='About Bestsellers']")
driver.execute_script("arguments[0].scrollIntoView(true);", Bestsellers)  #javascript scrollinto particular text
time.sleep(3)


print(driver.execute_script("return navigator.userAgent;")) #javascript user(browser) details
time.sleep(3)

driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")  #javascript scrollUp
time.sleep(3)

driver.execute_script("document.getElementById('twotabsearchtextbox').value='watches'") #javascript sendkeys
time.sleep(3)