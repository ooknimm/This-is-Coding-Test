n = int(input())

arr = []
for _ in range(n):
    a = input().split()
    arr.append((a[0], int(a[1])))


def partition(arr, lo, hi):
    pivot = lo
    left = lo + 1
    right = hi
    while left <= right:
        print(left, right)
        while left < hi and arr[left][1] >= arr[pivot][1]:
            if arr[left][1] == arr[pivot][1] and arr[left][0] > arr[pivot][0]:
                break
            left += 1
        while right > lo and arr[right][1] <= arr[pivot][1]:
            if arr[right][1] == arr[pivot][1] and arr[right][0] < arr[pivot][0]:
                break
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

print(quick_sort(arr, 0, len(arr)-1))