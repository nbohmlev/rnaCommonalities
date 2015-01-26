from rnaMotifs.getFastaSrc import getSeqsWrapper as GS
import sys
import glob

if __name__ == '__main__':

    
    fPath = '../geneLists/dhpgFxsOnlyDown.txt'
    #fList = glob.glob("../geneLists/dhpg*.txt")
    #for fPath in fList:
    fName = fPath.split("/")[-1].split(".")[0]
    utrSeqOutFile = '../utrLenOutput/%s.txt' %fName
    outFile = '../fastaOutput/%s.fasta' %fName
    GS.getSeqsWrapper(fPath, utrSeqOutFile, outFile)
