def containsDuplicates(nums):
    #sort array if it is not sorted in nlogn time
    nums.sort()
    if len(nums) <=1:
        return False
    for i in range(1, len(nums)):
        if nums[i-1]== nums[i]:
            return True
    return False
def main():
    nums = [1, 2, 3, 3]
    print(containsDuplicates(nums))
    nums = [1, 2, 3, 4]
    print(containsDuplicates(nums))

    nums = [1, 3, 4, 3]
    print(containsDuplicates(nums))


main()