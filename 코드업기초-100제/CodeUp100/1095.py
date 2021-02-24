n = int(input()) #출석 번호
numlist = map(int, input().split()) # 무작위로 부른 번호 

print(min(numlist))

# 또 다른 답안

# n = int(input())
# list = input().split()

# min = int(list[0])
# for i in range(1, n):
#     if min > int(list[i]):
#         min = int(list[i])
#     else:
#         i += 1

# print(min);