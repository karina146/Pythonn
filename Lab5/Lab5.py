#1
f = open('input.txt', 'r')
f1 = f.readline().split(' ')
f.close()
c = 1
for i in f1:
    c *= int(i)

d = open('output.txt', 'w')
d.write(str(c))
d.close()
#2
f = open('input2.txt', 'r')
f1 = f.readlines()
f2 = []
for i in f1:
    f2.append(int(i))
f.close()
f2 = sorted(f2)

d = open('output2.txt', 'w')
for i in f2:
    d.write(str(i))
    d.write('\n')
d.close()
#3
f = open('children.txt', 'r')
f1 = f.readlines()
f2 = []
for i in f1:
    f2.append(i)
f.close()

v = []
for i in f2:
    for j in i:
        if j.isdigit():
            v.append(j)
print(v)
maxind = v.index(max(v))
minind = v.index(min(v))
maxchild = f2[maxind]
minchild = f2[minind]
d = open('older.txt', 'w')
d.write(maxchild)
d.close()
w = open('younger.txt', 'w')
w.write(minchild)
w.close()