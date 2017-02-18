#!/usr/bin/python

import xml.sax
import sys
reload(sys)    # to re-enable sys.setdefaultencoding()
#sys.setdefaultencoding('utf8')

skip = 0

CONFABBRV = {'ISCA': 37, 'HPCA': 16, 'MICRO': 43, 'PACT': 19, 'ASPLOS': 15}

def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))


def conftitle(conf, year):
      return "Proc. of the "+ ord(int(year)-2010+CONFABBRV[conf]) + " " +conf
 

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      global skip
      self.CurrentData = tag
      if tag == "inproceedings":
         print "\n\n"
         skip = 0
      if tag == "proceedings":
         skip = 1
    
   # Call when an elements ends
   def endElement(self, tag):
      global skip
      if skip: 
         return
      if tag == "inproceedings":
         print "%R"
      if self.CurrentData == "author":
         print "%A", self.type.strip()
      elif self.CurrentData == "title":
         print "%T", self.format.strip()
      elif self.CurrentData == "year":
         print "%D", self.year.strip()
      elif self.CurrentData == "pages":
         print "%P", self.rating.strip()
      elif self.CurrentData == "booktitle":
         if (self.year != ''):
           print "%J", conftitle(self.stars.strip(),self.year.strip())
      elif self.CurrentData == "description":
         print "Description:", self.description
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "author":
        self.type = content
      elif self.CurrentData == "title":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "pages":
         self.rating = content
      elif self.CurrentData == "booktitle":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content


if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   
   parser.parse(str(sys.argv[1]))
#   xml.sax.parseString(text,Handler)
