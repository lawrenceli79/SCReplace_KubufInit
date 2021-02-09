import os
import sys
import re

if(len(sys.argv)<=1):
    print ("Usage:")
    print ("    py {} <InFile> ".format(os.path.basename(__file__)))
    sys.exit()

strFileIn = sys.argv[1]

varList = [ \
    'kubuf', \
    'tmpkubuf', \
    'tempkubuf', \
    'kubuftemp', \
    'kubufN', \
    'kubufS', \
    'kubufI', \
    'delkubuf', \
    'prekubuf', \
    'tkubuf', \
    'kubufflag', \
    'preKubuf', \
    'e_kubuf', \
    'PrevKubuf', \
]

sizeofList = [ \
    'KUBUF', \
    'XKUBUF', \
]

with open(strFileIn) as fin:
    for line in fin:
        lineOut = line
        bFound = False
        m = re.search(r"(DRSmemset|memset|lmemset)\(\s*(&?)([^,]+),\s*0,\s*sizeof\((\w+)\)(\*\w+)?\s*\);", line)
        if(m):
            strRef = m.group(2)
            strVar = m.group(3)
            
            mVar = re.match(r"(\w+)", strVar)
            bFullVar = mVar!=None

            mKubuf = re.search(r"kubuf", strVar, re.IGNORECASE)
            mDont = re.search(r"dcont", strVar, re.IGNORECASE)
            strSizeof = m.group(4)
            strSizeofMultiplier = m.group(5)
            #if(strVar in varList and (strSizeof==strVar or strSizeof in sizeofList)):
            #if(mKubuf and not mDont and ((strSizeof==strVar and bFullVar) or strSizeof in sizeofList)):
            bMatch = False
            if(strSizeof in sizeofList):
                bMatch = True
            if(mKubuf and not mDont and strSizeof==strVar and bFullVar ):
                bMatch = True
            if(bMatch):
                strBefore = line[:m.start()]
                strAfter = line[m.end():]

                strstrSizeofMultiplier2 = ""
                if(strSizeofMultiplier!=None):
                    strstrSizeofMultiplier2 = strSizeofMultiplier
                    strRef = ""
                
                strReplace = "KubufInit({0}{1},sizeof({2}){3});".format(strRef, strVar, strSizeof, strstrSizeofMultiplier2)
                lineOut = strBefore + strReplace + strAfter
                    

        print(lineOut, end='')


