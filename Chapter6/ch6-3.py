n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))


def merge(arr, left_arr, right_arr):
    lo, hi = 0, 0
    i = 0

    while lo < len(left_arr) and hi < len(right_arr):
        if left_arr[lo] <= right_arr[hi]:
            arr[i] = left_arr[lo]
            i += 1
            lo += 1
        else:
            arr[i] = right_arr[hi]
            i += 1
            hi += 1
    while lo < len(left_arr):
        arr[i] = left_arr[lo]
        i += 1
        lo += 1
    while hi < len(right_arr):
        arr[i] = right_arr[hi]
        i += 1
        hi += 1
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    arr = merge(arr, left_arr, right_arr)
    return arr


def partition(arr, lo, hi):
    pivot = lo
    left = lo + 1
    right = hi

    while left <= right:
        while left <= hi and arr[left] >= arr[pivot]:
            left += 1
        while right > lo and arr[right] < arr[pivot]:
            right -= 1
        if left >= right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return right

def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot-1)
        quick_sort(arr, pivot+1, hi)
        return arr

def swap_list(arr_a, arr_b, k):
    sort_arr_a = merge_sort(arr_a)
    sort_arr_b = quick_sort(arr_b, 0, len(arr_b)-1)

    for i in range(k):
        if sort_arr_a[i] < sort_arr_b[i]:
            sort_arr_a[i], sort_arr_b[i] = sort_arr_b[i], sort_arr_a[i]
        else:
            break

    return sort_arr_a

print(sum(swap_list(arr_a, arr_b, k)))


