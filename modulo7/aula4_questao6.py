

import pandas as pd

# Lendo o arquivo CSV, especificando o encoding e o separador
df = pd.read_csv('spotify-2023.csv', encoding='latin-1')

# Visualizando as primeiras linhas
print(df.head())

# Selecionando as colunas de interesse e filtrando por ano
df = df[['track_name', 'artist(s)_name', 'released_year', 'streams']]
df = df[df['released_year'].between(2012, 2022)]

# Função para remover aspas duplas e vírgulas dentro de nomes de músicas e artistas
def limpar_texto(texto):
    return texto.strip('"').replace('"', '')

df['track_name'] = df['track_name'].apply(limpar_texto)
df['artist(s)_name'] = df['artist(s)_name'].apply(limpar_texto)

# Filtrando para músicas com apenas um artista
df = df[df['artist_count'] == 1]

import numpy as np

# Agrupando por ano e encontrando a música mais tocada
musicas_mais_tocadas = df.groupby('released_year')['streams'].idxmax()
resultado = df.loc[musicas_mais_tocadas][['track_name', 'artist(s)_name', 'released_year', 'streams']].values.tolist()

print(resultado)