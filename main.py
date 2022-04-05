from field import Field, SquareField
from player import Player, HumanPlayer
from tkinter import *

k = 4
a = 40  # side of a Sell
n = k * a * 2
field = SquareField(k)

window = Tk()
c = Canvas(window, width=n, height=n, bg='white')
c.pack()
field.draw(window, c)

playerA = HumanPlayer(1)
playerB = HumanPlayer(2)

def click(event):
    x = event.x
    y = event.y

    if (x > n // 4 and y > n // 4 and (min(x % a, a - x % a) < a // 2 or  min(y % a, a - y % a) < a // 2) ):

        vertical = min(x % a, a - x % a) < min( y % a, a - y % a)
        if(vertical):
            i = (x + a // 2) // a
            j = y // a
        else:
            j = (y + a // 2) // a
            i = x // a
        i -= k // 2
        j -= k // 2

        if(   j < field.arr.__len__() and i < field.arr.__len__() and ((vertical and field.arr[i][j].left == False) or (vertical != True and field.arr[i][j].up != True) )):
            if not playerA.hasMoved:
                playerA.move(field, i, j, vertical)
            elif not playerB.hasMoved:
                playerB.move(field, i, j, vertical)
            field.draw(window, c)


def gameProccess(playerA, playerB, field):
    while not field.isFull():
        if isinstance(playerA, HumanPlayer):
            while (not playerA.hasMoved):
                window.update()
                if (field.isFull()):
                    break
        else:
            playerA.move(field)

        if  isinstance(playerB,HumanPlayer):
            while (not playerB.hasMoved):
                window.update()
                if (field.isFull()):
                    break
        else:
            playerB.move(field)
        playerA.hasMoved = False
        playerB.hasMoved = False
    scoreA, scoreB = field.calulateScore()
    if scoreA > scoreB:
        print("A win")
    elif scoreA < scoreB:
        print('B win')
    else:
        print("Tie")


window.bind('<Button-1>', click)

window.after(0, gameProccess(playerA, playerB, field))
