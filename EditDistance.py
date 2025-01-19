def minDistance(s1, s2):

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    #first init a memory of size m+1 n+1
    n= len(s1) # this is our row in memory grid
    m=len(s2)  #this is our column in memory grid
    memory = [[0 for j in range(0, m+1) ] for i in range (0, n+1)] #first element is null string for both s1 and s2

    #let add a comparasion with null string for both s1 and s2 like how many edits (inserts) we will need to convert null string into S1

    #remember s1 is rows
    for i in range(1, n+1):
        memory[i][0]=i #row is changing but col is same 0

    for j in range(1, m+1):
        memory[0][j]=j #col is changing but row is same 0

    for i in range(1, n+1): #rows
        for j in range(1, m+1): #columns
            if s1[i-1] == s2[j-1]: # to match indexes as
               memory[i][j] = memory[i-1][j-1] #just pluck value from previous diagonal position
            else:
                memory[i][j] = min (memory[i-1][j] +1, memory[i][j-1]+1,memory[i-1][j-1]+1 )

    #in end we will return from final position
    return memory[n][m]

def main():
    print(minDistance("faraz", "waseem"))  # Expected output: 0
    print(minDistance("waseem", "faraz"))  # Expected output: 0
    print(minDistance("faraz", "faraz"))
    print(minDistance("abc", "abcd"))  # Expected output: 1
    print(minDistance("abcd", "abc"))  # Expected output: 1
    print(minDistance("kitten", "sitting"))  # Expected output: 3
    print(minDistance("flaw", "lawn"))  # Expected output: 2
    print(minDistance("abc", "xyz"))  # Expected output: 3
    print(minDistance("", "abc"))  # Expected output: 3
    print(minDistance("abc", ""))  # Expected output: 3
    print(minDistance("horse", "ros"))  # Expected output: 3
    print(minDistance("abc", "ABC"))  # Expected output: 3

main()