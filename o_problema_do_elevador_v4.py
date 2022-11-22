"""
O problema do elevador


-o algoritmo vai ser capaz de tomar as decisões para definir qual elevador
é o com mais eficácia atende ao chamado.

-é uma árvore de decisão

1a pergunta da decisão:
    -qual elevador tem andar acima ou igual ao do andar solicitado
    
    -> é mais fácil descer do que subir (tem menos gasto de energia)
    -> caso haja elevador no andar solicitado -> esse elevador será o escolhido
    -> caso haja somente um elevador acima do andar solicitado:
        -> esse elevador será escolhido
    -> caso mais ou nenhum elevador acima:
        -> próxima pergunta:

2a pergunta da decisão:
    -quantas pessoas há em cada elevador?
    
    -> cada pessoa vai pesar em média 75kg (padrão)
    -> aquele elevador que tiver menos pessoas dentro, será o escolhido
    -> a partir da quantidade de pessoas, calcularemos o tempo que ele levará
a mais para percorrer um andar, esse tempo também calculará o esforço feito
pelo elevador (contabilizar o gasto de energia)

"""

import random
import pygame
import time
from pygame.locals import *
from sys import exit


andares_do_predio = int(input('Digite a quantidade de andares do seu predio: '))
andar_da_pessoa = int(input('Qual andar você se encontra? ')) 
while(andar_da_pessoa > andares_do_predio):
    andar_da_pessoa = int(input('Andar inválido!!! Redigite o andar que você se encontra: '))
andar_pessoa_vai = int(input('Qual andar você deseja ir? '))
while(andar_pessoa_vai > andares_do_predio):
    andar_pessoa_vai = int(input('Andar inválido!!! Redigite o andar que você quer ir: '))

pessoa = [andar_da_pessoa, andar_pessoa_vai]
andar1 = random.randint(1, andares_do_predio)
andar2 = random.randint(1, andares_do_predio)
andar3 = random.randint(1, andares_do_predio)
print(f'Elevador 1 está no: {andar1} andar.')
print(f'Elevador 2 está no: {andar2} andar.')
print(f'Elevador 3 está no: {andar3} andar.')

pessoas1 = random.randint(1, 6)
pessoas2 = random.randint(1, 6)
pessoas3 = random.randint(1, 6)
print(f'Há {pessoas1} pessoas no elevador 1.')
print(f'Há {pessoas2} pessoas no elevador 2.')
print(f'Há {pessoas3} pessoas no elevador 3.')

mov = ['subindo', 'descendo']
    
if (andar1 == andares_do_predio):
    movimento1 = 'descendo'
else:
    movimento1 = random.choice(mov)
        
if (andar2 == andares_do_predio):
    movimento2 = 'descendo'
else:
    movimento2 = random.choice(mov)    
    
if (andar3 == andares_do_predio):
    movimento3 = 'descendo'
else:
    movimento3 = random.choice(mov)
    


