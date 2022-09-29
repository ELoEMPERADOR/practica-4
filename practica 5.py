from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os

driver = webdriver.Chrome(executable_path=r"C:\Users\reyna\OneDrive\Escritorio\REY\chromedriver.exe")

driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()

Inicio = driver.find_element (By.ID, "signin2")
Inicio.click()

usuario = driver.find_element (By.ID, "sign-username").click()

usuario.send_keys("reynaldo10000@gmail.com")
time.sleep(secs=2)

password = driver.find_element (By.ID, "sign-password")
password.click()
password.send_keys("oruga40000.")
time.sleep(secs=2)

boton = driver.find_element(By.ID, "")

driver.quit()