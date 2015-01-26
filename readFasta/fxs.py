from rnaMotifs.readFastaSrc import readFasta as RF

if __name__ == '__main__':
    allSeqs = RF.readFasta('../fastaOutput/fxs.fasta')
    seqLengths = RF.getSeqLens(allSeqs)
    RF.printSeqLens('../seqLengths/fxs.txt', seqLengths, 'up')