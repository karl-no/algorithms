def find_duplicate(nums):
    nums.sort()
    for n in nums:
        if type(n) != int or n < 0 or len(nums) < 2:
            return False

    for n in range(len(nums) - 1):
        if nums[n] == nums[n + 1]:
            return nums[n]

    return False
