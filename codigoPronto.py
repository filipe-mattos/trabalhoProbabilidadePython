import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def gerar_notas_alunos(num_alunos):
  media_desejada = 60
  desvio_padrao = 10
  #Gera a nota dos alunos seguindo uma distribuição normal e Limita as notas entre 0 e 100
  return np.clip(np.random.normal(loc=media_desejada, scale=desvio_padrao, size=num_alunos), 0, 100)

def plot_distribuicao_notas(notas_alunos):
  plt.figure(figsize=(10, 6))
  # Histograma das notas dos alunos
  plt.hist(notas_alunos, density=True, bins=50, alpha=0.75, color='blue', edgecolor='white')
  # Distribuição normal
  x = np.linspace(0, 100, 10000)
  # Faz o calculo da formula PDF e define curva do grafico
  y = norm.pdf(x, loc=np.mean(notas_alunos), scale=np.std(notas_alunos))
  plt.plot(x, y, color='red', linestyle='-', linewidth=2)
  plt.xlim(0, 100)
  configuracoes_labels_grafico(plt)
  plt.show()

def configuracoes_labels_grafico(plt):
  plt.xlabel('Notas dos Alunos')
  plt.ylabel('Densidade de Probabilidade')
  plt.title('Distribuição de Notas dos Alunos')
  plt.grid(True)
  plt.legend(['Distribuição Normal', 'Distribuição de Notas'], loc='best')

def exibir_historiograma(notas_dictionary):
  for nota_dictionary in notas_dictionary:
      print(nota_dictionary['desvio_padrao'])
      print(nota_dictionary['media'])
      plot_distribuicao_notas(nota_dictionary['notas_alunos'])

def main():
  situation = True
  notas_dictionary = []
  while situation:
    print("\nMenu:")
    print("1. Gerar gráfico")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '0':
      print("Saindo...")
      exibir_historiograma(notas_dictionary)
      situation = False
    elif escolha == '1':
      num_alunos = int(input("Digite o número de alunos: "))
      notas_dictionary.append(
        {'desvio_padrao': np.std(gerar_notas_alunos(num_alunos)),
        'media': np.mean(gerar_notas_alunos(num_alunos)),
        'notas_alunos': gerar_notas_alunos(num_alunos)})
    else:
     print("Opção inválida. Por favor, escolha uma opção válida.")

main()
