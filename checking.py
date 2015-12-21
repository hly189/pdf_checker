#############################################################
# 
# Author: Hoa Ly
# Last Update: 12/21/2015
# Description: The core file of pdf checker 
# 
#############################################################
import util
import mechanize 
import urlparse

"""
This function is used to gather all the available links which are
available and not error in the given url. 
"""
def get_link_info(given_url, given_urls, given_visited): 
	br = mechanize.Browser()

	while given_urls.size >0:
		try: 
			br.open(given_urls.head.get_item())
			given_urls.remove(given_urls.head.get_item())
			for link in br.links(): 
				new_url = urlparse.urljoin(link.base_url, link.url)
				b1 = urlparse.urlparse(given_url).hostname 
				b2 = urlparse.urlparse(given_url).path 
				checking_name = "https://" +b1 + b2
				if given_urls.size == 0: 
					given_urls.insertFont(new_url)
				if checking_name in new_url and given_visited.search(new_url) is False: 
						given_visited.insertEnd(new_url)
						given_urls.insertEnd(new_url) 
						print(new_url)
		except: 
			print("error")
			given_urls.remove(given_urls.head.get_item())

	print ("Comleted")
	return given_visited

"""
This is used to gather all the available links which contain .pdf file
"""
def gather_pdf(given_link): 
	given_pdf = util.SList()

	current = given_link.head
	while current: 
		if util.check(current.item) is True: 
			if given_pdf.size == 0: 
				given_pdf.insertFont(current.item)
			else: 
				given_pdf.insertEnd(current.item)
		current = current.get_next()
	return given_pdf

"""
This is used download all the .pdf file to your file 
"""
def download_pdf(link_pdf): 
	current = link_pdf.head 
	while current: 
		file_name = urlparse.urlparse(current.item).path.rsplit("/", 1)[-1]
		util.download(current.item, file_name)
		current = current.get_next()
"""
url = "https://math.berkeley.edu/~murphy/"

urls = util.SList()
urls.insertFont(url)
visited = util.SList()
visited.insertFont(url)
get_link_info(url, urls, visited)
"""
