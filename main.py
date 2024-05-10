# import graph as gph
# import calcs as calc
# #Constantes
# ALTURA_MEDIA_HOMEM = 175
# ALTURA_MEDIA_MULHER = 162
#
# def main():
#     desvio_padrao = 7
#     populacao = 1000
#     dados_alturas = calc.geraDadosAleatorios(ALTURA_MEDIA_HOMEM, desvio_padrao, populacao)
#     dados_normalizados = calc.normalizaOsDados(dados_alturas)
#     gph.gerarGrafico(dados_normalizados)
#
# main()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Criação de 4 conjuntos de dados
data1 = np.random.normal(50, 10, 1000)
data2 = np.random.normal(30, 5, 1000)
data3 = np.random.normal(70, 15, 1000)
data4 = np.random.normal(90, 20, 1000)

# Criação de uma figura e 4 eixos (para 4 histogramas)
fig, axs = plt.subplots(4, sharex=True)

# Função para atualizar os histogramas
def update(curr):
    if curr == 100:
        a.event_source.stop()
    for ax in axs:
        ax.clear()
    bins = np.arange(0, 100, 5)
    axs[0].hist(data1[:curr], bins=bins, color='b', alpha=0.5)
    axs[0].set_title('Tema 1')
    axs[1].hist(data2[:curr], bins=bins, color='r', alpha=0.5)
    axs[1].set_title('Tema 2')
    axs[2].hist(data3[:curr], bins=bins, color='g', alpha=0.5)
    axs[2].set_title('Tema 3')
    axs[3].hist(data4[:curr], bins=bins, color='m', alpha=0.5)
    axs[3].set_title('Tema 4')
    plt.suptitle('Animação de 4 Histogramas Diferentes')

# Criação da animação
a = animation.FuncAnimation(fig, update, interval=100, save_count=100)

plt.show()

