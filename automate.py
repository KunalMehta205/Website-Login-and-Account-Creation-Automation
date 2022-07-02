import pandas as pd  # library for importing data
from selenium import webdriver  # automating the process
import time
import random  # generating random usernames

# importing emails from a csv file
df = pd.read_csv('C:/Users/hp/Desktop/Database1.csv')
emails = list(df.Emails)

# generating usernames
usernames = []
for i in range(400):
    user = "abcdefghijklmnopqrstuvwxyz12345678"
    user_Name = "".join(random.sample(user, 7))
    usernames.append(user_Name)

# generating set of a passwords
password = []
for i in range(400):
    passWord = "1234567890qwertyuiopmnbvcxzlkjhgfdsa!@#$%^&*"
    passName = "".join(random.sample(passWord, 10))
    password.append(passName)

# website to be tested
url = "https://streamm.io/signin"  # example - https://streamm.io/signin

driver = webdriver.Chrome("E:/chromedriver")  # chrome driver

count = 0
for i in range(0, len(emails)):
    driver.get(url)
    time.sleep(4)
    driver.find_element_by_class_name("btn-default").click()
    driver.find_element_by_id("email").send_keys(emails[i])
    driver.find_element_by_id("password").send_keys(password[i])
    driver.find_element_by_id("confirmPassword").send_keys(password[i])
    driver.find_element_by_id("checkbox").click()
    driver.find_element_by_class_name("btn-warning").click()
    time.sleep(2)
    count = count + 1

print("Success")
print(count)
