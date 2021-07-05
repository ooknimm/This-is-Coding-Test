import sys

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))


""" 1번 풀이
    단순한 방식의 풀이이다.
    i가 2이하일 때는 기존 값을 저장한다.
    두 칸 전 array 범위의 max값과 현재 값을 더해 저장한다.
    각 칸마다의 최적해가 저장되는 셈이다.
    그리고 최종 리스트의 max 값이 문제의 답이 된다.
"""
d = [0] * 100
for i in range(n):
    if i < 2:
        d[i] = array[i]
    else:
        d[i] = max(d[:i-1]) + array[i]

print(max(d))


""" 2번 풀이
    더 효율적인 풀이이다.
    각 index에 현재 최대 값을 담는다.
    그러면 위의 풀이처럼 범위를 잡아 max를 구할 필요가 없다.
    한 칸 전과 (두 칸 전 + 현재 값)만 비교하면 된다.
    1번 인덱스에 값을 지정할 때 유의해야한다.
    0번과 1번중 max값을 넣어야 풀이가 가능해진다.
"""
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])
print(d[n-1])



