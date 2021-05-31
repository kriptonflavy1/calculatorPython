from time import sleep
from random import randint

print('''
 _               _            _                    _   _    __                          _         
| |__     ___   | |_    ___  | |     ___    __ _  | | (_)  / _|   ___    _ __   _ __   (_)   __ _ 
| '_ \   / _ \  | __|  / _ \ | |    / __|  / _` | | | | | | |_   / _ \  | '__| | '_ \  | |  / _` |
| | | | | (_) | | |_  |  __/ | |   | (__  | (_| | | | | | |  _| | (_) | | |    | | | | | | | (_| |
|_| |_|  \___/   \__|  \___| |_|    \___|  \__,_| |_| |_| |_|    \___/  |_|    |_| |_| |_|  \__,_|
                                                                                                   

Bem Vindo Ao Seu Check-in no HOTEL CALIFORNIA Vamos Iniciar Cadastrando As Pessoas que Irão se Hospedar,
temos uma politica de seguro oque por pessoa deve-se pra seguro pagar R$50 - Adulto e R$25 - criança
fora hospedagem. a diaria será calculada apenas quando você sair e contará como valor adicional.
''')
print('-'* 120)
ok = int(input('tecle 1 para ver quais os beneficios do seguro ou Digite 0 se estiver de acordo, para darmos continuidade...'))

if ok == 1:

    print('''
S E G U R O:
Para evitar acontecimentos catastroficos temos a disposição sempre um medico, bombeiros e seguranças no hotel para lhe assegurar
de um maior conforto, cobrimos também com o seguro despesas de alimenação para café da manhã, almoço, e janta.
Ps:  a depender da Suite o serviço de quarto será pago      
    ''')

cont = 0

preco_adulto = preco_crianca = adulto = crianca = homem = mulher = 0

while True:
    cont += 1

    print('-' * 25)

    nome = str(input('Nome Do Hospede N°{}: '.format(cont))).strip().title()
    idade = int(input('Idade do Hospede:  '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [ M / f ]: ')).upper().strip()[0]

    if idade >= 18:
        adulto += 1
        preco_adulto += 50

    else:
        crianca += 1
        preco_crianca += 25
        

    if sexo == 'M':
        homem += 1
    else:
        mulher += 1    

    print('-' * 25)
    cad = ' '
    while cad not in 'SN':
        cad = str(input('Deseja Cadatrar Mais Alguem [ S / N ]: ')).upper().strip()[0]
    if cad == 'N':
        print('ENCERRANDO...')
        print('-' * 120)
        sleep(1)
        break
    
tot = preco_adulto + preco_crianca
print('entre os cadastrados existem {} adultos e {} crianças, {} deles são homens e {} são mulheres! total a pagar por seguro R${}'.format(adulto, crianca, homem, mulher, tot))

print('-' * 120)

if adulto <= 2 and crianca >=1:
    print('Por serem responsaveis por menores de idade podem se hospedar em apenas um quarto.')
if adulto > 2 and crianca >=1:
    print('Apenas 2 adultos acompanhando as crianças poderão ficar nos quartos padrão, os outros requerem a hospedagem em outro quarto.')
if adulto <=4 and crianca == 0:
    print('Todos as opções de suite estão disponiveis para essa quantidade de pessoas')
if adulto == 0 and crianca >= 1:
    print('Apenas podemos liberar a hospedagem para crianças em nosso hotel com a autorização dos pais ou responsaveis legais. ') 

print('-' * 120)

ok = input('digite enter para consultar suites disponiveis...')

print('''
S U I T E S   D I S P O N I V E I S :

1 - Suite Standart - R$150: suite padrão com 1 cama de casal  e 2 de solteiro podendo ser 2 de casal ou 4 de solteiro banheiro e tv (não é smart)

2 - Suite Master - R$350: suite confortavel com cama de molas podendo ser 2 de casal ou 4 de solteiro, banheiro com agua quente e tv com assinartura 
 
3 - Suite Deluxe - R$550: suite luxuosa com camas ortopedicas podendo ser 2 de casal ou 4 de solteiro, banheiro possui banheeira, (tv smart)

4 - Suite Presidencial - R$750: camas ortopedicas e com função de massagem, banheira, varanda com hidro, tv (tudo liberado) servico de quarto gratuito

''')
print('-' * 120)
while True:
    escolha = int(input('Qual Suite Deseja Se Hospedar: '))

    print('-' * 120)

    if escolha == 1:
        tot += 150
        print('O valor da Suite Standart mais o Seguro Obrigatorio é de R${}'.format(tot))
    elif escolha == 2:
        tot += 350
        print('O valor da Suite Master mais o Seguro Obrigatorio é de R${}'.format(tot))
    elif escolha == 3:
        tot += 550
        print('O valor da Suite Deluxe mais o Seguro Obrigatorio é de R${}'.format(tot))
    elif escolha == 4:
        tot += 750
        print('O valor da Suite Presidedncial mais o Seguro Obrigatorio é de R${}'.format(tot))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar e Partir ao Pagamento [ S / N ]: ')).upper().strip()[0]
    if continuar == 'N':
        print('Encerrando...')
        sleep(1)
        break
    print('-' * 25)
    print('''F O R M A S   D E   P A G A M E N T O:
    1 - Dinheiro 
    2 - Cheque
    3 - Cartão (A vista)
    4 - Cartão (Parcelado)
    ''')   
    print('-' * 25)
    pg = int(input('Qual será a sua forma de pagamento: '))
    tit = str(input('Nome do Pagante Responsavel: ')).title().strip()
    print('-' * 120)
    if pg == 1:
        ca = tot - (tot * 10 / 100)
        print('Com O pagamento em dinheiro houve um desconto de 10%, o total a pagar é de R${}'.format(ca))
    elif pg == 2:
        ca = tot - (tot * 5 / 100)
        print('Com O pagamento em cheque houve um desconto de 5%, o total a pagar é de R${}'.format(ca))
    elif pg == 3:
        print('O total a ser pago é de {}'.format(tot))
    elif pg == 4:
        print('Opções de Pagamento')
        print('-' * 15)
        for c in range(2,13):
            
            print('{:2}X de R${:.2f}'.format(c, tot / c))

    else: 
        print('Digite Valores Validos!!!')


    print('-' * 25)
    print('''NOTA FISCAL:
    pagante: {}
    N° de Hospedes: {}
    quarto de escolha:  {}
    pagará um total de:  R${}
    '''.format(tit,cont, escolha, tot))
    
    print('-' * 120)

    alt = ' '
    while alt not in 'SN':
        alt = str(input('Deseja alterar algo em relação ao pagamento e a suite [ S / N ]: ')).upper().strip()[0]
    if alt == 'N':
        print('Finalizando...')
        sleep(1)
        break
    tot = preco_adulto + preco_crianca 

print('-' * 120)
print('{:^120}'.format('Tenha Uma Boa Estadia Em Nosso Hotel!!!'))
print('-' * 120)
