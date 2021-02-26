"""
Python script template

"""

import os
import sys
import re
import glob
import csv
import json

class someclass:
    def __init__(self):
        pass
    def _read(self,arg1):
        pass
    def _write(self,arg2):
        pass
    def _process(self,arg3):
        pass


if __name__=='__main__':
    """
    if command line arg is CSV file,read it and process each its row.
    otherwise, process arg
    """
    if sys.argv[1][-4:]=='.csv':
        with open(sys.argv[1],'r') as f0:
            reader=csv.reader()
            datalist=[row for row in reader]

        for row in datalist:
            cs=someclass()
            cs._read(row)
            cs._process("")
            cs._write("")
            del cs                
    else:
        cs=someclass()
        cs._read(sys.argv[1])
        cs._process("")
        cs._write("")
        del cs
