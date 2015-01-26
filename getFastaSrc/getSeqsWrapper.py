from rnaMotifs.getFastaSrc import getAllSeqsInFasta as FGL


def getSeqsWrapper(fInput, utrSeqOutPath, fastaSeqOutPath):

    dbPath = '../geneDB/proteome-genes.txt'
    db = FGL.getRefSeqDB(dbPath)
    fPath = fInput
    geneList = FGL.retGeneList(fPath)
    geneToMrna, notInDb = FGL.getMrnaId(db, geneList)


    utrSeqs, noCds, negStrand = FGL.getUTRseqs(geneToMrna)
    FGL.printUTRlens(utrSeqs, utrSeqOutPath)

    allFastaSeqs = FGL.getMrnaSeqs(geneToMrna)
    outFile = fastaSeqOutPath
    FGL.printSeqsToFile(outFile, allFastaSeqs)