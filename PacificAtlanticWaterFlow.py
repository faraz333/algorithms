def pacificAtlanticWaterFlow(grid):
    #we will create two matrix, one for atantic flow and one for pacific flow
    #we will find intersection of these matrices to find cells which are reachable from both
    #for each we know corner are reachble to pacific ocean or atlantic ocean. We will assign it 1.
    # For rest of cells if they hit any cell with 1 we will mark them as 1 as well
    # will traverse to see if they can hit atlantic or pacific ocean cell block.
    atlantic =  [ [0 for j in range(len(grid[0]))] for i in range(len(grid)) ]
    pacific =  [ [0 for j in range(len(grid[0]))] for i in range(len(grid)) ]

    #now label pacific matrice
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if j == 0:
                pacific[i][j]=1
            if i == 0:
                pacific[i][j] = 1
    print(pacific)
    #now starting from these rows and col start a BFS. if cell is reachable than mark it as 1
    # if call is already 1 than there is no need to push it queue 


def main():
    print("Pacific Atlantic Water Flow matrix 1")

    matrix = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
    print(pacificAtlanticWaterFlow(matrix))
    print("Pacific Atlantic Water Flow matrix 2")
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(pacificAtlanticWaterFlow(matrix))

main()