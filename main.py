#Permite a manipulação de arquivos
import pandas as pd

#permite a construção de gráficos
import matplotlib.pyplot as plt

#classe utilizada para manipular dados da bola
from bola import bola

#classe utilizada para o cálculo da distância entre dois pontos
from distancia import distancia

#utiliza o pandas para abrir um log
partida = pd.read_csv("partida.csv")

#variável utilizada para interagir com o tempo da partida
tempo_de_partida = 1

#salvam a quantidade de posses
lista_possesl = [0,1,2,3,4,5,6,7,8,9,10]
lista_possesr = [0,1,2,3,4,5,6,7,8,9,10]

#salvam as distância da bola para cada jogador
lista_distancial = list()
lista_distanciar = list()

#loop que utiliza a variável responsável por interagir com o tempo da partida(fazendo com q todos os dados sejam
#coletados a cada tempo de partida

while(tempo_de_partida<6700):

    #coleta a posição da bola
    bola1 = bola(partida.loc[tempo_de_partida, "ball_x"], partida.loc[tempo_de_partida, "ball_y"])

    #controla o número do jogador análisado
    i = 1

    while(i<12):

        #coleta a posição X do jogador i do time L
        posxl = partida.loc[tempo_de_partida - 1, f"player_l{i}_x"]
        #coleta a posição Y do jogador i do time L
        posyl = partida.loc[tempo_de_partida - 1, f"player_l{i}_y"]
        #calcula a distancia entre a bola e o jogador i do time L
        distancia1 = distancia(bola1.posx, posxl, bola1.posy, posyl)
        #adiciona na lista a distância entre a bolar e o jogador i do time L na lista
        lista_distancial.append(distancia1.calcular_distancias())

        #coleta a posição X do jogador i do time R
        posxr = partida.loc[tempo_de_partida - 1, f"player_r{i}_x"]
        #coleta a posição Y do jogador i do time R
        posyr = partida.loc[tempo_de_partida - 1, f"player_r{i}_y"]
        #calcula a distancia entre a bola e o jogador i do time R
        distancia2 = distancia(bola1.posx, posxr, bola1.posy, posyr)
        # adiciona na lista a distância entre a bolar e o jogador i do time L na lista
        lista_distanciar.append(distancia2.calcular_distancias())
        i += 1

    #ordena as listas de distâncias do menor para o maior
    ldlo = sorted(lista_distancial)
    ldro = sorted(lista_distanciar)

    #Controla a posição lida
    c = 0

    while(c<11):

        #cria e zera a variável que armazena a quantidade de posse
        h = 0

        #checa se a distancia do jogador[c] em sua respetiva posição na lista é igual a
        #menor distância da lista ldlo(logo está é a posição [0])
        #se a condição for satisfeita quer dizer que o jogador está em posse da bola

        if(lista_distancial[c] == ldlo[0] and ldlo[0]<ldro[0]):
            #armazena 1 de posse do jogador[c]
            h +=1
            #acrescenta 1 de posse ao jogador[c]
            lista_possesl[c] = lista_possesl[c]+h

        # checa se a distancia do jogador[c] em sua respectiva posição na lista é igual a
        # menor distância da lista ldro(logo está é a posição [0])
        elif(lista_distanciar[c] == ldro[0] and ldro[0] < ldlo[0]):
            h +=1
            lista_possesr[c] = lista_possesr[c] + h
        c += 1

    #limpa as duas listas
    lista_distancial.clear()
    lista_distanciar.clear()

    tempo_de_partida += 1

    #soma 1 a variável controladora do tempo

#nomes utilizados nos gráficos
nomesl = ("l1","l2","l3","l4","l5","l6","l7","l8","l9","l10","l11")
nomesr = ("r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","r11")

#cria o gráfico do time L
plt.bar(nomesl,lista_possesl,color = "b")
plt.xlabel("Jogadores")
plt.ylabel("Quantidade de posses")
plt.title("Análise da partida")
plt.show()

#cria o gráfico do time R
plt.bar(nomesr, lista_possesr, color="r")
plt.xlabel("Jogadores")
plt.ylabel("Quantidade de posses")
plt.title("Análise da partida")
plt.show()