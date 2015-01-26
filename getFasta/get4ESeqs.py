from rnaMotifs.getFasta import getAllSeqsInFasta as FGL


if __name__ == '__main__':
    dbPath = '../geneDB/proteome-genes.txt'
    db = FGL.getRefSeqDB(dbPath)
    fPath = '../geneLists/fourEgenes.txt'
    geneList = FGL.retGeneList(fPath)
    geneToMrna, notInDb = FGL.getMrnaId(db, geneList)
    allFastaSeqs = FGL.getMrnaSeqs(geneToMrna)
    outFile = '../fastaOutput/fourE.fasta'
    FGL.printSeqsToFile(outFile, allFastaSeqs)
