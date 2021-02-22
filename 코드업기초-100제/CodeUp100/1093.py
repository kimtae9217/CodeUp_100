n = int(input()) #출석 번호
a = input().split() # 무작위로 부른 번호 

# 0값이 담긴 24개의 배열 선언
ls = []
for i in range(24):
    ls.append(0)

for i in range(n):
    ls[int(a[i])] += 1 # int(a[0]) = ls[1] = 0  즉, a[i]번째에 해당하는 수를 +1 씩 증가
                      

for i in range(1, 24): #한 칸씩 띄우고 출력
    print(ls[i], end=" ")
    