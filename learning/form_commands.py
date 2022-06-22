from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
# First Name
time.sleep(5)
first_name = driver.find_element(by=By.ID, value='RESULT_TextField-1')
first_name.send_keys('Muhammad')
time.sleep(2)
# Last Name
last_name = driver.find_element(by=By.ID, value='RESULT_TextField-2')
last_name.send_keys('Rizwan')
time.sleep(2)
# phone
phone = driver.find_element(by=By.ID, value='RESULT_TextField-3')
phone.send_keys('+923467374472')
time.sleep(2)
# country
country = driver.find_element(by=By.ID, value='RESULT_TextField-4')
country.send_keys('Pakistan')
time.sleep(2)
# city
city = driver.find_element(by=By.ID, value='RESULT_TextField-5')
city.send_keys('Lahore')
time.sleep(2)
# email
email = driver.find_element(by=By.ID, value='RESULT_TextField-6')
email.send_keys('muhammad.rizwan@viltco.com')
time.sleep(2)
# gender Radio Box
gender = driver.find_element(
    by=By.XPATH, value='//*[@id="RESULT_RadioButton-7_0"]').is_selected()
print(gender)
time.sleep(2)
# cheked male
driver.find_element(
    by=By.XPATH, value='/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label').click()

time.sleep(2)
gender = driver.find_element(
    by=By.XPATH, value='//*[@id="RESULT_RadioButton-7_0"]').is_selected()
print(gender)
time.sleep(2)

# check boxes
# Monday
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[17]/table/tbody/tr[2]/td/label').click()
time.sleep(2)
# Tuesday
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[17]/table/tbody/tr[3]/td/label').click()
time.sleep(2)
# Wednesday
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[17]/table/tbody/tr[4]/td/label').click()
time.sleep(2)
# Thursday
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[17]/table/tbody/tr[5]/td/label').click()
time.sleep(2)
# Friday
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[17]/table/tbody/tr[6]/td/label').click()


# Selection
driver.find_element(by=By.ID, value='RESULT_RadioButton-9').click()
time.sleep(2)
# select morning
driver.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[19]/select/option[2]').click()
time.sleep(2)
# Upload Image
driver.find_element(by=By.XPATH, value='//*[@id="q21"]').click()
time.sleep(5)

# Submit Form
driver.find_element(by=By.ID, value='FSsubmit').click()
time.sleep(2)
driver.back()
time.sleep(5)
driver.quit()
