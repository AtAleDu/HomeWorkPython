s = 0
i = 0
while i < 5:
    i += 1
s += 1/i
print("Первая задача = " + str(s))

s = 0
i = 1
while i > 1:
    s = s + 1/i
    i = i - 1
print("вторая задача задача = " + str(s))

s = 1
n = 1
for i in range(2, n):
    s = s + 1/i
print("третья задача задача = " + str(s))