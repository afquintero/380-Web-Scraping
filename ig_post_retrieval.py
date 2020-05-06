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
		time.sleep(3)

	else:
		chromeBrowser.stop_client()
		chromeBrowser.close()
	return post_links[:postCount]

def getPostLikes(urls):

	browser = Chrome()
	pic_or_vid = True
	likes = []
	picURLs = []
	views = []
	vidURLs = []

	#Begin iterating over list of urls
	for link in urls:
		browser.get(link)

		#Code inside this try block attempts to grab the element that contains no. of likes from post.
		#If done successfully, pic_or_vid will be set to True so that we can properly categorize the 
		#link once we are done scraping it's data.
		try:
			postlikes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span')
			likes.append(postlikes.text)
			pic_or_vid = True
		#Except block will run in the event that a NoSuchElement exception occurs. That is, if the no. of likes element doesn't exist on a post
		#then the post is a video. After no. of views element is retrieved from post, we set pic_or_vid = False so that we can once again properly
		#categorize the link once we are done scraping.
		except err:
			vidViews = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span/span')
			views.append(vidViews.text)
			pic_or_vid = False
		
		#Assigning links to their respective category of post.
		if(pic_or_vid == True):
			picURLs.append(link)
		else:
			vidURLs.append(link)

		time.sleep(3)

	#Since we have collected everything we need, we can close our browser instance.
	browser.close()
	
	#As long as picURLs isn't empty the code inside this block will print out the collected post details
	if(len(picURLs) != 0):		

		print("----------Like Counts for Posts with Photos----------\n\n")

		for i in range(0, len(picURLs)):
		 	print(picURLs[i] + "----->" + str(likes[i]) + " likes.")

		print("----------End of Like Counts for Posts with Photos--------\n\n")
	#Same as above, but for video
	if(len(vidURLs) != 0):



		print("----------View Counts for Posts with Videos----------\n\n")

		for i in range(0, len(vidURLs)):
			print(vidURLs[i] + "----->" + str(views[i]) + " views.\n")

		print("----------End of View Counts for Posts with Videos----------\n\n")

	#If both lists are empty, then the account must have no posts.
	elif(len(picURLs) == 0 and len(vidURLs) == 0):
		print("\n This account has no posts.")



myLinks = recentPosts("douglasmckinley")
print("Succesfully scraped " + str(len(myLinks)) + " post links from this account:\n " )
for element in myLinks:
	print(element + "\n")
getPostLikes(myLinks)
