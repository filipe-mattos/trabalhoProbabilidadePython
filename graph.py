from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
def gerarGrafico(dadosNormalizados):
    # Gerar o histograma
    plt.hist(dadosNormalizados, bins=30, density=True, alpha=0.6, color='b')

    # Plotar a distribuição normal teórica
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, 0, 1)
    plt.plot(x, p, 'k', linewidth=2)

    title = "Histograma da Distribuição Normalizada da Altura Populacional Brasileira"
    plt.title(title)
    plt.xlabel("Valores Normalizados")
    plt.ylabel("Densidade")

    # Mostrar o gráfico
    plt.show()
