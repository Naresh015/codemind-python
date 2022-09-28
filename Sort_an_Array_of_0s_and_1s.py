n=int(input())
b=list(map(int,input().split()))
b.sort()
for i in range(n):
    print(b[i],end=' ')