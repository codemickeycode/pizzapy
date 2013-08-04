from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome() # Get local session of Chrome

def check_exists_by_id(e_id):
    try:
        element = browser.find_element_by_id(e_id)
    except NoSuchElementException:
        return False
    return element

# Go to the login page
browser.get("http://www.pizzahut.com.ph/2007/order.php#") # Load page

check_elem_id = check_exists_by_id("frm_email")
if check_elem_id:
    element = check_elem_id
    element.send_keys("mcy133412@yahoo.com")
    time.sleep(0.2) # Let the page load

check_elem_id = check_exists_by_id("frm_pass1")
if check_elem_id:
    element = check_elem_id
    element.send_keys("testing...") #+ Keys.RETURN
    time.sleep(0.2) # Let the page load


