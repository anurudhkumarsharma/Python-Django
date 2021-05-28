def display_func(board):
    print('\n'*10)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

board=' '*10
display_func(board)

def player_input():
    worker=''
    while worker!='x' and worker!='o':
        worker=input('player 1 choose x or o:')
    player1=worker

    if player1=='x':
       player2='o'
    else:
        player2='x'
    return(player1,player2)
player_input()

    
    