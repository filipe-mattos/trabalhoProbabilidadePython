import numpy as np
def geraDadosAleatorios(altura_media, desvio_padrao, populacao):
    return np.random.normal(loc=altura_media, scale=desvio_padrao, size=populacao)
def normalizaOsDados(altura):
    # Normalizar os dados
    dados_normalizados = (altura - np.mean(altura)) / np.std(altura)
    return dados_normalizados
