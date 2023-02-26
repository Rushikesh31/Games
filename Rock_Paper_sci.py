import random as rd
winner = 0

def get_name():
    '''This will get the name of the user'''
    user = input("Enter your name : ").capitalize()
    print(f"Welcome {user} !!!")
    return user


def get_symbol():
    '''This will select the choice of the user'''
    print('''Choose the symbol
    🪨  -   1
    📄 -   2
    ✂️  -   3
    ''')
    choice = input('Enter the choice: ')
    symbols = {
        '1': "Rock",
        '2': "Paper",
        '3': "Scissor"
    }
    symbol = [y for x, y in symbols.items() if x == choice]
    return str(symbol[0])


def computers_choice():
    '''This will get the Computers choice'''
    choices = ["Rock", "Paper", "Scissor"]
    Computer_choice = rd.choice(choices)
    return Computer_choice

def main():
    '''This method will run till the user provides N as response'''

    user = get_name()  # It will get the user name

    while True:

        print() 
        your_turn = get_symbol()
        print()
        print(f"You have chosen {your_turn}.")
        print()
        computers_turn = computers_choice()
        print(f"Computer has chosen {computers_turn}.")
        print()
        if (your_turn == computers_turn):
            print('Match got tied. Try again.')
            winner = 0
        else:
            if (your_turn == "Rock"):
                if (computers_turn == "Paper"):
                    print('Sorry you lost 🙁.')
                    winner = 2
                else:
                    print('Hurray! you won 😀.')
                    winner = 1
            elif (your_turn == "Paper"):
                if (computers_turn == "Scissor"):
                    print('Sorry you lost 🙁.')
                    winner = 2
                else:
                    print('Hurray! you won 😀.')
                    winner = 1
            elif (your_turn == "Scissor"):
                if (computers_turn == "Rock"):
                    print('Sorry you lost 🙁.')
                    winner = 2
                else:
                    print('Hurray! you won 😀.')
                    winner = 1
        print()
        print("Conclusion: ")
        print('-*-'*10)
        if (winner == 0):
            print('Match got tied.')
        elif (winner == 1):
            print(f"{user} has won the game.")
        else:
            print('Computer has won the game.')

        print()

        play = input("Do you want to play again? (Y/N): ").upper()
        if (play != 'Y'):
            print()
            print("-----Thank you!-----")
            print()
            break
        
main()