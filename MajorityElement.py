def majorityElement(nums):
    counter=0
    majElement=None #let make 0 index
    for i in range(0, len(nums)):
        if counter == 0:
            majElement= nums[i]
        if nums[i] !=  majElement:
            counter = counter-1
        else:
            counter=counter+1

    if (nums.count(majElement) < (len(nums)/2) ):
        print("we have problem. there is no majority element ")
        majElement=None
    return  majElement

def main():
    # Test cases
    test_cases = [
        ([3, 2, 3], 3),  # Majority element exists
        ([1, 2, 3, 4], None),  # No majority element
        ([2, 2, 1, 1, 2], 2),  # Majority element is 2
        ([1], 1),  # Single element (majority)
        ([5, 5, 5, 5, 5], 5),  # All elements are the same
        ([10, 10, 20], 10),  # Majority element is 10
        ([1, 2, 2, 3, 3, 3, 3], 3),  # Majority element is 3
    ]

    # Run test cases
    for nums, expected in test_cases:
        result = majorityElement(nums)
        assert result == expected, f"Test failed for {nums}: expected {expected}, got {result}"

    print("All test cases passed.")

main()