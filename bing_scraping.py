from selenium.webdriver import Chrome
from time import sleep
from requests import get


def extract_images(save=False, start_save=0):

    sleep(delay * 2)
    scroll_down = "window.scrollTo(0,document.body.scrollHeight);"
    for _ in range(10):
        browser.execute_script(scroll_down)
        sleep(delay * 3)

    _images_ = browser.find_elements_by_class_name('mimg')

    if not save:
        return _images_

    for i, image in enumerate(_images_):
        errors = 0
        try:
            resp = get(image.get_attribute('src'))
        except Exception:
            errors += 1
            print(repr(Exception))
            continue
        extension = resp.headers['content-type'].split("/")[1]
        if extension == 'jpeg':
            with open("images/" + str(i - errors + start_save) + ".jpg", "wb") as file:
                file.write(resp.content)
        else:
            errors += 1

    return _images_


def extract_suggestions(base_search):
    suggestions = browser.find_elements_by_class_name('suggestion-title')
    for index, ELEMENT in enumerate(suggestions):
        suggestions[index] = base_search + \
                             ELEMENT.find_element_by_tag_name('strong').get_attribute('innerHTML').split('<br>')[0]
    return suggestions


def search_image(text):
    browser.get('https://www.bing.com')
    sleep(delay)
    search = browser.find_element_by_class_name('sb_form_q')
    search.send_keys(text)
    search.submit()
    sleep(delay)
    browser.find_element_by_id('b-scopeListItem-images').click()
    sleep(delay)
    return


def get_data(search_text, number_of_images):
    start_saving = 0
    needed_pages = int(200 / number_of_images)
    search_image(search_text)
    suggestions = extract_suggestions(search_text)
    start_saving = extract_images(True, start_saving).__len__()

    for i in range(needed_pages):
        if start_saving >= number_of_images:
            search_image(suggestions[i])
            start_saving = extract_images(True).__len__() + start_saving


delay = 4
browser = Chrome('./chromedriver')
browser.maximize_window()
get_data("cats", 200)
