def max_product_subarray(nums):
    n = len(nums)
    max_product = 0
    curr_product = nums[0]

    for i in range(1, n):
        if nums[i] == 0:
            continue
        _temp_product = nums[i] * curr_product
        curr_product = max(curr_product, _temp_product)
        max_product = max(max_product, curr_product)
        print(i, nums[i], _temp_product, curr_product, max_product, sep=" |-----| ")

    return max_product

nums = [-1,4,-4,5,-2,-1,-1,-2,-3]
print(max_product_subarray(nums))