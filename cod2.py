##Condições
nome  = "Anna"
idade = 27

if nome == "Anna":
    print("Passou")

if nome == "Anna" or idade == 30:
    print("Passou de novo")
    print("%s tem %d anos." %(nome, idade))

dias = ["sunday", "tuesday"]

if len(dias) == 0:
    print("sem dias")
elif len(dias) == 1:
    print("somente um dia")
else:
    print("mais de um dia")

##Loop
# for i in range(6):
#     print(i)

# for i in range(1, 6):
#     print(i)

for i in range(0, 6, 2):
    print(i)
