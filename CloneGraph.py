from collections import deque


class Graph:
    def __init__(self,index):
        self.adjacency_list = []  #every node mantains nodes adjacent to it. this is 2 directional graph
        self.index=index




def cloneGraph( node):
    #here is algo. we will use memory table to track which nodes have been created
    # we will move node by node
    memory = {}
    queue = deque([node])
    #also create clone node in memory
    memory[node.index]= Graph(node.index)
    visited = set()

    while queue:
        # retrieve all nodes from memory
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.index not in visited:
                #check if node exist otherwise create it
                if node.index not in memory:
                    memory[node.index] = Graph(node.index) #create node
                visited.add(node.index) #add visisted node
                #now look for its connected nodes
                sublings =node.adjacency_list
                for subling in sublings: #add all sublings to new node
                    if subling.index not in memory: #check if subling has been created
                        memory[subling.index] = Graph(subling.index) #create subling
                    memory[node.index].adjacency_list.append(memory[subling.index])
                    if subling.index not in visited: #if subling is not already visisted add it to visisted list
                        queue.append(subling)



    return memory[node.index]


def printGraphNode(node):

    queue = deque([node])
    visited = set()

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            print("node index > " +  str(node.index))
            visited.add(node.index)
            sublings = node.adjacency_list
            for subling in sublings:
                print("subling index " + str(subling.index))
                if subling.index not in visited:
                    queue.append(subling)


def main():
    node0 = Graph(0)
    node1=Graph(1)
    node2=Graph(2)
    node3=Graph(3)


    node0.adjacency_list={node2, node3,node1}
    node1.adjacency_list={node2, node0,node3}
    node2.adjacency_list={node0,node1}
    node3.adjacency_list={node0, node1}

    clone = cloneGraph(node0) # we can start from any node

    print("printing copy of graph")
    printGraphNode(clone)

main()