from field import Field, SquareField, RombField
from player import Player, HumanPlayer, CompPlayer
from tkinter import *

k = 9
a = 40  # side of a Sell
n = (k + 2) * a
field = RombField(k)

window = Tk()
c = Canvas(window, width=n, height=n, bg='white')
c.pack()
field.draw(window, c)

playerA = HumanPlayer(1)
playerB = CompPlayer(2)



def click(event):
    x = event.x
    y = event.y


    if ((min(x % a, a - x % a) < a // 2 or  min(y % a, a - y % a) < a // 2) ):

        vertical = min(x % a, a - x % a) < min( y % a, a - y % a)
        if(vertical):
            i = (x + a // 2) // a
            j = y // a
        else:
            j = (y + a // 2) // a
            i = x // a
        i -= 1
        j -= 1

        if(playerA.canMove(field, i, j, vertical)):
            if not playerA.hasMoved:
                playerA.move(field, i, j, vertical)
            elif not playerB.hasMoved:
                playerB.move(field, i, j, vertical)



def gameProccess(playerA, playerB, field):
    while not field.isFull():
        if isinstance(playerA, HumanPlayer):
            while (not playerA.hasMoved):
                window.update()
                if (field.isFull()):
                    break
        else:
            playerA.play(field)
            window.update()
            if (field.isFull()):
                break

        field.draw(window, c)

        if isinstance(playerB, HumanPlayer):
            while (not playerB.hasMoved):
                window.update()
                if (field.isFull()):
                    break
        else:
            playerB.play(field)
            window.update()
            if (field.isFull()):
                break

        field.draw(window, c)

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
