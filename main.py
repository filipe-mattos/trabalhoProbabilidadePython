# #Exemplo pe de cafe, passando x valor, x de media e x de desvioPadrao fazer um grafico da distribuicao normal
#pegartema sobre altura no inep populacaosileira

#Aprender como gerar um grafico historograma

import numpy as np #faz as somas
import matplotlib.pyplot as plt #cria grafico

# quantidade = 1
# media = 1
# desvioPadrao = 1

# data = np.random.normal(loc=0, scale=1, size=200)

# count, bins, ignored = plt.hist(data, 30)
# plt.show()

# print("Teste 12345")


mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
abs(mu - np.mean(s))
abs(sigma - np.std(s, ddof=1))

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.show()