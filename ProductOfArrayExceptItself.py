def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n  # Initialize the output array to 1

    # Left pass: Calculate the product of elements to the left of each index
    left_product = 1
    for i in range(n):
        output[i] = left_product  # Set the left product for the current index
        left_product *= nums[i]  # Update the left product for the next index

    # Right pass: Calculate the product of elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product  # Multiply the current output value by the right product
        right_product *= nums[i]  # Update the right product for the next index

    return output


def main():
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))  # Output: [0, 12, 0, 0]
    nums = [1, 2, 3, 6]
    print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]

main()