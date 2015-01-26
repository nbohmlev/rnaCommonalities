from rnaMotifs.getFastaSrc import getAllSeqsInFasta as FGL


if __name__ == '__main__':
    dbPath = '../geneDB/proteome-genes.txt'
    db = FGL.getRefSeqDB(dbPath)
    fPath = '../geneLists/fxsDown.txt'
    geneList = FGL.retGeneList(fPath)
    geneToMrna, notInDb = FGL.getMrnaId(db, geneList)


    utrSeqs, noCds, negStrand = FGL.getUTRseqs(geneToMrna)
    FGL.printUTRlens(utrSeqs, '../utrLenOutput/fxsDown.txt')

    allFastaSeqs = FGL.getMrnaSeqs(geneToMrna)
    outFile = '../fastaOutput/fxsDown.fasta'
    FGL.printSeqsToFile(outFile, allFastaSeqs)
