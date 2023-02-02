soma = 0

for contagem in range(3, 501, 3):
    if contagem % 2 == 1:
        soma += contagem

print(soma)