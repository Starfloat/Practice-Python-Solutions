# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

while True:
    # player 1 choice
    while True:
        player1 = input('Player1: Rock, paper, or scissors?\n')
        if player1 != 'rock' and player1 != 'paper' and player1 != 'scissors':
            continue
        print('Player1 chose', player1)
        break

    # player 2 choice
    while True:
        player2 = input('Player2: Rock, paper, or scissors?\n')
        if player2 != 'rock' and player2 != 'paper' and player2 != 'scissors':
            continue
        print('Player2 chose', player2)
        break

    if player1==player2:
        print('Draw!')
    elif player1=='rock' and player2=='scissors':
        print('Player 1 wins')
    elif player1=='scissors' and player2=='paper':
        print('Player 1 wins')
    elif player1=='paper' and player2=='rock':
        print('Player 1 wins')
    elif player1=='scissors' and player2=='rock':
        print('Player 2 wins')
    elif player1=='paper' and player2=='scissors':
        print('Player 2 wins')
    elif player1=='rock' and player2=='paper':
        print('Player 2 wins')
        
    print('Play again? (y/n)')

    replay = input()

    if replay != 'y' and replay != 'n':
        continue
    if replay == 'n':
        print('Goodbye.')
        break


