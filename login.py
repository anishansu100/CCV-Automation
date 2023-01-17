import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from chrome import driver
def click_b(time, path):
        WebDriverWait(driver, time).until(
                        EC.visibility_of_element_located((By.XPATH, path))).click()
#/Applications/Google Chrome.app/Contents/MacOS remote-debugging-port=9222 –user-data-dir=””
url = "https://groups.brown.edu/shibboleth-ds/index.html?entityID=https%3A%2F%2Fgroups.brown.edu%2Fshibboleth&return=https%3A%2F%2Fgroups.brown.edu%2FShibboleth.sso%2FLogin%3FSAMLDS%3D1%26target%3Dss%253Amem%253A1c95c7e21913e62e9c2825adc0179e584d6268c80640f128cc0201fb1165e46d"
def login_grouper(username, password):
        driver.get(url)
        click_b(30, "//*[@id='auth-form']/fieldset/div[1]/input")
        WebDriverWait(driver, timeout=10)
        if   len(driver.find_elements(By.XPATH, "//*[@id='username']")) > 0:
                user = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
                        (By.XPATH, "//*[@id='username']")))
                user.send_keys(username)
                passw = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
                        (By.XPATH, "//*[@id='password']")))
                passw.send_keys(password)
                click_b(3,  "//*[@id='login']/fieldset/button")
                click_b(30, "//*[@id='grouperLogin']/table/tbody/tr[5]/td/a")
                click_b(3, "//*[@id='Content']/div[2]/div[2]/div[2]/ul/li[3]/a")
                click_b(3, "//*[@id='Content']/div[2]/div[2]/div[2]/ul/li[5]/a")
                click_b(3, "//*[@id='Content']/div[2]/div[2]/div[2]/ul/li[31]/a")
                
        else:
                click_b(3, "//*[@id='grouperLogin']/table/tbody/tr[5]/td/a")
        click_b(30, "//*[@id='Content']/div[2]/div[2]/div[2]/ul/li[2]/a")
        click_b(30, "//*[@id='Content']/div/div/div[2]/div/div/a[3]")
                
def main():
        login_grouper("apradha7", "Vimala@100")
main()