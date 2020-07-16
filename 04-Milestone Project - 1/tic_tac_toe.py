def print_options():
    print("\n")
    print(' 7 | 8 | 9 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 1 | 2 | 3 ')
    print("\n")

def instructions():
    go = None
    print("\n")
    print('--------------------------------------')
    print('          TIC TAC TOE GAME            ')
    print('--------------------------------------')
    print("\n")
    print('Instructions: This is a 2 players game')
    print('                                      ')
    print('Player One: Select X or O to play     ')
    print("Later, choose your mark's place       ")
    print('                                      ')
    print('These are your options:               ')
    print('                                      ')
    print_options()
    print('                                      ')
    print('Are you ready to play?                ')

    while go not in ['Y','N']:
        go = (input('Select [Y] or [N]: ').upper())

    return go == 'Y'

def select_icons():
    d = {'Player ONE':'','Player TWO':''}
    mark = None

    print("\n"*50)
    print("Hey Player ONE: It's your turn to choose    ")
    print('')
    print("What mark do you prefer to play: 'X' or 'O'?  ")
    print('')

    while mark not in ['X', 'O']:
        mark = input("I want to be: ").upper()
        print("\n"*50)
    d['Player ONE'] = mark
    if d['Player ONE'] ==  'X':
        d['Player TWO'] = 'O'
    else:
        d['Player TWO'] = 'X'

    print('')
    print(f"Great, Player ONE will be {d['Player ONE']} and \nPlayer TWO will be {d['Player TWO']} \n")
    print("\nLet's go...\n")
    print_options()
    return(d)

def print_who_won(results, icons, game_over):
    win = game_over[1]
    if game_over[1] == 'tie':
        print("Shame on you. It was a tie")
    elif icons['Player ONE'] == win:
        print('')
        print('------------------------------------------')
        print(f'Congratulations: Player ONE wins with {win}')
        print('------------------------------------------')
        print('')
    else:
        print('')
        print('------------------------------------------')
        print(f'Congratulations: Player TWO wins with {win}')
        print('------------------------------------------')
        print('')

def play_again():
    again = None
    while again not in ['Y', 'N']:
        again = (input('Do you want to play again? [Y]es or [N]o: ')).upper()

    if again == 'N':
        print('Goodbye Cowboy')
    else:
        tic_tac_toe()

def print_board(results):
    r = results
    print('\n'*50)
    print(" " + r[7] + " | " + r[8] + " | " + r[9] + " " )
    print('-------------')
    print(" " + r[4] + " | " + r[5] + " | " + r[6] + " " )
    print('-------------')
    print(" " + r[1] + " | " + r[2] + " | " + r[3] + " " )
    print('\n')

def is_there_a_winner(results, posibilities):
    r = results
    p = posibilities
    if  r[1] == r[2] == r[3] == 'X' or r[4] ==r[5] ==r[6] == 'X' or r[7] == r[8] == r[9] == 'X' or r[1] == r[4] ==r[7] == 'X' or r[2] ==r[5] ==r[8] == 'X' or [3] == r[6] == r[9] == 'X' or r[1] ==r[5] ==r[9] == 'X' or r[3] == r[5] == r[7] == 'X':
        return [True,'X']
    elif r[1] == r[2] == r[3] == 'O' or r[4] ==r[5] ==r[6] == 'O' or r[7] == r[8] == r[9] == 'O' or r[1] ==r[4] ==r[7] == 'O' or r[2] ==r[5] ==r[8] == 'O' or [3] == r[6] == r[9] == 'O' or r[1] ==r[5] ==r[9] == 'O' or r[3] == r[5] == r[7] == 'O':
        return [True,'O']
    elif r.count('') > 0:
        return False
    else:
        return [True, 'tie']


def game(icons, results):
    i = icons
    r = results
    posibilities = ['x','1','2','3','4','5','6','7','8','9','0']
    turn_p1 = True
    game_over = False

    while game_over == False:
        if turn_p1 == True:
            choice = ''
            print(f"Choose one of the options: {posibilities[1:-1:]}")
            #print_board(r)
            while choice not in posibilities[1:-1:]:
                choice = input(f"Player ONE, Where do you want to put your {i['Player ONE']} mark? ")
                if choice in posibilities[1:-1:]:
                    # append choice in r
                    r[int(choice)] = i['Player ONE']
                    # print board with x or o
                    print_board(r)
                    # check if somebody win
                    game_over = is_there_a_winner(r, posibilities)
                    #remove choice from posibilites
                    posibilities.remove(choice)
                    # shift turn
                    turn_p1 = False
                    break

        else:
            print("\n")
            print(f"Player TWO, It's your turn. Choose one of the options: {posibilities[1:-1:]}")
            while choice not in posibilities:
                choice = input(f"Player TWO, Where do you want to put your {i['Player TWO']} mark? ")
                if choice in posibilities[1:-1:]:
                    # append choice in r
                    r[int(choice)] = i['Player TWO']
                    # print board with x or o
                    print_board(r)
                    # check if somebody win
                    game_over = is_there_a_winner(r, posibilities)
                    #remove choice from posibilites
                    posibilities.remove(choice)
                    # shift turn
                    turn_p1 = True
                    break

    print_who_won(r,i,game_over)

def tic_tac_toe():
    icons = {}
    results = ['_','','','','','','','','','']
    game_over = False

    go = instructions()

    if go == True:

        icons = select_icons()

        game(icons, results)

        play_again()

    else:
        print('Goodbye Cowboy')


if __name__ == "__main__" :

    tic_tac_toe()