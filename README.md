# DBLP2Bib
Capture DBLP entries and convert to Bib File
```
./DBLPToBib.sh [Year]
```
## Shell file Dependencies
```
HTML_FOLDER=./BibHTML
PYTHON=python
NAPPER=DBLPNap.py
ENDNOTE=XMLFileToEndNote.py
SPECIAL=Accents.py
BIB=trbib2bib.py
```

## BibHTML
```
wget "http://dblp2.uni-trier.de/db/conf/isca/isca2016"
```

## Bibentry example.

@inproceedings{albericio-isca-2016,
title = {Cnvlutin: Ineffectual-Neuron-Free Deep Neural Network Computing.},
author = {Jorge Albericio and Patrick Judd and Tayler H. Hetherington and Tor M\
. Aamodt and Natalie D. Enright Jerger and Andreas Moshovos},
booktitle = {Proc. of the 43rd ISCA},
year = {2016},
pages = {1-13}
}