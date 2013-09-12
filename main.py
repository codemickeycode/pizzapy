import config.settings as settings
#from config.settings import credentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
from pprint import pprint

'''
browser = webdriver.Chrome() # Get local session of Chrome

def check_exists_by_id(e_id):
    try:
        element = browser.find_element_by_id(e_id)
    except NoSuchElementException:
        return False
    return element

# Load your username and password from config/settings.py
uname = settings.credentials['username']
pwd = settings.credentials['pwd']

# Go to the login page
browser.get("http://www.pizzahut.com.ph/2007/order.php#") # Load page

check_elem_id = check_exists_by_id("frm_email")
if check_elem_id:
    element = check_elem_id
    element.send_keys(uname)
    time.sleep(0.2) # Let the page load

check_elem_id = check_exists_by_id("frm_pass1")
if check_elem_id:
    element = check_elem_id
    #element.send_keys(pwd)
    element.send_keys(pwd + Keys.RETURN)
    time.sleep(0.2) # Let the page load

textbox = browser.find_element_by_xpath(
        '//div/strong[contains(text(), "%s")]' \
        '/following-sibling::br[contains(text(), "%s"]' \
        '/following-sibling::input[1]' % \
        ("Super Supreme", "309"))
print "textbox: ", textbox
print "textbox: ", textbox.text
textbox.send_keys("1")
'''

json_data=open('config/products.json')

data = json.load(json_data)
print "data: ", data
print "\ndata - product: ", data['products'][0]
#pprint(data)
product_list = data['products']
json_data.close()


def find_product(product_data=[], product_name=None, product_size=None):
    item_found = None
    for item in product_data:
        print "item: ", item
        current_name = item.get('name')
        current_size = item.get('size')
        if current_name == product_name and current_size == product_size:
            item_found = True
            return item
            break

    if not item_found:
        return False

item = find_product(product_list, 'Hawaiian Supreme', "Family")
print "\nitem found: ", item

