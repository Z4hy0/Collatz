# Conjectura de Collatz

Este é um programa simples que implementa a **Conjectura de Collatz**, uma hipótese matemática intrigante, também conhecida como a "Sequência de Collatz" ou "Problema 3x+1". O programa solicita ao usuário que insira um número natural positivo e calcula a sequência de Collatz até o número atingir o valor 1.

## Índice
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Como Executar](#como-executar)
4. [Exemplo de Uso](#exemplo-de-uso)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

A **Conjectura de Collatz** é descrita da seguinte maneira:
1. Pegue qualquer número inteiro positivo.
2. Se for par, divida-o por 2.
3. Se for ímpar, multiplique por 3 e adicione 1.
4. Repita esse processo até que o número seja igual a 1.

Este projeto foi desenvolvido para explorar essa sequência, contando o número de iterações e exibindo os valores intermediários da sequência.

## Funcionalidades
- Aceita como entrada um número natural positivo.
- Calcula a sequência de Collatz até o número atingir 1.
- Conta e exibe o número total de iterações.
- Verifica a validade da entrada (somente números naturais positivos são aceitos).

## Como Executar

1. Certifique-se de ter o **Python** instalado no seu computador (versão 3.x).
2. Clone este repositório ou faça o download do arquivo `.py`.
3. Execute o programa no terminal com o seguinte comando:

    ```bash
    Collatz.py
    ```

4. Insira um número natural positivo quando solicitado.

## Exemplo de Uso

```bash
Digite um número natural positivo: 6
Valor atual de c0: 6
Valor atual de c0: 3
Valor atual de c0: 10
Valor atual de c0: 5
Valor atual de c0: 16
Valor atual de c0: 8
Valor atual de c0: 4
Valor atual de c0: 2
Valor final de c0: 1
Número total de etapas: 8
```

## Tecnologias Utilizadas
- Python


