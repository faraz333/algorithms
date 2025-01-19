from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def build_tree(inorder, preorder):
    """
    Builds a binary tree from inorder and preorder traversals.

    Arguments:
    inorder -- list of nodes visited in inorder (Left, Root, Right)
    preorder -- list of nodes visited in preorder (Root, Left, Right)

    Returns:
    The root of the binary tree.
    """
    if len(inorder) == 0:
        return None
    num=preorder[0]
    root = Node(num)
    #binary serach for index of inorder[0] in preorder
    idx = binary_search(inorder, num)
    #now call build tree again
    #length of preorder is
    leftSegment = idx # if idx is 3 it means thee are three elements of left in inrder
    #left segment will start from 1 index
    root.left = build_tree(inorder[:idx], preorder[1:leftSegment+1])
    root.right=build_tree(inorder[idx:], preorder[idx:])

    return root

def binary_search(array, num):
      #we will first middle element
      mid= int(len(array)/2) # for len 3 it will be 1, 2 it will be 1 and 1 it will be 0

      if array[mid] == num:
          return mid #that will be index of middle element
      elif  array[mid] > num: #go left
           return  binary_search(array[:mid],num)
      else:
          return binary_search(array[mid:], num)


def inorder_traversal(node):

    if not node:
        return
    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)
def preorder_traversal(node):

    if not node:
        return
    print(node.value)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def postorder_traversal(node):

    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value)

def main():
    # Example of inorder and preorder traversals
    inorder = [4, 2, 5, 1, 6, 3, 7]  # Left, Root, Right
    preorder = [1, 2, 4, 5, 3, 6, 7]  # Root, Left, Right

    # Construct the tree from inorder and preorder traversals
    root = build_tree(inorder, preorder)

    # Print inorder and preorder traversals of the constructed tree
    print("Inorder Traversal of the Constructed Tree:")
    inorder_traversal(root)
    print("pre order Traversal of the Constructed Tree:")
    preorder_traversal(root)
    print("post order Traversal of the Constructed Tree:")
    postorder_traversal(root)
main()
