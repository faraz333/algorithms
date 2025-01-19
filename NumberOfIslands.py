from collections import deque
import heapq

def getNeighbors(grid, visited, i, j):
    neighbors = []
    #add its neighbous if they are not visisted and are in range
    if i +1 < len(visited) and grid[i+1][j] and not visited[i+1][j]:
        neighbors.append((i+1,j))
    if j-1 >= 0 and grid[i][j-1] and not visited[i][j-1]:
        neighbors.append((i, j-1))
    if i-1 >= 0 and grid[i-1][j] and not visited[i-1][j]:
        neighbors.append((i-1,j))
    if j+1 < len(visited[0]) and grid[i][j+1] and not visited[i][j+1]:
        neighbors.append((i, j+1))
    return neighbors

def bfs(grid, visited,row,col ):

    queue=deque([(row,col)]) # start with queue with row,col as seed
    while queue:
        size = len(queue)
        for _ in range(size): #extract all entries in current queue
            row, col=queue.popleft()
            #add it to visited
            visited[row][col]=True
            for neighbor in getNeighbors(grid, visited, row, col):
                queue.appendleft(neighbor) #add all noon visited neighbours in queue



def numberOfIslands(grid):

    #first create a matrix to represent is visited state
    numRows= len(grid)
    numCols = len(grid[0])
    islandsVisited = [ [False for i in range(numCols)] for j in range(numRows)]
    print(islandsVisited)
    #here is alo. we will traverse through grid. for every one we will increase the island counter
    #and consume all adjacent blocks and mark them visited. in end we will get number of islands


    numOfIslands=0
    for i in range(numRows):
        for j in range(numCols):
            if grid[i][j] == 1 and not islandsVisited[i][j]: #we have not visited the island
                numOfIslands+=1
                bfs(grid=grid, visited=islandsVisited,row=i, col=j)

    return numOfIslands

def main():
    grid=[
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
    ]
    num = numberOfIslands(grid)
    print("Number of islands we have are " + str(num))

    grid2 = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]
    num = numberOfIslands(grid2)
    print("Number of islands we have are " + str(num))

    grid3 = [
        [1, 1, 1, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1]
    ]
    num = numberOfIslands(grid3)
    print("Number of islands we have are " + str(num))


main()