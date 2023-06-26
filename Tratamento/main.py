import pandas as pd

# URL do conjunto de dados
data_url = 'https://drive.google.com/uc?export=download&id=1SdCK7a5E9_vQKTEmMtEROrq-LBsKlTPE'

# Carregar o conjunto de dados a partir do URL
data = pd.read_csv(data_url)

# Renomear as colunas com os nomes traduzidos em português
data.rename(columns={
    'appid': 'ID',
    'name': 'Nome',
    'release_date': 'Data de Lançamento',
    'english': 'Inglês',
    'developer': 'Desenvolvedor',
    'publisher': 'Publicador',
    'platforms': 'Plataformas',
    'required_age': 'Idade Requerida',
    'categories': 'Categorias',
    'genres': 'Gêneros',
    'steamspy_tags': 'Tags do SteamSpy',
    'achievements': 'Conquistas',
    'positive_ratings': 'Avaliações Positivas',
    'negative_ratings': 'Avaliações Negativas',
    'average_playtime': 'Tempo Médio de Jogo',
    'median_playtime': 'Tempo Mediano de Jogo',
    'owners': 'Proprietários',
    'price': 'Preço'
}, inplace=True)

# Preencher valores nulos nas colunas 'Desenvolvedor' e 'Publicador' com mensagens personalizadas
data['Desenvolvedor'].fillna('Desenvolvedor não especificado', inplace=True)
data['Publicador'].fillna('Publicador não especificado', inplace=True)

# Substituir o caractere ';' por ' - ' em todas as colunas, exceto 'Nome'
columns_to_replace = data.columns.drop('Nome')
for column in columns_to_replace:
    data[column] = data[column].astype(str).str.replace(';', ' - ')

# Remover as colunas 'ID', 'Inglês', 'Proprietários' e 'Tags do SteamSpy'
data = data.drop(['ID', 'Inglês', 'Proprietários', 'Tags do SteamSpy'], axis=1)

# Imprimir uma amostra aleatória de 10 linhas do DataFrame modificado
print(data.sample(10))

# Salvar o DataFrame modificado como um novo arquivo CSV chamado 'steam.csv'
caminho_arquivo = 'steam.csv'
data.to_csv(caminho_arquivo, index=False)

# Observação: Este é um exemplo simples para fins ilustrativos
# e pode não abranger todas as possíveis operações de tratamento de dados.
