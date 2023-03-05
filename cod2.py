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

pares = [2, 4, 6, 8]
for i in range(len(pares)):
    print("índice %d - valor %d" %(i, pares[i]))

length = 0
word = "Hello World"
for char in word:
    length +=1
print(length)

loop = 1
while loop <=7:
    print(loop)
    loop += 1

count = 0
while True:
    print(count)
    count += 1
    if count >=5:
        break

naipes = ['copas', 'ouros', 'espadas', 'paus']

while True:
    elemento = naipes.pop()
    print(elemento)
    if elemento == "ouros":
        break

for i in range(5):
    if i == 3:
        continue
    print(i)

def hello_world():
    print('hello world')

hello_world()

def print_text(x):
    print("olá %s" %(x))

print_text("carlos")

def soma(a, b):
    return a + b

c = soma(1,5)
print(c)

nome = input("Como posso te chamar?")
print("olá! %s" %(nome))


nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
nota3 = float(input("Informe a terceira nota:"))

def media(nota1, nota2, nota3):
    result = (nota1+nota2+nota3)/3
    if result >= 6:
        return print("o aluno foi aprovado com a nota %.2f" %(result))
    else:
       return print("o aluno não foi aprovado por a nota foi: %.2f" %(result))

media(nota1, nota2, nota3)
