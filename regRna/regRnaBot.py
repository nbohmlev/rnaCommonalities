## Sameer Aryal 
## August 20, 2014
## Klann Laboratory, Center for Neural Science, NYU

## I intend to build a tool that allows me feed RNA sequences into
## RegRNA (http://regrna2.mbc.nctu.edu.tw/detection.html) and extract the
## xml file containing motif descriptions of the sequence

import sys

from selenium import webdriver

sys.path.append("/Users/SA/rnaMotifs/memeChipFasta")
import getAllSeqsInFasta as getSeq


def getFastaList(geneListPath):

    dbPath = "/Users/SA/rnaMotifs/proteome-genes.txt"
    db = getSeq.getRefSeqDB(dbPath)
    geneList = getSeq.retGeneList(geneListPath)
    geneToMrna, notInDb = getSeq.getMrnaId(db, geneList)
    return getSeq.getMrnaSeqs(geneToMrna)

class regRnaBot():

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        
    def openPage(self):
        driver = self.driver
        driver.get("http://regrna2.mbc.nctu.edu.tw/detection.html")
        
    def fillForm(self, seq):
        driver = self.driver
        form = driver.find_element_by_xpath("//form[1]")
        tArea = form.find_element_by_name("S1")
        tArea.send_keys(seq)
        form.find_element_by_name("B4").click()
        form.submit()

    def getResult(self):
        driver = self.driver
        driver.find_element_by_link_text("XML File").click()
        driver.switch_to_window(driver.window_handles[-1])
        return driver.page_source

    def killFox(self):
        driver = self.driver
        for item in driver.window_handles:
            driver.switch_to_window(item)
            driver.close()



        
if __name__ == "__main__":


    fPath = '/Users/SA/rnaMotifs/knownTopGenesLite.txt'
    fastaList = getFastaList(fPath)

    for key, item in fastaList.iteritems():
        num = 1
        for indiSeq in item:
            bot = regRnaBot()
            bot.openPage()
            bot.fillForm(indiSeq)
            xml = bot.getResult()
            bot.killFox()
            fName = key + "_" + str(num) + ".xml"
            fPath = '/Users/SA/rnaMotifs/xml/fxs/' + fName
            with open(fPath, 'w') as f:
                f.write(str(xml))
            num += 1
