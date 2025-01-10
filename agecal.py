import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

# Set up ChromeDriver service
s = Service(r'C:\Users\Asus\OneDrive\เดสก์ท็อป\narupon\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open the website
driver.get("https://www.calculator.net/")

# กดเข้า age calculation
agecal1 = driver.find_element(By.XPATH, '//*[@id="hl5"]/li[1]/a').click()

# เปลี่ยนเดือน
month_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="today_Month_ID"]'))
month_dropdown.select_by_index(7)

# เปลี่ยนวัน
day_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="today_Day_ID"]'))
day_dropdown.select_by_index(28)

# เปลี่ยนปี
year_field = driver.find_element(By.XPATH, '//*[@id="today_Year_ID"]')
for _ in range(4):
    year_field.send_keys(Keys.BACKSPACE)
year_field.send_keys("2000")


driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/form/table/tbody/tr[3]/td[2]/input').click()

result = driver.find_element(By.XPATH, '//*[@id="content"]/p[1]').text  # ปรับ XPath ให้ตรงกับตำแหน่งผลลัพธ์จริง
print(f"Result: {result}")

# ใช้ regular expression เพื่อแยกปี เดือน และวัน
age_match = re.search(r'(\d+)\s+years\s+(\d+)\s+months\s+(\d+)\s+days', result)

if age_match:
    years = age_match.group(1)
    months = age_match.group(2)
    days = age_match.group(3)
    formatted_age = f"{years} years, {months} months, {days} days"
    print(f"Age: {formatted_age}")
    
    # ค่าที่คาดหวัง
    expected_result = "24 years, 4 months, 12 days"
    
    # ใช้ assert เพื่อตรวจสอบว่าอายุที่คำนวณได้ตรงกับค่าที่คาดหวัง
    assert formatted_age == expected_result, f"Expected {expected_result}, but got {formatted_age}"
else:
    print("Age format not found.")

# expected_result = "23 years, 4 months, 13 days" 
# assert expected_result in result


time.sleep(5)


driver.quit()
