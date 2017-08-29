import sys
n=sys.stdin.readline().strip()
s=float(n)
i=int(s)
print(i if s-i<0.5 else i+1)
