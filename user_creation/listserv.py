from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from chrome import driver

url2 = "https://listserv.brown.edu/cgi-bin/wa?INDEX&X=OEBE49007A9D16C77D2&Y=anish_pradhan%40brown.edu"   
      
def add_listserv(user= None, email=None):
    print("Adding user email " + user + " to listserv")

    while "Logged in as:" not in driver.page_source:
        # Log in to Listserv manually
        driver.get("https://listserv.brown.edu/cgi-bin/wa?LOGON")
        try:
            print("Waiting for listserv login (times out after 60 seconds)")
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "logout.cell")))
            break
        except:
            driver.close()
    print("Logged into listserv")
    lists_to_add = ["CCV", "CCV_ANNOUNCE"]
    for list in lists_to_add:
        driver.get("https://listserv.brown.edu/cgi-bin/wa?ACTMGR1=" + list)
        driver.find_element(By.ID, "Do Not Notify the User").click()
        user_list = driver.find_element(By.ID, "Email Address and Name")
        user_list.clear()
        user_list.send_keys(("{name} <{b_email}>").format(name = user, b_email= email))
        user_list.send_keys(Keys.RETURN)
   