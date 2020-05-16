from selenium.webdriver import Chrome
from time import sleep


email = "mohammad.elassal04@gmail.com"
password = "Moe@Assal2004"
hash_tag = "aaronShwarts"
delay = 6


browser = Chrome('./chromedriver')
browser.maximize_window()
sleep(15)
browser.get('https://www.twitter.com/login')
sleep(delay * 2)
browser.find_element_by_name("session[username_or_email]").send_keys(email)
browser.find_element_by_name("session[password]").send_keys(password)
browser.find_element_by_name("session[password]").submit()
sleep(delay / 2)
# disable javascript manually
browser.get('https://twitter.com/search?q=%23' + hash_tag + '&src=typeahead_click')
sleep(delay / 2)
browser.find_element_by_tag_name('button').click()  # enter legacy mode


def like_tweets(number_of_tweets):
    pages_needed = int(number_of_tweets / 20)
    next_page = browser.find_element_by_class_name('w-button-more').find_element_by_tag_name('a').click
    for _ in range(pages_needed):
        loves = browser.find_elements_by_class_name('favorite')
        for i in range(loves.__len__()):
            loves = browser.find_elements_by_class_name('favorite')
            try:
                if loves[i].find_element_by_tag_name('span').get_attribute('title') == 'Like':
                    loves[i].click()
                    sleep(1)
                    loves = browser.find_elements_by_class_name('favorite')
            except IndexError:
                break
        next_page()
