import os

def printtitle():
    print(" _   _                   _     _                   _____                             ")
    print("| \ | |                 | |   | |         ___     / ____|                            ")
    print("|  \| | ___  _   _  __ _| |__ | |_ ___   ( _ )   | |     _ __ ___  ___ ___  ___  ___ ")
    print("| . ` |/ _ \| | | |/ _` | '_ \| __/ __|  / _ \/\ | |    | '__/ _ \/ __/ __|/ _ \/ __|")
    print("| |\  | (_) | |_| | (_| | | | | |_\__ \ | (_>  < | |____| | | (_) \__ \__ \  __/\__ \\")
    print("|_| \_|\___/ \__,_|\__, |_| |_|\__|___/  \___/\/  \_____|_|  \___/|___/___/\___||___/")
    print("                    __/ |")
    print("                   |___/")
player1piece='X'
player2piece='O'

def playerwon(playerturn,gameboard):
    os.system('cls')
    printtitle()
    print(f"Player {playerturn} won")
    print(gameboard)
    print("\nChoose an option\n1. Play again\n2. Quit")
    x=input("Choice: ")
    if x=="1":
        os.system('cls')
        printtitle()
        playgame()
    elif x=="2":
        os._exit(0)


def playgame():
    playerturn=1
    playing=True
    gameboardlist=[['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
    while playing:
        gameboard=f"{gameboardlist[0][0]} {gameboardlist[0][1]} {gameboardlist[0][2]}\n{gameboardlist[1][0]} {gameboardlist[1][1]} {gameboardlist[1][2]}\n{gameboardlist[2][0]} {gameboardlist[2][1]} {gameboardlist[2][2]}"
        invalid_move=False
        if playerturn==1:
            playerpiece=player1piece
        else:
            playerpiece=player2piece
        print(f"Turn: Player {playerturn}")
        print(gameboard)
        # Adding player piece to board
        move=input(f"\nPlayer {playerturn}, enter coordinates of your move (x y): ")
        if move=='1 1' or move=='1 2' or move=='1 3' or move=='2 1' or move=='2 2' or move=='2 3' or move=='3 1' or move=='3 2' or move=='3 3':
            if gameboardlist[int(move[2])-1][int(move[0])-1]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[int(move[2])-1][int(move[0])-1]=playerpiece
            else:
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
        
            if invalid_move==True:
                playerturn=playerturn
            else:
                if playerturn==1:
                    playerturn=2
                elif playerturn==2:
                    playerturn=1
        else:
            os.system('cls')
            printtitle()
            print("\nInvalid Move: Coordinates exceed 3x3 grid\n")
            
        # Checking for winner
        gameboard=f"{gameboardlist[0][0]} {gameboardlist[0][1]} {gameboardlist[0][2]}\n{gameboardlist[1][0]} {gameboardlist[1][1]} {gameboardlist[1][2]}\n{gameboardlist[2][0]} {gameboardlist[2][1]} {gameboardlist[2][2]}"
        
        # Vertical possibilities
        if gameboardlist[0][0]==gameboardlist[0][1]==gameboardlist[0][2] and gameboardlist[0][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        elif gameboardlist[1][0]==gameboardlist[1][1]==gameboardlist[1][2] and gameboardlist[1][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        elif gameboardlist[2][0]==gameboardlist[2][1]==gameboardlist[2][2] and gameboardlist[2][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        
        # Horizontal possibilities
        elif gameboardlist[0][0]==gameboardlist[1][0]==gameboardlist[2][0] and gameboardlist[0][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        elif gameboardlist[0][1]==gameboardlist[1][1]==gameboardlist[2][1] and gameboardlist[0][1]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        elif gameboardlist[0][2]==gameboardlist[1][2]==gameboardlist[2][2] and gameboardlist[0][2]!='_':
            playing=False
            playerwon(playerturn,gameboard)

        # Diagonal possibilities
        elif gameboardlist[0][0]==gameboardlist[1][1]==gameboardlist[2][2] and gameboardlist[0][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)
        elif gameboardlist[2][0]==gameboardlist[1][1]==gameboardlist[0][2] and gameboardlist[2][0]!='_':
            playing=False
            playerwon(playerturn,gameboard)

    


                            

            
        

def main():
    printtitle()
    print("\nChoose an option\n1. Play\n2. Quit")
    x=input("Choice: ")
    if x=="1":
        os.system('cls')
        printtitle()
        playgame()
    elif x=="2":
        os._exit(0)

main()
