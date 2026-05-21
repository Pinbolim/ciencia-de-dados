import matplotlib.pyplot as plt 
import pandas as pd

# Análise qualitativa
frutas = [
    "Maça", "Banana", "Maca",
    "Laranja", "Banana", "Banana",
    "Maça", "Uva", "Laranja",
]

serie = pd.Series(frutas)
frequencia = serie.value_counts()

print(frequencia)

# Criando gráficos de barras 
frequencia.plot(kind="bar")

plt.title("Frutas Preferidas dos Alunos")
plt.xlabel("Frutas")
plt.ylabel("Frequencia")

plt.show()
plt.savefig("aula06-qualitativo")