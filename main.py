n = int(input())

mas = []
age = []
r = []
first = []
second = []

for i in range(n):
    s = input()
    mas.append(s)

for i in range(n):
    l = mas[i].split()
    age.append(l[1])
    r.append(l[0])

for i in range(n):
    if 20 <= int(age[i]) <= 40:
        k = r[i]
        second.append(k)
    else:
        k = r[i]
        first.append(k)

first.sort()
second.sort()

print("First team:\n", *first)
print("Second team:\n", *second)
