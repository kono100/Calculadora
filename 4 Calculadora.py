

# Definindo as funções
def somar(x, y):
    resultado = x + y
    print('\n', x, ' + ', y, ' = ', resultado, '\n')

def subtrair(x, y):
    resultado = x - y
    print('\n', x, ' - ', y, ' = ', resultado, '\n')

def multiplicar(x, y):
    resultado = x * y
    print('\n', x, ' * ', y, ' = ', resultado, '\n')

def dividir(x, y):
    resultado = x / y
    print('\n', x, ' / ', y, ' = ', resultado, '\n')

# Iniciando o programa
print('Olá usuário, seja bem-vindo(a) a J-Calculator\n')
# Loop externo para permitir que o usuário continue realizando operações
while True:
    print('Digite um dos números abaixo para selecionar a operação desejada\n')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair do programa\n')

    escolha = input('Escolha o número da operação desejada: ')

    # Bloco de tratamento de erro para caso o usuário escolha uma opção divergente das suportadas
    try:
        escolha = int(escolha)
    except ValueError:
        print('Digite um número válido')
        continue

    if escolha == 5:
        print('Saindo da J-Calculator...')
        break

    # Loop interno para validar a entrada do primeiro número
    while True:
        x = input('\nPrimeiro valor: ')
        # Bloco de tratamento de erro para caso o usuário escolha uma opção divergente das suportadas
        try:
            x = float(x)
        except ValueError:
            print('Digite um número válido')
            continue
        else:
            break

    # Loop interno para validar a entrada do segundo número
    while True:
        y = input('Segundo valor: ')
        # Bloco de tratamento de erro para caso o usuário escolha uma opção divergente das suportadas
        try:
            y = float(y)
        except ValueError:
            print('Digite um número válido')
            continue
        else:
            if escolha == 4 and y == 0:
                print('Não é possível dividir por zero. Tente novamente.')
                continue  # Continuar no loop interno para pedir um novo y
            break

    if escolha == 1:
        somar(x, y)

    elif escolha == 2:
        subtrair(x, y)

    elif escolha == 3:
        multiplicar(x, y)

    elif escolha == 4:
        dividir(x, y)

    else:
        print('Operação inválida, por favor, selecione uma opção correta \n')


