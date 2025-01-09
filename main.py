from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time




s = Service(r'C:\Users\Asus\OneDrive\เดสก์ท็อป\narupon\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome(service=s)


driver.get("https://legendarywargame.com/")


# close2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/section[1]/div/section/div/div/button/svg"]').click()
# time.sleep(500)

login1 = driver.find_element(By.XPATH, '//*[@id="section3"]/div/nav/div[2]/div[1]/div/ul/li[5]/a').click()
time.sleep(3)
login2 = driver.find_element(By.XPATH, '//*[@id="frm_sign"]/div[1]/input')
login2.send_keys("Fam")
time.sleep(3)
login3 = driver.find_element(By.XPATH, '//*[@id="frm_sign"]/div[2]/input')
login3.send_keys("123456fam")
time.sleep(3)
login3 = driver.find_element(By.XPATH, '//*[@id="frm_sign"]/button[1]').click()
time.sleep(3)

search1 = driver.find_element(By.XPATH, '//*[@id="cn_q"]')
search1.send_keys("adeptus custodes"+ Keys.ENTER)
time.sleep(3)
search2 = driver.find_element(By.XPATH, '//*[@id="colum"]/div/div/div[3]/div[2]/button').click()
time.sleep(3)
search2 = driver.find_element(By.XPATH, '//*[@id="colum"]/div/div/div[3]/div[2]/button').click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()