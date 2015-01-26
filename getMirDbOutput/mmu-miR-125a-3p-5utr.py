from rnaMotifs.mirDbBot import mirDbBotWrapper as MB

if __name__=="__main__":
    url = "http://mirdb.org/miRDB/custom.html"
    region = "'5utr'"                                                                                             
    mirName = 'mmu-miR-125a-3p'
    #mode = "default"
    MB.mirDbBotWrapper(url, region, mirName)
