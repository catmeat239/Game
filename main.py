from field import Field, SquareField, RombField
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
    field.draw(window, c)
    scoreA, scoreB = field.calulateScore()
    if scoreA > scoreB:
        messagebox.showinfo("Game over", "first player won")
    elif scoreA < scoreB:
        messagebox.showinfo("Game over", "second player won")
    else:
        messagebox.showinfo("Game over", "Tie")

n = 1000
window = Tk()
window.title("Menu")

def clickPlayVSComputerButton():
    global onMenu, playVSComp
    s = sizeOfFieldEntry.get()
    if(len(s) < 3 and len(s) > 0 and ord(s[0]) >= ord('0') and ord(s[0]) <= ord('9') and  ord(s[-1]) >= ord('0') and ord(s[-1]) <= ord('9') and int(s) >= 5 and int(s) <= 25):
            onMenu = 0
            playVSComp = True
    else:
        messagebox.showwarning("change size of the field", "Size of the field must be a number from 5 to 25")

def clickPlayVSHumanButton():
    global onMenu, playVSComp
    s = sizeOfFieldEntry.get()
    if (len(s) < 3 and len(s) > 0 and ord(s[0]) >= ord('0') and ord(s[0]) <= ord('9') and  ord(s[-1]) >= ord('0') and ord(s[-1]) <= ord('9') and int(s) >= 5 and int(s) <= 25):
            onMenu = 0
            playVSComp = False
    else:
        messagebox.showwarning("change size of the field", "Size of the field must be a number from 5 to 25")

def clickRulesButton():
    messagebox.showinfo("Правила:", "    Игровое поле может представлять собой любую замкнутую область на клетчатой бумаге.\n"
                                 "    В игре участвует два игрока, которые ходят по очереди.Ход представляет собой постановку черты длиной в одну клетку — по вертикали или по горизонтали.\n"
                                 "    В случае если после хода игрока одна или две клетки становятся закрыты(т. е. были поставлены четвертые составляющие их черты)\n"
                                 "игрок обязан поставить в закрытых им квадратах свой знак(крестик или нолик) и сделать еще один ход (поставить еще одну черту)\n"
                                 "    Игроки ходят пока все поле не будет заполнено. В конце игры подсчитывается количество знаков каждого игрока, выигрывает тот, чьих знаков больше.")


playVSComp = False
onMenu = 1

fieldType = IntVar()
fieldType.set(1)

typeOfTheFieldlabel = Label(text = "Choose type of the field:", padx= 100, pady = 10)
typeOfTheFieldlabel.pack()


rombFieldButton = Radiobutton(text="romb", value=1, variable=fieldType, padx=100, pady=10)
rombFieldButton.pack()

squareFieldButton = Radiobutton(text="square", value=2, variable=fieldType, padx=100, pady=10)
squareFieldButton.pack()



sizeOfTheFieldlabel = Label(text = "Enter size of the field")
sizeOfTheFieldlabel.pack()
sizeOfFieldEntry = Entry()
sizeOfFieldEntry.pack()


playVSComputerButton = Button(text="play VS the bot", command=clickPlayVSComputerButton)
playVSComputerButton.pack()
playVSHumanButton = Button(text="play VS human", command=clickPlayVSHumanButton)
playVSHumanButton.pack()
rulesButton = Button(text="rules", command=clickRulesButton)
rulesButton.pack()

while (onMenu != 0):
    window.update()
k = 5
k = int(sizeOfFieldEntry.get())

squareFieldButton.destroy()
rombFieldButton.destroy()
rulesButton.destroy()
playVSComputerButton.destroy()
playVSHumanButton.destroy()
sizeOfFieldEntry.destroy()
sizeOfTheFieldlabel.destroy()
typeOfTheFieldlabel.destroy()

playerA = HumanPlayer(1)
if(playVSComp):
    playerB = CompPlayer(2)
else:
    playerB = HumanPlayer(2)


a = 40  # side of a Sell
n = (k + 2) * a
window.option_clear()
c = Canvas(window, width=n, height=n, bg='white')
c.pack()

if (fieldType.get() == 2):
    field = SquareField(k)
elif (fieldType.get() == 1):
    field = RombField(k)
c.create_rectangle(0, 0, n, n)
field.draw(window, c)

window.bind('<Button-1>', click)

window.after(0, gameProccess(playerA, playerB, field))
