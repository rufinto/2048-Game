import random
import numpy as np

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def create_grid(grid_length):
    game_grid = []
    for i in range(grid_length):
        game_grid.append([' ' for j in range(grid_length)])
    return game_grid

def grid_add_new_tile_at_position(game_grid, i, j):
    game_grid[i][j] = random.choice([2,4])
    return game_grid

def get_all_tiles(game_grid):
    grid_length = len(game_grid)
    tiles = []
    for i in range(grid_length):
        for j in range(grid_length):
            if game_grid[i][j] != ' ' :
                tiles.append(game_grid[i][j])
            else :
                tiles.append(0)
    return tiles

def get_value_new_tile():
    value = [2 for i in range(9)]
    value.append(4)
    value = random.choice(value)
    return value

def get_empty_tiles_positions(game_grid):
    grid_length = len(game_grid)
    empty_tiles_positions = []
    for i in range(grid_length):
        for j in range(grid_length) :
            if (game_grid[i][j] == ' ' or game_grid[i][j] == 0):
                empty_tiles_positions.append((i,j))
    return empty_tiles_positions

def get_new_position(game_grid):
    empty_tiles_positions = get_empty_tiles_positions(game_grid)
    i,j = random.choice(empty_tiles_positions)
    return (i,j)

def grid_get_value(game_grid, i, j):
    if game_grid[i][j] == ' ':
        return 0
    return game_grid[i][j]

def grid_add_new_tile(game_grid):
    (i,j) = get_new_position(game_grid)
    grid_add_new_tile_at_position(game_grid,i,j)
    return game_grid

def init_game(grid_length) :
    game_grid = create_grid(grid_length)
    grid_add_new_tile(game_grid)
    grid_add_new_tile(game_grid)
    return game_grid

def grid_to_string(game_grid, grid_length): #on enleve le premier et dernier retour chariot
    string = ""
    for i in range(grid_length):
        string += " ==="*grid_length
        string += "\n"
        string += "| "
        for j in range(grid_length):
            string += f"{game_grid[i][j]}"
            if (j == grid_length-1) :
                string+= " |\n"
            else :
                string += " | "
    string += " ==="*grid_length + " "
    return string

def long_value(game_grid):
    all_tiles = get_all_tiles(game_grid)
    max_length = 0
    for tile in all_tiles :
        if len(str(tile)) > max_length :
            max_length = len(str(tile))
    return max_length

def long_value_with_theme(game_grid, theme):
    all_tiles = get_all_tiles(game_grid)
    max_length = 0
    for tile in all_tiles :
        if len(theme[tile]) > max_length :
            max_length = len(theme[tile])
    return max_length

def numérique_grid(game_grid):
    for ligne in range(len(game_grid)):
        for colonne in range(len(game_grid[0])):
            if game_grid[ligne][colonne]==' ':
                game_grid[ligne][colonne]=0
    return(game_grid)

def grid_to_string_with_size_and_theme(game_grid,theme,grid_length):
    string = ''
    game_grid = numérique_grid(game_grid)
    lignes, colonnes = grid_length, grid_length
    longueur_max = long_value_with_theme(game_grid,theme)
    for ligne in range(lignes):
        for colonne in range(colonnes):
            string+=((' ')+('=')*(longueur_max+2))
        string+=('\n')
        for colonne in range(colonnes):
            différence_longueur = longueur_max - len(theme[game_grid[ligne][colonne]])
            répartition = différence_longueur
            espaces_gauche,espaces_droite=répartition//2+1,répartition-(répartition//2)+1
            string+=(('|')+(' ')*espaces_gauche+theme[game_grid[ligne][colonne]]+(' ')*espaces_droite)
        string+=('|\n') 
    for colonne in range(colonnes):
            string+=((' ')+('=')*(longueur_max+2))
    return string    

def move_row_left(row: list) -> list:
    length = len(row)
    new_row=row.copy()
    def decale_gauche(l: list) -> list:
        l_decalee = []
        for e in l:
            if e != 0:
                l_decalee.append(e)
        l_decalee = l_decalee + [0]*(length-len(l_decalee))
        return l_decalee

    new_row = decale_gauche(new_row)
    for i in range(length-1):
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            new_row[i+1] = 0
    new_row = decale_gauche(new_row)
    return new_row

def move_row_right(row: list) -> list:
    new_row=row.copy()
    new_row.reverse()
    new_row = move_row_left(new_row)
    new_row.reverse()
    return new_row

def move_grid_left(grid):
    n = len(grid)
    new_grid = grid.copy()
    for i in range(n):
        new_grid[i] = move_row_left(grid[i])
    return new_grid

def move_grid_right(grid):
    n = len(grid)
    new_grid = grid.copy()
    for i in range(n):
        new_grid[i] = move_row_right(grid[i])
    return new_grid

def transpose(grid):
    transposee = [list(t) for t in zip(*grid)]
    return transposee

def move_grid_up(grid):
    n = len(grid)
    new_grid = transpose(grid)
    for i in range(n):
        new_grid[i] = move_row_left(new_grid[i])
    return transpose(new_grid)
    
def move_grid_down(grid):
    n = len(grid)
    new_grid = transpose(grid)
    for i in range(n):
        new_grid[i] = move_row_right(new_grid[i])
    return transpose(new_grid) 

def move_grid(grid, d):
    n = len(grid)
    new_grid = grid.copy()
    if d == 'left':
        new_grid = move_grid_left(grid)
    elif d == 'right':
        new_grid = move_grid_right(grid)
    elif d == 'down':
        new_grid = move_grid_down(grid)
    elif d == 'up':
        new_grid = move_grid_up(grid)
    return new_grid

def is_grid_full(grid):
    L = np.array(grid)
    return 0 not in L

def move_possible(grid: list) -> list:
    moves = ["left", "right", "up", "down"]
    possible = ['']*len(moves)
    for i, move in enumerate(moves):
        possible[i] = move_grid(grid, move) != grid
    return possible

def is_game_over(grid):
    if move_possible(grid) == [False, False, False, False]:
        return True
    return False

def get_grid_tile_max(grid):
    L = np.array(grid)
    return np.max(L)