from grid_2048 import *

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def read_player_command():
    commands = ['left', 'right', 'up', 'down']
    move = ''
    while move not in commands :
        move = input("Entrez votre commande (left, right, up, down):")
    return move

def read_size_grid():
    size = input("Entrez votre taille de grille :")
    while int(size)<=0 :
        size = input("Entrez une taille de grille positive:")
    return int(size)
    
def read_theme_grid():
    theme = input("Entrez votre theme (1 (default), 2 (chemistry), 3 (alphabet)):")
    while int(theme) not in [1,2,3]:
        theme = input("Entrez votre theme (1 (default), 2 (chemistry), 3 (alphabet)):")
    return THEMES[str(int(theme) -1)]

def random_play():
    size, theme, consignes_déplacement = 4, THEMES["0"], ['left','right','up','down']
    grid = init_game(size)
    dessin_grid = grid_to_string_with_size_and_theme(grid,theme,size)
    print(dessin_grid)
    while not is_game_over(grid):
        d = consignes_déplacement[random.choice([0,1,2,3])]
        grid = move_grid(grid,d)
        grid = grid_add_new_tile(grid)
        dessin_grid = grid_to_string_with_size_and_theme(grid,theme,size)
        print(dessin_grid)
    if get_grid_tile_max(grid) == 2048:
        print('Victoire')
    else:
        print('Défaite')
    return 

def game_play():
    size, theme = read_size_grid(), read_theme_grid()
    grid = init_game(size)
    dessin_grid = grid_to_string_with_size_and_theme(grid,theme,size)
    print(dessin_grid)
    while not is_game_over(grid):
        d = read_player_command()
        grid = move_grid(grid,d)
        grid = grid_add_new_tile(grid)
        dessin_grid = grid_to_string_with_size_and_theme(grid,theme,size)
        print(dessin_grid)
    if get_grid_tile_max(grid) == 2048:
        print('Victoire')
    else:
        print('Défaite')
    return 

if __name__ == '__main__':
    game_play()
    exit(1)  

 