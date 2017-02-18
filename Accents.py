from __future__ import print_function
import os
import sys
import fileinput



for line in fileinput.input(str(sys.argv[1]), inplace=True):
    x=line.replace('&#160;','\'a')
    x=x.replace('&#225;','\\\'a')
    x=x.replace('&#228;','\\"a')  
    x=x.replace('&#233;','\'u')  
    x=x.replace('&#263;','\\\'c')
    x=x.replace('&#243;','')
    x=x.replace('&#246;','\\"o') 
    x=x.replace('&#252;','\\"u')   
    x=x.replace('&#252;','\\"u')   
    x=x.replace('&#252;','\\"u')   
    x=x.replace('&#232;','\\`e')   
    x=x.replace('&#223;','\\\'e')    
    x=x.replace('&#246;','\\"o') 
    print (x,end="")



