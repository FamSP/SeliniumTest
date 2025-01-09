from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver service
s = Service(r'C:\Users\Asus\OneDrive\เดสก์ท็อป\narupon\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open the website
driver.get("https://legendarywargame.com/")

# #######################LOGIN PROCESS#########################################
login1 = driver.find_element(By.XPATH, '//*[@id="section3"]/div/nav/div[2]/div[1]/div/ul/li[5]/a').click()
time.sleep(3)
login2 = driver.find_element(By.XPATH, '//*[@id="frm_sign"]/div[1]/input')
login2.send_keys("Fam")
time.sleep(3)
login3 = driver.find_element(By.XPATH, '//*[@id="frm_sign"]/div[2]/input')
login3.send_keys("123456fam")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="frm_sign"]/button[1]').click()
time.sleep(3)

# #######################SEARCH PROCESS#########################################
search1 = driver.find_element(By.XPATH, '//*[@id="cn_q"]')
search1.send_keys("adeptus custodes" + Keys.ENTER)
time.sleep(3)

# Add item to cart and handle the alert
try:
    search2 = driver.find_element(By.XPATH, '//*[@id="colum"]/div/div/div[3]/div[2]/button')
    search2.click()
    time.sleep(2)
    
    # Handle the alert
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)  # For debugging
    alert.accept()  # Accept the alert
    print("Alert accepted successfully.")
    
except Exception as e:
    print("Error handling alert:", str(e))
time.sleep(3)


# #######################PURCHACE PROCESS#########################################
purchace1 = driver.find_element(By.XPATH, '/html/body/div[4]/a/img').click()
time.sleep(3)
purchace2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[1]/form/div[2]/div/button[2]').click()
time.sleep(5)
purchace2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/form/button').click()
time.sleep(10)
driver.quit()