while True:
    
    elevador1 = [andar1, pessoas1, movimento1]
    elevador2 = [andar2, pessoas2, movimento2]
    elevador3 = [andar3, pessoas3, movimento3]
    print(f'Situação do Elevador 1-> andar: {elevador1[0]} ; quantidade de pessoas: {elevador1[1]}; o elevador está: {elevador1[2]}')
    print(f'Situação do Elevador 2-> andar: {elevador2[0]} ; quantidade de pessoas: {elevador2[1]}; o elevador está: {elevador2[2]}')
    print(f'Situação do Elevador 3-> andar: {elevador3[0]} ; quantidade de pessoas: {elevador3[1]}; o elevador está: {elevador3[2]}')

    print(f'Você está no {andar_da_pessoa} andar')
    print(f'Você vai para o {andar_pessoa_vai} andar')

        
    dec1, dec2, dec3 = 0, 0, 0
        
           
    """
        andar_da_pessoa = int(input('Qual andar você se encontra? '))
        while(andar_da_pessoa > andares_do_predio):
            andar_da_pessoa = int(input('Andar inválido!!! Redigite o andar que você se encontra? '))
        andar_pessoa_vai = int(input('Qual andar você deseja ir? '))
        pessoa = [andar_da_pessoa, andar_pessoa_vai]
    """
        
        # nosso elevador tem potência de 7kW
        # cada pessoa aumenta em 1.5 segundos o tempo para percorrer 1 andar
        # uma hora tem 3600 segundos
        # o consumo de um elevador é:
            #a potência base multiplicada pelo tempo de uso
        # para calcular o tempo de uso:
            #pessoas * tempo_pessoa + (andar que o elevador se encontra - andar que ele vai)*tempo_elevador
    tempo_elevador = 10 #por andar
    tempo_pessoa_descer = 1.25
    tempo_pessoa_subir = 1.75
    pot_elevador = 7000
        
    if(elevador1[2] == 'subindo'):
        consumo_elevador1 = (pot_elevador * (elevador1[1]*tempo_pessoa_subir + abs(elevador1[0]-andar_da_pessoa)*tempo_elevador))/3600
    else:
        consumo_elevador1 = (pot_elevador * (elevador1[1]*tempo_pessoa_descer + abs(elevador1[0]-andar_da_pessoa)*tempo_elevador))/3600
        
    if(elevador2[2] == 'subindo'):
        consumo_elevador2 = (pot_elevador * (elevador2[1]*tempo_pessoa_subir + abs(elevador2[0]-andar_da_pessoa)*tempo_elevador))/3600    
    else:
        consumo_elevador2 = (pot_elevador * (elevador2[1]*tempo_pessoa_descer + abs(elevador2[0]-andar_da_pessoa)*tempo_elevador))/3600
        
    if(elevador3[2] == 'subindo'):
        consumo_elevador3 = (pot_elevador * (elevador3[1]*tempo_pessoa_subir + abs(elevador3[0]-andar_da_pessoa)*tempo_elevador))/3600  
    else:
        consumo_elevador3 = (pot_elevador * (elevador3[1]*tempo_pessoa_descer + abs(elevador3[0]-andar_da_pessoa)*tempo_elevador))/3600
        
    print(f'Consumo do elevador 1: {consumo_elevador1:.2f} kW')    
    print(f'Consumo do elevador 2: {consumo_elevador2:.2f} kW')     
    print(f'Consumo do elevador 3: {consumo_elevador3:.2f} kW')
        
    pygame.init()
          
    fonte = pygame.font.SysFont('arial', 20, True, False)
    
    texto_elevador1 = f'Situação do Elevador 1-> andar: {elevador1[0]} ; quantidade de pessoas: {elevador1[1]}; o elevador está: {elevador1[2]}'
    texto_elevador2 = f'Situação do Elevador 2-> andar: {elevador2[0]} ; quantidade de pessoas: {elevador2[1]}; o elevador está: {elevador2[2]}'
    texto_elevador3 = f'Situação do Elevador 3-> andar: {elevador3[0]} ; quantidade de pessoas: {elevador3[1]}; o elevador está: {elevador3[2]}'
    texto_pessoa = f'Você está no {andar_da_pessoa} andar e vai para o {andar_pessoa_vai} andar'
    texto_consumo_e1 = f'Consumo do elevador 1: {consumo_elevador1:.2f} kW'
    texto_consumo_e2 = f'Consumo do elevador 2: {consumo_elevador2:.2f} kW'
    texto_consumo_e3 = f'Consumo do elevador 3: {consumo_elevador3:.2f} kW'
    texto_formatado_e1 = fonte.render(texto_elevador1, True, (255,255,255))
    texto_formatado_e2 = fonte.render(texto_elevador2, True, (255,255,255))
    texto_formatado_e3 = fonte.render(texto_elevador3, True, (255,255,255))
    texto_formatado_p = fonte.render(texto_pessoa, True, (255,255,255))
    texto_formatado_c1 = fonte.render(texto_consumo_e1, True, (255,255,255))
    texto_formatado_c2 = fonte.render(texto_consumo_e2, True, (255,255,255))
    texto_formatado_c3 = fonte.render(texto_consumo_e3, True, (255,255,255))
    
    largura = 1080
    altura = 720
        
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('O PROBLEMA DO ELEVADOR')
    relogio = pygame.time.Clock()
    relogio.tick(3)
        
    altura_andar = altura / andares_do_predio
    largura_elevador = 40
    if elevador1[0] == 1:
        ypos_elevador1 = 720 - altura_andar
    else:
        ypos_elevador1 = 720 - (elevador1[0] * altura_andar)
    if elevador2[0] == 1:
        ypos_elevador2 = 720 -  altura_andar
    else:    
        ypos_elevador2 = 720 - (elevador2[0] * altura_andar)
    if elevador3[0] == 1:
        ypos_elevador3 = 720 - altura_andar
    else:
        ypos_elevador3 = 720 - (elevador3[0] * altura_andar)
        # 720 - (largura_elevador * quantidade_de_elevadores (3) = 600, sobra 120
        # 120/4 = 30 - espaço de paredes
    xpos_elevador1 = 20
    xpos_elevador2 = 80
    xpos_elevador3 = 140
    
        
    tela.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
                
    pygame.draw.rect(tela, (255,0,0), (xpos_elevador1, ypos_elevador1, 40, altura_andar))
    pygame.draw.rect(tela, (255,0,0), (xpos_elevador2, ypos_elevador2, 40, altura_andar))
    pygame.draw.rect(tela, (255,0,0), (xpos_elevador3, ypos_elevador3, 40, altura_andar))
    pygame.draw.line(tela, (255,255,255), (200,0), (200,840), 10)
    
    print('Decisão:')
    if(consumo_elevador1 <= consumo_elevador2 and consumo_elevador1 <= consumo_elevador3):
            print('Elevador 1 se dirigindo...')
            andar1 = andar_pessoa_vai
            pessoas1 = random.randint(1, 6)
            pessoas2 = random.randint(1, 6)
            pessoas3 = random.randint(1, 6)
            andar2 = random.randint(1, andares_do_predio)
            andar3 = random.randint(1, andares_do_predio)
            texto_decision = 'Decisão: Elevador 1 a caminho'
                
    if(consumo_elevador2 <= consumo_elevador1 and consumo_elevador2 <= consumo_elevador3):
            print('Elevador 2 se dirigindo...')
            andar2 = andar_pessoa_vai
            pessoas1 = random.randint(1, 6)
            pessoas2 = random.randint(1, 6)
            pessoas3 = random.randint(1, 6)
            andar1 = random.randint(1, andares_do_predio)
            andar3 = random.randint(1, andares_do_predio)
            texto_decision = 'Decisão: Elevador 2 a caminho'
     
    if(consumo_elevador3 <= consumo_elevador1 and consumo_elevador3 <= consumo_elevador2):
            print('Elevador 3 se dirigindo...')
            andar3 = andar_pessoa_vai
            pessoas1 = random.randint(1, 6)
            pessoas2 = random.randint(1, 6)
            pessoas3 = random.randint(1, 6)
            andar1 = random.randint(1, andares_do_predio)
            andar2 = random.randint(1, andares_do_predio)
            texto_decision = 'Decisão: Elevador 3 a caminho'
            
    time.sleep(5)
    
    texto_formatado_d = fonte.render(texto_decision, True, (255,255,255))
    
    tela.blit(texto_formatado_e1, (220, 20))
    tela.blit(texto_formatado_e2, (220, 60))
    tela.blit(texto_formatado_e3, (220, 100))
    tela.blit(texto_formatado_p, (220, 140))
    tela.blit(texto_formatado_c1, (220, 180))
    tela.blit(texto_formatado_c2, (220, 220))
    tela.blit(texto_formatado_c3, (220, 260))
    tela.blit(texto_formatado_d, (220, 300))
    
    pygame.display.update()      
    # andar_da_pessoa = andar_pessoa_vai -> "buga" o código... sempre vai dar o último elevador q a pessoa usou...
    andar_da_pessoa = random.randint(1, andares_do_predio)
    andar_pessoa_vai = random.randint(1, andares_do_predio)
    if andar_da_pessoa == andar_pessoa_vai:
        andar_da_pessoa = random.randint(1, andares_do_predio)

    print('---------------------\n')
    
    