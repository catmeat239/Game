from field import Field, SquareField, RombField, CustomField
from player import Player, HumanPlayer, CompPlayer
from tkinter import *
from tkinter import messagebox



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
        if (not playerA.hasMoved):
            if isinstance(playerA, HumanPlayer):
                while (not playerA.hasMoved):
                    window.update()
                    field.draw(window, c)
                    if (field.isFull()):
                        break
            else:
                playerA.play(field)
                window.update()
                if (field.isFull()):
                    break
            playerB.hasMoved = not playerA.hasMoved
        else:
            if isinstance(playerB, HumanPlayer):
                while (not playerB.hasMoved):
                    window.update()
                    field.draw(window, c)
                    if (field.isFull()):
                        break
            else:
                playerB.play(field)
                window.update()
                if (field.isFull()):
                    break
            playerA.hasMoved = not playerB.hasMoved

        field.draw(window, c)

    scoreA, scoreB = field.calulateScore()
    if scoreA > scoreB:
        print("A win")
    elif scoreA < scoreB:
        print('B win')
    else:
        print("Tie")

n = 1000
window = Tk()

def clickPlayVSComputerButton():
    global onMenu, playVSComp
    onMenu = 0
    playVSComp = True
def clickPlayVSHumanButton():
    global onMenu, playVSComp
    onMenu = 0
    playVSComp = False

def clickRulesButton():
    messagebox.showinfo("Правила:", "    Игровое поле может представлять собой любую замкнутую область на клетчатой бумаге.\n"
                                 "    В игре участвует два игрока, которые ходят по очереди.Ход представляет собой постановку черты длиной в одну клетку — по вертикали или по горизонтали.\n"
                                 "    В случае если после хода игрока одна или две клетки становятся закрыты(т. е. были поставлены четвертые составляющие их черты)\n"
                                 "игрок обязан поставить в закрытых им квадратах свой знак(крестик или нолик) и сделать еще один ход (поставить еще одну черту)\n"
                                 "    Игроки ходят пока все поле не будет заполнено. В конце игры подсчитывается количество знаков каждого игрока, выигрывает тот, чьих знаков больше.")

playVSComputerButton = Button(text="playVScomputer", command=clickPlayVSComputerButton)
playVSComputerButton.pack()
playVSHumanButton = Button(text="playVShuman", command=clickPlayVSHumanButton)
playVSHumanButton.pack()
rulesButton = Button(text="rules", command=clickRulesButton)
rulesButton.pack()

fieldType = IntVar()


squareFieldButton = Radiobutton(text="square", value=1, variable=fieldType, padx=15, pady=10)
squareFieldButton.pack()

rombFieldButton = Radiobutton(text="romb", value=2, variable=fieldType, padx=15, pady=10)
rombFieldButton.pack()




onMenu = 1
while(onMenu != 0):
    window.update()
squareFieldButton.destroy()
rombFieldButton.destroy()
rulesButton.destroy()
playVSComputerButton.destroy()
playVSHumanButton.destroy()

playerA = HumanPlayer(1)
if(playVSComp):
    playerB = CompPlayer(2)
else:
    playerB = HumanPlayer(2)

k = 5
a = 40  # side of a Sell
n = (k + 2) * a
window.option_clear()
c = Canvas(window, width=n, height=n, bg='white')
c.pack()
if (fieldType.get() == 0):
    field = CustomField(k)
elif (fieldType.get() == 1):
    field = SquareField(k)
elif (fieldType.get() == 2):
    field = RombField(k)
c.create_rectangle(0, 0, n, n)
field.draw(window, c)

window.bind('<Button-1>', click)

window.after(0, gameProccess(playerA, playerB, field))
