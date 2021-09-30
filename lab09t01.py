sum = 0
for x in range(7):
    num = input("Insert number (rainfall): ")

    if num.isnumeric():
        num = int(num)
        sum += num
    else:
        break

print("Rainfall sum is ", sum)
