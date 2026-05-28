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

plt.clf()

# Análise quantitativa 
notas = [
    5, 6, 7, 8, 7, 
    6, 5, 9, 10, 8,
    7, 6, 2, 10, 10,
]

serie2 = pd.Series(notas)
frequencia = serie2.value_counts()

print(frequencia)

serie2.plot(kind="hist")

plt.title("Distribuição das Notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")

plt.show()
plt.savefig("aula06-quantitativo")