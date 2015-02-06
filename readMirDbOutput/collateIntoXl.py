import glob
import pandas as pd
import ipdb

def CollateXL(fList):
    outFile = pd.ExcelWriter('allMirCrossRefs.xlsx')
    for item in fList:
        #ipdb.set_trace()
        with open (item, 'r') as f:
            data = pd.read_csv(f, sep='\t')
            sName = item[item.rfind('/')+1:-4]
            data.to_excel(outFile, sheet_name=sName, index=False)
    outFile.save()

if __name__ == "__main__":
 #   ipdb.set_trace()
    allFiles = glob.glob("../crossRefOutput/*.txt")
    CollateXL(allFiles)
