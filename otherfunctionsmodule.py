import random

import autoresponsemodule
spotcheck = ['ignore', 'top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']


def board(theBoard):
    print('\t',theBoard['top-L'],'|',theBoard['top-M'],'|',theBoard['top-R'])
    print('\t','---------')
    print('\t',theBoard['mid-L'],'|',theBoard['mid-M'],'|',theBoard['mid-R'])
    print('\t','---------')
    print('\t',theBoard['low-L'],'|',theBoard['low-M'],'|',theBoard['low-R'])

def helpfulboard():
    print('\t\t\t\t\tPossible moves index:\n')
    print('\t\t\t\t\t top-L','|','top-M','|','top-R')
    print('\t\t\t\t\t-----------------------')
    print('\t\t\t\t\t mid-L','|','mid-M','|','mid-R')
    print('\t\t\t\t\t-----------------------')
    print('\t\t\t\t\t low-L','|','low-M','|','low-R')
def pickXorO():
    player = input('X or O? : ')

    while player.upper() != 'X' and player.upper() != 'O':
        print("please enter either an X or an O")
        player = input('X or O? : ')
    player = player.upper()
    if player == 'X':
        notplayer = 'O'
    else:
        notplayer = 'X'

    print(f"{player.upper()}'s it is then",end='')
    return player, notplayer
def shortcheck(value1,value2,value3,board,np,p,status):
    if board[value1] == np and board[value2] == np and board[value3] == np:
        status = 1
    elif board[value1] == p and board[value2] == p and board[value3] == p:
        status = 1
    return status
def windetector(board,player,nonplayer):
    status = 0
    status = shortcheck('top-L', 'top-M', 'top-R', board, nonplayer, player,status)
    status = shortcheck('mid-L', 'mid-M', 'mid-R', board, nonplayer, player,status)
    status = shortcheck('low-L', 'low-M', 'low-R', board, nonplayer, player,status)
    status = shortcheck('top-L', 'mid-L', 'low-L', board, nonplayer, player,status)
    status = shortcheck('top-M', 'mid-M', 'low-M', board, nonplayer, player,status)
    status = shortcheck('top-R', 'mid-R', 'low-R', board, nonplayer, player,status)
    status = shortcheck('top-L', 'mid-M', 'low-R', board, nonplayer, player,status)
    status = shortcheck('top-R', 'mid-M', 'low-L', board, nonplayer, player,status)

    return status

def ifwinpossible(np,p,theboard,b,r,r3):
    global spotcheck

    if theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['adj.neigh.1']]] == np and theboard[spotcheck[r['adj.cor.1']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['adj.cor.1']])
    elif theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['mid']]] == np and theboard[spotcheck[r['opp.cor.']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['opp.cor.']])
    elif theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['adj.neigh.2']]] == np and theboard[spotcheck[r['adj.cor.2']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['adj.cor.2']])
    elif theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['adj.cor.1']]] == np and theboard[spotcheck[r['adj.neigh.1']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['adj.neigh.1']])
    elif theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['adj.cor.2']]] == np and theboard[spotcheck[r['adj.neigh.2']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['adj.neigh.2']])
    elif theboard[spotcheck[r['start']]] == np and theboard[spotcheck[r['opp.cor.']]] == np and theboard[spotcheck[r['mid']]] == ' ':
        b = autoresponsemodule.botplace(np,theboard,b,[r['mid']])

    return b
def iwp2short(np,p,tb,b,iio,val1,val2,val3):
    if iio == 'no':
        if iio == 'you will achieve nothing':
            print('damn')
        elif tb[spotcheck[val1]] == np and tb[spotcheck[val2]] == np and tb[spotcheck[val3]] == ' ':
            b = autoresponsemodule.botplace(np, tb, b, [val3])
            iio = 'yes'
        elif tb[spotcheck[val1]] == np and tb[spotcheck[val2]]  == ' ' and tb[spotcheck[val3]] == np:
            b = autoresponsemodule.botplace(np, tb, b, [val2])
            iio = 'yes'
        elif tb[spotcheck[val1]] == ' ' and tb[spotcheck[val2]]  == np and tb[spotcheck[val3]] == np:
            b = autoresponsemodule.botplace(np, tb, b, [val1])
            iio = 'yes'
    return b,iio
def ifwinpossible3(np,p,tb,b):
    global spotcheck
    isitover = 'no'

    b,isitover = iwp2short(np, p, tb, b, isitover, 1, 2, 3)
    b,isitover = iwp2short(np, p, tb, b, isitover, 4, 5, 6)
    b,isitover = iwp2short(np, p, tb, b, isitover, 7, 8, 9)
    b,isitover = iwp2short(np, p, tb, b, isitover, 1, 4, 7)
    b,isitover = iwp2short(np, p, tb, b, isitover, 2, 5, 8)
    b,isitover = iwp2short(np, p, tb, b, isitover, 3, 6, 9)
    b,isitover = iwp2short(np, p, tb, b, isitover, 1, 5, 9)
    b,isitover = iwp2short(np, p, tb, b, isitover, 3, 5, 7)

    return b, isitover

def ilpshort(np,p,tb,b,cwl,val1,val2,val3):
    if cwl == 'no':
        if cwl == 'you will achieve nothing':
            print('damn')
        elif tb[spotcheck[val1]] == p and tb[spotcheck[val2]] == p and tb[spotcheck[val3]] == ' ':
            b = autoresponsemodule.botplace(np, tb, b, [val3])
            cwl = 'yes'
        elif tb[spotcheck[val1]] == p and tb[spotcheck[val2]]  == ' ' and tb[spotcheck[val3]] == p:
            b = autoresponsemodule.botplace(np, tb, b, [val2])
            cwl = 'yes'
        elif tb[spotcheck[val1]] == ' ' and tb[spotcheck[val2]]  == p and tb[spotcheck[val3]] == p:
            b = autoresponsemodule.botplace(np, tb, b, [val1])
            cwl = 'yes'
    return b,cwl
def iflosepossible(np,p,tb,b):
    global spotcheck
    canwelose = 'no'

    b,canwelose = ilpshort(np, p, tb, b, canwelose, 1, 2, 3)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 4, 5, 6)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 7, 8, 9)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 1, 4, 7)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 2, 5, 8)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 3, 6, 9)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 1, 5, 9)
    b,canwelose = ilpshort(np, p, tb, b, canwelose, 3, 5, 7)

    return b, canwelose


def ifdoesnotmatter(np,p,tb,b,r):
    global spotcheck


    while True:
        tile = random.choice(spotcheck)
        if tile not in b:
            b = autoresponsemodule.botplace(np,tb,b,[spotcheck.index(tile)])
            #print('the random tile was',tile)
            break


    return b

def resetboard(b):
    b = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    return b