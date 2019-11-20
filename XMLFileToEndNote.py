#!/usr/bin/python

import xml.sax
import sys
import io
reload(sys)    # to re-enable sys.setdefaultencoding()
# sys.setdefaultencoding('utf8')

skip = 0

CONFABBRV = {'ISCA': 37, 'HPCA': 16, 'MICRO': 43, 'PACT': 19, 'ASPLOS': 15}

output = ""


def ord(n):
    return str(n)+("th" if 4 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))


def conftitle(conf, year):
    return "Proc. of the " + ord(int(year)-2010+CONFABBRV[conf]) + " " + conf


class MovieHandler(xml.sax.ContentHandler):
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
        global output
        self.CurrentData = tag
        if tag == "inproceedings":
            output = output + "\n\n"
            skip = 0
        if tag == "proceedings":
            skip = 1

    # Call when an elements ends
    def endElement(self, tag):
        global skip
        global output
        if skip:
            return
        if tag == "inproceedings":
            output = output + "%R " + "\n"
        if self.CurrentData == "author":
            output = output + "%A " + self.type.strip() + "\n"
        elif self.CurrentData == "title":
            output = output + "%T " + self.format.strip() + "\n"
        elif self.CurrentData == "year":
            output = output + "%D " + self.year.strip() + "\n"
        elif self.CurrentData == "pages":
            output = output + "%P " + self.rating.strip() + "\n"
        elif self.CurrentData == "booktitle":
            if (self.year != ''):
                output = output + \
                    "%J " + conftitle(self.stars.strip(),
                                      self.year.strip()) + "\n"
        elif self.CurrentData == "description":
            output = output + "Description:" + self.description + "\n"
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


if (__name__ == "__main__"):

    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse(str(sys.argv[1]))
#   xml.sax.parseString(text,Handler)
    with io.open(str(sys.argv[2]), "w") as text_file:
        text_file.write(output)
