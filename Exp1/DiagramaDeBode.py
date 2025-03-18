import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do CSV
data = np.loadtxt(r'C:\Users\lucas\Downloads\dados.csv', delimiter=',', skiprows=1)

# Separar as colunas
freq = data[:, 0]  # Frequência (Hz)
T_dec = data[:, 5] # Ganho em dB
phase = data[:, 3] # Fase (graus)

plt.figure(figsize=(10, 8))

# Gráfico de Ganho
plt.subplot(2, 1, 1)
plt.semilogx(freq, T_dec, 'b-', label='Ganho (dB)')  # Log no eixo X
plt.scatter(freq, T_dec, color='blue', marker='o', edgecolors='black', label='Pontos experimentais')  # Pontos usados

# 🔍 **Marcar o ponto de -3 dB (frequência de corte)**
idx_3dB = np.argmin(np.abs(T_dec + 3))  # Índice do ponto mais próximo de -3 dB
freq_3dB = freq[idx_3dB]
T_3dB = T_dec[idx_3dB]

plt.scatter(freq_3dB, T_3dB, color='purple', marker='D', s=100, edgecolors='black', label='Frequência de Corte (-3 dB)')
plt.text(freq_3dB, T_3dB - 5, f'{freq_3dB:.2f} Hz', color='purple', fontsize=10, ha='center')

plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.title('Diagrama de Bode - Magnitude')
plt.grid(True, which='both', linestyle='--')
plt.legend()

# Gráfico de Fase
# adicionando os erros (incertezas):
erro_freq = np.full_like(freq, 0.0000001)  # 5% de erro na frequência
erro_phase = np.full_like(phase, 0.00000001)  # Erro fixo de ±5 graus

plt.subplot(2, 1, 2)
plt.semilogx(freq, phase, 'r-', label='Fase (graus)')  # Log no eixo X
plt.scatter(freq, phase, color='red', marker='o', edgecolors='black', label='Pontos experimentais')  # Pontos usados
# adicionando a barra de erro
plt.errorbar(freq, phase, xerr=erro_freq, yerr=erro_phase, fmt='o', color='red', 
             ecolor='black', capsize=4, label='Pontos experimentais')  
# Encontrar a frequência mais próxima de -45° na fase
# Encontramos o valor da fase correspondente a essa frequência
idx_fase_corte = np.argmin(np.abs(freq - freq_3dB))
fase_corte = phase[idx_fase_corte]

# Plotamos esse ponto no gráfico de fase
plt.scatter(freq_3dB, fase_corte, color='purple', marker='D', s=100, edgecolors='black', label='Frequência de Corte (-3 dB)')
plt.text(freq_3dB, fase_corte + 5, f'{freq_3dB:.2f} Hz', color='purple', fontsize=10, ha='center')


plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.title('Diagrama de Bode - Fase')
plt.grid(True, which='both', linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()
