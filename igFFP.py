from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException

igAccount = input('Which Instagram Account? ')
target = "https://www.instagram.com/"

browser = Chrome()

browser.get(target + igAccount)
try:
    unavailable = browser.find_element_by_xpath('/html/body/div/div[1]/div/div/h2')
except NoSuchElementException:
    followers = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    posts = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span')
    following = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
    print(igAccount)
    print(followers.text + " followers")
    print(posts.text + " posts")    
    print("Following " + following.text)
    browser.get("https://www.instagram.com/p/B_nPSlABiFl/")
    postlikes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span')
    print(postlikes.text + " likes")
else:
    print(unavailable.text)
    browser.close()

