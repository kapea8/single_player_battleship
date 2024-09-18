#Code provided by professor and tweaked for my project
import random

def place_ships(board):
    # stores the length of each ship to be placed
    ships = [3, 2, 2]
    height = len(board)
    width = len(board[0])
    ships_dict = {}
    # create a list of tuples containing every position
    all_positions = [(j, i) for i in range(height) for j in range(width)]

    ships_placed = 0
    # make sure we're modifying a copy, not the original board
    board_copy = [row.copy() for row in board]
    # stop when we've placed all ships
    while ships_placed < len(ships):
        random_positions = all_positions.copy()
        # get a list of random position to try to place the ship in
        random.shuffle(random_positions)
        position_found = False
        ship_length = ships[ships_placed]
        # continue to try to place the ship until we find a working position
        for position in random_positions:
            position_found = try_place_ship(board_copy, position, ship_length)
            if position_found != False:
                # move our counter to the next ship we need to place
                ships_placed += 1
                ships_dict[f'Ship {ships_placed}'] = position_found[1]
                break
    return board_copy, ships_dict

# Tries to place a ship and returns False if it doesn't succeed
def try_place_ship(board, position, ship_length):
    (x, y) = position
    # A list of the increments to x and y for every direction (up, right, left, down)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if not is_empty_coords(board, x, y):
        return False
    position_found = False
    random.shuffle(directions)
    # Try to place the ship facing in every direction (using a random order)
    for direction in directions:
        # See if all of the spaces in this direction are empty
        for i in range(1, ship_length):
            if not is_empty_coords(board, x + (i * direction[0]), y + (i * direction[1])):
                position_found = False
                break
            position_found = True
        # if the all of the spaces are empty, place the ship by modifying board
        if position_found:
            ship = []
            for i in range(0, ship_length):
                board[y + (i * direction[1])][x + (i * direction[0])] = 'B'
                ship.append((y + (i * direction[1]), x + (i * direction[0])))
            return True, ship
    # if we get here we tried all directions and still couldn't place the ship
    return False


def is_empty_coords(board, x, y):
    # a space is empty if the space is within bounds and it contains an E
    return y >= 0 and y < len(board) and x >= 0 and x < len(board[0]) and board[y][x] == '-'
