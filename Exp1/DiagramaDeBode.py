import matplotlib.pyplot as plt
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


# Criar o diagrama de Bode (dois gráficos)
plt.figure(figsize=(10, 8))

# 1️⃣ Gráfico do ganho (Magnitude)
plt.subplot(2, 1, 1)  # 2 linhas, 1 coluna, 1º gráfico
plt.semilogx(freq, T_dec, 'b-', label='Ganho (dB)')  # Eixo X logarítmico
plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.title('Diagrama de Bode - Magnitude')
plt.grid(True, which='both', linestyle='--')
plt.legend()

# 2️⃣ Gráfico da fase
plt.subplot(2, 1, 2)  # 2 linhas, 1 coluna, 2º gráfico
plt.semilogx(freq, phase, 'r-', label='Fase (graus)')  # Eixo X logarítmico
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.title('Diagrama de Bode - Fase')
plt.grid(True, which='both', linestyle='--')
plt.legend()

# Exibir os gráficos
plt.tight_layout()
plt.show()
