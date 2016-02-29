PDF CHECKER:
===================

This tool will search all the links which contain the .pdf files in the provided url and download all or a selected file for you. 

## REQUIREMENT: 
Please set up mechanize in order to run this tool. If you did not set it up yet, please run: 

`pip install mechanize `

or download the mechanize [distribution](http://wwwsearch.sourceforge.net/mechanize/src/), 

then run `python setup.py install`

Usage: 

 - run command: python run.py [options]

VERSION 1.0: 
  the default mode is to download all the .pdf files which are found. 
  
VERSION 1.0.1: 

  Update options for run.py: (24/12/2015)
  
    "-v": Shows the current version of pdf_checker.
    
    "-a": allows you to download all the .pdf files which contain in the provided link.
    
    "-s": allows you to download selected .pdf file. It will ask to see which .pdf file that you want to.
    
    "-i": shows all the links which cannot be downloaded.
    
    "-z": shows all the .pdf files in provided link.
    
UPDATE 1:  
  - check to see if the link has 403 and 404 error to download it. 
  
UPDATE 2: 
  - some minor changes for download functions. 
  - updaing "-i" option which shows the links that cannot be downloaded. 

UPDATE 3: 
   - Adding input for url and fixing some bugs. 

P/S: I am in the process of fixing the bugs and updating the program. Therefore, it is probably not perfect. 


