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
		publicOrPrivate = chromeBrowser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div/div[1]/a/div/div[2]')

	except err:
		chromeBrowser.stop_client()
		sys.exit("Sorry, this account is private so we can't scrape it.")

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

		
	#else:
	#	print("Sorry! This account is private, so we can't scrape it. :/")
	#	return -1

myLinks = recentPosts("douglasmckinley")
for element in myLinks:
	print(element)
