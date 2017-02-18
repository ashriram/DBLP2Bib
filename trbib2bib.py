#bib-napper tool, written by jason mars

import os;
import sys;
import re;
import urllib2;
from urllib import FancyURLopener;

# os.system("cat *.html >> ids.clump;");

final=[];

    

def bibdecoder(filepath,conference):
  title = ""
  authors = ""
  journal = ""
  date  = ""
  pages = ""
  keyflag = 0
  count = 0
  key = ""
  keys = {""}
  try:
          fd = open(filepath, 'r')
          filecontents_source = fd.readlines()
          fd.close()
  except:
          print 'Could not open file:', filepath
  do_print=0;
  for j in filecontents_source:  
    if len(j)<2: continue;
    if j[1]=="T":
      title = "title = {" + j[2:-1].lstrip() + "}"

    if j[1]=="J":  
       journal = "booktitle = {" + j[2:-1].lstrip() + "}"

    if j[1]=="A":
      if keyflag == 0:
        authors = "author = {" + j[2:-1].lstrip()
        list = j.split()
        list.reverse()
        key = key + list[0] 
        keyflag = 1
      else:
        authors = authors + " and " + j[2:-1].lstrip()
          
    # Termination character.
    if j[1]=="R":
     do_print = 1

    if j[1]=="P":
      pages = "pages = {" + j[3:-1] + "}";
 
    if j[1]=="D":
     date = "year = {" + j[3:-1] + "}";
     key = key + "-" + conference + "-" +  j[2:-1].strip()
     key = re.sub('[^A-Za-z0-9\-]+', '', key)
     alpha=97
     # eliminate duplicate keys. This will keep adding characters until a unique key is found.
     # Hopefully we won't have more than 26 papers from the same first author at the same conference.
     # Otherwise we will start adding non-alpha suffixes. Who knows what's going to happen then.
     duplicatekey = key
     while (duplicatekey in keys):
       duplicatekey = key + "-"+ chr(alpha)
       alpha=alpha+1
     key = duplicatekey  
     keys.add(key) 
 

    if do_print: 
      sys.stdout.write("\n\n@inproceedings{")
      sys.stdout.write(key.lower()+",\n")
      sys.stdout.write(title+",\n")
      sys.stdout.write(authors+"},\n")
      sys.stdout.write(journal+",\n")
      sys.stdout.write(date + ",\n")
      sys.stdout.write(pages + "\n}")
      do_print = 0
      key = ""
      keyflag = 0
      title = ""
      authors = ""
      journal = ""
      date = ""
      count=count+1
  print count


def main():
    filepath = sys.argv[1];
    if sys.argv[1:]:
        filepath = sys.argv[1];
        conference = sys.argv[2];
        bibdecoder(filepath,conference)
    else:
        print "No input file"
        sys.exit()

if __name__ == "__main__": main()

