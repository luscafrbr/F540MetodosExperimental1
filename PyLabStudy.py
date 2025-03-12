import pylab as plt
import numpy as np

# Carregar os dados do arquivo CSV (substitua 'dados.csv' pelo nome do seu arquivo)
data = np.loadtxt(r'C:\Users\lucas\Downloads\dados.csv', delimiter=',', skiprows=1)

# Separar as colunas em variáveis X e Y
freq = data[:, 0] # frequency
Vpp1 = data[:, 1] # Vpp1
Vpp2 = data[:, 2] # Vpp2
phase = data[:, 3] # phase
T = data[:, 4] # T
T_dec = data[:,5] # T decibeis

print('freq =', freq)
print('Vpp1 = ', Vpp1)
print('Vpp2 = ', Vpp2)
print('phase = ', phase)
print('T = ', T)
print('T_dec =', T_dec)

# Criar um gráfico de dispersão dos dados
plt.figure(figsize=(8, 6))
plt.scatter(freq, T, color='blue', label='Dados experimentais', alpha=0.6) # X = freq; Y = T;
plt.xlabel('Variável Independente (freq)')
plt.ylabel('Variável Dependente (T)')
plt.title('Análise de Dados com PyLab')
plt.legend()
plt.grid(True)
plt.show()
'''
# Ajustar uma regressão linear aos dados
coef = np.polyfit(X, Y, 1)  # Ajuste linear (1º grau)
polinomio = np.poly1d(coef)  # Criar a função polinomial
Y_ajustado = polinomio(X)

# Plotar a linha de melhor ajuste
plt.plot(X, Y_ajustado, color='red', label=f'Ajuste Linear: y = {coef[0]:.2f}x + {coef[1]:.2f}')
plt.legend()
plt.show()

# Exibir estatísticas básicas
print("Estatísticas básicas:")
print(f"Média de X: {np.mean(X):.2f}")
print(f"Média de Y: {np.mean(Y):.2f}")
print(f"Desvio padrão de X: {np.std(X):.2f}")
print(f"Desvio padrão de Y: {np.std(Y):.2f}")
print(f"Coeficiente de correlação: {np.corrcoef(X, Y)[0, 1]:.2f}")
'''