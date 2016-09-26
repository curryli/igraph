import sys
import re
import os

def main():

    CardEncodeSet = set()
    with open("CardsEncode.csv","r") as FILEIN:
        for line in FILEIN:
            CardEncodeSet.add(line.strip())

    AllCardDicts = {}
    r = re.compile('\s+')
    with open("AllCardDicts.txt","r") as FILEIN:
        for line in FILEIN:
            ItemList = r.split(line)
            AllCardDicts[ItemList[1]] = ItemList[0]
        
    with open("Kcards.txt","r") as FILEIN:
        with open("KcardsOut.txt","w") as FILEOUT:
            for line in FILEIN:
                    if AllCardDicts[line.strip()] in CardEncodeSet:
                        print>>FILEOUT, line.strip()
    
if __name__ == "__main__":
    main()
