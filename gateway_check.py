#!/usr/bin/env python

import subprocess
import os.path
import sys

ips = "C:\\Users\\A69077588.EMEA2\\Desktop\\ping_subnets.txt"

def subnet_check(list):
    try:
        if os.path.isfile(list):
            #print("File is valid")
            pass
        elif os.path.isfile(list):
            print("Invalid filepath .|.")
            sys.exit()

        with open(ips, 'r') as f:
            f.seek(0)
            sor = f.readlines()

            for ip in sor:
                ip = ip.rstrip("\n")

                octet = ip.split('.')
                oc = octet[-1]
                three_oc = octet[0:3]
                o = int(oc) + 1
                new_ip = ".".join(three_oc) + "." + str(o)
                
                cmd = os.system('ping %s -n 2' % (new_ip))
                #return cmd

    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()


subnet_check(ips)
