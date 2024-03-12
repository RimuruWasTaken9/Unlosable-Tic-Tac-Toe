#so much wasted time
'''
#original code for turn 3 middle response(bot went first)(bot goes in opposite corner from first move)

        if block[1] == spotcheck[1]:
            block = botplace(notPlayer, theBoard, block, spotcheck, [9])
        elif block[1] == spotcheck[3]:
            block = botplace(notPlayer, theBoard, block, spotcheck, [7])
        elif block[1] == spotcheck[7]:
            block = botplace(notPlayer, theBoard, block, spotcheck, [3])
        elif block[1] == spotcheck[9]:
            block = botplace(notPlayer, theBoard, block, spotcheck, [1])

'''
"""
#turn 5 no middle response(bot went first)
#if player didn't block the impending TIC-TAC-TOE, bot wins

        if block[1] == spotcheck[1] and block[3] == spotcheck[3] and block[4] != spotcheck[2]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[2])
        elif block[1] == spotcheck[3] and block[3] == spotcheck[1] and block[4] != spotcheck[2]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[2])
        elif block[1] == spotcheck[1] and block[3] == spotcheck[7] and block[4] != spotcheck[4]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[4])
        elif block[1] == spotcheck[7] and block[3] == spotcheck[1] and block[4] != spotcheck[4]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[4])
        elif block[1] == spotcheck[7] and block[3] == spotcheck[9] and block[4] != spotcheck[8]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[8])
        elif block[1] == spotcheck[9] and block[3] == spotcheck[7] and block[4] != spotcheck[8]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[8])
        elif block[1] == spotcheck[3] and block[3] == spotcheck[9] and block[4] != spotcheck[6]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[6])
        elif block[1] == spotcheck[9] and block[3] == spotcheck[3] and block[4] != spotcheck[6]:
            block = botplace(notPlayer,theBoard,block,spotcheck,[6])
"""
'''
    #old dictionaries to save
    dict1 = {'adj.neigh.1':2,'adj.neigh.2':4,'adj.cor.1':3,'adj.cor.2':7,'knight.1':6,'knight.2':8,'opp.cor.1':9,'mid':5}
    dict3 = {'adj.neigh.1':6,'adj.neigh.2':2,'adj.cor.1':9,'adj.cor.2':1,'knight.1':8,'knight.2':4,'opp.cor.1':7,'mid':5}
    dict7 = {'adj.neigh.1':4,'adj.neigh.2':8,'adj.cor.1':1,'adj.cor.2':9,'knight.1':2,'knight.2':6,'opp.cor.1':3,'mid':5}
    dict9 = {'adj.neigh.1':8,'adj.neigh.2':6,'adj.cor.1':7,'adj.cor.2':3,'knight.1':4,'knight.2':2,'opp.cor.1':1,'mid':5}


'''
"""

    #turn 3 no middle response(bot went first)
        if block[1] == spotcheck[1]:
            block = botthink(notPlayer, theBoard, block, spotcheck, 2, 2, [7], 4, [3], [3, 7])

        elif block[1] == spotcheck[9]:
            block = botthink(notPlayer, theBoard, block, spotcheck, 2, 8, [3], 6, [7], [3, 7])

        elif block[1] == spotcheck[3]:
            block = botthink(notPlayer, theBoard, block, spotcheck, 2, 2, [9], 6, [1], [1, 9])

        elif block[1] == spotcheck[7]:
            block = botthink(notPlayer, theBoard, block, spotcheck, 2, 4, [9], 8, [1], [1, 9])
"""
'''
#old functions I was calling
def botsimplethink(np,tb,block,sc,pt,ptp,ctp):
    if block[pt] in sc[ptp]:
        block = botplace(np, tb, block, sc, ctp)
        return block
def botthink(np, tb, block, sc,Lt,Ltp1,ntm1,Ltp2,ntm2,loo): #takes into account very specific circumstances
    if block[Lt] == sc[Ltp1]:  #checks for players last move (last move = count-1)(lastturnplace = location of move)
        block = botplace(np, tb, block, sc, ntm1) #starts the function that picks the bots spot from given moves
        #nextturnmoves = which spots the bot is allowed to go           #same principle for the elif statement
    elif block[Lt] == sc[Ltp2]:
        block = botplace(np, tb, block, sc, ntm2)
    else:
        block = botplace(np, tb, block, sc, loo) #listofoptions usually equals nextturnmoves1+nextturnmoves2
    return block #returns which spots on the board have an X or O on them already

'''
"""
#t5-nmr- was run if the player blocked the impending tic-tac-toe
            botsimplethink(notPlayer, theBoard, block, spotcheck, 3, 1, [3, 7])
            botsimplethink(notPlayer, theBoard, block, spotcheck, 3, 3, [1, 9])
            botsimplethink(notPlayer, theBoard, block, spotcheck, 3, 7, [1, 9])
            botsimplethink(notPlayer, theBoard, block, spotcheck, 3, 9, [3, 7])
"""
'''    
#old part of botplace function
    else:
        while spots[choice] in block:
            print("Already Taken, Retrying")
            choice = random.choice(keypad)
        theBoard[spots[choice]] = notPlayer
        block.append(spots[choice])
        return block
'''
"""
  #idek what this one was
  if block[count-1] == spotcheck[1] or block[count-1] == spotcheck[9]:   #if the players move is in top left or bottom right
            block = botplace(notPlayer,block,spotcheck,[3,7])           #go to the 
        elif block[count-1] == spotcheck[3] or block[count-1] == spotcheck[7]:
            block = botplace(notPlayer, block,spotcheck,[1,9])
            """
