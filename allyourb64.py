#!/usr/bin/python
#Jeremy Galloway 2014
#This script converts a text file *Line By Line* into b64 encoded strings
#This is often useful for attacking BASIC www auth
#Simply pass in the source file are the first arguement and redirect STDOUT

import sys
import base64

import sys
import base64


for filename in sys.argv[1:]:
    with open(filename, 'r') as f:
        for line in f:
            print base64.b64encode(line.strip())
