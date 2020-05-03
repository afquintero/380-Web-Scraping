# -*- coding: utf-8 -*-
"""
This is the source code for a basic Instagram Scraper
"""

import pandas as relevantData
import sys
import time
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException as err

referenceURL = "https://www.instagram.com/"


#This method will scrape 25 most recent posts from an account
def recentPosts(IGHandle, postCount = 25):
	target = referenceURL + IGHandle + "/"
	chromeBrowser = Chrome()
	chromeBrowser.get(target)
	post = 'https://www.instagram.com/p/'                                                       #All post links will start with this format in their URL,
	numOfPosts = chromeBrowser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span')																							#So we will use this to filter for what we want.
	numOfPosts = numOfPosts.text

	try:
		publicOrPrivate1 = chromeBrowser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')
		#publicOrPrivate2 = chromeBrowser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div')

	except err:
		chromeBrowser.stop_client()
		sys.exit("Data cannot be collected from here at this time. The account might be private or have no posts.")

	post_links = []                                                                             #Initializes list to store links of interest.

	#if ():
	while(len(post_links) < postCount and len(post_links) < int(numOfPosts)):
			
		links = [a.get_attribute('href') for a in chromeBrowser.find_elements_by_tag_name('a')] #This line of code collects all the html href attributes
	                                                                                                #from the anchor elements ('a') we collect from a page.	                                                                                                #This is repeated until we have collected 25 links.
		for eachLink in links:
			   if(post in eachLink and eachLink not in post_links):
			   	post_links.append(eachLink)
		scroll_down = "window.scrollTo(0,document.body.scrollHeight);"
		chromeBrowser.execute_script(scroll_down)
		time.sleep(10)

	else:
		chromeBrowser.stop_client()
		return post_links[:postCount]
		chromeBrowser.close()

def getPostDetails(urls):

	xpath_comment = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[1]/div/div/div'
	browser = Chrome()
	post_details = []

	for link in urls:
		browser.get(link)
		try:
			#This will get the generic like count of a post, as long as it isn't a video
			likes = browser.find_elements_by_partial_link_text(' likes')
			print(likes)
			#comment = browser.find_element_by_xpath(xpath_comment).text

		except:
			xpath_view = '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span'
			#likes = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text
			age = browser.find_element_by_css_selector('a time').text			
			comment = browser.find_element_by_xpath(xpath_comment).text
			insta_link = link.replace('https://www.instagram.com/p','')
			post_details.append({'link': insta_link,'likes/views': likes,'age': age, 'comment': comment})
			time.sleep(10)
	return post_details



myLinks = recentPosts("evan.nordin")
for element in myLinks:
	print(element)
postDetails = getPostDetails(myLinks)
print(postDetails)
