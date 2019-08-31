from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import csv

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("ignore-ssl-errors")
dir_path = os.getcwd() + '/chromedriver'

browser = webdriver.Chrome(executable_path=dir_path, chrome_options=options)

browser.get("https://www.osprey.com/us/en/category/technical-packs/backpacking/")

timeout = 30

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='thumb-img pdp-link']")))

    while True:
        more_button = browser.find_elements_by_xpath("//span[@class='btn btn-lg btn-action']")
        if len(more_button) > 0:
            more_button[0].click()
            time.sleep(5)
            continue
        else:   
            break

    link_elements = browser.find_elements_by_xpath("//a[@class='thumb-img pdp-link']")
    links = [ele.get_attribute('href') for ele in link_elements]
    print(links)
    time.sleep(4)

    items = []
    for i in range(len(links)):
        browser.get(links[i])
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='js-radio-bkg-img']")))
        name = browser.find_element_by_class_name('pdp-desktop-title').text
        size_info = browser.find_elements_by_xpath("//tr[@class='sizedisplay-us us-sizing']")
        size_text = [_.text for _ in size_info]
        sizes = ['-'.join([x.split(' ')[0], x.split(' ')[len(x.split(' '))-2]]) for x in size_text]
        final_sizes = '_'.join(sizes)

        items.append([name, final_sizes])
        time.sleep(5)

    browser.quit()

    with open('backpacks.csv', 'w') as data:
        writer = csv.writer(data)
        writer.writerow(['Name', 'Sizes'])
        writer.writerows(items)

except TimeoutException:
    print("Timed out")
    browser.quit()

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
