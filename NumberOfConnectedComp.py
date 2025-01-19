from collections import deque


def number_of_connected_components(graph, nodes):
    #do a bfs ans dfs and cons=ume al connected nodes
    #total number of times we do search is number of connected componenets
    compNumber=0
    queue = deque()
    #start from node 0
    visited = [False] * nodes
    #first create an outlet map
    outlets = [[] for  i in range(nodes)]

    for edge in graph:
        outlets[edge[0]].append(edge[1])

    for index in range(nodes):
        if not visited[index]:
            queue.append(index)
            compNumber = compNumber + 1 #for one queue we will do DFS
        while queue:
            size = len(queue)
            for i in range(size):
                nodeIndex=  queue.popleft()
                visited[nodeIndex] = True

                for outlet in outlets[nodeIndex]:
                    if visited[outlet] == False:
                        queue.append(outlet)
    #start from any node and we will do BDF untill we visit all nodes
    return compNumber
def main():
    n = 3
    edges = [[0, 1], [0, 2]]
    number = number_of_connected_components(edges, n)
    print("number of connected components: {}".format(number))
    n = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
    number = number_of_connected_components(edges, n)
    print("number of connected components: {}".format(number))
main()