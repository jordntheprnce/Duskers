class Game:
    def __init__(self):
        self.flag = True
        self.control = True

    def thanks(self):
        print('Thank you for playing, bye!')
        exit()

    def invalid(self):
        print('Invalid input')

    def command(self):
        command_input = input('\nYour command:\n')
        return command_input

    def hub(self):
        loop = True
        while loop:
            print('''+==============================================================================+
               ╔═╗      |       ╔═══╗      |     ═╦═
            ╔═╗╚╦╝╔═╗   |     ╔═╩═══╩═╗    |      ║
            ║ ╚═╬═╝ ║   |     ║       ║    |     ╔╩═╦═════════╗
               ╔╩╗      |     ║ ║║ ║║ ║    |     ╚══╣         ║
             ╔═╝ ╚═╗    |     ║ ║║ ║║ ║    |        ╚╦╦═════╦╦╝
             ║     ║    |     ║       ║    |       ╔═╝╚═╗ ╔═╝╚═╗
             ║     ║    |     ╚═══════╝    |       ║    ║ ║    ║
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+''')

            while True:
                hub_choice = self.command().upper()
                if hub_choice == 'EX':
                    print('\nComing SOON! Thanks for playing!')
                    exit()

                elif hub_choice == 'SAVE':
                    print('\nComing SOON! Thanks for playing!')
                    exit()

                elif hub_choice == 'UP':
                    print('\nComing SOON! Thanks for playing!')
                    exit()

                elif hub_choice == 'M':
                    game_menu_choice = self.game_menu()
                    if game_menu_choice == 'MAIN':
                        return False

                    elif game_menu_choice == 'BACK':
                        break

                    elif game_menu_choice == 'SAVE':
                        print('\nComing SOON! Thanks for playing!')
                        exit()

                    else:
                        self.thanks()

                elif hub_choice == 'EXIT':
                    self.thanks()

                else:
                    self.invalid()

    def game_menu(self):
        print('''                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|''')

        return self.command().upper()

    def main_menu(self):
        b = '⚫'
        w = '⚪'

        if self.control:
            print(f"""{b * 5}{w}   {b * 4}{w}   {b * 3}{w}    {b * 5}{w}   {b * 2}{w}  {b * 2}{w}    {b * 3}{w}
{b * 6}{w}  {b * 3}{w}   {b * 4}{w}   {b * 6}{w} {b * 2}{w}  {b * 2}{w}   {b * 4}{w}
{b * 2}{w}  {b * 2}{w}   {b * 2}{w}   {b * 2}{w}        {b * 2}{w}  {b * 2}{w} {b * 2}{w}  {b * 2}{w}  {b * 2}{w}
{b * 2}{w}  {b * 2}{w}   {b * 2}{w}   {b * 2}{w}        {b * 2}{w}  {b * 2}{w} {b * 2}{w}  {b * 2}{w}  {b * 2}{w}
{b * 2}{w}  {b * 2}{w}   {b * 2}{w}   {b * 2}{w} {b * 2}{w} {b * 2}{w}  {b * 2}{w} {b * 2}{w}  {b * 2}{w}  {b * 2}{w} {b * 2}{w}
{b * 2}{w}  {b * 2}{w}   {b * 2}{w}   {b * 2}{w} {b * 2}{w} {b * 2}{w}  {b * 2}{w} {b * 2}{w}  {b * 2}{w}  {b * 2}{w} {b * 2}{w}
{b * 6}{w}  {b * 3}{w}   {b * 4}{w}   {b * 6}{w} {b * 6}{w}   {b * 4}{w}
{b * 5}{w}   {b * 4}{w}   {b * 3}{w}    {b * 5}{w}   {b * 6}{w}    {b * 3}{w}""")
            print('''
[Play]
[High] Scores
[Help]
[Exit]''')

        return self.command().upper()

    def play(self):
        name = input('\nEnter your name:\n')
        print('\nGreetings, commander %s!\nAre you ready to begin?\n[Yes] [No] Return to Main[Menu]' % name)
        return name

    def high(self):
        while True:
            print('\nNo scores to display.\n    [Back]')

            back = self.command().lower()

            if back == 'back':
                print('\n')
                break

            elif back == 'exit':
                self.thanks()

            else:
                self.invalid()

    def help_(self):
        print('\nComing SOON! Thanks for playing!')

    def main(self):
        while self.flag:
            menu_choice = self.main_menu()
            self.control = True

            if menu_choice in ('EXIT', 'QUIT'):
                self.thanks()

            elif menu_choice == 'PLAY':
                self.play()

                while True:
                    ready = self.command().upper()
                    if ready in ('EXIT', 'QUIT'):
                        self.thanks()

                    elif ready == 'YES':
                        self.hub()
                        break

                    elif ready == 'NO':
                        print('How about now.\nAre you ready to begin?\n   [Yes]  [No]')
                        continue

                    elif ready == 'MENU':
                        break

                    else:
                        self.invalid()

            elif menu_choice == 'HIGH':
                self.high()

            elif menu_choice == 'HELP':
                self.help_()
                break

            else:
                self.invalid()
                self.control = False
                continue


if __name__ == '__main__':
    game = Game()
    game.main()
