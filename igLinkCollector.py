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
		publicOrPrivate = chromeBrowser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]')

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

def getPostLikes(urls):

	browser = Chrome()
	likes = []
	views = []

	for link in urls:
		browser.get(link)
		try:
			postlikes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span')
			likes.append(postlikes.text)
		except err:
			vidViews = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span/span')
			views.append(vidViews)
		
		time.sleep(5)
			
	# for i in range(0, len(urls)):
	# 	print(urls[i] + "----->" + str(likes[i]) + " likes.")
	browser.close()

myLinks = recentPosts("douglasmckinley")
print("Succesfully scraped " + str(len(myLinks)) + " post links from this account:\n " )
for element in myLinks:
	print(element + "\n")
getPostLikes(myLinks)
