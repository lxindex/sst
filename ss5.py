import sys
import collections
'''
4
1 2
3 4
2 4
3 5
'''
from collections import OrderedDict
def getkey(x):
    return x[0]
n=int(sys.stdin.readline().strip())
l=OrderedDict()
for i in range(n):
    line=list(map(int,sys.stdin.readline().strip().split(' ')))
    if line[0] in l:
        l[line[0]]=l[line[0]]+line[1]
        print('add!')
    else:
        l[line[0]]=line[1]
        print('new')
l2=sorted(list(l.items()),key=getkey)

