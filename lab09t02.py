sum = 0
count = 0
while 1:
    num = input("Anna luku: ")

    if num.isnumeric():
        num = int(num)
        sum += num
        count += 1
    else:
        break

print("Lukuja annettu:", count)
print("Lukujen summa:", sum)
