print("Trabalhando com tipo de dados")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Seu nome é {nome}, você tem {idade} anos e {altura:.2f}m de altura.")

print(type(nome))
print(type(idade))
print(type(altura))

# Usando condições (if, elif, else)
numero = int(input("Digite um número para verificar se é par ou ímpar: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar. \n")

#Usando laços de repetição (while)
print("Digite números positivos para somar. Digite um número negativo para parar.")
soma = 0
while True: # Laço infinito até que a condição de parada seja atingida
    num = int(input("Digite um número: "))
    if num < 0: # Condição de parada
        break
    soma += num # Soma apenas positivos
print(f"A soma dos números positivos é {soma}. \n")

#Usando laços de repetição (for)
numero = int(input("Digite um número para ver sua tabela de multiplicação: "))
print(f"Tabela de multiplicação do {numero}:")
for i in range (1,11): # range (1, 11) gera números de 1 a 10
    print(f"{numero} x {i} = {numero * i}")
print()

# Trabalhando com strings (exemplo: contar vogais)
frase = input("Digite uma frase: ").lower() # .lower() para ignorar maiúsculas/minúsculas
vogais = "aeiou"
contador = 0
for letra in frase: #Iterar sobre cada carectere da frase
    if letra in vogais: # Verfica vogal
        contador += 1
print(f"A frase contém {contador} vogais. \n")

# Trabalhando com listas
numeros = [] # Criando uma lista vazia
print("Digite 5 números para adicionar a lista. ")
for _ in range(5): #Repetir 5 vezes
    n = int(input("Digite um número: "))
    numeros.append(n) # Adicionar o número à lista
print(f"A lista de números é: {numeros}")
print(f"A soma dos números é: {sum(numeros)}\n") # sum() para somar os elementos da lista

# Funções (exemplo: verificar se um número é primo)
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
        return True
    
    num_primo = int(input("Digite um número para verificar se é primo: "))
    if eh_primo (num_primo):
        print(f"{num_primo} é um número primo.")
    else:
        print(f"{num_primo} não é um número primo. \n")
        
# Fatorial usando while
num_fatorial = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = num_fatorial
while contador > 0: # Multiplica enquanto contador for maior que 0
    fatorial *= contador
    contador -= 1
    print(f"O fatorial de {num_fatorial} é {fatorial}. \n ")

# Jogo de adivinhação (laço + randomização)
import random # Biblioteca para gerar números aleatórios
numero_secreto = random.randint (1, 20)
print ("Tente adivinhar o número entre 1 e 20!")
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palite > numero_secreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou!")
        break

