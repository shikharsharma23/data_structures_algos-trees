## A simple implementation of routine to print all paths from root to leave for a tree

class Tree:
    def __init__(self,data): # make a tree structure
        self.data=data
        self.left=None
        self.right=None
    
def get_all_leaves(root,path): # function to print all paths
    if root is None: # if at a null node, just return
        return
    
    path.append(root.data) # keep track of path
 
    if root.left is None and root.right is None: # if at leaf node   
        print(path) # print path traversed
    else:
        get_all_leaves(root.left, path.copy())  # go to left
        get_all_leaves(root.right, path.copy()) # go to right
        # path to copy required as in Python list by default dont pass with copies
 
        
        
if __name__=="__main__": 
    # make a dummy tree
    #               2
    #             /  \
    #           3     4
    #         /  \    / \
    #        7   10  11  null
    
    path=[]
    tree=Tree(2)
    tree.left=Tree(3)
    tree.right=Tree(4)
    tree.left.left=Tree(7)
    tree.left.right=Tree(10)
    tree.right.left=Tree(11)
    get_all_leaves(tree,path) # print all paths
    
    
    
    
    
    