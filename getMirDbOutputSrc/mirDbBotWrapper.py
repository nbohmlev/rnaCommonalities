from rnaMotifs.getMirDbOutputSrc import mirDbBot as MDB
import ipdb

class mirBotInput():

    def __init__(self, url, region):
        
        self.url = url
        self.region = region


def mirDbBotWrapper(mirName):
    ipdb.set_trace()
    
    defUrl = "http://mirdb.org/miRDB/index.html"
    custUrl = "http://mirdb.org/miRDB/custom.html"

    region5utr = "'5utr'" 
    regionCds = "'cds'" 
    region3utr = "'3utr'" 

    allBotInputs = []
    allBotInputs.append(mirBotInput(custUrl, region5utr))
    allBotInputs.append(mirBotInput(custUrl, regionCds))
    allBotInputs.append(mirBotInput(defUrl, region3utr))

    for item in allBotInputs:
        bot = MDB.mirDbBot()
        url = item.url
        bot.openPage(url)
        species = "'Mouse'"
        region = item.region
        bot.fillForm(species, region, mirName)
        resDict = bot.getResult()
        bot.killFox()
        fPath = '../mirDbOutput/%s_%s_%s' %(mirName, region[1:-1], species[1:-1])
        bot.printOutput(fPath, resDict)
