#1
a = input('Задайте список через пробел: ').split()
for i in range(0, len(a), 2):
    print(a[i])
#2
s=input('введите элемент списка через пробел: ')
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=',')
#3     
a=[int(i) for i in input('введите элементы: ').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
#4        
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break 
#5
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

#6
a=[int(i) for i in input().split()]
for i in range(len(a)):
    if a[i]==max(a):
        print('max(a)',max(a),'[i]',i)
        break
#7
a = [int(i) for i in input('введите рост по убыванию: ')]
x = int(input('Рост Пети: '))
pos = 0
while pos < len(a) and a[pos] >=x:
    pos += 1
print(pos + 1)

#8
a = [int(i) for i in input('Введите элемент: ').split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)

#9
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

#10
a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))

#11
a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))

#12
a = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
 
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))


#13
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

#14
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

#15
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))


#16
a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))
