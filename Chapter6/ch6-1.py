arr = [0,5,9,7,3,1,6,2,4,8]

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr

print(selection_sort(arr))


arr_2 = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        #i부터 0까지 -1씩 감소
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

print(insertion_sort(arr_2))


arr_3 = [5,7,9,0,3,1,6,2,4,8]

def partition(arr, lo, hi):
    pivot = lo
    left = lo + 1
    right = hi
    while left <= right:
        while left <= hi and arr[left] < arr[pivot]:
            left += 1
        while right > lo and arr[right] > arr[pivot]:
            right -= 1
        
        if right <= left:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    return right

def quick_sort_left_pivot(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort_left_pivot(arr, lo, pivot-1)
        quick_sort_left_pivot(arr, pivot+1, hi)
        return arr

print(quick_sort_left_pivot(arr_3, 0, len(arr_3)-1))


arr_4 = [4,9,7,2,3,0,5,1,6,8]

def quick_sort_right_pivot(arr, lo, hi):
    if lo < hi:
        pivot = hi
        left = lo
        for right in range(lo, hi):
            if arr[pivot] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[pivot], arr[left] = arr[left], arr[pivot]
        pivot = left

        quick_sort_right_pivot(arr, pivot+1, hi)
        quick_sort_right_pivot(arr, lo, pivot-1)

        return arr

print(quick_sort_right_pivot(arr_4, 0, len(arr_4)-1))


arr_5 = [4,9,7,2,3,0,5,1,6,8]

def quick_sort_mid_pivot(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    left = []
    right = []

    for i in range(len(arr)):
        if pivot > arr[i]:
            left.append(arr[i])
        elif pivot < arr[i]:
            right.append(arr[i])
    
    left_result = quick_sort_mid_pivot(left)
    right_result = quick_sort_mid_pivot(right)

    return left_result + [pivot] +  right_result


print(quick_sort_mid_pivot(arr_5))


arr_6 = [4,9,7,2,3,0,5,1,6,8]

def merge(left_arr, right_arr):
    result = []
    while right_arr or left_arr:
        while right_arr and left_arr:
            right = right_arr[0]
            left = left_arr[0]
            if right < left:
                result.append(right)
                right_arr = right_arr[1:]
            else:
                result.append(left)
                left_arr = left_arr[1:]
        while right_arr:
            right = right_arr[0]
            result.append(right)
            right_arr = right_arr[1:]
        while left_arr:
            left = left_arr[0]
            result.append(left)
            left_arr = left_arr[1:]

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    # 분할의 기준이 될 가운데 인덱스
    mid = len(arr) // 2

    # 분할
    right_arr = merge_sort(arr[:mid])
    left_arr = merge_sort(arr[mid:])

    # 정복
    result = merge(left_arr, right_arr)

    return result

print(merge_sort(arr_6))


arr_7 = [4,9,7,2,3,0,5,1,6,8]

def merge_sort_2(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = merge_sort_2(arr[:mid])
        right_arr = merge_sort_2(arr[mid:])

        lo, hi = 0, 0
        i = 0
        while len(left_arr) > lo and len(right_arr) > hi:
            if left_arr[lo] > right_arr[hi]:
                arr[i] = right_arr[hi]
                hi += 1
                i += 1
            else:
                arr[i] = left_arr[lo]
                lo += 1
                i += 1
        while len(left_arr) > lo:
            arr[i] = left_arr[lo]
            lo += 1
            i += 1
        while len(right_arr) > hi:
            arr[i] = right_arr[hi]
            hi += 1
            i += 1
        
    return arr

print(merge_sort_2(arr_7))


arr_8 = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def counting_sort(arr):
    count = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1
    
    result = []
    for i in range(len(count)):
        for _ in range(count[i]):
            result.append(i)

    return result

print(counting_sort(arr_8))