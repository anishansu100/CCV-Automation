import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
global driver
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)