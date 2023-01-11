import random


game_board = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']
game_on = True
player2_choice = ''


def display_board(board):
    print('\n' * 100)
    print(f'{board[7]} | {board[8]} | {board[9]}\n---------\n{board[4]} | {board[5]} | {board[6]}\n---------\n'
          f'{board[1]} | {board[2]} | {board[3]}')


def player_input():
    global player2_choice
    initial_marker_choice = True

    while initial_marker_choice:
        user_marker_choice = str(input('Player 1 Do you want X or O? '))

        if user_marker_choice == 'X' or user_marker_choice == 'O':
            if user_marker_choice == 'X':
                player2_choice = 'O'
            else:
                player2_choice = 'X'
            initial_marker_choice = False

    return user_marker_choice


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    global game_on
    if board[1] == mark and board[2] == mark and board[3] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        print('Congratulations! You have won the game!')
        game_on = False
        return True
    return False


def choose_first():
    choose_player = random.randint(1, 3)
    if choose_player == 1:
        print('Player 1 Will Go First')
        return 'player1'
    else:
        print('Player 2 Will Go First')
        return 'player2'


def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    return True


def full_board_check(board):
    if '-' in board:
        return False
    else:
        return True


def player_choice(board):

    user_position = int(input('Choose your next position: '))

    if space_check(board, user_position) and not full_board_check(board):
        return user_position
    else:
        print('You have chosen incorrect position')


def replay():
    game_continue = input('Do you want to continue with game? Y or N')
    if game_continue == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    player1_choice = player_input()
    user_preference = choose_first()

    play_or_not = input('Are you ready to play? Enter Yes or No. ')
    if play_or_not == 'Yes':
        display_board(game_board)
        while game_on:
            if user_preference == 'player1':
                player1_position = player_choice(game_board)
                place_marker(game_board, player1_choice, player1_position)
                display_board(game_board)
                win_check(game_board, player1_choice)
                user_preference = 'player2'
            else:
                player2_position = player_choice(game_board)
                place_marker(game_board, player2_choice, player2_position)
                display_board(game_board)
                win_check(game_board, player2_choice)
                user_preference = 'player1'
    else:
        break

    if not replay():
        break





