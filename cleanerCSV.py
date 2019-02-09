#!/usr/bin/env python
import re
import sys
import os.path

csv = 'test.csv'

def cleanCSV(input):

    # check whether file is found
    if os.path.isfile(csv):
        print('%s is valid\n' % (csv))
    elif os.path.isfile(csv) == False:
        print('%s is invalid\n' % (csv)) 
    
    # open file
    with open(csv, 'r') as f:
        f.seek(0)
        # not used for this code
        header = next(f).split(',')

        # read file line by line
        g = f.readlines()
        
        for line in g:
            # to take off new line character
            line = line.rstrip('\n')
            
            # match anything thats not needed in a CSV
            regex = re.compile(r'^\s*|\s*$|approx\.\s+|\$|\?', re.IGNORECASE)
            line = re.sub(regex, '', line)

            regexx = re.compile(r'\s*,\s*')
            z = re.sub(regexx, ',', line)

            # make list for checkin values
            mylist = z.split(',')
            # if value < 3 --> skip line
            mylist = list(filter(None, mylist))

            # if the length of the line is '0' --> skip line
            if len(z) == 0:
                continue

            # if value < 3 (less than 3 column) --> skip line
            if len(mylist) < 3:
                continue

            # cool, but not needed for now.
            mydict = {}
            for i in range(len(header)):
                heading = header[i]
                vlue = mylist[i]

                mydict[heading.rstrip('\n')] = vlue
            
            # replace ',' with ';' in the cleaned CSV
            print(z.replace(',', ';'))

cleanCSV(csv)