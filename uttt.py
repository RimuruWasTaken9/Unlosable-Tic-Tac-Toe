#! python3
import random
import autoresponsemodule
import otherfunctionsmodule

spotcheck = ['ignore', 'top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']
if __name__ == "__main__":
    player, notPlayer = otherfunctionsmodule.pickXorO()
    loopControl = 'yes'
    while loopControl != 'no':
        theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
        route = 't1'
        block = ['ignore']
        relative = {'ignore': 1}

        count = 1
        first = random.choice("001")#add1 after 0 to put it back to random
        if first == '1':
            print(f"\n{player} is going first\n")
        else:
            print(f"\n{notPlayer} is going first\n")
        otherfunctionsmodule.helpfulboard()
        while True:

            status = otherfunctionsmodule.windetector(theBoard,player,notPlayer)
            if status == 1:
                print("\n\nTIC-TAC-TOE, game over.\n")
                break
            print(f"\n\tTurn {count}:\n")

            if count == 10:
                print("Board Filled - Draw\n")
                break

            if count % 2 == int(first):
                otherfunctionsmodule.board(theBoard)
                future = input(f'\npick a spot to go in: ')

                if future in theBoard:
                    if future in block:
                        print('already taken')
                        continue
                    else:

                        theBoard[future] = player
                        block.append(future)
                        count += 1
                        otherfunctionsmodule.helpfulboard()
                        #time.sleep(1)


                else:
                    print("Please type a valid response")
                    continue
            else:
                count,block, route,relative = autoresponsemodule.autoresponse(theBoard,notPlayer,player,count,block,route,relative)
                otherfunctionsmodule.board(theBoard)



        otherfunctionsmodule.board(theBoard)
        loopControl = input('\n Play again? (type no to stop): ')


