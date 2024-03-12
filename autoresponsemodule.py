import random
import otherfunctionsmodule

spotcheck = ['ignore', 'top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']
#this is the brain of the computer. It checks for a possible win, possible loss
def autoresponse(theBoard,notPlayer,player,count,block,route,relative):
    global spotcheck

    #if the bot ever has a chance to win on its next move, it will take it
    block,isitover = otherfunctionsmodule.ifwinpossible3(notPlayer,player,theBoard,block)
    if isitover == 'yes':
        count += 1
        return count,block,route,relative
    block,canwelose = otherfunctionsmodule.iflosepossible(notPlayer,player,theBoard,block)
    if canwelose == 'yes':
        #print('a loss is possible, stopping it')
        count += 1
        return count,block,route,relative
    else:

        #turn 1 response(bot went first)
        if count == 1:
            block = botplace(notPlayer, theBoard, block, [1, 3, 7, 9])
            relative = detectrelativepos(spotcheck.index(block[1]))

        #turn 2 response(player went first)
        elif count == 2:
            relative = detectrelativepos(spotcheck.index(block[1]))
            if theBoard[spotcheck[1]] == player or theBoard[spotcheck[3]] == player or theBoard[spotcheck[7]] == player or theBoard[spotcheck[9]] == player:
                block = botplace(notPlayer,theBoard,block,[5])
                route = 't1-cr'
            elif theBoard[spotcheck[5]] == player:
                block = botplace(notPlayer,theBoard,block,[1,3,7,9])
                route = 't1-mr'
            else:
                route = random.choice(['t1-sr-acr']) #t1-sr-mr', 't1-sr-osr', '
                if route == 't1-sr-mr':
                    block = botplace(notPlayer, theBoard, block, [5])
                elif route == 't1-sr-osr':
                    block = botplace(notPlayer, theBoard, block, [relative['opp.side.']])
                elif route == 't1-sr-acr':
                    block = botplace(notPlayer, theBoard, block, [relative['adj.cor.2'],relative['adj.cor.1']])
                    if block[2] == spotcheck[relative['adj.cor.1']]:
                        route = 't1-sr-acr-ac1'
                    else:
                        route = 't1-sr-acr-ac2'

        #turn 3 no middle response(bot went first)
        elif count == 3 and theBoard[spotcheck[5]] != player:
            if spotcheck[relative['adj.neigh.1']] in block:
                block = botplace(notPlayer,theBoard,block,  [relative['adj.cor.2']])
            elif spotcheck[relative['adj.neigh.2']] in block:
                block = botplace(notPlayer,theBoard,block,  [relative['adj.cor.1']])
            else:
                block = botplace(notPlayer, theBoard, block,  [relative['adj.cor.1'],relative['adj.cor.2']])

            route = 't2-nmr'

        #turn 3 middle response(bot went first)
        elif count == 3 and theBoard[spotcheck[5]] == player:
            block = botplace(notPlayer,theBoard,block,[relative['opp.cor.']])
            route = 't2-mr'

        #turn 4 corner response(player went first)
        elif count == 4 and route == 't1-cr':
            if spotcheck[relative['opp.cor.']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.neigh.1'],relative['adj.neigh.2'],relative['knight.1'],relative['knight.2']])
                route = 't1-cr-ate'
            elif spotcheck[relative['knight.1']] in block:
                block = botplace(notPlayer, theBoard, block,[relative['opp.cor.'], relative['adj.cor.2'], relative['knight.2'],relative['adj.neigh.1']])
                if block[4] == spotcheck[relative['adj.neigh.1']]:
                    route = 't1-cr-more'
            elif spotcheck[relative['knight.2']] in block:
                block = botplace(notPlayer, theBoard, block,[relative['opp.cor.'], relative['adj.cor.1'], relative['knight.1'],relative['adj.neigh.2']])
                if block[4] == spotcheck[relative['adj.neigh.2']]:
                    route = 't1-cr-more'

        #turn 4 middle response(player went first)
        elif count == 4 and route == 't1-mr':
            relative = detectrelativepos(spotcheck.index(block[2]))
            if spotcheck[relative['opp.cor.']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'], relative['adj.cor.2']])

        #turn 4 side response(player went first)
        elif count == 4 and route == 't1-sr-mr':
            if spotcheck[relative['knight.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'], relative['adj.cor.2'],relative['diag.neigh.1'],relative['diag.neigh.2']])
                if spotcheck[relative['diag.neigh.1']] in block:
                    route = 't1-sr-mr-dn1'
                else:
                    route = 't1-sr-mr-ate'
            elif spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'], relative['adj.cor.2'],relative['diag.neigh.1'],relative['diag.neigh.2']])
                if spotcheck[relative['diag.neigh.2']] in block:
                    route = 't1-sr-mr-dn2'
                else:
                    route = 't1-sr-mr-ate'
            else:
                block = otherfunctionsmodule.ifdoesnotmatter(notPlayer, player, theBoard, block, relative)

        #turn 4 opposite side response(player went first)
        elif count == 4 and route == 't1-sr-osr':
            if spotcheck[relative['mid']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'],relative['adj.cor.2'],relative['knight.cor.1'],relative['knight.cor.2']])
                route = 't1-sr-osr-ate'
            elif spotcheck[relative['knight.cor.1']] in block or spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer,theBoard,block,[relative['adj.cor.1'],relative['adj.cor.2']])
                route = 't1-sr-osr-kcm'
            elif spotcheck[relative['diag.neigh.1']] in block or spotcheck[relative['diag.neigh.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'], relative['adj.cor.2']])
                route = 't1-sr-osr-dnm'
            else:
                block = otherfunctionsmodule.ifdoesnotmatter(notPlayer, player, theBoard, block, relative)

        #very niche play to prevent getting double trapped and optimize win chance
        elif count == 4 and route == 't1-sr-acr-ac1':
            if spotcheck[relative['knight.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'], relative['opp.side.']])
                if spotcheck[relative['opp.side.']] in block:
                    route = 't1-sr-acr-ac1-kcm'
                else:
                    route = 't1-sr-acr-ac1-ate'
            elif spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'], relative['opp.side.'],relative['knight.cor.1']])
                if spotcheck[relative['opp.side.']] in block or spotcheck[relative['knight.cor.1']] in block:
                    route = 't1-sr-acr-ac1-kcm'
                else:
                    route = 't1-sr-acr-ac1-ate'
            elif spotcheck[relative['adj.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['diag.neigh.1'], relative['knight.cor.1']])
                if spotcheck[relative['knight.cor.1']] in block:
                    route = 't1-sr-acr-ac1-kcc'
                else:
                    route = 't1-sr-acr-ac1-kcm'
            elif spotcheck[relative['diag.neigh.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.1']])
                route = 't1-sr-acr-ac1-ate'
            elif spotcheck[relative['diag.neigh.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'],relative['opp.side.'],relative['diag.neigh.2']])
                if spotcheck[relative['opp.side.']] in block:
                    route = 't1-sr-acr-ac1-osm'
                elif spotcheck[relative['diag.neigh.2']] in block:
                    route = 't1-sr-acr-ac1-dnm'
                else:
                    route = 't1-sr-acr-ac1-ate'

        elif count == 4 and route == 't1-sr-acr-ac2':
            if spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'], relative['opp.side.']])
                if spotcheck[relative['opp.side.']] in block:
                    route = 't1-sr-acr-ac1-kcm'
                else:
                    route = 't1-sr-acr-ac2-ate'
            elif spotcheck[relative['knight.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'], relative['opp.side.'],relative['knight.cor.2']])
                if spotcheck[relative['opp.side.']] in block or spotcheck[relative['knight.cor.2']] in block:
                    route = 't1-sr-acr-ac1-kcm'
                else:
                    route = 't1-sr-acr-ac2-ate'
            elif spotcheck[relative['adj.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['diag.neigh.2'], relative['knight.cor.2']])
                if spotcheck[relative['knight.cor.2']] in block:
                    route = 't1-sr-acr-ac1-kcc'
                else:
                    route = 't1-sr-acr-ac2-kcm'
            elif spotcheck[relative['diag.neigh.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])
                route = 't1-sr-acr-ac2-ate'
            elif spotcheck[relative['diag.neigh.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'],relative['opp.side.'],relative['diag.neigh.1']])
                if spotcheck[relative['opp.side.']] in block:
                    route = 't1-sr-acr-ac2-osm'
                elif spotcheck[relative['diag.neigh.1']] in block:
                    route = 't1-sr-acr-ac2-dnm'
                else:
                    route = 't1-sr-acr-ac2-ate'

        #turn 5 no middle response(bot went first)
        elif count == 5 and route == 't2-nmr':

            #if the player went to an adjacent neighbor move 1
            if spotcheck[relative['adj.neigh.1']] in block and spotcheck[relative['adj.neigh.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'],relative['opp.cor.']])
                route = 't2-nmr-ate'
            #if the player went a knights move way move 1
            elif spotcheck[relative['knight.1']] in block and spotcheck[relative['adj.neigh.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'],relative['adj.cor.2']])
                route = 't2-nmr-ate'
            elif spotcheck[relative['knight.2']] in block and spotcheck[relative['adj.neigh.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid'],relative['adj.cor.1']])
                route = 't2-nmr-ate'
            #if the player went to an adjacent corner move 1
            elif spotcheck[relative['adj.cor.1']] in block and spotcheck[relative['adj.cor.2']] in block:
                block = botplace(notPlayer,theBoard,block,[relative['opp.cor.']])
                route = 't2-nmr-ate'
            #if the player went to the opposite corner move 1
            else:
                block = botplace(notPlayer,theBoard,block,[relative['adj.cor.1'],relative['adj.cor.2']])
                route = 't2-nmr-ate'
        #turn 6 niche code to optimize the win chance for the bot       
        elif count == 6 and route == 't1-cr-more':
            block = botplace(notPlayer, theBoard, block, [relative['opp.cor.']])

        elif count == 6 and route == 't1-sr-mr-dn1':
            block = botplace(notPlayer, theBoard, block, [relative['adj.cor.2'],relative['knight.cor.2']])
        elif count == 6 and route == 't1-sr-mr-dn2':
            block = botplace(notPlayer, theBoard, block, [relative['adj.cor.1'],relative['knight.cor.1']])

        elif count == 6 and route == 't1-sr-osr':
            if block[5] == spotcheck[relative['diag.neigh.1']]:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])
            elif block[5] == spotcheck[relative['diag.neigh.2']]:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.1']])
            else:
                block = otherfunctionsmodule.ifdoesnotmatter(notPlayer, player, theBoard, block, relative)

        elif count == 6 and route == 't1-sr-osr-kcm':
            if spotcheck[relative['mid']] not in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
            else:
                block = otherfunctionsmodule.ifdoesnotmatter(notPlayer, player, theBoard, block, relative)


        elif count == 6 and route == 't1-sr-osr-dnm':
            if block[5] == spotcheck[relative['adj.cor.2']]:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])
            elif block[5] == spotcheck[relative['knight.cor.2']]:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
            else:
                block = otherfunctionsmodule.ifdoesnotmatter(notPlayer, player, theBoard, block, relative)

        elif count == 6 and route == 't1-sr-acr-ac1-kcm':
            block = botplace(notPlayer, theBoard, block, [relative['mid']])

        elif count == 6 and route == 't1-sr-acr-ac1-osm':
            if spotcheck[relative['adj.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])
            elif spotcheck[relative['knight.cor.1']] in block or spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
        elif count == 6 and route == 't1-sr-acr-ac1-dnm':
            if spotcheck[relative['knight.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])
            elif spotcheck[relative['knight.cor.2']] in block or spotcheck[relative['adj.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
        elif count == 6 and route == 't1-sr-acr-ac1-kcc':
            block = botplace(notPlayer, theBoard, block, [relative['knight.cor.1']])

        elif count == 6 and route == 't1-sr-acr-ac2-osm':
            if spotcheck[relative['adj.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.1']])
            elif spotcheck[relative['knight.cor.2']] in block or spotcheck[relative['knight.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
        elif count == 6 and route == 't1-sr-acr-ac2-dnm':
            if spotcheck[relative['knight.cor.2']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['knight.cor.1']])
            elif spotcheck[relative['knight.cor.1']] in block or spotcheck[relative['adj.cor.1']] in block:
                block = botplace(notPlayer, theBoard, block, [relative['mid']])
        elif count == 6 and route == 't1-sr-acr-ac2-kcc':
            block = botplace(notPlayer, theBoard, block, [relative['knight.cor.2']])

        #if the bot doesn't know where to go or it doesn't matter where he goes, he just picks at random
        else:
            block = otherfunctionsmodule.ifdoesnotmatter(notPlayer,player,theBoard,block,relative)


        count += 1

        return count,block,route,relative


#the bot actually putting their move on the board
def botplace(notPlayer,theBoard,block, keypad):
    global spotcheck
    breakout = 1
    choice = random.choice(keypad)
    while spotcheck[choice] in block and breakout < 40:
        breakout += 1
        print("Already Taken, Retrying")
        choice = random.choice(keypad)
        if breakout == 39:
            print('infinite loop breaking out')

    theBoard[spotcheck[choice]] = notPlayer
    block.append(spotcheck[choice])
    return block

#since a tictactoe board is symmetrical both horizontally and vertically, this function essentially
#makes the way I chose to code the computer 4x shorter code length wise.
def detectrelativepos(observedtile):
    dict1 = {'start':observedtile,'adj.neigh.1':2,'adj.neigh.2':4,'adj.cor.1':3,'adj.cor.2':7,'knight.1':6,'knight.2':8,'opp.cor.':9,'mid':5}
    dict3 = {'start':observedtile,'adj.neigh.1':6,'adj.neigh.2':2,'adj.cor.1':9,'adj.cor.2':1,'knight.1':8,'knight.2':4,'opp.cor.':7,'mid':5}
    dict7 = {'start':observedtile,'adj.neigh.1':4,'adj.neigh.2':8,'adj.cor.1':1,'adj.cor.2':9,'knight.1':2,'knight.2':6,'opp.cor.':3,'mid':5}
    dict9 = {'start':observedtile,'adj.neigh.1':8,'adj.neigh.2':6,'adj.cor.1':7,'adj.cor.2':3,'knight.1':4,'knight.2':2,'opp.cor.':1,'mid':5}
    dict2 = {'start':observedtile,'adj.cor.1':3,'adj.cor.2':1,'diag.neigh.1':6,'diag.neigh.2':4,'knight.cor.1':9,'knight.cor.2':7,'opp.side.':8,'mid':5}
    dict4 = {'start':observedtile,'adj.cor.1':1,'adj.cor.2':7,'diag.neigh.1':2,'diag.neigh.2':8,'knight.cor.1':3,'knight.cor.2':9,'opp.side.':6,'mid':5}
    dict6 = {'start':observedtile,'adj.cor.1':9,'adj.cor.2':3,'diag.neigh.1':8,'diag.neigh.2':2,'knight.cor.1':7,'knight.cor.2':1,'opp.side.':4,'mid':5}
    dict8 = {'start':observedtile,'adj.cor.1':7,'adj.cor.2':9,'diag.neigh.1':4,'diag.neigh.2':6,'knight.cor.1':1,'knight.cor.2':3,'opp.side.':2,'mid':5}
    dict5 = {'start':observedtile,'adj.neigh.1':2,'adj.neigh.2':6,'adj.neigh.3':8,'adj.neigh':4,'adj.cor.1':1,'adj.cor.2':3,'adj.cor.3':9,'adj.cor.4':7,'mid':5}
    if observedtile == 1:
        relativespots = dict1
    elif observedtile == 3:
        relativespots = dict3
    elif observedtile == 7:
        relativespots = dict7
    elif observedtile == 9:
        relativespots = dict9
    elif observedtile == 2:
        relativespots = dict2
    elif observedtile == 4:
        relativespots = dict4
    elif observedtile == 6:
        relativespots = dict6
    elif observedtile == 8:
        relativespots = dict8
    elif observedtile == 5:
        relativespots = dict5
    else:
        assert False, 'Need to enter a valid value for observedtile'
    return relativespots



