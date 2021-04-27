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
        while left <= hi and arr[left] <= arr[pivot]:
            left += 1
        while lo < right and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return right

def quick_sort(arr, lo, hi):
    
    if lo < hi:
        print(lo, hi)
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot-1)
        quick_sort(arr, pivot+1, hi)  
        return arr

print(quick_sort(arr_3, 0, len(arr_3)-1))