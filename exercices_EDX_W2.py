# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:51:31 2020

@author: Sam
"""

import numpy as np

# Excercice 1

def create_board():
    array = np.zeros((3,3))
    
    return array
    
#print(create_board())
board = create_board()    


# Excercice 2
    
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        
    return board

player_1 = 1
player_2 = 2
position_0 = (0, 0)

board = place(board, player_1, position_0)
#print(board)


# Exercice 3

def possibilities(board):
    possible_tuple = tuple()
    possible_list = np.where(board < 1)
    
    for i in range(len(possible_list[0])):
        possible_tuple = possible_tuple + tuple([(possible_list[0][i], possible_list[1][i])])
    
    return possible_tuple

#possible = possibilities(board)
#print(possible)

# Exercice 4

import random 
random.seed(1)

def random_place(board, player):
    possible = possibilities(board)

    if possible:
        placement = random.choice(possible)
        board = place(board, player, placement)
    
    return board

board = random_place(board, player_2)
#print(board)


# Exercice 5

random.seed(1)
new_board = create_board()

for i in range(3):
    new_board = random_place(new_board, player_1)
    new_board = random_place(new_board, player_2)

#print(new_board)


# Exercice 6

def row_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    
    return False

#print(row_win(new_board, player_1))


# Exercice 7

def col_win(board, player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    return False

#print(col_win(new_board, player_1))



# Exercice 8
            
#new_board[1,1] = 2

def diag_win(board, player):
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player or
            board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True

        return False
        
#print(diag_win(new_board, player_2))



# Exercice 9
            
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or 
            diag_win(board, player)):
            return player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

#print(evaluate(new_board))



# Exercice 10
"""
random.seed(1)

def play_game():
    player_1 = 1
    player_2 = 2
    board = create_board()
    
    while not board.all():
        board = random_place(board, player_1)
        if evaluate(board) > 0:
            return evaluate(board)
        board = random_place(board, player_2)
        if evaluate(board) > 0:
            return evaluate(board)

    return -1


result = []

for i in range(1000):
    result.append(play_game());

#print(result)  
print(result.count(-1))
print(result.count(1))
print(result.count(2))

import matplotlib.pyplot as plt

plt.hist(result)
"""
# Exercice 11

random.seed(1)

def play_strategic_game():
    player_1 = 1
    player_2 = 2
    board = create_board()
    
    while not board.all():
        if not board.any():
            place(board, player_1, (1,1))
        else:
            board = random_place(board, player_1)    
        if evaluate(board) > 0:
            return evaluate(board)
        board = random_place(board, player_2)
        if evaluate(board) > 0:
            return evaluate(board)

    return -1


result = []

for i in range(1000):
    result.append(play_strategic_game());


#print(result.count(-1))
#print(result.count(1))
#print(result.count(2))

import matplotlib.pyplot as plt
plt.hist(result)



























