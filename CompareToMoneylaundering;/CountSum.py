import sys
import re
import os


def SumCount(filein,fileout):
        SumDict = {}
        CountDict = {}
        r = re.compile('\s')
        aPairSet = set()
        with open(filein,'r') as FILEIN:
##                n=0
                for line in FILEIN:
##                        print n
##                        n = n+1
                        ItemList = r.split(line)  #in, out, money, location, date
                        aIn = ItemList[0]
                        aOut = ItemList[1]
                        aPair = (aIn,aOut)
                        money = ItemList[2]
                        
                        if aPair not in SumDict.keys():
                                SumDict[aPair] = int(money)
                        else:
                                SumDict[aPair] = SumDict[aPair] + int(money)
                        

                        if aPair not in CountDict.keys():
                                CountDict[aPair] = 1
                        else:
                                CountDict[aPair] = CountDict[aPair] + 1

                        aPairSet.add(aPair)
                         
        print "Create Dict Done."
                        
        with open(fileout,'w') as FILEOUT:
                for ap in aPairSet:
                        print >>FILEOUT, ap[0], " ", ap[1], " ", SumDict[ap], " ", CountDict[ap]       
        print "Print File Done."        
        
if __name__ == '__main__':
        SumCount('MappedInOut.txt','TransEdge.txt')

        

 
        
