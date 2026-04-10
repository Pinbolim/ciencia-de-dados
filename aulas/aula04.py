import pandas as pd

# Criação do DataFrame
df = pd.DataFrame({
    # Cria uma coluna com descrição de valores
    "idade": [20, 22, 20, 23, 24]
})

print(df['idade'].describe())

print('Média: ' + str(df['idade'].mean()))
print('Mediana: ' + str(df['idade'].median()))
print('Moda: ' + str(df['idade'].mode().iloc[0]))

