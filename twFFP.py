from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

twAccount = input('Which Twitter Account? ')
target = "https://www.twitter.com/"

browser = Chrome()

browser.get(target + twAccount)
followers = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
following = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span')
joined = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[4]/div/span[2]')
name = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span')

print(name.text)
print("@" + twAccount)
print(followers.text + " followers")
print("following " + following.text)
print("joined " + joined.text)