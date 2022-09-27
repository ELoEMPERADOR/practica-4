from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time #para dar pausas a las acciones de selenium por que se buguea esta chikito
import pandas

driver = webdriver.Chrome(executable_path=r"C:\Users\reyna\OneDrive\Escritorio\REY\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.clima.com/")


driver.find_element (By.XPATH, "//li[@class= 'm_list_countrys_mx']/a").click()
time.sleep(secs=10)

driver.find_element (By.XPATH, "//input[@id=\'term']").send_keys("Querétaro")
time.sleep(secs=10)
#driver.find_element (By.CSS_SELECTOR, "li:nth-child(1) .item-name").click()


driver.quit()
#usuario.send_keys("queretaro")
#usuario.send_keys(Keys.ENTER)

#password = driver.find_element (By.ID, "password")
#time.sleep(secs=10)
#password.send_keys("oruga2000.")

#usuario.send_keys(Keys.ENTER)
