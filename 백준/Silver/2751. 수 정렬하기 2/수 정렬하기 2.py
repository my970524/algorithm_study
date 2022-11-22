n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

def merge(list1, list2):
    i, j = 0, 0
    result = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

def merge_sort(nums, start_i, end_i):
    if start_i < end_i:
        mid_i = (start_i+end_i) // 2
        list1 = merge_sort(nums, start_i, mid_i)
        list2 = merge_sort(nums, mid_i+1, end_i)
        return merge(list1, list2)
    else:
        return nums[start_i:start_i+1]

sorted_nums = merge_sort(nums, 0, n-1)

for num in sorted_nums:
    print(num)