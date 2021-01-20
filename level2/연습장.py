arr = []
while True:
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        break
    if b % a == 0:
        arr.append('factor')
    elif a % b == 0:
        arr.append('multiple')
    else:
        arr.append('neither')
for i in arr:
    print(i)
