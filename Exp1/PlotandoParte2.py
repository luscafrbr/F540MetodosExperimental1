import pylab as plt
import numpy as np

# Carregar os dados do arquivo CSV (substitua 'dados.csv' pelo nome do seu arquivo)
data = np.loadtxt(r'C:\Users\lucas\Downloads\parte2_ch1_dados.csv', delimiter=',', skiprows=1)

# Separar as colunas em variáveis X e Y
freq = data[:, 0] # frequency
amplitude = data[:, 1] # amplitude

plt.scatter(freq, amplitude)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Amplitude')
plt.title('Amplitude x Frequência - Canal 1')
# plt.legend('Dados Coletados')
plt.show()