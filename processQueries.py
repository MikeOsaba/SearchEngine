import glob
import os
import WebPageIndex
import re
import WebpagePriorityQueue
def readFiles(file):#Access given directory
    file_list = glob.glob(os.path.join(os.getcwd(), file, "*.txt"))
    webPageIndexList= []
    for files in file_list:
        webPageIndexList.append(WebPageIndex.WebPageIndex(files))
    return webPageIndexList
    

def searchEngine(dataFilename, queryFilname,numResultsInitial=-1):
    text_file=queryFilname
    
    with open(text_file) as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
    WebpageList= readFiles(dataFilename)
    webQueue= WebpagePriorityQueue.WebpagePriorityQueue("initialization throwaway", WebpageList)
    for querie in content:
        numResults=numResultsInitial
        webQueue.reheap(querie)
        print("Current search: '"+ querie+ "'")
        print("Top matched results: ")
        if numResults==-1:
            while webQueue.WebpagePriorityQueue[0].key != 0:#if user has not specified a result limit, poll until no files match the querie
                #print(webQueue.WebpagePriorityQueue[0].key)
                print(webQueue.poll())
        else:
            while numResults!= 0 and webQueue.WebpagePriorityQueue[0].key != 0:#Otherwise, poll until no files match OR limit has been met
                #print(webQueue.WebpagePriorityQueue[0].key)
                print(webQueue.poll())
                numResults-=1
        print("\n")


def main():
    yesNo= input("Would you like to limit your search result amount? (Y/N)")
    if yesNo == "N":
        searchEngine("./data", "queries.txt")
    elif yesNo== "Y":
        searchAmount= input("How many searches would you like to set the limit to?")
        print("Limiting search results to top " + searchAmount + " results.")
        searchEngine("./data", "queries.txt", int(searchAmount))
    else:
        print("Invalid response. Exiting search.")
main()