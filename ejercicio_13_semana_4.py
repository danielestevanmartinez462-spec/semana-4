#Contar pares e impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = 0
impares = 0

for n in lista:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Pares:", pares)
print("Impares:", impares)
 