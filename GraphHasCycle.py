from collections import deque


def hasCycleUndirected(graph, nodes):
    # first creates outlet map ajdajacency list from given arguemnets
    outlets = [set() for i in range(nodes)]
    for edge in graph:
        outlets[edge[0]].add(edge[1])

    #now we have graph. let start bfs. we will need queue and
    queue = deque([])
    visited = [False] * nodes
    numOfComp=0
    cycle=False
    for i in range(nodes):
        if not visited[i]:
            queue.append(i)
            numOfComp = numOfComp + 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                visited[node] = True

                for outlet in list(outlets[node]):
                    if  visited[outlet] == True and node  not in outlets[outlet]: #not a direct child
                        cycle = True
                        break
                    if  visited[node] == False:
                        queue.append(outlet)

    if not cycle and  numOfComp==1:
        return True
    else:
        return False

def main():
    # Test Case 1: Undirected Graph with a cycle
    graph1 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]
    }
    n1 = 4
    print(hasCycleUndirected(graph1, n1))  # Expected Output: True (cycle exists)

    # Test Case 2: Undirected Graph without a cycle
    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1]
    }
    n2 = 3
    print(hasCycleUndirected(graph2, n2))
main()