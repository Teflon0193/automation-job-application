from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

service = Service(executable_path=YOUR_PATH)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get(YOUR_HTTPS_LINK)

sing_in_button = driver.find_element(By.CLASS_NAME, "btn-secondary-emphasis")
sing_in_button.click()

#Wait for the next page to load.
time.sleep(3)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(YOUR_EMAIL)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(YOUR_PASSWORD)
password_field.send_keys(Keys.ENTER)

#Locate the apply button
time.sleep(2)
easyapply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
time.sleep(2)

#You can modify it according to your set up applying process

#Submit the application
click_next = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button").click()
time.sleep(2)
resume_next = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end .artdeco-button--primary").click()
time.sleep(3)

location = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/fieldset/div[1]/label")
location.click()
time.sleep(1)

Python_experience = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[5]/div/div/div[1]/div/input")
Python_experience.send_keys("1")
time.sleep(1)

Work_experience = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[6]/div/div/div[1]/div/input")
Work_experience.send_keys("1")
time.sleep(1)

select_option = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[7]/div/div/select/option[2]")
select_option.click()

review = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
review.click()
time.sleep(1)

submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[4]/button[2]")
submit.click()


#driver.close()