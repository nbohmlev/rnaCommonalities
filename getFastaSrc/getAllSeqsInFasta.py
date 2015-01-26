from collections import defaultdict

from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils import GC

Entrez.email = 'sa6@williams.edu'


def getRefSeqDB(dbPath):
    ## Load the "proteome-genes.txt" refseq mouse database
    ## (database maps refseq IDs to gene names
    ## Return gene name-->[list of unique protein IDs for the gene] dictionary
    geneDict = defaultdict(list)
    with open(dbPath, 'rb') as db:
        for line in db:
            allIds = line.split()
            if allIds[0][0:2] == 'NP':
                geneDict[allIds[2]].append(allIds[0])

    return geneDict


def retGeneList(fPath):
    # Opens the supplied file [a csv column of gene names]
    # and returns the gene names as an iterable list
    with open(fPath, 'r') as f:
        geneList = f.read().split()

    if geneList[0].startswith("'") and geneList[0].endswith("'"):
        for idx, item in enumerate(geneList):
            geneList[idx] = item[1:-1]

    return geneList


def printSeqsToFile(fPath, seqsList):
    # Writes the fasta sequences sequentially to the
    # supplied file
    with open(fPath, 'w') as f:
        for seq in seqsList.values():
            for innerSeq in seq:
                f.write(innerSeq)


def getMrnaId(db, geneList):
    # Iterates through the list of genes
    # Check if the gene is in the gene -> refseq protein ID database
    # If it's there, query NCBI to find mRNA refseq ID
    # Store the mRna ID in a gene->mRnaID dictionary

    # Genes not in db are added to notInDb list
    geneToMrna = defaultdict(list)
    notInDb = []
    for item in geneList:
        allGenes = item.split(';')
        for gene in allGenes:
            if db.has_key(gene):
                allProteinIDs = db[gene]
                for indiProID in allProteinIDs:
                    handle = Entrez.efetch(db='protein', id=indiProID, rettype='gb', retmode='xml')
                    record = Entrez.read(handle)
                    sourceDB = record[0]['GBSeq_source-db']
                    mRnaId = sourceDB.split()[-1].split('.')[0]
                    geneToMrna[gene].append(mRnaId)
            else:
                notInDb.append(gene)

    return geneToMrna, notInDb


def getMrnaSeqs(geneToMrna):
    # Use the gene-->[list of mRna Id] dictionary
    # Iterate through mRnaID list for every gene
    # Fetch fasta sequence for every mRnaID
    # Put every fasta sequence in a list
    # Return the list
    allFastaSeqs = defaultdict(list)
    for gene, allmRnaId in geneToMrna.iteritems():
        for indiMrnaId in allmRnaId:
            handle = Entrez.efetch(db='nucleotide', id=indiMrnaId, rettype='text', retmode='fasta')
            allFastaSeqs[gene].append(handle.read())

    return allFastaSeqs


def getUTRseqs(geneToMrna):
    yesCDS = defaultdict(list)
    noCDS = defaultdict(list)
    negStrand = defaultdict(list)

    for gene, allmRnaId in geneToMrna.iteritems():

        for indiMrnaId in allmRnaId:
            handle = Entrez.efetch(db='nucleotide', id=indiMrnaId, rettype='text', retmode='gb')
            record = SeqIO.read(handle, "gb")
            handle.close()
            cdsDoesNotExist = True
            negativeStrand = True

            for feature in record.features:
                if feature.type == 'CDS':
                    seq = record.seq.tostring()
                    start = feature.location.start.position
                    end = feature.location.end.position
                    strand = feature.location.strand

                    if strand == 1:
                        # IF ON NEGATIVE STRAND DO NOT INCLUDE IN OUTPUT
                        # WHETHER IT HAS CDS OR NOT

                        fiveUTR = seq[0:start - 1]
                        threeUTR = seq[end + 1:]
                        cds = feature.extract(record.seq).tostring()
                        negativeStrand = False

                        yesCDS[gene].append(
                            dict(fullSeq=seq,
                                 cds=cds,
                                 fiveUTR=fiveUTR,
                                 threeUTR=threeUTR,
                                 cdsStart=start,
                                 cdsEnd=end,
                                 cdsQuals=feature.qualifiers,
                                 strand=strand,
                                 refSeqId=indiMrnaId))

                    cdsDoesNotExist = False

            if cdsDoesNotExist:
                noCDS[gene].append(indiMrnaId)

            if negativeStrand:
                negStrand[gene].append(indiMrnaId)

    return yesCDS, noCDS, negStrand


def printUTRlens(utrSeqs, fPath):
    with open(fPath, 'w') as f:
        f.write('Gene\tlength\tGC\tcds\tcdsGC\tfiveUTR\tfiveUTRgc\tthreeUTR\tthreeUTRgc\n')
        for key, value in utrSeqs.iteritems():
            for item in value:
                fiveUTR = len(item['fiveUTR'])
                fiveUTRgc = GC(item['fiveUTR'])

                threeUTR = len(item['threeUTR'])
                threeUTRgc = GC(item['threeUTR'])

                cds = len(item['cds'])
                cdsGC = GC(item['cds'])

                seq = len(item['fullSeq'])
                seqGC = GC(item['fullSeq'])

                # gID = item['cdsQuals']['db_xref'][2]
                # col = gID.find(':')
                # gName = key + '_%s' % gID[col + 1:]

                out = '%s\t%d\t%0.2f\t%d\t%0.2f\t%d\t%0.2f\t%d\t%0.2f\n' % (key, seq, seqGC, cds, cdsGC, fiveUTR, fiveUTRgc, threeUTR, threeUTRgc)

                f.write(out)


if __name__ == '__main__':
    dbPath = '../proteome-genes.txt'
    db = getRefSeqDB(dbPath)
    fPath = '../fxsGeneListNew.txt'
    geneList = retGeneList(fPath)
    geneToMrna, notInDb = getMrnaId(db, geneList)
    allFastaSeqs = getMrnaSeqs(geneToMrna)
    outFile = 'fxs.fasta'
    printSeqsToFile(outFile, allFastaSeqs)
