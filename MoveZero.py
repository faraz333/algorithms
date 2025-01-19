def moveZeroes(nums):
    #use two pointer solution
    nonZeroIndex=0 # left pointer
    #iterate through array and if we encounter non zero, move it to nonZeroIndex and increament it
    #once we done, we will fill rest of array from nonZeroIndex to end

    for i in range (0, len(nums)):
        if nums[i] !=0:
            nums[nonZeroIndex]= nums[i]
            nonZeroIndex = nonZeroIndex +1
    #now fill 0 in rest of array
    for j in range (nonZeroIndex, len(nums)):
        nums[j]=0

    return nums

def main():
    test_cases = [
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),
        ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        ([1, 0], [1, 0]),
        ([0, 0, 0, 1, 2, 3], [1, 2, 3, 0, 0, 0]),
        ([-1, 0, 2, 0, 3], [-1, 2, 3, 0, 0]),
        ([0], [0]),
        ([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]),
        ([0, -1, 2, 0, 3, 4, 0], [-1, 2, 3, 4, 0, 0, 0]),
        ([1, 0, 0, 0], [1, 0, 0, 0]),
    ]

    for nums, expected in test_cases:
        result = moveZeroes(nums)
        print(f"Input: {nums}\nExpected: {expected}\nResult: {result}\n{'-' * 40}")

main()