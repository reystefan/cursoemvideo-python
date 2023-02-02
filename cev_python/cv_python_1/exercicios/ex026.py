frase = input('Digite um frase qualquer: ').strip()
frase_lower = frase.lower()

print(f'Possui {frase_lower.count("a")} caracteres "a"')
print(f'Aparece pela primeira vez em {frase_lower.find("a") + 1}')
print(f'Aparece pela última vez em {frase_lower.rfind("a") + 1}')
