a, b = map(int, input().split())
if a == 0 and b == 0:
    print(1)
else:
    print(0)

#또 다른 풀이
# a, b = map(int, input().split())
# print(int(not(a|b)))