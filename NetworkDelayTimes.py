from pydoc import visiblename
from queue import PriorityQueue
from collections import deque
import heapq
from collections import OrderedDict


def networkDelayTimes2(times, n, k):
    # Step 1: Create adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))  # edge from u to v with weight w

    # Step 2: Dijkstra's algorithm initialization
    # Distance table: Start with inf for all nodes except the starting node (k)
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0

    # Min-heap (priority queue) to process nodes by the shortest known distance
    pq = [(0, k)]  # (distance, node)

    while pq:
        curr_dist, node = heapq.heappop(pq)

        # Skip if the current distance is already greater than the best known distance
        if curr_dist > dist[node]:
            continue

        # Step 3: Relax the edges
        for neighbor, time in graph[node]:
            new_dist = curr_dist + time
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # Step 4: Find the maximum delay
    max_delay = max(dist.values())

    # If any node is unreachable, the max delay will be inf
    return max_delay if max_delay < float('inf') else -1

def networkDelayTimes( inputGraph, startingNode, numOFNodes ):

    #first create a directed graph with adjacency lists
    outdegree = [[] for i in range(numOFNodes)]

    memory = [ float('inf') for i in range(numOFNodes)] #this is default costs of every node. we will make first node as 0
    #let populate the graph
    #while creating graph make all indexes as zero based. also create edges in both directions
    for edge in inputGraph:
        outdegree[edge[0]-1].append((edge[2], edge[1]-1)) # we are creating a weighted graph we will add delay , number format. this is handy for prority queeu
        outdegree[edge[1] - 1].append((edge[2], edge[0] - 1))

    #this starting delay at node 3. we will push node 3 on queue and will do BFS . in end if visited is equal to   numOFNodes we are good otherwise we will return -1
    #for queue will use prority queeu
    queue = PriorityQueue()
    memory[startingNode]=0 #make starting point as 0
    #push node k which is n-1 index in outdegree
    for weightedEdge in outdegree[startingNode]:
        queue.put(weightedEdge)
    #now let start BFS
    while queue.qsize() > 0:
        size = queue.qsize()
        for _ in range(size):
            weightedEdge = queue.get()
            #we will also update memory with best we can do for this node. this will be handy to decide if we want to visit it again

            edgeDelay =   weightedEdge[0]
            if edgeDelay >= memory[weightedEdge[1]]:
                continue #skip the node
            else:
                memory[weightedEdge[1]] = edgeDelay  # this best weight we got for this vissted node
            #now retrieve child elements
            edges = outdegree[weightedEdge[1]]
            # for each edge first check if node is not already viisted before. if that is case push it to queue with delay = parent delay + edge delay
            for edge in edges:
                    weight = edgeDelay + edge[0]
                     #once we visit this node again from queue we will reset its memory weight as well
                    if  memory[edge[1]] > weight: #if current weight is more than new weight
                        queue.put((weight, edge[1]))
                        memory[edge[1]] = weight #it is new weight


    maxDelay = max(memory)
    if maxDelay >= float('inf'):
        return -1
    else:
        return maxDelay




def main():
    times = [[3, 1, 1], [2, 3, 1], [2, 4, 1]]
    n=4 #total num of nodes
    k=3 #starting node
    delayTime = networkDelayTimes(times,  k-1, n)
    print("delay time we have " + str(delayTime))

    # Test cases
    times1 = [
        (2, 1, 1),
        (2, 3, 1),
        (3, 4, 1)
    ]
    n1 = 4
    k1 = 2
    print(networkDelayTimes(times1,  k1-1, n1))  # Output: 2

    times2 = [
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 1),
        (3, 4, 1)
    ]
    n2 = 4
    k2 = 1
    print(networkDelayTimes(times2,  k2-2, n2))  # Output: 3

    times3 = [
        (1, 2, 1),
        (2, 3, 1)
    ]
    n3 = 4
    k3 = 1
    print(networkDelayTimes(times3,  k3-1, n3))  # Output: -1

    times4 = [
        (1, 2, 5),
        (1, 3, 2),
        (2, 3, 1),
        (3, 4, 3),
        (2, 4, 10)
    ]
    n4 = 4
    k4 = 1
    print(networkDelayTimes(times4,  k4-1, n4))  # Output: 5

    times5 = []
    n5 = 1
    k5 = 1
    print(networkDelayTimes(times5,  k5-1, n5))  # Output: 0



main()