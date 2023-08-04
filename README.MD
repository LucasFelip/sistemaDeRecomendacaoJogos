# Sistema de Recomendação de Jogos

Este é um projeto de sistema de recomendação de jogos baseado em dados da plataforma Steam. O sistema fornece recomendações personalizadas de jogos com base em critérios como título, gênero, número de recomendações, preço máximo, data de lançamento mínima e plataformas desejadas.

## Utilização

1. Execute o arquivo `gui.py` para abrir a interface gráfica do sistema.
2. Preencha os critérios desejados nos campos apropriados.
3. Clique no botão "Recomendar" para obter as recomendações de jogos.
4. As recomendações serão exibidas em uma tabela na interface.

## Requisitos
1. Certificar-se de que possui o Python 3.x instalado no sistema.
> Caso não tenha o Python instalado, você pode baixá-lo em python.org e seguir as instruções de instalação para o seu sistema operacional.

2. Instalar as bibliotecas necessárias: pandas, requests, e tkinter (que geralmente já está incluída na biblioteca padrão do Python).
> Para instalar as bibliotecas, você pode abrir um terminal ou prompt de comando e executar os seguintes comandos:
>
> `pip install pandas requests`

## Arquivos

- `Tratamento/main.py`: Realiza o pré-processamento dos dados da Steam.
- `main.py`: Implementa a operações por terminal e interage com o sistema de recomendação.
- `gui.py`: Implementa a interface gráfica e interage com o sistema de recomendação.
- `user_input.py`: Funções para obter os inputs do usuário.
- `game_recommendation_system.py`: Implementa o sistema de recomendação.

## Observações

- O projeto é um exemplo simples de sistema de recomendação de jogos.
- Este projeto foi desenvolvido para fins educacionais.

## Autor

[<img align="left" height="84px" width="84px" alt="@LucasFelip" src="https://avatars.githubusercontent.com/LucasFelip?size=64">](https://github.com/LucasFelip)
**Lucas Ferreira** \
[**IFMA**](https://portal.ifma.edu.br/inicio/) • São Luís \
Linguagens & Tecnologias: `Java`, `IntelliJ`

<br>

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE). Sinta-se livre para utilizar, modificar e distribuir este código conforme os termos da licença.