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
items = []

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

    with open('backpack_links.csv', 'w') as data:
        writer = csv.writer(data)
        writer.writerows(links)
    
    print(links)
    time.sleep(4)

    for link in links:
        browser.get(link)
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//tr[@class='sizedisplay-us us-sizing']")))
        name = browser.find_element_by_class_name('pdp-desktop-title').text.encode('ascii', 'ignore').decode('utf-8')
        size_info = browser.find_elements_by_xpath("//tr[@class='sizedisplay-us us-sizing']")
        size_text = [_.text for _ in size_info]
        sizes = [u'-'.join([
            x.split(' ')[0], 
            x.split(' ')[len(x.split(' '))-2]
            ]).encode('utf-8').strip() for x in size_text]
        final_sizes = '_'.join(sizes)
        items.append([name, final_sizes])
        time.sleep(5)

    browser.quit()


except TimeoutException:
    print("Timed out")
    browser.quit()

with open('backpacks.csv', 'w') as data:
    writer = csv.writer(data)
    writer.writerow(['Name', 'Sizes'])
    writer.writerows(items)

browser.quit()
