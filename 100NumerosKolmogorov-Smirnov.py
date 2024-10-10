import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generar 100 números aleatorios entre 0 y 1 (distribución uniforme)
data = np.random.uniform(0, 1, 100)

# Realizar la prueba de Kolmogorov-Smirnov para una distribución uniforme
ks_statistic, p_value = stats.kstest(data, 'uniform')

print('Estadístico de Kolmogorov-Smirnov:', ks_statistic)
print('p-valor:', p_value)

# Visualización
plt.hist(data, bins=20, density=True, alpha=0.6)
plt.title('Histograma de 100 Números Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Densidad')

plt.plot(np.sort(data), np.arange(1, len(data)+1) / len(data), color='red', label='Empírica')
x = np.linspace(0, 1, 100)
plt.plot(x, x, color='blue', label='Teórica')

plt.legend()
plt.show()