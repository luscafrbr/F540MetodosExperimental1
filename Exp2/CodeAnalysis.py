import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# Carregar os dados 
# data = np.loadtxt(r'C:\Users\lucas\Downloads\planilha_exp2 - Página1.csv', delimiter=',', skiprows=1) # carregar csv
data = pd.ExcelFile(r'C:\Users\lucas\Downloads\planilha_exp2.xlsx')

# print(data.sheet_names) # mostra os nomes das páginas da planilha

# Usando o nome da aba
df = data.parse('Página1')
print(df)
# print(df.columns) # mostra os nomes das colunas da planilha
# "C:\Users\lucas\Downloads\planilha_exp2.xlsx"
# .astype(str) converte em string e o .astype(float) converte em float
Vripple = df['V(ripple)'].astype(str).str.replace(',', '.').astype(float)  # tensão Vripple em Volts
R = df['R (ohms)'].astype(str).str.replace(',', '.').astype(float) # resistência em Ohms
inv_R = 1/R
# print(Vripple)
# print(R)

'''
# Criar um gráfico de dispersão dos dados
plt.figure(figsize=(8, 6))
plt.scatter(inv_R, Vripple, color='blue', label='Dados experimentais', alpha=0.6) # X = freq; Y = T;
plt.xlabel('Variável Independente (R)')
plt.ylabel('Variável Dependente (Vripple)')
plt.title('Análise de Dados com PyLab')
plt.legend()
plt.grid(True)
plt.show()
'''
#### AJUSTE EXPONENCIAL ########
# Define o modelo de ajuste
def modelo(x, Vp, k):
    return Vp * (1 - np.exp(-k * x)) # k = t/C x = 1/R

t = 1/60
# Chute inicial para Vp e RC
p0 = [max(Vripple), 1.0]

params, _ = curve_fit(modelo, inv_R, Vripple, p0=p0)
Vp_fit, k_fit = params

print(f'Vp ajustado: {Vp_fit:.4f} V')
print(f'k ajustado: {k_fit:.4f} s')

x_fit = np.linspace(min(inv_R), max(inv_R), 200)
y_fit = modelo(x_fit, Vp_fit, k_fit)

t = 1/60  # tempo fixo em segundos
C = t / k_fit

print(f"Capacitância estimada: {C:.6f} F") # checar valor da capacitância


plt.scatter(inv_R, Vripple, label='Dados experimentais')
plt.plot(x_fit, y_fit, color='red', label='Ajuste exponencial')
plt.xlabel('Inverso da Resistência (1/R) Ohms^-1')
plt.ylabel('V(ripple) (V)')
plt.legend()
plt.grid(True)
plt.title('Ajuste da função exponencial')
plt.show()

