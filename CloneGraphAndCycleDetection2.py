from collections import deque


class Node:
    def __init__(self, value:int=0, neighbors=None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

# Function to print graph (for testing purposes)
def print_graph(node):
    visited = set()

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        print(f"Node {n.value} -> {[neighbor.value for neighbor in n.neighbors]}")
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)

def cloneGraph(node, n):
    #we can start from any node. we will mantain queue to do bsf.
    # we will mantain visited set. we will create an empty adjaceny list graph and will populate it as we go
    if node == None:
        return None# we can not clone an empty graph

    cloneGraph = [None for i in range(n+1)] #This will serve as our memory n+1 will make it easy to maange operations

    #create head node.
    head:Node = Node(node.value)
    cloneGraph[node.value] = head
    queue = deque() #create an ampty queue
    visited = [False for i in range(n+1)] #create visited set
    #push node to queue.
    queue.append(node)

    while (queue):
        size = len(queue)
        for i in range(size):
            origNode = queue.popleft()
            visited[origNode.value] = True #mark this node as visisted. visisted means we are dealing with its neighbour
            #old node
            if cloneGraph[origNode.value] == None: #it means we need create copy of Node
                newnode= Node(origNode.value)
            for  neighbour in  origNode.neighbors: #now we want to create connections for this new clone node
                if  cloneGraph[neighbour.value] == None: #creare neighbour first
                     newneighbour = Node(neighbour.value)
                     cloneGraph[neighbour.value] = newneighbour #set this new neigbour
                cloneGraph[origNode.value].neighbors.append(cloneGraph[neighbour.value] )
                #if this new neigbour is not in visisted add it to queue
                if not visited[neighbour.value]:
                    queue.append(neighbour)


    return head


def detectCycle(node, n):
    pass

# Example usage:
# Create the graph:
# node 1 -> [2, 4]
# node 2 -> [1, 3]
# node 3 -> [2, 4]
# node 4 -> [1, 3]
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph
n=4
cloned_graph = cloneGraph(node1,n)


# Print the original and cloned graphs
print("Original Graph:")
print_graph(node1)

print("\nCloned Graph:")

print_graph(cloned_graph)
