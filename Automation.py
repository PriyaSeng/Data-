# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\PRIYA\Downloads\MIT\chromedriver.exe")

driver.get(r"https://web.whatsapp.com")

search = driver.find_elements_by_class_name(r"_2S1VP")


search[0].send_keys("Nidhi"+Keys.ENTER)

search=driver.find_elements_by_class_name(r"_2S1VP")

search[1].send_keys("Hi"+Keys.ENTER)







