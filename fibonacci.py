# leedcode fibonacci sorusu çözümü
n = int(input("enter a number: "))
fibonacci = []

for i in range(n + 1):
    if i == 0:
        fibonacci.append(i)
    elif i == 1:
        fibonacci.append(i)
    else:
        f_number = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(f_number)

print(fibonacci[-1])
