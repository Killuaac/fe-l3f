year = int(input())

a = year % 4
b = year % 100
c = year % 400

if a == 0 and b != 0 or c == 0:
    print('YES')
else:
    print('NO')