import random

def pularLinhas(n):
    print('\n' * n)

def substituir(a, b, lista):
    for index, value in enumerate(lista):
        if value == a or value == b:
            lista[index] = ' '

mapa = ' 7 | 8 | 9 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 1 | 2 | 3 '

pularLinhas(1)
print('=x' * 30)
pularLinhas(1)
logo = 'JOGO DA VELHA'
print(logo.center(60))
pularLinhas(1)
print('=x' * 30)
pularLinhas(1)


lista_user1 = []
lista_user2 = []

lista = list('   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   ')

pont_user1 = 0
pont_user2 = 0
pont_robo = 0


while pont_user1 >= 0 and pont_user2 >= 0:
    try:
        menu2 = int(input('[0] - Robô\n[1] - P2P\n\nOpção: '))
        if menu2 == 1:
            pularLinhas(20)
            print('Escolha uma posição correspondente: ')
            pularLinhas(1)
            print(mapa)
            pularLinhas(1)
            while len(lista_user1) < 6:
                while True:   
                    user1 = int(input('\nUsuário 1 [O]: '))
                    if user1 > 9 or user1 == 0:
                        pularLinhas(20)
                        print('\nEscolha um número da tabela!')
                        pularLinhas(1)
                        print(mapa)
                    elif user1 in lista_user2:
                        pularLinhas(20)
                        print('\nEscolha uma posição diferente do seu adversário!')
                        pularLinhas(1)
                        print(''.join(lista))
                    elif user1 in lista_user1:
                        pularLinhas(20)
                        print('\nEscolha outra posição!')
                        pularLinhas(1)
                        print(''.join(lista))
                    else:
                        
                        find = mapa.find(str(user1))
                        lista[find] = 'O'
                        lista_user1.append(user1)
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(''.join(lista))
                        break
                if 1 in lista_user1 and 2 in lista_user1 and 3 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user1 and 4 in lista_user1 and 7 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user1 and 5 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 2 in lista_user1 and 5 in lista_user1 and 8 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user1 and 6 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user1 and 5 in lista_user1 and 7 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 4 in lista_user1 and 5 in lista_user1 and 6 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 7 in lista_user1 and 8 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif len(lista_user1) == 5:
                    print('\nDeu velha!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break


                while True:
                    
                    user2 = int(input('\nUsuário 2 [X]: '))
                    if user2 > 9 or user2 == 0:
                        pularLinhas(20)
                        print('\nEscolha um número da tabela!')
                        pularLinhas(1)
                        print(mapa)
                    elif user2 in lista_user1:
                        pularLinhas(20)
                        print('\nEscolha uma posição diferente do seu adversário!')
                        pularLinhas(1)
                        print(''.join(lista))
                    elif user2 in lista_user2:
                        pularLinhas(20)
                        print('\nEscolha outra posição!')
                        pularLinhas(1)
                        print(''.join(lista))
                    else:

                        find = mapa.find(str(user2))
                        lista[find] = 'X'
                        lista_user2.append(user2)
                        pularLinhas(1)
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(''.join(lista))
                        break
                if 1 in lista_user2 and 2 in lista_user2 and 3 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user2 and 4 in lista_user2 and 7 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user2 and 5 in lista_user2 and 9 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 2 in lista_user2 and 5 in lista_user2 and 8 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user2 and 6 in lista_user2 and 9 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user2 and 5 in lista_user2 and 7 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 4 in lista_user2 and 5 in lista_user2 and 6 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 7 in lista_user2 and 8 in lista_user2 and 9 in lista_user2:
                    print('\nUsuário 2 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos User 1: {pont_user1}\nPontos User 2: {pont_user2}')
                        pularLinhas(1)
                        print(mapa)
                    break
        elif menu2 == 0:
            pularLinhas(20)
            print('Escolha a posição correspondente: ')
            pularLinhas(1)
            print(mapa)
            while len(lista_user1) < 6:
                while True:   
                    user1 = int(input('\nUsuário [O]: '))
                    if user1 > 9 or user1 == 0:
                        pularLinhas(20)
                        print('\nEscolha um número da tabela!')
                        pularLinhas(1)
                        print(mapa)
                    elif user1 in lista_user2:
                        pularLinhas(20)
                        print('\nEscolha uma posição diferente do seu adversário!')
                        pularLinhas(1)
                        print(''.join(lista))
                    elif user1 in lista_user1:
                        pularLinhas(20)
                        print('\nEscolha outra posição!')
                        pularLinhas(1)
                        print(''.join(lista))
                    else:
                        
                        find = mapa.find(str(user1))
                        lista[find] = 'O'
                        lista_user1.append(user1)
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(''.join(lista))
                        break
                if 1 in lista_user1 and 2 in lista_user1 and 3 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user1 and 4 in lista_user1 and 7 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user1 and 5 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 2 in lista_user1 and 5 in lista_user1 and 8 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user1 and 6 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário 1 ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user1 and 5 in lista_user1 and 7 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 4 in lista_user1 and 5 in lista_user1 and 6 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 7 in lista_user1 and 8 in lista_user1 and 9 in lista_user1:
                    print('\nUsuário ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user1 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif len(lista_user1) == 5:
                    print('\nDeu velha!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break


                while True:
                    
                    user2 = random.randint(1, 9)

                    if user2 in lista_user1:
                        pularLinhas(20)
                        print('\nEscolha uma posição diferente do seu adversário!')
                        pularLinhas(1)
                        print(''.join(lista))
                    elif user2 in lista_user2:
                        pularLinhas(20)
                        print('\nEscolha outra posição!')
                        pularLinhas(1)
                        print(''.join(lista))
                    else:

                        find = mapa.find(str(user2))
                        lista[find] = 'X'
                        
                        lista_user2.append(user2)
                        pularLinhas(1)
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(''.join(lista))
                        break
                if 1 in lista_user2 and 2 in lista_user2 and 3 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user2 and 4 in lista_user2 and 7 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 1 in lista_user2 and 5 in lista_user2 and 9 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 2 in lista_user2 and 5 in lista_user2 and 8 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user2 and 6 in lista_user2 and 9 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 3 in lista_user2 and 5 in lista_user2 and 7 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_robo += 1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_user2 += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 4 in lista_user2 and 5 in lista_user2 and 6 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
                elif 7 in lista_user2 and 8 in lista_user2 and 9 in lista_user2:
                    print('\nRobô ganhou!')
                    pularLinhas(1)
                    menu = int(input('[0] - Sair\n[1] - Continuar\n:'))
                    if menu == 0:
                        pont_user1 = -1
                    
                    else:
                        lista_user1.clear()
                        lista_user2.clear()
                        substituir('O', 'X', lista)
                        pont_robo += 1
                        pularLinhas(20)
                        print(f'Pontos Usuário: {pont_user1}\nPontos Robô: {pont_robo}')
                        pularLinhas(1)
                        print(mapa)
                    break
        else:
            print('Número inválido')
    except:
        print('!!Digite um valor válido!!')


    
