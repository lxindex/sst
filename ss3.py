import sys
n=int(sys.stdin.readline().strip())
while n!=1:
    i=2
    for i in range(2,n+1):
        if n%i==0:
            n=n//i
            print(i)
            break
