L = ["ram", 1, "shyam", 2, "aman", 3]
L1 = []  # for integers
L2 = []  # for strings

for i in L:
    try:
        L1.append(int(i))  # try to treat it like a number
    except:
        L2.append(i)       # if error, it's a string

L1.sort()
L2.sort()
L3 = L1 + L2
print(L3)
