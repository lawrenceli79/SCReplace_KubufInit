import os
import sys
import re

if(len(sys.argv)<=1):
    print ("Usage:")
    print ("    py {} <InFile> ".format(os.path.basename(__file__)))
    sys.exit()

strFileIn = sys.argv[1]

varList = [
    'kubuf', \
    'tempkubuf', \
    'kubuftemp', \
    'kubufN', \
    'kubufS', \
    'kubufI', \
    'delkubuf', \
    'prekubuf', \
    'tkubuf', \
]

sizeofList = [
    'KUBUF', \
    'XKUBUF', \
]

with open(strFileIn) as fin:
    for line in fin:
        lineOut = line
        bFound = False
        m = re.search(r"(DRS)*memset\((&?)(\w+),\s*0,\s*sizeof\((\w+)\)\);", line)
        if(m):
            strRef = m.group(2)
            strVar = m.group(3)
            strSizeof = m.group(4)
            if(strVar in varList and (strSizeof==strVar or strSizeof in sizeofList)):
                nStart = m.start()
                nEnd = m.end()
                strBefore = line[:nStart]
                strAfter = line[nEnd:]
                strReplace = "KubufInit({0}{1},sizeof({2}));".format(strRef, strVar, strSizeof)
                lineOut = strBefore + strReplace + strAfter
        print(lineOut, end='')


