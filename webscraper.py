from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

browser = webdriver.Chrome(executable_path='/Users/adamkendis/software projects/chromedriver', chrome_options=option)

browser.get("https://www.phptravels.net/demo")

timeout = 30

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='img-responsive']")))

except TimeoutException:
    print("Timed out waiting for page to finish loading")
    browser.quit()

titles_element = browser.find_elements_by_xpath("//p[@class='sc-6z3jy0-3 fGcVuz']")
titles = [x.text for x in titles_element]
print('titles:')
print(titles, '\n')

# language_element = browser.find_elements_by_xpath("//s[@itemprop='programmingLanguage']")
# languages = [x.text for x in language_element]
# print('languages:')
# print(languages, '\n')

# for title, language in zip(titles, languages):
#     print("RepoName : Language")
#     print(title + ": " + language, '\n')
