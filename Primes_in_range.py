

import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if (prime(i)==1 and i!=1):
        c+=1
print(c)