"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node

"""
# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def depth_helper(node):
    if (node.left is None) & (node.right is None):
        return 1 # this node is a leaf
    elif node is None: # back up just in case root is empyu
        return 0
    else: # at least one child exists
        if node.left is not None:
            left = 1 + depth_helper(node.left) # get the left depth recursively
        else: left = 0

        if node.right is not None:
            right = 1 + depth_helper(node.right) # get the right depth recursively
        else: right = 0

        return max(left, right) # figure out which is bigger!

#PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
	depth = depth_helper(tree)
	return depth



#test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print ("Depth of tree is %d, and the expected result is 3" %(find_max_depth(root),))

if __name__ == "__main__":
    main()
