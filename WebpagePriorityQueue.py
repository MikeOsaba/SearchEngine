import AVLTreeMap
import re
import WebPageIndex
#import processQueries #for tesing with file opening
class WebpagePriorityQueue: #make regular maxheap but use keyvals, where key is the priority decided by the sum of the
#word counts of the page for the words in the query, and val is page itself. push everything from list onto 
    #avl tree, then put that avl tree into a heap list
    def __init__(self, query, webPageIndexList):
            self.currentQuery = query.lower()
            self.unalteredList= webPageIndexList #lower the case of every word in the query for matching purposes
            """webPageTree= AVLTreeMap.AvlTreeMap()#create an AVL tree mapping to store our key:
            queryArray= stripRepeatedWords(query)
            for i in range(len(webPageIndexList)): Adhering to DRY coding practice 
                appearanceSum = 0
                for j in range(len(queryArray)):
                    appearanceSum += webPageIndexList[i].getCount(queryArray[j])
                webPageTree.put(appearanceSum, webPageIndexList[i])
            """
            self.WebpagePriorityQueue = None #webPageTree.AVLtoList(webPageTree.root) #Convert our AVL tree into a maxheap
            self.reheap(query)
    def peek(self):
        temp = self.WebpagePriorityQueue
        return temp[0].value.filepath #WebpageIndex with highest priority in the priority queue will be the first webpage
    def poll(self):
        temp = self.WebpagePriorityQueue
        tempReturn= temp[0].value.filepath
        del(temp[0])
        #pop off the webpageindex with the highest priority 
        return tempReturn

    def reheap(self, newQuery):
        if self.WebpagePriorityQueue != None: #clear our list to prevent doubling
            self.WebpagePriorityQueue.clear()
        webPageTree= AVLTreeMap.AvlTreeMap()#create an AVL tree mapping to store our key:
        queryArray= stripRepeatedWords(newQuery)
        webPageIndexList= self.unalteredList
        for i in range(len(webPageIndexList)):
            appearanceSum = 0
            for j in range(len(queryArray)):#with amount of appearances as key, and webpage index as value, add to avltreemap structure
                appearanceSum += webPageIndexList[i].getCount(queryArray[j])
            webPageTree.put(appearanceSum, webPageIndexList[i])
        self.WebpagePriorityQueue = webPageTree.AVLtoList(webPageTree.root) #Convert our AVL tree into a maxheap



def stripRepeatedWords(s):#To ensure we dont get botched word counts for repeated words in the query
    inputAsArray= re.sub("[^\w]", " ",  s.lower()).split()
    strippedArray=[]
    for i in range(len(inputAsArray)):
        if inputAsArray[i] in strippedArray:
            pass
        else:
            strippedArray.append(inputAsArray[i])

    return strippedArray

if __name__ == '__main__':
    testString= "uniqueOne repeat1 unique2 repeat1 unique3 repeat2 repeat2"
    print(stripRepeatedWords(testString)) #Expecting ['uniqueone', 'repeat1', 'unique2', 'unique3', 'repeat2'], repeat values stripped

    #Uncomment this block as well as line 4 to test behaviour of webpagepriority queue. Integrity of program compromised unless testing is isolated here
    #with line 4 only being uncommented when needed
    """WebpageList= processQueries.readFiles("./data")
    webQueue= WebpagePriorityQueue("binary tree", WebpageList)
    print(len(webQueue.WebpagePriorityQueue))

    for i in range(len(webQueue.WebpagePriorityQueue)):
        print("appearances: " + str(webQueue.WebpagePriorityQueue[i].key) + " match" + webQueue.WebpagePriorityQueue[i].value.filepath)
    webQueue.reheap("tree")

    print(" ")
    print("after reheap")
    print("\n\n")
    print(len(webQueue.WebpagePriorityQueue))

    for i in range(len(webQueue.WebpagePriorityQueue)):
        print("appearances: " + str(webQueue.WebpagePriorityQueue[i].key) + "match" + webQueue.WebpagePriorityQueue[i].value.filepath)
    """
