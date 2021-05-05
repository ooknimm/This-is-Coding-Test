n = int(input())

arr = []
[arr.append(int(input())) for _ in range(n)]




def partition(arr, lo, hi):
    pivot = hi
    left = lo
    for right in range(lo, hi):
        if arr[right] > arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    arr[left], arr[pivot] = arr[pivot], arr[left]
    return left

def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot-1)
        quick_sort(arr, pivot+1, hi)
        return arr

print(quick_sort(arr, 0, len(arr)-1))
