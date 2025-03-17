#0
numbers = [1,2,3,2,5,4,6]
numbers2 = []
for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
        numbers2.append(numbers[i+1])
print(numbers2)
#1
numbers = [1,2,3,2,5,4,6]
maxi = numbers.index(max(numbers))
mini = numbers.index(min(numbers))
for i in range(len(numbers)):
    if numbers[i] == numbers[maxi] or numbers[i] == numbers[mini]:
        temp = numbers[mini]
        numbers[mini] = numbers[maxi]
        numbers[maxi] = temp
        break
print(numbers)
#2
numbers = [1,2,8,9,3,2,5,4]
numbers2 = [1,2,3,2,5,4,6,7]
c = 0
for i in numbers:
    if i in numbers2:
        c+=1
print(c)
#3
s = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(d[i], end= ' ')