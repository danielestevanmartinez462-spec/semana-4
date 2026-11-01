#  Contador de vocales

frase = "Me gusta programar en Python"
vocales = "aeiouAEIOU"

contador = 0
for letra in frase:
    if letra in vocales:
        contador += 1
print("La frase tiene", contador, "vocales")