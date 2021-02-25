n = int(input())
location=[]

for i in range(20):
    location.append([])
    for j in range(20):
        location[i].append(0)
for i in range(n):
    x, y = map(int, input().split())
    location[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(location[i][j], end=" ")
    
    print("")