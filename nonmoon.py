from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = open("nonmoon.txt", "r", encoding='UTF-8')
lines = f.readlines()
Line=[]
for line in lines:
    if line == "\n":
        continue
    else:
        print(line)
        Line.append(line)
print(Line)
f.close()

driver = webdriver.Firefox()
driver.get('https://sci-hub.se/')

for line in Line:
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/form/input[2]').send_keys(line)
    driver.find_element_by_css_selector('div#open').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li/a').click()
    time.sleep(15)

    driver.back()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/form/input[2]')

        
driver.close()