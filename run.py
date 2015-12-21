import checking
import util 

url = "https://math.berkeley.edu/~jcalder/"

def main(): 
	urls = util.SList()
	urls.insertFont(url)
	visited = util.SList()
	visited.insertFont(url)

	pdf = checking.gather_pdf(checking.get_link_info(url, urls, visited))
	checking.download_pdf(pdf)

if __name__ == "__main__":
    main()