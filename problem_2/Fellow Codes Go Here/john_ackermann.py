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

    def get_depth(node):
        if node.left is None and node.right is None:
            return 0
        else:
            depth_l = get_depth(node.left)
            depth_r = get_depth(node.right)

            if node.left:
                depth_l += 1
            if node.right:
                depth_r += 1

            return  max(depth_l, depth_r)

    # traverse the left and right branches
    # adding 1 for each node
    # then add 1 for the root node
    max_depth = get_depth(node)
    return max_depth + 1

# PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
    depth = depth_helper(tree)
    return depth


# test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Depth of tree is %d, and the expected result is 3" % (find_max_depth(root),))


if __name__ == "__main__":
    main()