def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        # for each element, we check if its complement has already been visited
        if complement in num_map:
            # If it has, we have found a pair of elements that add up to that target
            return [num_map[complement], i]

        num_map[num] = i

    return []


nums_array = [2, 3, 4, 5]
print(two_sum(nums_array, 5))
