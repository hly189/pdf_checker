#############################################################
# 
# Author: Hoa Ly
# Last Update: 12/22/2015
# Update: adding "-i" option which show that can't be downloaded 
# 
#############################################################
import checking
import util 
import optparse, sys 

url = "http://persson.berkeley.edu/"

def get_options():
	parser = optparse.OptionParser()
	parser.add_option('-s', '--single', 
						action="store_true",
                  		dest="download_single", 
                  		default=False,
                  			)
	parser.add_option('-a', '--all',
					  action="store_true",
	                  dest="download_all",
	                  default=False
	                  )
	parser.add_option('--show',
					  action="store_true",
	                  dest="show_pdf",
	                  default=False
	                  )
	parser.add_option('-i', '--invalid',
					  action="store_true",
	                  dest="invalid_link",
	                  default=False
	                  )
	parser.add_option('--version',
	                  dest="version",
	                  default="1.0.1",
	                  type="string",
	                  ) 
	parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  )
	return parser


def main():

	parser = get_options()
	options, args = parser.parse_args()

	urls = util.SList()
	urls.insertFont(url)
	visited = util.SList()
	visited.insertFont(url)


	if options.verbose: 
		print 'VERSION   :', options.version
	else: 
		pdf = checking.gather_pdf(checking.get_link_info(url, urls, visited))
		
		if options.invalid_link: 
			a = checking.invalid(pdf)
			a.show()
		if options.show_pdf: 
			pdf.show_pdf()

		if options.download_all: 
			checking.download_pdf_all(pdf)

		if options.download_single: 
			i = 0
			while i >= 0: 
				answer = raw_input("Do you want to show the name of files: (y/n): ")
				if answer == "y": 
					pdf.show_pdf()
					checking.download_pdf(pdf)
					break
				elif answer == "n": 
					checking.download_pdf(pdf)
					break
				else:
					i = i + 1
				print "Please Enter (y/n)" 


if __name__ == "__main__":
    main()