class BST:
     def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

def insert(root, value):#switch to left or right side of recursively accessed tree and place new node
    #in correct location 
    if root is None:
        root = BST(value)
    elif (value < root.value ):
        root.leftNode= insert(root.leftNode, value)
    else:
        root.rightNode= insert(root.rightNode, value)
    return root

def getTotalHeight(root): #recursively iterate through tree, calculating height for each node and summing
    #using the max of the left and right for the calculation
    if root is None:
        return -1
    leftHeight= getTotalHeight(root.leftNode)
    rigtHeight= getTotalHeight(root.rightNode)
    return max(leftHeight, rigtHeight) +1

def nodeCount(root): #Helper function, count amount of nodes in a given tree
    count=1
    if root is None:
        return 0

    count+= nodeCount(root.leftNode)
    count+= nodeCount(root.rightNode)
    return count
def getWeightBalanceFactor(root, countList=[]): #calculate weight for every node, then return the max.
    
    if root is None:
        return 0
    countList.append(individualFactor(root.leftNode))
    countList.append(individualFactor(root.rightNode))
    return max(countList)

def individualFactor(root):#helper function, calculate weight for a given node
    return abs(nodeCount(root.rightNode)-nodeCount(root.leftNode))
def inorder(root): #Printer function
    if not root:
        return
    inorder(root.leftNode)
    print (root.value)
    inorder(root.rightNode)

if __name__ == "__main__":
    
    testTree = BST(6)
    insert(testTree, 4)
    insert(testTree, 9)
    insert(testTree, 5)
    insert(testTree, 8)
    insert(testTree, 7)
    inorder(testTree)
    print("  ")
    print(getTotalHeight(testTree))#Expecting 3
    #print(individualFactor(testTree))
    print(getWeightBalanceFactor(testTree))#Expecting 2


