n = int(input()) #출석 번호
numlist = input().split() # 무작위로 부른 번호 

numlist.reverse()

for i in range(0, n):
    print(numlist[i], end=" ")


# 또 다른 풀이
# arr = []

# a = input()
# b = input().split()

# n =int(a)
# for i in range(n):
#     arr.append(int(b[i]))

# i = n-1
# while i >= 0:
#     print(arr[i], end=" ")
#     i -= 1
