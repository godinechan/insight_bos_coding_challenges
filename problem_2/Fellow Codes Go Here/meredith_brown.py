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
    # Recursive solution with a helper function that keeps track of the depth
    
    def depth_helper_helper(n, d):
        if n.left and n.right:
            return max(depth_helper_helper(n.left, d+1), depth_helper_helper(n.right, d+1))
        elif n.left:
            return depth_helper_helper(n.left, d+1)
        elif n.right:
            return depth_helper_helper(n.right, d+1)
        else:
            return d
    return depth_helper_helper(node, 1)

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
