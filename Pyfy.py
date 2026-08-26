from pygame import mixer
from random import shuffle
mixer.init()

biblioteca = [ # Unica coisa que precisa modificar no codigo caso queira adicionar/remover
    "Tá Rindo, é - Ana Carolina", # Nomes tem que ser iguais ao arquivo da musica
    "Talking to the Moon - Bruno Mars",
    "We Don't Talk Anymore - Charlie Puth",
    "There's Nothing Holding Me Back - Shawn Mendes (DJ Ice ver.)",
    "Accidentally In Love - Counting Crows",
    "Oceano - Djavn",
    "A luz dos olhos - Tom Jobim",
    "Aliança - Tribalistas",
    "Recomeçar - Colo de Deus"
    ]

vezes = {} # Existe apenas para otimizar buscas

for musica in biblioteca:
    vezes[musica] = 0

fila = []
historico = []
historico_copia = []
tocando_agora = None

def ver_menu(nome):
    if (nome == None): nome = "nada"
    
    print("=== MEU PLAYER ===")
    print("Tocando agora: ({})".format(nome))
    
    if (nome != "nada"):
        print("Quantidade de vezes que foi tocada: {}".format(vezes[nome]))

    print(
"""
1. Ver biblioteca
2. Adicionar música à fila
3. Ver fila
4. Tocar próxima
5. Voltar
6. Ver histórico
7. Modo festa
0. Sair
""")

def ver_biblioteca():
    for i in range(1, len(biblioteca)+1):
        print("{}. {}".format(i, biblioteca[i-1]))
    print()
    
def ver_fila():
    print("Próximas músicas:\n")
    for musica in fila:
        print(musica)
    print("\nHá {} músicas na fila\n".format(len(fila)))
    
def ver_historico():
    print("Músicas tocadas:\n")
    for i in range(len(historico)-1, -1, -1):
        print(historico[i])
    print()
    
def adicionar_na_fila(pos):
    if (1 <= pos <= len(biblioteca)):
        fila.append(biblioteca[pos-1])
    else:
        print("Posição inválida!\n")

def tocar_proxima():
    if (fila):
        musica = fila.pop(0)
        historico.append(musica)
        historico_copia.append(musica)
        vezes[musica] += 1
        
        recente = historico[len(historico) - 1] # Serve para deixar o codigo mais legivel
        
        mixer.music.load(recente + ".mp3")
        mixer.music.play()
        
        return recente
    
    print("Não há músicas na fila!\n")
    mixer.quit()
    mixer.init()
    return None

def voltar(toc_agora):
    if (len(historico_copia) > 1):
        historico_copia.pop()
        
        recente = historico_copia[len(historico_copia)-1] # Serve para deixar o codigo mais legivel
        historico.append(recente)
        vezes[recente] += 1

        mixer.music.load(recente + ".mp3")
        mixer.music.play()
        
        return recente
    else:
        print("Não é possível mais retroceder!\n")
        return toc_agora
    
def festa():
    shuffle(fila)
    print("UHUU!!! A FILA FOI MISTURADA!\n")











ver_menu(tocando_agora)
opcao = int(input())

while (opcao != 0):
    if (opcao == 1):
        ver_biblioteca()
    elif (opcao == 2):
        adicionar_na_fila(int(input("Posição da música para por na fila: ")))
    elif (opcao == 3):
        ver_fila()
    elif (opcao == 4):
        tocando_agora = tocar_proxima()
    elif (opcao == 5):
        tocando_agora = voltar(tocando_agora)
    elif (opcao == 6):
        ver_historico()
    elif (opcao == 7):
        festa()
    else:
        print("Número inválido!\n")
    
    ver_menu(tocando_agora)
    opcao = int(input())

mixer.quit()
print("Obrigado por usar este programa!")
