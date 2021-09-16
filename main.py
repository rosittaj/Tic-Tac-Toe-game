import random #Tic Tac Toe game
board = {'1': " ", '2': " ", '3': " ", '4': " ", '5': " ", '6': " ", '7': " ", '8': " ", '9': " ", }
history = {1: []}
allhistory=['']
board_keys = []
for key in board:
    board_keys.append(key)
def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'], "\n-----")
    print(board['4'] + '|' + board['5'] + '|' + board['6'], "\n-----")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def player_choice(board, turn):
    position = 0
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while position not in list:
        if turn == 'X':
            position = input("The " + turn + " Choose your next position: (1-9):  ")
        else:
            position = random.choice(list)
            print("The " + turn + " Choosed position: (1-9) is :  ", position)
    return position
def player(turn):
    if turn == 'X':
        turn = 'O'
        return turn
    else:
        turn = 'X'
        return turn
def replay():
    restart = input('Do you want to play again? Enter Yes or No: ').lower()
    if restart == 'y':
        for key in board_keys:
            board[key] = " "
        game()
def space_check(board, position, turn, count):
    if board[position] == ' ':
        board[position] = turn
        count += 1
        return count
    else:
        print("alredy used! ")
        count += 1
        return count
def historydetails(allhistory):
    round_history = int(input(" enter the round (1-10) : 0 exit"))
    while round_history != 0:
        print(allhistory[round_history])
        round_history = int(input(" enter the round (1-10) : "))
def game():
    turn = 'X'
    count = 0
    for i in range(0, 9):
        print_board(board)
        position = player_choice(board, turn)
        count = space_check(board, position, turn, count)
        if count >=3 and board['1'] == board['2'] == board['3'] != ' ' or board['1'] == board['4'] == board['7'] != ' ' or board['1'] == board['5'] == board['9'] != ' ' or board['7'] == board['8'] == board['9'] != ' ' or board['4'] == board['5'] == board['6'] != ' ' or board['7'] == board['5'] == board['3'] != ' ' or board['2'] == board['5'] == board['8'] != ' ' or board['3'] == board['6'] == board['9'] != ' ':
            print_board(board)
            print("\nGame Over.\n **** " + turn + " won. ****")
            break
        if count== 9 and board['1'] != board['2'] != board['3'] == ' ' and board['1'] != board['4'] != board['7'] == ' ' and board['1'] != board['5'] != board['9'] == ' ' and board['7'] != board['8'] != board['9'] == ' ' and board['4'] != board['5'] != board['6'] == ' ' and board['7'] != board['5'] != board['3'] == ' ' and board['2'] != board['5'] != board['8'] == ' ' and board['3'] != board['6'] != board['9'] == ' ':
            print("\nGame Over...!!")
            break
        value = board.values()
        history = [value, turn]
        allhistory.append(history)
        turn = player(turn)
for i in range(2):
    for key in board_keys:
        board[key] = " "
    game()
historydetails(allhistory)