from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(x+y)) # ищем элемент с текстом "Python"
  
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла




