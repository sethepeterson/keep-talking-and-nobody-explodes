from os import system

class PasswordCracker:

    def __init__(self):
        self.test_mode = False

        self.first_column_chars = None
        self.second_column_chars = None
        self.third_column_chars = None
        self.fourth_column_chars = None
        self.fifth_column_chars = None

        self.word_bank = ['about', 'after', 'again', 'below', 'could',
                            'every', 'first', 'found', 'great', 'house',
                            'large', 'learn', 'never', 'other', 'place',
                            'plant', 'point', 'right', 'small', 'sound',
                            'spell', 'still', 'study', 'their', 'there',
                            'these', 'thing', 'think', 'three', 'water',
                            'where', 'which', 'world', 'would', 'write']


    def crack_password(self):
        _ = system('cls')
        print('\nPASSWORD CRACKER....\n___________________________')

        if self.test_mode:
            self.first_column_chars = 'TYHQVF'.lower()
            self.second_column_chars = 'CGIBWH'.lower()
            self.third_column_chars = 'BZUSIT'.lower()
            self.fourth_column_chars = 'WVMHNG'.lower()
            self.fifth_column_chars = 'ZRMVKO'.lower()
                
        else:
            self.get_columns()

        for first_char in self.first_column_chars:
            for second_char in self.second_column_chars:
                for third_char in self.third_column_chars:
                    for fourth_char in self.fourth_column_chars:
                        for fifth_char in self.fifth_column_chars:
                            possible_word = first_char + second_char + third_char + fourth_char + fifth_char

                            for word in self.word_bank:
                                if word == possible_word:
                                    print('\nPassword: {}\n'.format(possible_word))
                                    _ = input()
                                    return

                            print(possible_word)
        
        print('\n\nPassword cracking failed.')
        _ = input()




    def get_columns(self):
        print('\nInput columns character choices as one word (case-insensitive, 6 characters)!')
        self.first_column_chars = self.get_column_input('\n\tFirst column: ')
        self.second_column_chars = self.get_column_input('\n\tSecond column: ')
        self.third_column_chars = self.get_column_input('\n\tThird column: ')
        self.fourth_column_chars = self.get_column_input('\n\tFourth column: ')
        self.fifth_column_chars = self.get_column_input('\n\tFifth column: ')

        
    def get_column_input(self, prompt_message: str) -> str:
        user_input = input(prompt_message)

        while user_input is None or not isinstance(user_input, str) or len(user_input) != 6:
            print('\tInvalid input (6 characters required).')
            user_input = input(prompt_message)
        
        return user_input.lower()
        
password_cracker = PasswordCracker()
password_cracker.crack_password()
