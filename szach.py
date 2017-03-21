n = 5

print("Maximize")
f = ''
for x in range(ord('a'),ord('a') + n):
    for y in range(1, n + 1):
        f += (chr(x) + str(y))
        if y < n:
            f += ('+')
    if x < (ord('a') + n - 1):
        f += ('+')
print(f)
print(' ')

print("Subject To")
for x in range(ord('a'),ord('a') + n):
    f = ''
    for y in range(1, n + 1):
        f += (chr(x) + str(y))
        if y < n:
            f += ('+')
    print(f + ('<=1'))
       

for y in range(1, n + 1):
    f = ''
    for x in range(ord('a'),ord('a') + n):
        f += (chr(x) + str(y))
        if x < (ord('a')+ n - 1):
            f += ('+')
    print(f + ('<=1'))


for j in range(1, n):
    f = ''
    for i in range(1, n + 1):
        if (i + j - 1) <= n:
            f += (chr(ord('a') + i - 1) + str( i + j - 1))
        if (i + j - 1) < n:
            f += ('+')
    print(f + ('<=1'))
    
for j in range(2, n):
    f = ''
    for i in range(1, n + 1):
        if (i + j - 1) <= n:
            f += (chr(ord('a') + i + j - 2) + str(i))
        if (i + j - 1) < n:
            f += ('+')
    print(f + ('<=1'))
    
    
for j in range(1, n):
    f = ''
    for i in range(1, n + 1):
        if (i + j - 1) <= n:
            f += (chr(ord('a') + n - i) + str(i + j - 1))
        if (i + j - 1) < n:
            f += ('+')
    print(f + ('<=1'))

for j in range(2, n):
    f = ''
    for i in range(1, n + 1):
        if (i + j - 1) <= n:
            f += (chr(ord('a') + n - (i + j - 1)) + str(i))
        if (i + j - 1) < n:
            f += ('+')
    print(f + ('<=1'))

print(' ')
print("Bounds")
for x in range(ord('a'),ord('a') + n):
    for y in range(1, n + 1):
        print(('0<=') + (chr(x) + str(y)) + ('<=1'))
        
print(' ')
print("Generals")
for x in range(ord('a'),ord('a') + n):
    for y in range(1, n + 1):
        print(chr(x) + str(y))
        
print(' ')
print("End")