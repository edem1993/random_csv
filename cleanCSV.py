#!/usr/bin/env python
import re
import sys
import os.path

csv = 'test.csv'

def cleanCSV(input):

    if os.path.isfile(csv):
        print('%s is valid\n' % (csv))
    elif os.path.isfile(csv) == False:
        print('%s is invalid\n' % (csv)) 

    with open(csv, 'r') as f:
        f.seek(0)
        header = next(f).split(',')

        g = f.readlines()
        
        for line in g:
            line = line.rstrip('\n')
            
            regex = re.compile(r'^\s*|\s*$|approx\.\s+|\$|\?', re.IGNORECASE)
            line = re.sub(regex, '', line)

            regexx = re.compile(r'\s*,\s*')
            z = re.sub(regexx, ',', line)

            mylist = z.split(',')
            mylist = list(filter(None, mylist))

            if len(z) == 0:
                continue

            if len(mylist) < 3:
                continue


            mydict = {}
            for i in range(len(header)):
                heading = header[i]
                vlue = mylist[i]

                mydict[heading.rstrip('\n')] = vlue
            
            #print(mydict["Payment"])
            #print(mydict.values())
            #print(mydict.keys())
            #print(mydict.items())
            #print(mydict)

            for letter, number in mydict.items():
                print('{0} : {1}'.format(letter, number))

cleanCSV(csv)