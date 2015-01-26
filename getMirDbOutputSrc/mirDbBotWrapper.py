from rnaMotifs.mirDbBot import mirDbBot as MDB

def mirDbBotWrapper(url, region, mirName):
    bot = MDB.mirDbBot()
    bot.openPage(url)
    species = "'Mouse'"
    #region = "'5utr'"
    #mirName = 'mmu-miR-125a-5p'
    bot.fillForm(species, region, mirName)
    resDict = bot.getResult()
    bot.killFox()
    fPath = '../mirDbOutput/%s_%s_%s' %(mirName, region[1:-1], species[1:-1])
    bot.printOutput(fPath, resDict)
    sa = "sameer"
