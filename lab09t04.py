first_name = input("Anna etunimi: ")
last_name = input("Anna sukunimi: ")

for i in range(len(first_name)):
    print(first_name[0], end = "")

print(" ", end = "") 

i = len(last_name)
while i > 0:
    print(last_name[i-1], end = "")
    i = i-1