import matplotlib.pyplot as plt
import numpy as np

# aumenta o tamanho dos textos nos gráficos
plt.rcParams.update({
    'font.size': 25,  # Aumenta tamanho global da fonte
    'axes.titlesize': 25,  # Tamanho do título do gráfico
    'axes.labelsize': 22,  # Tamanho dos rótulos dos eixos
    'xtick.labelsize': 22,  # Tamanho dos valores do eixo X
    'ytick.labelsize': 22,  # Tamanho dos valores do eixo Y
    'legend.fontsize': 14  # Tamanho da legenda
})

def uncertainty_Av_db(w, wc, sigma_w):
    """Calcula a incerteza de A_v(dB) usando propagação de incertezas"""
    # Derivada parcial de A_v(dB) em relação a w
    dAv_db_dw = (20 / np.log(10)) * (1 / w) - (20 / np.log(10)) * ((w / wc) / (1 + (w / wc) ** 2)) * (2 / w)
    
    # Propagação de incerteza
    sigma_Av_db = abs(dAv_db_dw) * sigma_w  # Módulo da derivada vezes a incerteza de w

    return sigma_Av_db
# Carregar os dados do CSV
data = np.loadtxt(r'C:\Users\lucas\Downloads\dados.csv', delimiter=',', skiprows=1)

# Separar as colunas
freq = data[:, 0]  # Frequência (Hz)
T_dec = data[:, 5] # Ganho em dB
phase = data[:, 3] # Fase (graus)

plt.figure(figsize=(10, 8))

# Gráfico de Ganho
# calculando incertezas para o ganho:
erro_freq = np.full_like(freq, 0.0000001)  # 5% de erro na frequência
erro_Av = uncertainty_Av_db(freq, 7847.60,  0.0000001)  # Erro apos propagacao


plt.subplot(2, 1, 1)
plt.semilogx(freq, T_dec, 'b-', label='Ganho (dB)')  # Log no eixo X
plt.scatter(freq, T_dec, color='blue', marker='o', edgecolors='black', label='Pontos experimentais')  # Pontos usados
# adicionando a barra de erro
plt.errorbar(freq, T_dec, xerr=erro_freq, yerr=erro_Av, fmt='o', color='red', 
             ecolor='black', capsize=4, label='Pontos experimentais')  

# 🔍 **Marcar o ponto de -3 dB (frequência de corte)**
idx_3dB = np.argmin(np.abs(T_dec + 3))  # Índice do ponto mais próximo de -3 dB
freq_3dB = freq[idx_3dB]
T_3dB = T_dec[idx_3dB]

plt.scatter(freq_3dB, T_3dB, color='purple', marker='D', s=100, edgecolors='black', label='Frequência de Corte (-3 dB)')
plt.text(freq_3dB, T_3dB - 5, f'{freq_3dB:.2f} Hz', color='purple', fontsize=22, ha='center')

plt.xlabel('Frequência (Hz)')
plt.ylabel('Ganho (dB)')
plt.title('(a) Diagrama de Bode - Magnitude')
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
plt.text(freq_3dB, fase_corte + 5, f'{freq_3dB:.2f} Hz', color='purple', fontsize=22, ha='center')


plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.title('(b) Diagrama de Bode - Fase')
plt.grid(True, which='both', linestyle='--')
plt.legend()

plt.tight_layout()
plt.show()
