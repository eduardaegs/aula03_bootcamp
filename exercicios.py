'''Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva 
um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.'''

# quantidade = 40
# preco = 20

# if quantidade >0 and preco > 0:
#     print('Valores válidos')
# else:
#     print('Valores inválidos')


'''Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa',
 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'''



'''6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.'''

texto = 'Hoje é a nossa segunda aula do bootcamp. Bootcamp de Python para Data Engineer.'
texto = texto.replace('.', '')

palavras = texto.split(" ")


print(palavras)

contagem = {}

for palavra in palavras:
    if palavra.lower() in contagem:
        contagem[palavra.lower()] += 1
    else:
        contagem[palavra.lower()] = 1
print(contagem)