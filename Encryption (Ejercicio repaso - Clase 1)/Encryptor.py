import Constants
import math


class Encryptor:
    def replace_char_by_n_positions(self, string, positions):
        encrypted_string = ""
        for char in string:
            if char in Constants.SPANISH_ALPHABET_LOWERCASE:
                try:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                        (Constants.SPANISH_ALPHABET_LOWERCASE.find(char) + positions)]
                except IndexError:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                        self.calculate_position_index(Constants.SPANISH_ALPHABET_LOWERCASE, char, positions)]
            elif char in Constants.SPANISH_ALPHABET_LOWERCASE_TILDE:
                try:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                        (Constants.SPANISH_ALPHABET_LOWERCASE_TILDE.find(char) + positions)]
                except IndexError:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                        self.calculate_position_index(Constants.SPANISH_ALPHABET_LOWERCASE_TILDE, char, positions)]
            elif char in Constants.SPANISH_ALPHABET_UPPERCASE:
                try:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                        (Constants.SPANISH_ALPHABET_UPPERCASE.find(char) + positions)]
                except IndexError:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                        self.calculate_position_index(Constants.SPANISH_ALPHABET_UPPERCASE, char, positions)]
            elif char in Constants.SPANISH_ALPHABET_UPPERCASE_TILDE:
                try:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                        (Constants.SPANISH_ALPHABET_UPPERCASE_TILDE.find(char) + positions)]
                except IndexError:
                    encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                        self.calculate_position_index(Constants.SPANISH_ALPHABET_UPPERCASE_TILDE, char, positions)]
            else:
                encrypted_string = encrypted_string + char
        return encrypted_string

    def calculate_position_index(self, alphabet, char, positions_to_move):
        self.self_not_used()
        # (1) Se calcula restándole 27 (una vuelta completa al abecedario) al index total (es decir, el index de la
        # letra elegida + las posiciones que eligió el usuario) cuantas veces sea necesario sin sobrepasar el index
        # total (es decir, de x/27 = 2.99, se tomaría el 2 solamente, de lo contrario 27*3 podría dar un número negativo
        # si el index total fuese a ser 80 por ejemplo)
        #
        # (2) Todos estos cálculos son innecesarios, un simple mod era suficiente. Ej: 28 % 27
        calculated_position_index = ((alphabet.find(char) + positions_to_move) -
                                     (Constants.SPANISH_ALPHABET_NUMBER_OF_LETTERS *
                                      math.floor(
                                          ((alphabet.find(char) + positions_to_move)
                                           / Constants.SPANISH_ALPHABET_NUMBER_OF_LETTERS))))
        return calculated_position_index

    def self_not_used(self):
        pass
