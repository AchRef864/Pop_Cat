from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Edge("{the path of the msedgedriver}\msedgedriver.exe")

def give_url(link):
    driver.get(link)

def one_click(cat):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, cat)))
    driver.find_element_by_id(cat).click()

give_url("https://popcat.click/")

while True:
    one_click("app")
