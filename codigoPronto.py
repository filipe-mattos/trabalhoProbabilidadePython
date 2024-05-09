##################################### notas #################################
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def gerar_notas_alunos(num_alunos):
  media_desejada = 60
  desvio_padrao = 10

  # Gerar notas dos alunos seguindo uma distribuição normal
  notas = np.random.normal(loc=media_desejada, scale=desvio_padrao, size=num_alunos)

  # Limitar as notas entre 0 e 100
  notas = np.clip(notas, 0, 100)

  return notas

def plot_distribuicao_notas(notas_alunos):
  plt.figure(figsize=(10, 6))
  # Histograma das notas dos alunos
  n, bins, patches = plt.hist(notas_alunos, density=True, bins=50, alpha=0.75, color='blue', edgecolor='black')

  # Parâmetros da distribuição normal
  media = np.mean(notas_alunos)
  desvio_padrao = np.std(notas_alunos)

  # Distribuição normal
  x = np.linspace(0, 100, 10000)

  print(x)
  y = norm.pdf(x, loc=media, scale=desvio_padrao)
  plt.plot(x, y, color='red', linestyle='-', linewidth=2)

  plt.xlabel('Notas dos Alunos')
  plt.ylabel('Densidade de Probabilidade')
  plt.title('Distribuição de Notas dos Alunos')
  plt.grid(True)
  plt.legend(['Distribuição Normal', 'Distribuição de Notas'], loc='best')
  plt.xlim(0, 100)
  plt.show()

def main():
  situation = True
  graphs = []
  while situation:
    print("\nMenu:")
    print("1. Gerar gráfico")
    print("0. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '0':
      print("Saindo...")
      situation = False
    elif escolha == '1':
      num_alunos = int(input("Digite o número de alunos: "))
      notas_alunos = gerar_notas_alunos(num_alunos)
      print("Desvio Padrão:", np.std(notas_alunos))
      print("Média:", np.mean(notas_alunos))
      plot_distribuicao_notas(notas_alunos)
    else:
     print("Opção inválida. Por favor, escolha uma opção válida.")
main()