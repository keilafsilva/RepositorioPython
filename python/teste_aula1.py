print("\n\n\n\tHello world")

arraynumb = [2, 3, 4, 1, 5, 6]
menor = arraynumb[0]

for i in range(1, len(arraynumb)):
    if arraynumb[i] < menor:
        menor = arraynumb[i]

print(f"O menor numero é {menor}")
    