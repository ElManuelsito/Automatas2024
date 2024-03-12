import Constants


class Encryptor:
    def replace_char_by_n_positions(self, string, positions):
        self.self_not_used()
        encrypted_string = ""
        for char in string:
            if char in Constants.SPANISH_ALPHABET_LOWERCASE:
                encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                    (Constants.SPANISH_ALPHABET_LOWERCASE.find(char) + positions)]
            elif char in Constants.SPANISH_ALPHABET_LOWERCASE_TILDE:
                encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_LOWERCASE[
                    (Constants.SPANISH_ALPHABET_LOWERCASE_TILDE.find(char) + positions)]
            elif char in Constants.SPANISH_ALPHABET_UPPERCASE:
                encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                    (Constants.SPANISH_ALPHABET_UPPERCASE.find(char) + positions)]
            elif char in Constants.SPANISH_ALPHABET_UPPERCASE_TILDE:
                encrypted_string = encrypted_string + Constants.SPANISH_ALPHABET_UPPERCASE[
                    (Constants.SPANISH_ALPHABET_UPPERCASE_TILDE.find(char) + positions)]
            else:
                encrypted_string = encrypted_string + char
        return encrypted_string

    def self_not_used(self):
        pass
