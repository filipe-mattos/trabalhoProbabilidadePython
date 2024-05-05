import graph as gph
import calcs as calc
#Constantes
ALTURA_MEDIA_HOMEM = 175
ALTURA_MEDIA_MULHER = 162

def main():
    desvio_padrao = 7
    populacao = 1000000
    dados_alturas = calc.geraDadosAleatorios(ALTURA_MEDIA_HOMEM, desvio_padrao, populacao)
    dados_normalizados = calc.normalizaOsDados(dados_alturas)
    gph.gerarGrafico(dados_normalizados)

main()
