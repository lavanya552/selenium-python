from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.common.exceptions import ElementNotInteractableException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

un='yupp552@gmail.com'
pwd='yupp@123'

driver = webdriver.Firefox(executable_path=r'D:\geckodriver-v0.19.1-win64\geckodriver.exe')
driver.get(('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))
driver.implicitly_wait(30)
username=driver.find_element_by_id('identifierId')
username.send_keys(un)
nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
nextButton.click()
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
password.click()    
password.send_keys(pwd)
signInButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
signInButton.click()

