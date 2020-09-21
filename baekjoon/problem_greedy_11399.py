N= int(input())
K=list(map(int(input().split()))

num=0
K.sort()
for i in range(N):
  for j in range(i+1):
    num+= K[j]

print(num)
