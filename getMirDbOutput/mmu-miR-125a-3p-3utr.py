from rnaMotifs.mirDbBot import mirDbBotWrapper as MB

if __name__=="__main__":
    url = "http://mirdb.org/miRDB/index.html"
    region = "'3utr'"                                                                                             
    mirName = 'mmu-miR-125a-3p'
    #mode = "notDefault"
    MB.mirDbBotWrapper(url, region, mirName)
