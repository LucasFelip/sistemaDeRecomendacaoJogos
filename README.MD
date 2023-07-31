# Sistema de Recomendação de Jogos

O Sistema de Recomendação de Jogos é um projeto que visa fornecer recomendações personalizadas de jogos com base em preferências e critérios específicos do usuário. O projeto está organizado em diferentes módulos e utiliza dados da plataforma Steam para realizar as recomendações.

## Funcionamento do Projeto

### Pasta Tratamento

Na pasta "Tratamento", o projeto realiza o pré-processamento dos dados obtidos da plataforma Steam. O objetivo é tornar os dados mais adequados para análises e consultas no sistema de recomendação. O arquivo principal nesta pasta é o `main.py`.

O pré-processamento inclui as seguintes etapas:

1. Carregar o conjunto de dados a partir de uma URL que contém um arquivo CSV com informações dos jogos.
2. Renomear as colunas com nomes em português para facilitar a compreensão dos dados.
3. Preencher valores nulos nas colunas "Desenvolvedor" e "Publicador" com mensagens personalizadas.
4. Substituir o caractere ';' por ' - ' em todas as colunas, exceto a coluna "Nome".
5. Remover as colunas "ID", "Inglês", "Proprietários" e "Tags do SteamSpy" do DataFrame.
6. Salvar o DataFrame modificado como um novo arquivo CSV chamado "steam.csv".

Essas etapas visam melhorar a capacidade de operação de consulta do usuário no sistema de recomendação.

### Arquivos no diretório principal

O diretório principal contém os seguintes arquivos:

1. `main.py`: Este é o arquivo principal onde a interface do sistema de recomendação é implementada. Ele utiliza a classe `GameRecommendationSystem` para obter as recomendações de jogos com base nos critérios fornecidos pelo usuário.

2. `user_input.py`: Este arquivo contém as funções para obter os inputs do usuário, como título do jogo desejado, gênero, número de recomendações, preço máximo, data de lançamento mínima e plataformas desejadas.

3. `game_recommendation_system.py`: Este arquivo contém a classe `GameRecommendationSystem`, que realiza as operações de pré-processamento dos dados e calcula as recomendações de jogos com base nos critérios fornecidos pelo usuário.

4. `gui.py`: Este arquivo implementa uma interface gráfica para interação com o sistema de recomendação. Ele utiliza a biblioteca `tkinter` para criar os elementos da interface.

## Utilização do Sistema de Recomendação de Jogos

Para utilizar o sistema de recomendação, siga os passos abaixo:

1. Execute o arquivo `gui.py` ou `main.py`.
2. A interface gráfica será aberta ou terminal.
3. Preencha os critérios desejados para as recomendações nos campos apropriados, como título do jogo, gênero, número de recomendações, preço máximo, data de lançamento mínima e plataformas desejadas.
4. Clique no botão "Recomendar" ou "Enter" para calcular e exibir as recomendações de jogos que correspondam às preferências informadas.
5. As recomendações serão exibidas em uma tabela na interface gráfica ou terminal.

## Observações

- O sistema de recomendação é baseado na análise das avaliações positivas e negativas dos jogos, e utiliza um limiar (quantile) para filtrar os jogos recomendados.
- Os dados utilizados pelo sistema são obtidos da plataforma Steam e podem estar sujeitos a alterações e atualizações.
- Este projeto é um exemplo simples de sistema de recomendação de jogos para fins ilustrativos e não abrange todas as possíveis operações de tratamento de dados ou estratégias avançadas de recomendação.

## Requisitos do Sistema

O sistema requer a instalação das seguintes bibliotecas Python:

- pandas
- requests
- tkinter (incluída na biblioteca padrão do Python)

As bibliotecas podem ser instaladas utilizando o gerenciador de pacotes `pip`.

```bash
pip install pandas requests
```

## Autor
[<img align="left" height="84px" width="84px" alt="@LucasFelip" src="https://avatars.githubusercontent.com/LucasFelip?size=64">](https://github.com/LucasFelip)
**Lucas Ferreira** \
[**IFMA**](https://portal.ifma.edu.br/inicio/) • São Luís \
Linguagens & Tecnologias: `Java`, `IntelliJ`

<br>

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE). Sinta-se livre para utilizar, modificar e distribuir este código conforme os termos da licença.