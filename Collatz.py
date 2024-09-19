while True:
    c0 = int(input("Digite um número"))
    if c0 > 0:
        break
    else:
        print("Erro! Digite um número natural positivo maior que zero")
steps = 0  # Contagem das etapas

while c0 != 1:  # Loop while até que c0 seja igual a 1
    print(f"O valor atual de c0: {c0}")
    if c0 % 2 == 0:  # Descobrindo se o c0 é par, Se a diferença de c0 dividido por 2 não for 0, o número é impar

        c0 = c0 // 2  # Se for par, divide por 2
    else:
        c0 = 3 * c0 + 1  # Se for impar, multiplica por 3 e soma +1

    steps += 1  # Incrementa +1 na contagem de etapas
    print(f"O valor Final de c0: {c0}")  # Imprime o c0 quando ele for 1
    print("Número de steps", steps)  # Imprime o número de etapas
