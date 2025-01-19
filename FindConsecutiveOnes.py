def findConswecutiveOnes(array):
    max1=0
    counter1=0
    for i in range (0, len(array)):
        if array[i] ==1:
            counter1 =counter1+1
            if counter1 > max1:
                max1=counter1
        else:
            counter1=0 #reset counter
    return  max1

def main():
    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]
    print(findConswecutiveOnes(arr))
    arr = [1, 0, 1, 0, 1,1, 0, 1]
    print(findConswecutiveOnes(arr))  # Output: 1

main()