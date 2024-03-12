import os
import time
import Encryptor
import Constants
os.system("")


class Menu:

    def initialize_encryptor_menu(self):
        self.show_message(Constants.MAIN_MENU)
        self.wait_seconds(Constants.TIME_BETWEEN_MESSAGES)
        self.show_message(Constants.MAIN_MENU_OPTIONS)
        self.wait_seconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            user_menu_choice = self.get_user_choice()
            self.wait_seconds(Constants.TIME_BETWEEN_MESSAGES)
            if user_menu_choice == "1":
                self.show_message(Constants.ENCRYPT_CHAR_BY_N_POSITIONS_DESC)
                while True:
                    user_encryption_mode_confirmation = self.get_user_choice(Constants.CONFIRM_CHOICE_YES_OR_NO)
                    if user_encryption_mode_confirmation in Constants.USER_SET_FOR_YES:
                        string_to_encrypt = self.get_user_string()
                        positions_to_move = int(self.get_user_choice(Constants.REQUEST_USER_POSITIONS_TO_MOVE))
                        encrypted_string = Encryptor.Encryptor().replace_char_by_n_positions(string_to_encrypt,
                                                                                             positions_to_move)
                        self.show_message(Constants.SUCCESSFUL_ENCRYPTION)
                        self.show_message(encrypted_string)
                        break
                    elif user_encryption_mode_confirmation in Constants.USER_SET_FOR_NO:
                        self.wait_seconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.show_message(Constants.MAIN_MENU_OPTIONS)
                        self.wait_seconds(Constants.TIME_BETWEEN_MESSAGES)
                        continue
                    else:
                        self.show_warning(Constants.WARNING_INVALID_YES_OR_NO_CHOICE)
                break
            else:
                self.show_warning(Constants.WARNING_INVALID_CHOICE)

    # --------Relacionado a texto-------- |
    def self_not_used(self):
        # IDE deja de advertir "static" utilizando este método en otros que no hacen uso de self
        pass

    def show_message(self, message):
        self.self_not_used()
        return print(message)

    def show_warning(self, warning):
        self.self_not_used()
        self.show_message("\n" + warning)
        self.wait_seconds(Constants.TIME_BETWEEN_WARNINGS)
        up = '\x1b[1A'
        clear = '\x1b[2K'
        print(up, end=clear)
        print(up, end=clear)
        print(up, end=clear)
        return

    def get_user_choice(self, prompt=Constants.CONFIRM_CHOICE):
        self.self_not_used()
        return input(prompt)

    def get_user_string(self):
        self.self_not_used()
        return input(Constants.REQUEST_USER_STRING)

    def wait_seconds(self, seconds):
        self.self_not_used()
        return time.sleep(seconds)


