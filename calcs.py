import numpy as np
def geraDadosAleatorios(altura_media, desvio_padrao, populacao):
    return np.random.normal(loc=altura_media, scale=desvio_padrao, size=populacao)
def normalizaOsDados(alturas):
    # Normalizar os dados
    dados_normalizados = (alturas - np.mean(alturas)) / np.std(alturas)
    return dados_normalizados
