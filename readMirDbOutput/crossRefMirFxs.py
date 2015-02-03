#Sameer Aryal
#Klann Laboratory
#CNS, NYU

#I want to cross reference mmu-miR-125a targets with the results
#from the FMRP proteomics study.

import pandas as pd
import ipdb
import glob

def loadProtStudy(fPath):
    
    # Opens the supplied file [a csv column of gene names]                                              # and returns the gene names as an iterable list                                                
    with open(fPath, 'r') as f:
        geneList = f.read().split()

    if geneList[0].startswith("'") and geneList[0].endswith("'"):
        for idx, item in enumerate(geneList):
            geneList[idx] = item[1:-1]
            
    newGeneList = []
    for item in geneList:
        spList = item.split(';')
        for innerItem in spList:
            newGeneList.append(innerItem)
    
    return newGeneList

def loadMirTargets(fPath):

     return pd.read_csv(fPath, sep='\t')

def compareTwo(protList, mirTab):

    mirList = mirTab.ix[:,0].tolist()
    return set(mirList) & set(protList)
    
#def extractMirInfo():

if __name__ == "__main__":
    allProtFiles = glob.glob("../geneLists/*.txt")
    allMirFiles = glob.glob("../mirDbOutput/*")

    num = 0
    ipdb.set_trace()
    while num < len(allMirFiles):
        mirFile = allMirFiles[num]
        fPath = "../crossRefOutput/%s.txt" % (mirFile[mirFile.find("-")+5:mirFile.find("_")])
        with open (fPath, 'w') as f:
            for item in allProtFiles:
                protTab = loadProtStudy(item)
                for innerItem in allMirFiles:
                    mirTab = loadMirTargets(innerItem)
                    intSect = compareTwo(protTab, mirTab)
                    primStr = item.split('/')[2][0:-4]
                    secStr = innerItem.split('/')[2]
                    id1 = secStr.rfind('-')
                    id2 = secStr.rfind('_')
                    secStr = secStr[id1+1:id2]
                #ipdb.set_trace()
                    finList = []
                    for gene in intSect:
                        currRow = mirTab.ix[mirTab["Gene Symbol"] == gene]
                        tScore = currRow["Target Score"]
                        finName = "%s, %d" %(gene, tScore)
                        finList.append(finName)
                        str = "%s\t%s\t%s\n" %(primStr, secStr, ' ,'.join(finList))
                        f.write(str)
        num = num + 3
