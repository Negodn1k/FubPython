a = 0
b = 1
c = 0
i = 0
print(a, "\n", b)
while (i <= 20):
    c = b
    b = a + b
    a = c
    print(b)
    i = i + 1
