from Bio import SeqIO as seqIO


def readFasta(fName):
    with open(fName, "rU") as handle:
        return seqIO.to_dict(seqIO.parse(handle, 'fasta'))


def getSeqLens(allSeqs):
    seqLengths = {}

    for key, seq in allSeqs.iteritems():
        seqLengths[key] = len(seq)

    return seqLengths


def printSeqLens(fName, seqLengths, idStr):
    with open(fName, 'w') as f:
        for item in seqLengths.values():
            f.writelines(idStr + '\t' + str(item) + '\n')

if __name__ == '__main__':
    allSeqs = readFasta('../fastaOutput/fxs.fasta')
    seqLengths = getSeqLens(allSeqs)
    printSeqLens('../seqLengths/fxs.txt', seqLengths, 'up')


