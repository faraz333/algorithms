def maxProductSubaray(nums):

    minProduct= nums[0]
    maxProduct = nums[0]
    result = nums[0]


    for i in range(1, len(nums)):
        current= nums[i]
        if current < 0: #if it is negative, min and max are swapped
            #swap max and min due to neg sign
            minProduct, maxProduct= maxProduct, minProduct #swap

        minProduct = min(current, current * minProduct)
        maxProduct = max(current, current * maxProduct)

        result = max( current, maxProduct)


    return  result

def main():
    nums = [2, 3, -2, 4]
    print("max product subarray has value  " + str(maxProductSubaray(nums)))
    nums = [-2, 0, -1]
    print("max product subarray has value  " + str(maxProductSubaray(nums)))
    nums = [1, 2, 3, 4]
    print("max product subarray has value  " + str(maxProductSubaray(nums)))
    nums = [-1, -3, -10, 0, 60]
    print("max product subarray has value  " + str(maxProductSubaray(nums)))

main()