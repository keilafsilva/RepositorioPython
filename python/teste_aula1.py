print("\n\n\n\tHello world")

arraynumb = [2, 3, 4, 1, 5, 6]
menor = arraynumb[0]

for i in range(1, len(arraynumb)):
    if arraynumb[i] < menor:
        menor = arraynumb[i]

print(f"O menor numero é {menor}")


a = 5
b = 5
c = a + b

print("A soma de ", a, " + ", b, " é igual a ", c)
    
if c > 10:
    print("Maior que 10")
elif c == 10:
    print("Igual a 10")
else:
    print("Menor que 10")

