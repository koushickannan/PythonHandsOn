def find_second_largest(lst):
    first, second = float('-inf'), float('-inf')
    for num in lst:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second


my_nums = [2789, 348, 3109, 3459,2598, 9]
second_largest = find_second_largest(my_nums)
print("second largest number is, ", second_largest)
