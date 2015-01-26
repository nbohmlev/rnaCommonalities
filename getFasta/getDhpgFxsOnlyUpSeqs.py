from rnaMotifs.getFastaSrc import getSeqsWrapper as GS
if __name__ == '__main__':
    fPath = '../geneLists/dhpgWtOnlyUp.txt'
    utrSeqOutFile = '../utrLenOutput/dhpgWtOnlyUp.txt'
    outFile = '../fastaOutput/dhpgWtOnlyUp.fasta'
    GS.getSeqsWrapper(fPath, utrSeqOutFile, outFile)