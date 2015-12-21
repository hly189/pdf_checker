
import urllib2


"""
This is used to check if the link contains pdf file or not 
"""
def check(url): 
	if ".pdf" in url: 
		return True 
	return False 


"""
This is used to download .pdf file contains in the link and asking to see
if you want to download it or not 
"""
def download_file(download_url):
	i = 1
	while i>0: 
   		answer = raw_input("Do you want to download the file (y/n): ")
   		if answer == 'n': 
   			break  
   		elif answer == 'y': 
   			response = urllib2.urlopen(download_url)
   			a = raw_input("Enter name of your file: ")
   			file = open(a + '.pdf', 'w')
   			file.write(response.read())
   			file.close()
   			print("Download File Completed")
   			break 
   		else: i = i+1 

"""
This function is used to download file
"""
def download(download_url, name): 
	response = urllib2.urlopen(download_url)
   	file = open(name, 'w')
   	file.write(response.read())
   	file.close()
   	print("Download File Completed") 

"""
Below is the implementation of Singly Linked List 
"""
# Node of the Linked List 
class SListNode(object):
	"""Node for Singly Linked List """
	def __init__(self, item, next = None):
		self.item = item 
		self.next = next

	def get_next(self): 
		return self.next

	def set_next_equal(self, n): 
		self.next = n
		return self.next 

	def get_item(self): 
		return self.item 

	def set_item_equal(self, d): 
		self.item = d
		return self.item 

# Implementation of Linked List 
class SList(object):
	"""Singly Linked List """
	def __init__(self, head = None):
		self.head = head
		self.size = 0

	def get_length(self): 
		return self.size

	def show(self): 
		current = self.head

		while current is not None: 
			print(current.item)
			current = current.get_next()
	
	def insertFont(self, d): 
		new_head = SListNode(d, self.head)
		self.head = new_head
		self.size += 1

	def insertEnd(self,d): 
		if self.head is None: 
			new_node = SListNode(d,None)
		else: 
			new_node = self.head 
			while new_node.next is not None: 
				new_node = new_node.get_next()
			new_node.next = SListNode(d,None)
			self.size += 1

	def search(self, key): 
		current = self.head
		while current is not None: 
			if key == current.get_item(): 
				return True
			current = current.get_next()
		return False 

	def remove(self, key): 
		current = self.head
		previous = None

		while current is not None: 
			if current.get_item() == key: 
				if previous is not None: 
					previous.set_next_equal(current.get_next())
				else: 
					self.head = current.get_next()
			previous = current
			current = current.get_next()
		self.size = self.size -1 
