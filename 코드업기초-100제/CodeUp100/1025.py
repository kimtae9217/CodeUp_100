n = input()
print("[%d]" %(int(n[0]) * 10000))
print("[%d]" %(int(n[1]) * 1000))
print("[%d]" %(int(n[2]) * 100))
print("[%d]" %(int(n[3]) * 10))
print("[%d]" %(int(n[4]) * 1))

# for문을 이용한 풀이
# num = input()
# for i in range(5):
#     print('[',num[i]+"0"*(4-i),']',sep="")