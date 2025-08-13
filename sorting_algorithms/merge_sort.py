def merge_sort(nums):
    count = len(nums)
    
    if count < 2:
        return nums

    half = count//2

    sorted_left_side = merge_sort(nums[0:half])
    sorted_right_side = merge_sort(nums[half:])
    
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    i=0
    j=0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    final.extend(first[i:])
    final.extend(second[j:])
    
    return final