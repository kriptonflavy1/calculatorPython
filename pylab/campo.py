import math
from colorama import init, Fore

init(convert=True, autoreset=True)

print( Fore.LIGHTGREEN_EX +  '''
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

ESCOLHA A OPERAÇÃO E DIGITE SEU NUMERO:

0 - Sair
1 - Soma
2 - Subtração
3 - Multiplicação 
4 - Divisão                                   
5 - Raiz Quadrada
6 - Potenciação                   
7 - Seno, Cosseno e Tangente
8 - Hipotenusa
9 - Consultar Tabuada
''')
calc = 0
cont = 0
d = r = 1

while True:
    print('-' * 82 )
    escolha = int(input('Qual Sua Escolha: ')) 
    print('-' * 82 )
    
    if escolha == 0:
        break
    
    elif escolha == 1:
        

        while True:
            cont += 1
            n1 = float(input('Digite o {}° Numero Para Somar: '.format(cont)))
            calc += n1
            
            if cont >= 2:
                ac = str(input('Deseja Acrescentar Mais Algum numero a soma [ S/N ]: ')).upper().strip()[0]
                while ac not in 'NS':
                    ac = str(input('Deseja Acrescentar Mais Algum numero a soma [ S/N ]: ')).upper().strip()[0]
                if ac == 'N':
                    break
        print(Fore.LIGHTBLUE_EX + 'A Soma Entre Todos Os Numeros Apresentados é de {}'.format(calc))

    elif escolha == 2:
        
        n1 = float(input('Digite Um Numero Para realizar a subtração: '))
        n2 = float(input('Digite Outro Numero Para Realizar a Subtração: '))       

        sub = n1 - n2

        print(Fore.LIGHTBLUE_EX + 'A Subtração Entre Todos os Numeros Apresentados é de {}'.format(sub))

    elif escolha == 3:
        while True:
            cont += 1
            n = float(input('Digite um Numero Para Multiplicar: '))
            r *= n 

            if cont >= 2:
                ac = str(input('Deseja Continuar Adicionando Numeros Para Multiplicar [ S/N ]: ')).upper().strip()[0]
                while ac not in 'SN':
                   ac = str(input('Deseja Continuar Adicionando Numeros Para Multiplicar [ S/N ]: ')).upper().strip()[0]
                if ac == 'N':
                       break
        print(Fore.LIGHTBLUE_EX + 'O Resultado Da Multiplicação Entre Todos Os Numeros Foi de: {}'.format(r))
    
    elif escolha == 4:       
        n = float(input('Digite Um Numero Para Dividir: '))
        n1 = float(input('Digite Outro Numero Para Dividir: '))
        d = n / n1
        di = n // n1
        rd =  n % n1
        print(Fore.LIGHTBLUE_EX + 'O Resultado da Divisão Entre Os Numeros Fornecidos é de: {} A Divisão Inteira: {:.0f} e o Resto da Divisão: {:.0f}'.format(d, di, rd))
  
    elif escolha == 5:
        n = float(input('Digite Um Numero Para Ver Sua Raiz Quadrada: '))
        rq = n ** (1/2)
        print(Fore.LIGHTBLUE_EX + 'A Raiz Quadrada de {} é Igual a {:.2f}'.format(n, rq))
    
    elif escolha == 6:
        n = float(input('Digite um Numero Para Ver Sua Potencia: '))
        p = int(input('Digite a potencia: '))
        pt = n ** p
        print(Fore.LIGHTBLUE_EX + 'O resultado de  {} Elevado a {} Potencia é Igual a {}'.format(n, p, pt))

    elif escolha == 7:
        a = int(input('Digite um Angulo: °'))

        sen = math.sin(math.radians(a))
        cos = math.cos(math.radians(a))
        tg = math.tan(math.radians(a))

        print(Fore.LIGHTBLUE_EX + '''
        O Resultado foi:

        Seno = {}
        Cosseno = {}
        Tangente = {}
        '''.format(sen, cos, tg))
    elif escolha == 8:
        co = float(input('Cateto Oposto: '))
        ca = float(input('Cateto Adjacente: '))

        hyp = math.hypot(co, ca)

        print(Fore.LIGHTBLUE_EX + 'A Hipotenusa Mede: {}'.format(hyp))
    elif escolha == 9:
        n = int(input('Digite Um Numero Para Ver Sua Tabuada: '))
        for c in range(1, 11):
            print(Fore.LIGHTBLUE_EX + '{} X {:2} = {}'.format(n, c, n*c))
    else:
        print('Insira Numeros Validos')

print('-' * 82 )
print(Fore.BLUE + '{:^82}'.format('Obrigado Por Usar o Programa - Kriptonflavy'))
print('-' * 82 )
