def maxSumSubarray(nums):

    #boundary conditions

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    maxSum = float('-inf')
    sum = nums[0] #this is best so far first position
    #this is strategy. think of it like sliding window. we need to decide when to keep current sum and when to
    # forget it like make current number as best we have so far. we will keep checking maxSum with current sum

    for i in range(1, len(nums)):
        current=nums[i]
        sum = max(current, sum + current)
        maxSum = max(maxSum, sum)

    return maxSum

def main():
    test_cases = [
        ([2, 3, 4, 5], 14),
        ([-2, -3, -4, -5], -2),
        ([1, -2, 3, 4, -1, 2, 1, -5, 4], 10),
        ([0, 0, 0, 0, 0], 0),
        ([5], 5),
        ([-3], -3),
        ([1, -1, 5, 3, -2, 4], 10),
        ([2, -1, 2, 3, -5, 4], 6),
        ([10, -2, 3, 4, -1, 5, -2, 1], 19),
        ([-2, -3, -4, -1, -5], -1),
        ([0, 0, 3, 0, 5, 0], 8),
        ([1000, -500, 2000, 3000, -1000, 1500, 2500], 8500),
        ([-2, -3, -4, -1, -5], -1),
        ([2, 3, 4, -1, 2, 1], 10),
        ([-1, -2, -3, -4], -1)
    ]

    for nums, expected in test_cases:
        result = maxSumSubarray(nums)
        print(f"Input: {nums}\nExpected: {expected}\nResult: {result}\n{'-' * 40}")

main()
