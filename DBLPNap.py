#!python3
from bs4 import BeautifulSoup
import re
import urllib.request
import sys

ecj_data = open(str(sys.argv[1]), 'r').read()


soup = BeautifulSoup(ecj_data, "html.parser")
#  markup_type=markup_type))
#soup = BeautifulSoup(ecj_data)

# Header for XML file
print("<?xml version=\"1.0\"?>")
print("<dblp>")

# Processing links from conference html
# for link in soup.findAll('a', attrs={'href': re.compile("^https://dblp.dagstuhl.de/rec/xml/conf/.*xml")}):
for link in soup.findAll('a', attrs={'href': re.compile("^https://dblp.uni-trier.de/rec/conf/" + sys.argv[2] + "/.*xml")}):

    link = link.get('href')
    f = urllib.request.urlopen(link)
    xmltext = f.read().decode('utf-8')
    xmltext = xmltext.replace(
        "<?xml version=\"1.0\" encoding=\"US-ASCII\"?>", "")
    xmltext = xmltext.replace("<dblp>", "")
    xmltext = xmltext.replace("</dblp>", "")
    print(xmltext)
    print("\n\n")

# Print Footer for XML file
print("</dblp>")
