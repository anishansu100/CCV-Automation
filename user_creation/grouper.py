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
url = "https://groups.brown.edu/grouper/populateFindNewMembers.do?extension=ALL&displayNameDb=BROWN%3ASERVICES%3AHPC%3AALL&displayName=BROWN%3ASERVICES%3AHPC%3AALL&typeOfGroupDb=group&groupId=a815bed6b1ae442d9d4df08c4f3d61ff&description=&stemId=7d3f0eb75c2c4e1f9f95a9e5128f1d2b&subjectType=group&uuid=a815bed6b1ae442d9d4df08c4f3d61ff&subjectId=a815bed6b1ae442d9d4df08c4f3d61ff&modifierUuid=912ee0429eac4947894109787475a30a&displayExtensionDb=ALL&nameDb=BROWN%3ASERVICES%3AHPC%3AALL&parentStemName=BROWN%3ASERVICES%3AHPC&id=a815bed6b1ae442d9d4df08c4f3d61ff&group=Group%5Bname%3DBROWN%3ASERVICES%3AHPC%3AALL%2Cuuid%3Da815bed6b1ae442d9d4df08c4f3d61ff%5D&creatorUuid=7c3179121b454e9b8efea1865b1732cf&alternateName=&contextId=88ff4ce754c6468faa23495ac73b0141&parentUuid=7d3f0eb75c2c4e1f9f95a9e5128f1d2b&displayExtension=ALL&groupName=ALL&name=BROWN%3ASERVICES%3AHPC%3AALL&extensionDb=ALL&isGroup=true&alternateNameDb=&descriptionDb=&desc=ALL"
def add_user(driver, user):
    driver.get(url)
    brown_user = WebDriverWait(driver, 120).until(EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='searchTerm']")))
    brown_user.clear() 
    brown_user.send_keys(user)  
    click_b(60, "//*[@id='SearchFormBean']/fieldset/table/tbody/tr[1]/td[2]/input")  
    click_b(60, "//*[@id='Content']/div/div/div[2]/form/div[4]/p/input")     