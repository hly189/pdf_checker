#############################################################
# 
# Author: Hoa Ly
# Last Update: 12/22/2015
# Description: adding if no option is choses, it will print help  
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
                  		help = "download a single file",
                  			)

	parser.add_option('-a', '--all',
					  action="store_true",
	                  dest="download_all",
	                  default=False,
	                  help = "download all the file ",
	                  )

	parser.add_option('-i', '--invalid',
					  action="store_true",
	                  dest="invalid_link",
	                  default=False,
	                  help = "show all the file which cannot be downloaded",
	                  )

	parser.add_option('--show',
					  action="store_true",
	                  dest="show_pdf",
	                  default=False,
	                  help = "show all the .pdf links in provided link",
	                  )                  

	parser.add_option('--version',
	                  dest="version",
	                  default="1.0.1",
	                  type="string",
	                  help = "the most current version",
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


	if len(args) <= 0:  
		parser.print_help()
		print("Please enter which options do you want to choose")

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