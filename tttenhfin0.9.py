import sys
import os
import datetime
import random



project_board = ['1','2','3','4','5','6','7','8','9']


start = datetime.datetime.now()

print('''888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888  ''')

print('\n'*2)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

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

while True:
    try:
        gamemode = int(input("Select mode: (1)PvP, (2) VS AI "))
        break
        
    except ValueError:
            print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah shit, here we go again.''')
            continue

    
def game2():
    
    def checkLine(char, spot1, spot2, spot3):
        if project_board[spot1] == char and project_board[spot2] == char and project_board[spot3] == char:
            return True

    def checkAll(char):
        if checkLine(char, 0, 1, 2):
            return True
        if checkLine(char, 3, 4, 5):
            return True
        if checkLine(char, 6, 7, 8):
            return True

        if checkLine(char, 0, 3, 6):
            return True
        if checkLine(char, 1, 4, 7):
            return True
        if checkLine(char, 2, 5, 8):
            return True

        if checkLine(char, 0, 4, 8):
            return True
        if checkLine(char, 2, 4, 6):
            return True

        if project_board[0] == 1 or project_board[1] == 2 or project_board[2] == 3 or project_board[3]==4 or project_board[4] ==   5 or project_board[5]==6 or project_board[6]==7 or project_board[7]==8 or project_board[8]==9 :
            return False
            
        elif '1' not in project_board and '2' not in project_board and '3' not in project_board and '4' not in project_board and '5' not in project_board and '6' not in project_board and '7' not in project_board and '8' not in project_board and '9' not in project_board:
            printboard()
            print('TIE')
            end = datetime.datetime.now()
            elapsed = end - start
            print('Elapsed time: ', str(datetime.timedelta(seconds=elapsed.seconds)) ,'s')
            if __name__ == "__main__":
                answer = input("Do you want to play again ? Y/N ")
                if answer.lower().strip() in "y yes".split():
                    print('\n'*50)
                    restart_program()
                elif answer.lower().strip() in "n no".split():
                    print(exit())
                else:
                    print('''⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉''')
                    print(quit())
                


        #    return True


    
 
    while True:
        try:

            input1 = int(input("Select a Spot: "))
            if input1 <= 9 and input1 >= 1:
                input2 = (input1 - 1)
            
            elif input1 == 11:
                print('See ya chump')
                print(exit())
                break
            else:
                print('Cheeky Breeky')
                continue
            
            if project_board[input2] != 'o' and project_board[input2] != 'x':
                project_board[input2] = 'o'
                if checkAll('o') == True:
                    printboard()
                    print ("Player wins")
                    break
            elif project_board[input2] == 'o' or project_board[input2] == 'x':
                print('Spot taken')
                continue
                

            while True:
                random.seed()  
                computer = random.randint(0,8)
                if project_board[computer] != 'x' and project_board[computer] != 'o':
                    project_board[computer] = 'x'
                    printboard()
                    #if checkAll('x') == True:
                    #    printboard()
                    #    break
                    break

            else:
                print('\n')
                print ('The spot is taken m8!')
                print('\n')
        except ValueError:
            print('Cheeky Breeky')
            continue
            printboard()
        if checkAll('x') == True:
            
            
            print ("Terminator Wins?")
            break

if gamemode == 1:

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

if gamemode == 1:
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
                ques = int(input('P1, choose a number between 1-9 or 11 to quit \n '))
                if ques <= 9 and ques >= 1:
                    check = (ques - 1)
                    if project_board[check] == player2 or project_board[check] == player1:
                        print('\n')
                        print('A player is already in that location! Try another. ')
                        print('\n')
                        continue

                    elif project_board[check] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                        project_board[check] = player1
                        x += 1
               

                elif ques == 11:
                     print(quit())
                     break
                else:
                    print('\n')
                    print('Invalid ')
                    print('\n')
                    continue

            else:
                ques = int(input('P2, choose a number between 1-9 or 11 to quit \n '))
                if ques <= 9 >= 1:
                    check = (ques - 1)
                    if project_board[check] == player1 or project_board[check] == player2:
                        print('\n')
                        print('A player is already in that location! Try another. ')
                        print('\n')
                        continue

                    elif project_board[check] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
                        project_board[check] = player2
                        x -= 1
                
                
                elif ques == 11:
                     print(quit())
                     break
                
                else:
                    print('\n')
                    print('Invalid  ')
                    print('\n')
                    continue
                    

        except ValueError:
            print('Invalid ')
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
    
    z = str(datetime.datetime.now())

    with open('history.txt', 'r+') as f:
        x = len(f.readlines())
        f.write(winner + ' Finished at: '+ z + '\n'*2)
        
        f.close()


    print(winner)

    


    
if gamemode == 1:
    game()
    

if gamemode == 2:
    game2()


#printboard()

end = datetime.datetime.now()
elapsed = end - start
print('Elapsed time: ', str(datetime.timedelta(seconds=elapsed.seconds)) ,'s') 





    
if __name__ == "__main__":
    answer = input("Do you want to play again ? Y/N ")
    if answer.lower().strip() in "y yes".split():
        print('\n'*50)
        restart_program()
    elif answer.lower().strip() in "n no".split():
        print(exit())
    else:
        print('''▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒
▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒
▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒
▒█▀░░░░███░░░░▄█▄░░░░▀█▒
▒█░░░░░░▀░░░░░▀█▀░░░░░█▒
▒█░░░░░░░░░░░░░░░░░░░░█▒
▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒
▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒
▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒
▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒
▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒
▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒''')
        
