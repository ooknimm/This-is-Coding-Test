n = int(input())



array = [0] * 1001


""" 1칸일 때, 2칸일 떄 경우의 수를 입력해놓고 시작한다.
    왼쪽씩 채워가면서 최적해를 구하는 방향이다.
    바로 전 최적해(한칸)에 전전번 최적해(두칸) * 2(좌우배치를 고려)를 하면 된다.
"""

array[1] = 1
array[2] = 3
for i in range(3, n+1):
    array[i] = array[i-1] + array[i-2] * 2 % 796796

print(array[i])
