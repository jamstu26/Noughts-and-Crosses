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

def playgame():
    playing=True
    player1piece='X'
    player2piece='O'
    playerturn=1
    
    gameboardlist=['_','_','_','_','_','_','_','_','_',]
    
    while playing:
        gameboard=f"{gameboardlist[0]} {gameboardlist[1]} {gameboardlist[2]}\n{gameboardlist[3]} {gameboardlist[4]} {gameboardlist[5]}\n{gameboardlist[6]} {gameboardlist[7]} {gameboardlist[8]}"
        invalid_move=False
        if playerturn==1:
            playerpiece=player1piece
        else:
            playerpiece=player2piece
        print(f"Player {playerturn}'s turn")
        print(gameboard)
        move=input(f"\nPlayer {playerturn}, enter coordinates of your move (x y): ")
        if move=='1 1' or move=='1 2' or move=='1 3' or move=='2 1' or move=='2 2' or move=='2 3' or move=='3 1' or move=='3 2' or move=='3 3':
            if move=="1 1" and gameboardlist[0]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[0]=playerpiece
            elif move=="1 1" and gameboardlist[0]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="2 1" and gameboardlist[1]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[1]=playerpiece
            elif move=="2 1" and gameboardlist[1]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="3 1" and gameboardlist[2]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[2]=playerpiece
            elif move=="3 1" and gameboardlist[2]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            
            elif move=="1 2" and gameboardlist[3]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[3]=playerpiece
            elif move=="2 2" and gameboardlist[3]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="2 2" and gameboardlist[4]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[4]=playerpiece
            elif move=="2 2" and gameboardlist[4]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="3 2" and gameboardlist[5]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[5]=playerpiece
            elif move=="3 2" and gameboardlist[5]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True

            elif move=="1 3" and gameboardlist[6]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[6]=playerpiece
            elif move=="1 3" and gameboardlist[6]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="2 3" and gameboardlist[7]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[7]=playerpiece
            elif move=="2 3" and gameboardlist[7]!='_':
                os.system('cls')
                printtitle()
                print("\nInvalid Move: Place Occupied\n")
                invalid_move=True
            elif move=="3 3" and gameboardlist[8]=='_':
                os.system('cls')
                printtitle()
                gameboardlist[8]=playerpiece
            elif move=="3 3" and gameboardlist[8]!='_':
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
