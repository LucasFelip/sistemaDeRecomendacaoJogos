from datetime import datetime

class UserInputs:
    @staticmethod
    def get_title():
        """
        Obtém o título desejado do usuário.

        Returns:
            str: O título desejado.
        """
        return input("Digite o título desejado: ")

    @staticmethod
    def get_genre():
        """
        Obtém o gênero desejado do usuário.

        Returns:
            str: O gênero desejado.
        """
        return input("Digite o gênero desejado: ")

    @staticmethod
    def get_top_n():
        """
        Obtém o número de recomendações desejado do usuário.

        Returns:
            int or None: O número de recomendações desejado ou None se não especificado.
        """
        top_n_input = input("Digite o número de recomendações desejado: ")
        if top_n_input:
            return int(top_n_input)
        else:
            return None

    @staticmethod
    def get_price():
        """
        Obtém o preço máximo desejado do usuário.

        Returns:
            float or None: O preço máximo desejado ou None se não especificado.
        """
        price_input = input("Digite o preço máximo desejado: ")
        if price_input:
            return float(price_input)
        else:
            return None

    @staticmethod
    def get_release_date():
        """
        Obtém a data de lançamento mínima desejada do usuário.

        Returns:
            datetime.date or None: A data de lançamento mínima desejada ou None se não especificada ou inválida.
        """
        release_date_input = input("Digite a data de lançamento mínima desejada (no formato AAAA-MM-DD): ")
        if release_date_input:
            try:
                release_date = datetime.strptime(release_date_input, '%Y-%m-%d').date()
                return release_date
            except ValueError:
                print("Data de lançamento inválida. Utilizando valor padrão.")
        return None

    @staticmethod
    def get_platforms():
        """
        Obtém as plataformas desejadas do usuário.

        Returns:
            str: As plataformas desejadas.
        """
        return input("Digite as plataformas desejadas: ")

    @staticmethod
    def get_game_id():
        """
        Obtém o ID do jogo desejado do usuário.

        Returns:
            int: O ID do jogo desejado.
        """
        return int(input("Digite o ID do jogo para obter detalhes: "))


def get_user_inputs():
    """
    Obtém todos os inputs do usuário.

    Returns:
        tuple: Uma tupla contendo o título, gênero, número de recomendações, preço máximo, data de lançamento mínima e plataformas desejadas.
    """
    user_inputs = UserInputs()
    title = user_inputs.get_title()
    genre = user_inputs.get_genre()
    price = user_inputs.get_price()
    release_date = user_inputs.get_release_date()
    platforms = user_inputs.get_platforms()
    top_n = user_inputs.get_top_n()
    return title, genre, top_n, price, release_date, platforms

def get_user_inputs_id():
    """
    Obtém o ID do jogo desejado do usuário.

    Returns:
        int: O ID do jogo desejado.
    """
    user_inputs = UserInputs()
    id = user_inputs.get_game_id()
    return id

def clear_screen():
    """
    Limpa a tela do console.
    """
    print("\n" * 130)