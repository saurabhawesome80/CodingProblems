"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
"""

class Node:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root,serializedBinaryTree):
    if root == None:
        serializedBinaryTree.append("Mark");
        return
    serializedBinaryTree.append(root.val)
    serialize(root.left,serializedBinaryTree)
    serialize(root.right,serializedBinaryTree)

def deserialize(serializedBinaryTree, index):
    if index[0] >= len(serializedBinaryTree) or serializedBinaryTree[index[0]] == "Mark":
        return None
    root = Node(serializedBinaryTree[index[0]])
    index[0] += 1
    root.left = deserialize(serializedBinaryTree, index)
    root.right = deserialize(serializedBinaryTree, index)
    return root

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serializedBinaryTree = []
    serialize(node,serializedBinaryTree)
    # print(serializedBinaryTree)
    index = [0]
    node1 = deserialize(serializedBinaryTree, index)
    print(node1.left.left.val == "left.left")
    

if __name__ == "__main__":
    main()