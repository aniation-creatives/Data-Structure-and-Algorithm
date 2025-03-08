def shortest_sum(nums, target, memo = {}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    shortest_nums = None

    for num in nums:
        remainder = target - num
        remainder_result = shortest_sum(nums, remainder)
        if remainder_result != None:
            remainder_result = remainder_result + [num]
            if shortest_nums == None or (len(remainder_result) < len(shortest_nums)):
                shortest_nums = remainder_result

    memo[target] = shortest_nums
    return shortest_nums


nums = [2, 3, 5, 6]
target = 800
print(shortest_sum(nums, target))