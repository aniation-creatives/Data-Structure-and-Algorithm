'''
def how_sum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        remainder = target - num
        remainder_result = how_sum(remainder, nums, memo)
        if remainder_result != None:
            memo[target] = remainder_result + [num]
            return memo[target]
    memo[target] = None
    return memo[target]
'''

def is_subset_sum(nums, target, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for i in range(len(nums)):
        remainder = target - nums[i]
        popped_element = nums.pop(i)
        remainder_result = is_subset_sum(nums, remainder, memo)
        nums.insert(i, popped_element)
        if remainder_result:
            memo[remainder] = True
            return True

    memo[target] = False
    return False


nums = [4, 0, 40, 56, 77, 92, 3, 57, 91, 58, 40, 6, 89, 33, 60, 35, 65, 86, 98, 17, 92, 99, 74, 14, 12, 38, 18, 27, 1,
        94, 40, 31, 18, 5, 37, 23, 76, 86, 73, 71, 70, 12, 26, 96, 40, 61, 58, 88, 66, 87, 72, 47, 11, 10, 27, 89, 15,
        80, 43, 45, 44, 17, 42, 38, 7, 27, 68, 90, 89, 69, 72, 77, 98, 40, 27, 70, 77, 85, 80, 11, 7, 75, 48, 27, 43,
        44, 8, 19, 38, 84, 86, 5, 48, 57, 9, 44, 93]
target = 3848
print(is_subset_sum(nums, target))