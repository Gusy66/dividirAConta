
# Quando você vai no bar com os seus amigos
# ou em um restaurante, quanto que cada um deve pagar? Esse sistema serve para resolver esse tipo de problema!

# Contador para encerrar o ciclo
i = 0

# Looping para fazer as contas
while i == 0:
    valor = float(input('Qual o valor da conta? '))
    qtde_pessoas = int(input('Quantas pessoas para pagar junto a você? '))
    taxa = int(input('Qual a taxa que você quer pagar? (valor em porcentagem) '))

    valor_taxa = valor * (taxa / 100)
    novo_total = valor - valor_taxa


    pagar_cada = novo_total / (qtde_pessoas - 1)

    print('O valor que cada um deve pagar é: {}R$'.format(pagar_cada))

    # Encerrar o ciclo ou fazer mais uma conta
    while True:
        contador = input('Deseja fazer mais uma operação? S/N ')
        contador = contador.upper()
        if contador == 'S':
            break
        elif contador == 'N':
            i = i + 1
            print('Obrigado por usar o contador do Gustavo Bocci Pimentel.')
            break
        else:
            print('Por favor digite S ou N')

# O nome das variáveis não foram as melhores, porém tentei fazer o máximo que pode para ser intuitivo. Quem p
# Obrigado!
