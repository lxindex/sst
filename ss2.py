import sys
line1=sys.stdin.readline().strip()
line2=sys.stdin.readline().strip()
num1=len(line1)
num2=len(line2)
i=0
l=[]
for i in range(num1//8):
    l.append(''.join(line1[i*8:(i+1)*8]))
s=''.join(line1[-(num1%8):])
for i in range(8-num1%8):
    s=s+'0'
for i in range(num2//8):
    l.append(''.join(line2[i*8:(i+1)*8]))
s=''.join(line2[-(num2%8):])
for i in range(8-num2%8):
    s=s+'0'
l.append(s)
print(l)
