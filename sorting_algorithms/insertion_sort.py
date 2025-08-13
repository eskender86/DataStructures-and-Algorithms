def insertion_sort(nums):
    i = 0
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            prevEl = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = prevEl
            j -= 1
        i += 1

    return nums