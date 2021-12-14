n = int(input())
a = []

for i in range(1, n + 1):
    for i1 in range(1, n + 1):
        if i * i1 == n and i not in a and i1 not in a:
            a.append(i)
            print(i1, i)

            
            
            
            
from math import gcd


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# counter
h = gcd(abs(x2 - x1), abs(y2 - y1))
dx = (x2 - x1) / h
dy = (y2 - y1) / h

count = 0
for i in range(1, h):
    count += 1 if (x1 + dx * i) % 1 == 0 and (y1 + dy * i) % 1 == 0 else 0
print(count + 2)




symb = input()
sqr = int(input())

for i in range(1, sqr + 1):
    for i1 in range(1, sqr + 1):
        print(symb, end=' ') if i == i1 or i + i1 - 1 == sqr else print(' ', end=' ')
    print()
