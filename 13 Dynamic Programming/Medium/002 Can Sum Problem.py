count = 0
# def can_sum(target, nums, count = 0):
def can_sum(target, nums, memo = {}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        remainder = target - num
        if can_sum(remainder, nums, memo):
            memo[remainder] = True
            return True
        # if can_sum(remainder, nums, count):
            # count += 1
    # return count
    return False

target = 700
nums = [5, 3, 4, 7]
print(can_sum(target, nums))