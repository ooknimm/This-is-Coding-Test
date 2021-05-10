import sys

my_n = int(sys.stdin.readline().rstrip())

my_array = list(map(int, sys.stdin.readline().rstrip().split()))

req_n = int(sys.stdin.readline().rstrip())

req_array = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search_recursive(arr, target):
    if len(arr) > 1:
        mid = len(arr) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            return binary_search_recursive(arr[:mid], target)
        else:
            return binary_search_recursive(arr[mid:], target)
    

def answer_recursive(my_array, req_array):
    for n in req_array:
        if binary_search_recursive(my_array, n):
            print('yes', end=' ')
        else:
            print('no', end=' ')


def binary_search_loop(arr, lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

def answer_loop(my_array, req_array):
    for n in req_array:
        if binary_search_loop(my_array, 0, len(my_array)-1, n):
            print('yes', end=' ')
        else:
            print('no', end=' ')




answer_recursive(my_array, req_array)
answer_loop(my_array, req_array)