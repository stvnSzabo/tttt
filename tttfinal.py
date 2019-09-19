project_board = ['1','2','3','4','5','6','7','8','9']


def printboard():
    print('\n'*2)
    print(' -------------')
    print( ' | ' + project_board[0] + ' | ' + project_board[1] + ' | ' + project_board[2] + ' | ')
    print(' -------------')
    print( ' | ' +  project_board[3] + ' | ' + project_board[4] + ' | ' + project_board[5] + ' | ')
    print(' -------------')
    print( ' | ' +  project_board[6] + ' | ' + project_board[7] + ' | ' + project_board[8] + ' | ')
    print(' -------------')
    print('\n')



def setplayer():
    player1 = ''
    player2 = ''
    while player1 == '' and player2 == '':
        ques = input('Player1, do you want to be X or O? ').upper()
        if ques == 'X':
            player1 = 'X'
            player2 = 'O'
        elif ques == 'O':
            player1 = 'O'
            player2 = 'X'
            
    return (player1,player2)


player1,player2 = setplayer()

print('\n'*2)
print(' -------------')
print( ' | ' + project_board[0] + ' | ' + project_board[1] + ' | ' + project_board[2] + ' | ')
print(' -------------')
print( ' | ' +  project_board[3] + ' | ' + project_board[4] + ' | ' + project_board[5] + ' | ')
print(' -------------')
print( ' | ' +  project_board[6] + ' | ' + project_board[7] + ' | ' + project_board[8] + ' | ')
print(' -------------')
print('\n')



def game():
    x = 0
    o = 0
    while True:
        try:
            if x == o:
                ques = int(input('Player1, choose a number between 1-9 or 11 to quit \n '))
                if ques <= 9 and ques >= 1:
                    check = (ques - 1)
                    if project_board[check] == player2 or project_board[check] == player1:
                        print('A player is already in that location! Try another. ')
                        continue

                    elif project_board[check] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                        project_board[check] = player1
                        x += 1
               

                elif ques == 11:
                     print(quit())
                     break
                else:
                    print('Please choose a number between 1-9 or 11 to quit ')
                    continue

            else:
                ques = int(input('Player2, choose a number between 1-9 or 11 to quit \n '))
                if ques <= 9 >= 1:
                    check = (ques - 1)
                    if project_board[check] == player1 or project_board[check] == player2:
                        print('A player is already in that location! Try another. ')
                        continue

                    elif project_board[check] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                        project_board[check] = player2
                        x -= 1
                

                elif ques == 11:
                     print(quit())
                     break
                
                else:
                    print('Please choose a number between 1-9 or 11 to quit ')
                    continue
                    

        except ValueError:
            print('Please choose a number between 1-9')
            continue
        
        if project_board[0] == project_board[1] == project_board[2] and project_board[0] != '1':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[6] == project_board[7] == project_board[8] and project_board[6] != '7':
            winner = f'{project_board[6]} is the winner!'
            break
        elif project_board[2] == project_board[5] == project_board[8] and project_board[2] != '3':
            winner = f'{project_board[2]} is the winner!'
            break
        elif project_board[0] == project_board[4] == project_board[8] and project_board[0] != '1':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[2] == project_board[4] == project_board[6] and project_board[2] != '3':
            winner = f'{project_board[2]} is the winner!'
            break
        elif project_board[3] == project_board[4] == project_board[5] and project_board[3] != '4':
            winner = f'{project_board[3]} is the winner!'
            break
        elif project_board[0] == project_board[3] == project_board[6] and project_board[0] != '1':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[1] == project_board[4] == project_board[7] and project_board[1] != '2':
            winner = f'{project_board[1]} is the winner!'
            break
        elif '1' not in project_board and '2' not in project_board and '3' not in project_board and '4' not in project_board and '5' not in project_board and '6' not in project_board and '7' not in project_board and '8' not in project_board and '9' not in project_board:
            winner = 'Nobody won. Tie game!'
            break
        printboard()
    printboard()
    print(winner)
game()
