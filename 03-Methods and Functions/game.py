from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    
    while guess not in ['0', '1', '2']:
        guess = input('Make a choice, where is the ball: 0, 1 or 2: ?')
    return int(guess)

    
def play_game(my_list, guess):
        if my_list[guess] == 'O':
            print('Correct')
        else:
            print('Wrong!')
            print(my_list)

if  __name__ == '__main__':
    original_list = [' ', 'O', ' ']
    mixed_list = shuffle_list(original_list)
    guess = player_guess()
    play_game(mixed_list, guess)