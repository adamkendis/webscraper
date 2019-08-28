from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("ignore-ssl-errors")
dir_path = os.getcwd() + '/chromedriver'

browser = webdriver.Chrome(executable_path=dir_path, chrome_options=options)

browser.get("https://www.osprey.com/us/en/category/backpacks/")

timeout = 20

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='thumb-img pdp-link']")))
    more_button = browser.find_element_by_xpath("//span[@class='btn btn-lg btn-action']")

    for i in range(0,5):
        more_button.click()
        time.sleep(5)

    link_elements = browser.find_elements_by_xpath("//a[@class='thumb-img pdp-link']")
    links = [ele.get_attribute('href') for ele in link_elements]
    print(links)
    browser.quit()

except TimeoutException:
    print("Timed out waiting for page to finish loading")
    browser.quit()

# titles_element = browser.find_elements_by_xpath("//tr[@class='sizedisplay-us us-sizing']")
# titles_name = browser.find_element_by_class_name('pdp-desktop-title')
# titles = [x.text for x in titles_element]
# print(titles_name.text)
# print('titles:')
# print(titles, '\n')
# browser.quit()



# language_element = browser.find_elements_by_xpath("//s[@itemprop='programmingLanguage']")
# languages = [x.text for x in language_element]
# print('languages:')
# print(languages, '\n')

# for title, language in zip(titles, languages):
#     print("RepoName : Language")
#     print(title + ": " + language, '\n')
