
import os
import re

def iterateFiles():
    fPath = 'C:\\A\\'
    fileList = os.listdir(fPath)
    for i in fileList:
        listItem = os.path.join(fPath, i) 
        result = re.search('.txt', listItem)
        if result:
            print(listItem)
            print(os.path.getmtime(listItem))        


if __name__ == '__main__':
    iterateFiles()
