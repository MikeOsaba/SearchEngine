class AvlNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None
        self.height = 0

class AvlTreeMap: #Standard AVL tree modified to use key:value objects
    def __init__(self):
        self.root = None

    def height(self, n): 
        if n==None:
            return -1
        return n.height

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None: #x is root
            self.root = y

        elif x == x.parent.left: #x is left child
            x.parent.left = y

        else: #x is right child
            x.parent.right = y
 
        y.left = x
        x.parent = y

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None: #x is the root node
            self.root = y

        elif x == x.parent.right: #x is the right child node
            x.parent.right = y

        else: #x is the left child node
            x.parent.left = y

        y.right = x
        x.parent = y

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

    def balance_factor(self, n):
        if n == None:
            return 0
        return self.height(n.left) - self.height(n.right)

    def put(self, key, value):
        newKeyVal= KeyValPair(key, value)
        newKeyValNode = AvlNode(newKeyVal)
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if newKeyValNode.data.key < temp.data.key:
                temp = temp.left
            else:
                temp = temp.right

        newKeyValNode.parent = y

        if y == None: #Case which handles empty tree, new node becomes root
            self.root = newKeyValNode
        elif newKeyValNode.data.key < y.data.key:
            y.left = newKeyValNode
        else:
            y.right = newKeyValNode

        z = newKeyValNode

        while y != None:
            y.height = 1 + max(self.height(y.left), self.height(y.right))

            x = y.parent

            if self.balance_factor(x) <= -2 or self.balance_factor(x) >= 2:#Parent of parent node (grandparent) is unbalanced
                if y == x.left:
                    if z == x.left.left: #Left left AVL insertion imbalance case
                        self.right_rotate(x)

                    elif z == x.left.right: #Left right AVL insertion imbalance case
                        self.left_rotate(y)
                        self.right_rotate(x)


                elif y == x.right:
                    if z == x.right.right: #Right right insertion imbalance case
                        self.left_rotate(x)

                    elif z == x.right.left: #Right left insertion imbalance case
                        self.right_rotate(y)
                        self.left_rotate(x)
                break

            y = y.parent
            z = z.parent
    def get(self, searchKey):
        temp= self.root
        return search(temp, searchKey)

    def inorder(self, n): #Printer function for testing purposes 
        if n != None:
            self.inorder(n.left)
            print(str(n.data.key) + " " + n.data.value)
            self.inorder(n.right)

    def AVLtoList(self, n, avlList=[]): #Responsible for converting AVL to list for later heap implementation
        
        if n != None:
            self.AVLtoList(n.right)
            avlList.append(n.data)
            self.AVLtoList(n.left)
        return avlList

def search(root, needle): #Helper function for get() which makes recursive implementation easier 
    if root is None:
        return None 
    if root.data.key == needle:
        return root.data.value
    if needle<root.data.key:
        return search(root.left, needle)
    else:
        return search(root.right, needle)  
class KeyValPair: #Class which handles implicit key:value operations
    def __init__(self, key, value):
        self.key = key
        self.value = value




if __name__ == '__main__':
    testTree= AvlTreeMap()
    
    testTree.put(15, "bob")
    testTree.put(20, "anna")
    testTree.put(24, "tom")
    testTree.put(10, "david")
    testTree.put(13, "david")
    testTree.put(7, "ben")
    testTree.put(30, "karen")
    testTree.put(36, "erin")
    testTree.put(25, "david")
    print(testTree.get(20))#Expecting anna, as its key is 20

    testTree.inorder(testTree.root)

    testTreeAsList= testTree.AVLtoList(testTree.root)
    print("First item in test tree as list: " + str(testTreeAsList[0].key) + " " + testTreeAsList[0].value) #Should be 36 Erin as it is the highest value
    print("list conversion testing: ")
    for i in range(len(testTreeAsList)): #Expecting same result as testree inorder printing
        print(str(testTreeAsList[i].key) + " " + testTreeAsList[i].value)
   