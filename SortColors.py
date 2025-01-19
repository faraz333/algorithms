def sortColors(nums):
    #we will use partitioning approcah.
    # we need zeroPointer which will map to position of
    #we need 2 pointer which will map to position to 2
    #first we will find number of 0 in n times and our nonZeroPointer will point to that
    #we will have something like [0,0,2,2,1,1]
    # than we will count number of
    #we will first count number of zero, 1 and 2 and than set start pointers. we will
    #We can just rewrite original array. this will take
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return  nums

def main():
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),  # Standard test case
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),  # Already sorted
        ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),  # All elements are the same (2s)
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),  # All elements are the same (0s)
        ([1, 1, 1, 1], [1, 1, 1, 1]),  # All elements are the same (1s)
        ([2, 0, 1], [0, 1, 2]),  # Three elements out of order
        ([0, 1, 2], [0, 1, 2]),  # Already sorted (small array)
        ([2, 1, 0], [0, 1, 2]),  # Reverse order
        ([0], [0]),  # Single element (0)
        ([1], [1]),  # Single element (1)
        ([2], [2]),  # Single element (2)
        ([0, 1, 2, 0, 1, 2, 0], [0, 0, 0, 1, 1, 2, 2])  # More repetitions
    ]

    for nums, expected in test_cases:
        result = sortColors(nums)
        assert result == expected, f"Test failed for {nums}: expected {expected}, got {result}"
main()