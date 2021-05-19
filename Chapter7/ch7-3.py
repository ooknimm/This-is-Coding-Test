import sys

n, m = map(int, input().split())
ricecake_array = list(map(int, sys.stdin.readline().rstrip().split()))

max_h = max(ricecake_array)
h_array = [i for i in range(max_h+1)]

def h_calculator(r_array, h):
    total = 0
    for i in r_array:
        if h < i:
            total += i - h
    return total

def binary_search(array, ricecake_array, m):
    if len(array) > 1:
        mid = len(array) // 2
        h = h_calculator(ricecake_array, array[mid])
        if h == m:
            return array[mid]
        elif h < m:
            return binary_search(array[:mid], ricecake_array, m)
        else:
            return binary_search(array[mid:], ricecake_array, m)

print(binary_search(h_array, ricecake_array, m))


def binary_search_2(array, ricecake_array, m):
    start = 0
    end = max(array)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for a in ricecake_array:
            if a > mid:
                total += a - mid
        
        if total == m:
            return mid

        elif total < m:
            end = mid - 1
        else:
            start = mid + 1
        
print(binary_search_2(h_array, ricecake_array, m))
