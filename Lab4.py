d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
#1
key = input()
for i in d:
    if i == key:
        print(d[i])
#2
val = input()
for k in d.keys():
    if d[k] == val:
        print(k)