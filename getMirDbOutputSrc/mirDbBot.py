## Sameer Aryal 
## January 20, 2015
## Klann Laboratory, Center for Neural Science, NYU

## I intend to build a tool that allows me to 
## extract predicted 5'UTR target sites of a particular miRna
## ex. (mmu-miR-125a-5p) from the mirDb website.

import sys
import time
from selenium import webdriver
import ipdb

class mirDbBot():

    def __init__(self):
        self.driver = webdriver.PhantomJS()
    
    def getDriver(self):
        return self.driver

    def openPage(self, url):  
        driver = self.driver
        driver.get(url)
        
    def fillForm(self, species, region, mirName):
        driver = self.driver
        xPath = "//select[@name='species']/option[text()=%s]"%(species)
        driver.find_element_by_xpath(xPath).click()
        #ipdb.set_trace()
        if region != "'3utr'":
            xPath = "//select[@name='location']/option[@value=%s]"%(region)
            driver.find_element_by_xpath(xPath).click()

        driver.find_element_by_xpath("//input[@name='searchBox']").send_keys(mirName)
        driver.find_element_by_xpath("//input[@name='submitButton']").click()
        #ipdb.set_trace()
        
        #tArea = form.find_element_by_name("S1")
        #tArea.send_keys(seq)
        #form.find_element_by_name("B4").click()
        #form.submit()

    def getResult(self):
        driver = self.driver
        resLinks = driver.find_elements_by_link_text('Details')
        bigResDict = {}
        for idx in range(len(resLinks)):
            resLinksTemp = driver.find_elements_by_link_text('Details')
            item = resLinksTemp[idx]
            item.click()
            #time.sleep(2)
            resTab = driver.find_elements_by_tag_name("table")[1]
            resCell = resTab.find_elements_by_xpath("//td")
            num = 2
            resDict = {}
            while num < len(resCell):
                resDict[resCell[num].text] = resCell[num+1].text
                num = num + 2
            #ipdb.set_trace()
            bigResDict[resCell[21].text] = resDict
            driver.back()
        
        return bigResDict

    def killFox(self):
        driver = self.driver
        driver.close()
        driver.quit()
        
    def printOutput(self, fPath, resDict):

        with open(fPath, 'w') as f:
            f.write("Gene Symbol\tGene Description\tGene ID\tGenbank Accession\tSeed Location\tTarget Score\n")
            
            for key, value in resDict.iteritems():
                geneSymbol = value['Gene Symbol']
                geneDesc = value['Gene Description']
                geneID = value['NCBI Gene ID']
                genBankName = value['GenBank Accession']
                seedLoc = value['Seed Location']
                tScore = value['Target Score']
                f.write("%s\t%s\t%s\t%s\t%s\t%s\n" %(geneSymbol, geneDesc, geneID, genBankName, seedLoc, tScore))

if __name__ == "__main__":

    bot = mirDbBot()
    bot.openPage("http://mirdb.org/miRDB/custom.html")
    species = "'Mouse'"
    region = "'5utr'"
    mirName = 'mmu-miR-125a-5p'
    bot.fillForm(species, region, mirName)
    resDict = bot.getResult()
    bot.killFox()
    fPath = '../mirDbOutput/%s_%s_%s' %(mirName, region[1:-1], species[1:-1])
    bot.printOutput(fPath, resDict)
    sa = "sameer"
