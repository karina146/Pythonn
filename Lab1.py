#1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
maximum = 0
minimum = 0
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c


n = int(input("Введите натуральное число n: "))
#2.1
for i in range(n, 0, -1):
    d = ''
    for j in range(1, i + 1):
        d += str(j)
    print(d)

#2.2
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    leftpart = ""
    for j in range(i, 0, -1):
        leftpart += str(j)
    rightpart = ""
    for j in range(2, i + 1):
        rightpart += str(j)
    string = leftpart + rightpart
    print(spaces + string)
#3
triangle = [[1]]
    
for i in range(1, n):
    row = [1]
    for j in range(len(triangle[i - 1]) - 1):
        row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
    row.append(1)
    triangle.append(row)
    
for i in triangle:
    d = ''
    for j in i:
        d += str(j) + ' '
    print(' '*(len(triangle) - len(i)) + d)
