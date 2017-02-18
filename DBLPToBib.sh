#!/bin/bash

HTML_FOLDER=./BibHTML
PYTHON=python
NAPPER=DBLPNap.py
ENDNOTE=XMLFileToEndNote.py
SPECIAL=Accents.py
BIB=trbib2bib.py

YEAR=$1


for CONFERENCE in isca
do
	echo "Processing "$CONFERENCE"-"$YEAR
    FILENAME=$HTML_FOLDER/$CONFERENCE$YEAR.html
    cat $FILENAME > master.html
    echo "Napping"
    `$PYTHON $NAPPER master.html > master.xml`
    echo "Replacing Special chars"
    `$PYTHON $SPECIAL master.xml`
    perl -p -i -e 's/<\?xml version="1.0" encoding="US-ASCII"\?>//g' master.xml
    echo "XML->ENDNOTE"
    `$PYTHON $ENDNOTE master.xml > master.endnote`
    echo "ENDNOTE->BIB" 
    `$PYTHON $BIB master.endnote $CONFERENCE > master.bib`
#    `rm master.html`
#    `rm master.xml`
#    `rm master.endnote`
done


#`$GrabEndNote`
