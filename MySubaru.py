from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mysubaru.com/login.html")
assert "MySubaru" in driver.title
userName = driver.find_element_by_name("username")
userName.clear()
userName.send_keys("user@name")

passWord = driver.find_element_by_name("password")
passWord.clear()
passWord.send_keys("password")

passWord.send_keys(Keys.RETURN)

mileage = driver.find_element_by_id("estMileage").text

output = "{}, {}\n".format(dt_string, mileage)

with open('C:\Python\Subaru.txt', 'a') as file:
    file.writelines(output)

driver.close()