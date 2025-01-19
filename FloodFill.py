from collections import deque

from collections import deque
import heapq
from collections import OrderedDict
from collections import UserDict

def getNeigbours(row,col, image) -> list[(int,int)]:

    neighbourList = []
    rows=len(image)
    cols = len(image[0])
    if row+1 < rows and image[row][col] == image[row+1][col]: #we can check for right neigbhour
        neighbourList.append((row+1, col))
    if row-1 >= 0 and image[row][col] == image[row-1][col]: #we can check for right neigbhour
        neighbourList.append((row-1, col))
    if col+1 < cols and image[row][col] == image[row][col+1]: #we can check for right neigbhour
        neighbourList.append((row, col+1))
    if col-1 >= 0 and image[row][col] == image[row][col-1]: #we can check for right neigbhour
        neighbourList.append((row, col-1))

    return  neighbourList

def flood_fill(image, sr, sc, color):
    rows=len(image)
    cols=len(image[0])
    visited= [ [False for j in range(cols)] for i in range(rows) ]   #we dont want to visit a cell twice
    queue = deque()
    #first change color of source pixel
    # we will also use visited to update color in end
    #push it to queue
    queue.append((sr,sc)) #/push the tuple to queue

    while (queue):
        size= len(queue)
        for i in range(size):
            (x,y) = queue.popleft()
            visited[x][y]=True
            neighbours = getNeigbours(x,y ,image)
            for neighbour in neighbours:
                 #fill color
                 if not visited[neighbour[0]][neighbour[1]]:
                     #append it to queue
                     queue.append(neighbour)

    for row in rows:
        for col in cols:
            if visited[rows][cols]==True:
                image[rows][cols]=color

    return image

def main():

    # Example usage:
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr, sc = 1, 1  # Starting position
    new_color = 2  # New color to fill

    # Perform flood fill
    result = flood_fill(image, sr, sc, new_color)

    # Output the modified image
    print("Modified Image after Flood Fill:")
    for row in result:
        print(row)
main()