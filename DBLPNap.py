from bs4 import BeautifulSoup
import re
import urllib2
import sys

ecj_data = open(str(sys.argv[1]),'r').read()


soup = BeautifulSoup(ecj_data)

# Header for XML file
print "<?xml version=\"1.0\"?>"
print "<dblp>"

# Processing links from conference html
for link in soup.findAll('a', attrs={'href': re.compile("^http://dblp.uni-trier.de/rec/xml/conf/.*xml")}):
    link = link.get('href')
    f = urllib2.urlopen(link)
    xmltext = f.read()
    xmltext = xmltext.replace("<?xml version=\"1.0\"?>","")
    xmltext = xmltext.replace("<dblp>","")
    xmltext = xmltext.replace("</dblp>","")
    print xmltext
    print "\n\n"

# Print Footer for XML file
print "</dblp>"