'''
#old code for             
            #if player didn't block the impending TIC-TAC-TOE, bot wins
            if block[3] == spotcheck[relative['adj.cor.1']] and block[4] != spotcheck[relative['adj.neigh.1']]:
                block = botplace(notPlayer, theBoard, block,  [relative['adj.neigh.1']])
            elif block[3] == spotcheck[relative['adj.cor.2']] and block[4] != spotcheck[relative['adj.neigh.2']]:
                block = botplace(notPlayer, theBoard, block,  [relative['adj.neigh.2']])


'''
"""
#old code for how to finish the game on turn 7

        if count == 7 and 't2-nmr' in route:
            if route == 't2-nmr-fwac':
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'], relative['adj.cor.2'],relative['opp.cor.']])
            elif route == 't2-nmr-fwm&s':
                if block[6] != spotcheck[relative['mid']]:
                    block = botplace(notPlayer, theBoard, block, [relative['mid']])
                else:
                    if block[5] == spotcheck[relative['adj.cor.1']]:
                        block = botplace(notPlayer, theBoard, block, [relative['adj.neigh.1']])
                    elif block[5] == spotcheck[relative['adj.cor.2']]:
                        block = botplace(notPlayer, theBoard, block, [relative['adj.neigh.2']])
                    elif block[3] == spotcheck[relative['adj.cor.1']]:
                        block = botplace(notPlayer, theBoard, block, [relative['knight.1']])
                    elif block[3] == spotcheck[relative['adj.cor.2']]:
                        block = botplace(notPlayer, theBoard, block, [relative['knight.2']])
                    else:
                        print('the bot did something else.')
"""
'''
#old function for detecting a win possibilitity
def ifwinpossible2(np,p,tb,b):
    global spotcheck
    isitover = 'no'

    #top horizontal tictactoe
    if tb[spotcheck[1]] == np and tb[spotcheck[2]] == np and tb[spotcheck[3]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [3])
        isitover = 'yes'
    elif tb[spotcheck[1]] == np and tb[spotcheck[2]]  != (np or p) and tb[spotcheck[3]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [2])
        isitover = 'yes'
    elif tb[spotcheck[1]] != (np or p) and tb[spotcheck[2]]  == np and tb[spotcheck[3]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [1])
        isitover = 'yes'

    #middle horizontal tictactoe
    elif tb[spotcheck[4]] == np and tb[spotcheck[5]] == np and tb[spotcheck[6]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [6])
        isitover = 'yes'
    elif tb[spotcheck[4]] == np and tb[spotcheck[5]]  != (np or p) and tb[spotcheck[6]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [5])
        isitover = 'yes'
    elif tb[spotcheck[4]] != (np or p) and tb[spotcheck[5]]  == np and tb[spotcheck[6]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [4])
        isitover = 'yes'

    #lower horizontal tictactoe
    elif tb[spotcheck[7]] == np and tb[spotcheck[8]] == np and tb[spotcheck[9]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [9])
        isitover = 'yes'
    elif tb[spotcheck[7]] == np and tb[spotcheck[8]]  != (np or p) and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [8])
        isitover = 'yes'
    elif tb[spotcheck[7]] != (np or p) and tb[spotcheck[8]]  == np and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [7])
        isitover = 'yes'

    # left vertical tictactoe
    elif tb[spotcheck[1]] == np and tb[spotcheck[4]] == np and tb[spotcheck[7]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [7])
        isitover = 'yes'
    elif tb[spotcheck[1]] == np and tb[spotcheck[4]] != (np or p) and tb[spotcheck[7]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [4])
        isitover = 'yes'
    elif tb[spotcheck[1]] != (np or p) and tb[spotcheck[4]] == np and tb[spotcheck[7]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [1])
        isitover = 'yes'

    # middle vertical tictactoe
    elif tb[spotcheck[2]] == np and tb[spotcheck[5]] == np and tb[spotcheck[8]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [8])
        isitover = 'yes'
    elif tb[spotcheck[2]] == np and tb[spotcheck[5]] != (np or p) and tb[spotcheck[8]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [5])
        isitover = 'yes'
    elif tb[spotcheck[2]] != (np or p) and tb[spotcheck[5]] == np and tb[spotcheck[8]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [2])
        isitover = 'yes'

    # right vertical tictactoe
    elif tb[spotcheck[3]] == np and tb[spotcheck[6]] == np and tb[spotcheck[9]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [9])
        isitover = 'yes'
    elif tb[spotcheck[3]] == np and tb[spotcheck[6]] != (np or p) and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [6])
        isitover = 'yes'
    elif tb[spotcheck[3]] != (np or p) and tb[spotcheck[6]] == np and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [3])
        isitover = 'yes'

    # tl to br diagonal tictactoe
    elif tb[spotcheck[1]] == np and tb[spotcheck[5]] == np and tb[spotcheck[9]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [9])
        isitover = 'yes'
    elif tb[spotcheck[1]] == np and tb[spotcheck[5]] != (np or p) and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [5])
        isitover = 'yes'
    elif tb[spotcheck[1]] != (np or p) and tb[spotcheck[5]] == np and tb[spotcheck[9]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [1])
        isitover = 'yes'

    # tr to bl diagonal tictactoe
    elif tb[spotcheck[3]] == np and tb[spotcheck[5]] == np and tb[spotcheck[7]] != (np or p):
        b = autoresponsemodule.botplace(np, tb, b, [7])
        isitover = 'yes'
    elif tb[spotcheck[3]] == np and tb[spotcheck[5]] != (np or p) and tb[spotcheck[7]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [5])
        isitover = 'yes'
    elif tb[spotcheck[3]] != (np or p) and tb[spotcheck[5]] == np and tb[spotcheck[7]] == np:
        b = autoresponsemodule.botplace(np, tb, b, [3])
        isitover = 'yes'


    return b,isitover
'''
"""
#oldcode for turn 5 responding to corner move
            if spotcheck[relative['adj.cor.1']] in block or spotcheck[relative['adj.cor.2']] in block:
                block = botplace(notPlayer,theBoard,block,[relative['adj.cor.1'],relative['adj.cor.2']])
"""
'''
code for finishing off the t2-mr draw part
        elif count == 5 and route == 't2-mr':
            block,canwelose = otherfunctionsmodule.iflosepossible(notPlayer,player,theBoard,block)
            route = 't2-mr-di'
            
        elif count == 7 and route == 't2-mr-di':
            block, canwelose = otherfunctionsmodule.iflosepossible(notPlayer, player, theBoard, block)
            route = 't2-mr-di'
'''
"""
#not that old board function
def board(theBoard):
    print(theBoard['top-L'],'|',theBoard['top-M'],'|',theBoard['top-R'])
    print('---------')
    print(theBoard['mid-L'],'|',theBoard['mid-M'],'|',theBoard['mid-R'])
    print('---------')
    print(theBoard['low-L'],'|',theBoard['low-M'],'|',theBoard['low-R'])
"""
'''
#old code used for responding to a loss opportunity in a specific route
        elif route == 't2-mr':
            block,canwelose = otherfunctionsmodule.iflosepossible(notPlayer,player,theBoard,block)
            route = 't2-mr'

'''
"""

#old code for if they block the TIC-TAC-TOE and are about to get their own TIC-TAC-TOE in t5-nmr
if spotcheck[relative['knight.1']] in block and spotcheck[relative['adj.neigh.2']] in block:
    block = botplace(notPlayer, theBoard, block,  [relative['mid']])
    route = 't2-nmr-atf'
elif spotcheck[relative['knight.2']] in block and spotcheck[relative['adj.neigh.1']] in block:
    block = botplace(notPlayer, theBoard, block,  [relative['mid']])
    route = 't2-nmr-atf' 
    
"""
'''
#optional code for getting a random place to go, this isn't really random, it just looks in a set order. It is cool tho
    for count,tile in enumerate(spotcheck):
        if tile not in b:
            b = autoresponsemodule.botplace(np,tb,b,[count])
            break

'''