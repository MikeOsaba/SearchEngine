import re
class WebPageIndex:
    
    def __init__(self, file):
        self.filepath = str(file) #Path of filed saved 
        with open(file, 'r') as f:
            data = f.read()
        self.data =data.lower() #Input file saved as a lowercase string
        self.dataListVer= re.sub("[^\w]", " ",  data.lower()).split()#Used to count amount of appearances of a given string in used text.
         #Sourced from https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
    def getCount(self, s):#Returns count of word appearances as described in 2.2 requirement 2)
        tempString= self.dataListVer
        appearance=0
        for i in range(len(tempString)):
            if tempString[i] == s:
                appearance+=1
        return appearance

if __name__ == '__main__':
    """with open('data/doc1-arraylist_1.txt', 'r') as f:
        data = f.read()
    data=data.lower()
    print(data)
    """

    testFileReader= WebPageIndex('data/doc1-arraylist_1.txt')
    print(testFileReader.data)
    print(testFileReader.getCount("an")) #Excpecting 4
    print(testFileReader.getCount("array")) #Excpecting 3
    print(testFileReader.getCount("arraylist")) #Expecting 2

    

