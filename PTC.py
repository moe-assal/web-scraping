"""
4/21/2020
useless.
"""
from selenium.webdriver import Chrome
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from time import sleep


def back_to_base():
    browser.switch_to.window(browser.window_handles[1])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])


browser = Chrome('./chromedriver')
browser.get('http://wad.ojooo.com/login.php')
browser.find_element_by_id('login_username').send_keys('Moe Assal')
browser.find_element_by_id('pwd').send_keys('Moe@Assal2004')
input()   # pass recaptcha
browser.find_element_by_class_name('biggerinput').click()
sleep(5)
browser.get('http://wad.ojooo.com/ads.php')
ads = browser.find_element_by_class_name('pagination_box').find_elements_by_tag_name('a')
for i in range(ads.__len__()):
    try:
        ads[i].click()
    except (ElementNotInteractableException, ElementClickInterceptedException):
        ads = browser.find_element_by_class_name('pagination_box').find_elements_by_tag_name('a')
        continue
    sleep(15)
    back_to_base()
    sleep(3)
    ads = browser.find_element_by_class_name('pagination_box').find_elements_by_tag_name('a')
