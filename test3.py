import mechanize 
import urlparse
import util 


url = "https://math.berkeley.edu/~jcalder"

urls = util.SList()
urls.insertFont(url)
visited = util.SList()
visited.insertFont(url)

link_pdf  = util.SList()

br = mechanize.Browser()

while urls.size >0:
	try: 
		br.open(urls.head.get_item())
		urls.remove(urls.head.get_item())
		for link in br.links(): 
			new_url = urlparse.urljoin(link.base_url, link.url)
			if urls.size == 0: urls.insertFont(new_url)
			if urlparse.urlparse(url).hostname in new_url and visited.search(new_url) is False: 
				visited.insertEnd(new_url)
				urls.insertEnd(new_url)
				#print new_url
	except: 
		urls.remove(urls.item)
print("Completed")


current = visited.head 
while current: 
	if util.check(current.item) is True: 
		if link_pdf.size == 0: 
			link_pdf.insertFont(current.item)
		else: 
			link_pdf.insertEnd(current.item)
	current = current.get_next()

"""
i = 0
while i < len(visited):  
    if util.check(visited[i]) is True: 
    	link_pdf.append(visited[i])
    i = i +1
link_pdf.pop(0)
"""


"""
def main():
    util.download_file(link_pdf[0])

if __name__ == "__main__":
    main()
"""