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
driver.get("https://www.orangehrm.com/contact-sales/")

#using select dropdown
def Select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)

#using without select dropdown
def Select_values_from_dropdown(DropdownList, value):
    print(len(DropdownList))
    for ele in DropdownList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break



eleEmployee = driver.find_element(By.ID, 'Form_getForm_NoOfEmployees')
eleEmployees = driver.find_elements(By.XPATH, "//select[@id='Form_getForm_NoOfEmployees']/option")


Select_values_from_dropdown(eleEmployees, '501 - 600')
Select_values_from_dropdown(eleEmployees, '601 - 700')
#Select_values(eleEmployee, '251 - 300')
#Select_values(eleCountry, 'India')

#select = Select(eleEmployee)
#select.select_by_index(2)


#select = Select(eleCountry)
#select.select_by_visible_text('India')


# without using select method /using generic method
eleCountry = driver.find_element(By.ID, 'Form_getForm_Country')
select = Select(eleCountry)
countryList = select.options
for ele in countryList:
    print(ele.text)
    if(ele.text == 'Germany'):
        ele.click()
        break



time.sleep(5)
driver.quit()
