import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import linregress

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
##### AJUSTE EXPONENCIAL (COM LINEARIZAÇÃO) ########
# Converte Vr para um array do NumPy
Vr_array = np.array(Vripple)

# Aplica a equação em todos os elementos
V0 = 14.7 # escrever valor
resultado = np.log(np.abs((V0 - Vr_array) / V0))

print(resultado)
resultado_lista = resultado.tolist()

# FAZENDO A REGRESSÃO
# Dados
X = inv_R
Y = resultado_lista

# Regressão linear
slope, intercept, r_value, p_value, std_err = linregress(X, Y)

print(f"Inclinação (slope): {slope}")
print(f"Intercepto: {intercept}")
print(f"R²: {r_value**2}")

t = 1/120  # tempo fixo em segundos
# slope = t/C
C = - t / slope

print(f"Capacitância estimada: {C:.6f} F") # checar valor da capacitância
'''

#'''
#### AJUSTE EXPONENCIAL ########
# Define o modelo de ajuste
def modelo(x, C):
    t = 1/120 
    Vp = 14.7
    return Vp * (1 - np.exp(-(t/C) * x)) # k = t/C x = 1/R

#t = 1/120
# Chute inicial para Vp e RC
p0 = [1.0]

params, _ = curve_fit(modelo, inv_R, Vripple, p0=p0)
C_fit = params[0]

#print(f'Vp ajustado: {Vp_fit:.4f} V')
#print(f'k ajustado: {k_fit:.4f} s')

x_fit = np.linspace(min(inv_R), max(inv_R), 200)
y_fit = modelo(x_fit, C_fit)

#t = 1/120  # tempo fixo em segundos
#C = t / k_fit

print(f"Capacitância estimada: {C_fit:.6f} F") # checar valor da capacitância


plt.scatter(inv_R, Vripple, label='Dados experimentais')
plt.plot(x_fit, y_fit, color='red', label='Ajuste exponencial')
plt.xlabel('Inverso da Resistência (1/R) Ohms^-1')
plt.ylabel('V(ripple) (V)')
plt.legend()
plt.grid(True)
plt.title('Ajuste da função exponencial')
plt.show()

#'''