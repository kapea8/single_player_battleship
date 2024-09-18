import ships
import termcolor

def create_board(length):
    lst = []
    for i in range(length):
        lst.append(['-']*length)
    return lst

def create_ships_grid(ships, guesses_grid):
    ships_grid = [row.copy() for row in guesses_grid]
    for val in ships.values():
        for item in val:
            ships_grid[item[0]][item[1]] = 'B'
    return ships_grid

def print_board(board):
    column_labels = '   '.join(str(i) for i in range(len(board)))
    print('    ' + column_labels)
    print('  ' + '-' * ((len(board) * 4) + 1))
    for row in range(len(board)): 
        for item in range(len(board[row])):
            if board[row][item] == 'M':
                board[row][item] = termcolor.colored(board[row][item],'blue')
            elif board[row][item] == 'H':
                board[row][item] = termcolor.colored(board[row][item], 'red')
        display_row = str(row) + ' | ' + ' | '.join(board[row]) + ' |'
        print(display_row)
        print('  '+'-' * ((len(board) * 4) + 1))

def reading_guesses(guesses_grid):
    row = int(input(f'Pick a row number (0-{len(guesses_grid)-1}): '))
    column = int(input(f'Pick a column number (0-{len(guesses_grid)-1}): '))
    while not 0 <= row < len(guesses_grid) or not 0 <= column < len(guesses_grid) or guesses_grid[row][column] != '-':
        if not 0 <= int(row) < len(guesses_grid) or not 0 <= int(column) < len(guesses_grid):
            print('That is outside the bounds of the board. Please choose again.')
        elif guesses_grid[row][column] != '-':
            print('You have already guessed that spot. Please choose again.')
        row = int(input(f'Pick a row number (0-{len(guesses_grid)-1}): '))
        column = int(input(f'Pick a column number (0-{len(guesses_grid)-1}): '))
    guess = (row, column)
    return guess

def updating_guesses(guesses_grid, ships_grid, guess):
    if ships_grid[guess[0]][guess[1]] == 'B':
        guesses_grid[guess[0]][guess[1]] = 'H'
        print('Hit!')
    else:
        guesses_grid[guess[0]][guess[1]] = 'M'
        print('Miss!')
    return guesses_grid

def count_ships(ships_grid):
    ship_squares = 0
    for i in range(len(ships_grid)):
        for j in range(len(ships_grid[i])):
            if ships_grid[i][j] == 'B':
                ship_squares += 1
    return ship_squares

def sunk_ship(ships, guesses_grid, ships_grid):
    for key in ships:
        count = 0
        for item in ships[key]:
            if guesses_grid[item[0]][item[1]] != '-' and ships_grid[item[0]][item[1]] == 'B':
                count += 1      
        if count == len(ships[key]):
            print(f'You sunk a ship of length {len(ships[key])}!')
            del ships[key]
            return True
    return False

guesses_grid = create_board(4)
ships = ships.place_ships(guesses_grid)[1]
ships_grid = create_ships_grid(ships, guesses_grid)

def playing_game(guesses_grid, ships_grid, ships):
    print("Welcome to Battleship!")
    print_board(guesses_grid)
    guesses = 12
    print(f'Guesses: {guesses}')
    ships_sunk = 0
    while guesses > 0 and ships_sunk < len(ships):
        guess = reading_guesses(guesses_grid)
        guesses -= 1
        guesses_grid = updating_guesses(guesses_grid, ships_grid, guess)
        sunk_ship(ships, guesses_grid, ships_grid)
        if sunk_ship(ships, guesses_grid, ships_grid):
            ships_sunk += 1
        print_board(guesses_grid)
        print(f'Guesses remaining: {guesses}')
    if ships_sunk == len(ships):
        print('Congrats! You sunk all the ships!')
    else:
        print('Sorry, you lost.')

playing_game(guesses_grid, ships_grid, ships)
