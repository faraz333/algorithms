# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeafNode(node):
    if node.left == None and node.right==None:
        return True
    else:
        return False

def hasPathSum(node: TreeNode, targetSum: int) -> bool:

  if node == None:
      return False
  targetSum=targetSum-node.val
  if isLeafNode(node) and targetSum ==0:
      return True
  # let do traversal of tree
  foundLeft=   hasPathSum(node.left, targetSum)
  foundRight= hasPathSum(node.right, targetSum)

  return foundLeft or foundRight


def getAllPartialPaths(node: TreeNode, targetSum: int, currentPath:list[int],
                       allpths :list[list[int]]) -> None:

  if node == None:
      return
  #add current node val to current path
  targetSum=targetSum-node.val
  currentPath.append(node.val) #add this node to current path

  if targetSum ==0: # it means we got our sum so far coming from root
      #add current list to result
      allpths.append(currentPath.copy()) # add copy of full list so far to all paths

  elif targetSum < 0: # it means we pass beyond target sum, we need to remove  elements of currentPath
      # in continous order and see if we reach our path
      currentRemovalSum = 0 #we need to add numbers and get our removal sum
      for i in range (0, len(currentPath)-1): #target sum is more than
          currentRemovalSum = currentPath[i] + currentRemovalSum
          if targetSum + currentRemovalSum == 0: #it means if we remove upto ith element we are good
              partialPath = currentPath.copy()[i:]
              allpths.append( partialPath)
              #it means after removing i elements we are good
          elif targetSum + currentRemovalSum > 0: #we need to stop as we can not remove more elements
              return


  # let do traversal of tree
  getAllPartialPaths(node.left, targetSum, currentPath,allpths)
  getAllPartialPaths(node.right, targetSum, currentPath, allpths)

  currentPath.pop() # pop last added element from current path

def getAllFullPaths(node: TreeNode, targetSum: int, currentPath:list[int], allpths :list[list[int]]) -> None:

  if node == None:
      return
  #add current node val to current path
  targetSum=targetSum-node.val
  currentPath.append(node.val) #add this node to current path

  if isLeafNode(node) and targetSum ==0:
      #add current list to result
      allpths.append(currentPath.copy()) # add copy of list to all paths
  # let do traversal of tree
  getAllFullPaths(node.left, targetSum, currentPath,allpths)
  getAllFullPaths(node.right, targetSum, currentPath, allpths)

  currentPath.pop() # pop last added element from current path

def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target = 22
    print(hasPathSum(root, target))  # Output: True (because 5 -> 4 -> 11 -> 2 = 22)
    target=20
    print(hasPathSum(root, target))  # Output: True (because 5 -> 4 -> 11 -> 2 = 22)
    target = 18
    print(hasPathSum(root, target))  # Output: True (because 5 -> 4 -> 11 -> 2 = 22)

    #now this is tree for path sum2
    # Construct a binary tree:
    #         5
    #        / \
    #       4   8
    #      /   / \
    #     11  13  4
    #    /  \      \
    #   7    2      1

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target = 22
    allPaths = [[]]
    currentPath=[]
    getAllFullPaths(root, target, currentPath, allPaths)
    print(allPaths)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)

    target = 10
    allPaths = [[]]
    currentPath = []
    getAllPartialPaths(root, target, currentPath, allPaths)
    for i, paths in enumerate(allPaths):
        if len(paths)==0:
            allPaths.remove(paths)

    print(allPaths)

main()

# Construct a binary tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1