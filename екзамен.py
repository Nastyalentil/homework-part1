from random import randint

board = list(range(1, 10))

wins_coordinates = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def user_position(player_token):
    while True:
        user_char = input('Оберіть клітинку: ' + player_token)
        if not (user_char in '123456789'):
            print('Цієї клітинуи немає, оберіть одну із запропонованих та введіть ще раз.')
            continue
        user_char = int(user_char)
        if str(board[user_char - 1]) in 'XO':
            print('Ця клітинка вже зайнята.')
            continue
        board[user_char - 1] = player_token
        break


def computer_position(player_token):
    computer_char = randint(0, 8), randint(0, 8)
    while computer_char != '_':
        computer_char = randint(0, 8), randint(0, 8)
        board = player_token
        return computer_char


def check_win():
    for each in wins_coordinates:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            user_position('X')
        else:
            computer_position('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'Переміг.')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Нічия.')
            break


main()
