def merge_sort(nums):
    if len(nums)< 2:
        return nums
    first = nums[: len(nums)// 2]
    second = nums[len(nums) // 2:]
    left_sorted = merge_sort(first)
    right_sorted = merge_sort(second)
    sorted_merged = merge(left_sorted, right_sorted)
    return sorted_merged

def merge(first, second):
    final = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    while i < len(first):
        final.append(first[i])
        i += 1

    while j < len(second):
        final.append(second[j])
        j += 1

    return final
