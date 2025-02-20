s = input()
#1
s2 = ''
symbols = []
digits = []
c = 0
for i in s:
    if i not in symbols:
        symbols.append(i)
for i in symbols:
    if s.count(i) == 1:
        s2 += i
    else:
        s2 = s2 + i + str(s.count(i))
print(s2) 
#№1.1
s2 = ''
for i in range(len(s)-1):
    if s[i].isdigit()==False and s[i+1].isdigit() == True:
        s2 = s2 + s[i]*int(s[i+1])
    elif s[i].isdigit()==False and s[i+1].isdigit() == False:
        s2 += s[i]
if not s[-1].isdigit():
    s2 += s[-1]
print(s2)

#№2
s = s.replace(' ', '')

char_count = []
for i in set(s):
    count = s.count(i)
    char_count.append((i, count))

for i in range(len(char_count)-1):
    for j in range(i+1, len(char_count)):
        if char_count[i][1] < char_count[j][1]:
            temp = char_count[i]
            char_count[i] = char_count[j]
            char_count[j] = temp
n = 3
for i in range(n):
    print(char_count[i])

#3
number = int(input())
ones = {
        1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
        6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 0: ''}
teens = {
        10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
        14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать",
        17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
tens = {
        2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
        6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто", 0: ''}
hundreds = {
        1: "сто", 2: "двести", 3: "триста", 4: "четыреста",
        5: "пятьсот", 6: "шестьсот", 7: "семьсот",
        8: "восемьсот", 9: "девятьсот"}

result = ''
st = str(number)
if number == 1000:
    print('тясяча')
if 99 < number < 1000:
    
    if int(st[1]) == 1:
        result = hundreds[int(st[0])] + ' ' + teens[int(st[1:])]
    else:
        result = hundreds[int(st[0])] + ' ' + tens[int(st[1])] + ' ' + ones[int(st[2])]
if 19 < number < 100:
    result = tens[int(st[0])] + ' ' + ones[int(st[1])]

if 9 < number < 20:
    result = teens[number]

if 0 < number < 10:
    result = ones[number]
print(result)
