from tkinter import *

a = 40  # side of a Sell
def to_display_coord(x):
    return a * x + a


class Sell:
    """
    :param value:
     0 if empty;
     1 if X;
     2 if O;
    -1 if not a part of field
    """

    def __init__(self, value: int = -1, left=False, right=False, up=False, down=False):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.value = value


class Field:
    arr = []
    emptySellCounter = 0

    def __init__(self, n: int = 0):
        self.arr = [[Sell() for j in range(n)] for i in range(n)]

    def draw(self, window: Tk, c):
        window.title("Labirint")

        k = self.arr.__len__()
        # a = 40  # side of a Sell
        n = (k + 2) * a
        window.geometry(str(n) + 'x' + str(n))

        # drawing Sells

        # c.create_line(a, 0, a, n, width = 4, fill='black')
        # c.create_line(0, a , n, a, width=4, fill='black')
        for i in range(a, n, a):
            c.create_line(i, 0, i, n, width=1, fill='grey')
        for i in range(a, n, a):
            c.create_line(0, i, n, i, width=1, fill='grey')

        # drawing signes and used sells
        for i in range(k):
            for j in range(k):
                if (self.arr[i][j].left):
                    c.create_line(to_display_coord(i), to_display_coord(j), to_display_coord(i), to_display_coord(j + 1), width=4,
                                  fill='black')
                if (self.arr[i][j].up):
                    c.create_line(to_display_coord(i), to_display_coord(j), to_display_coord(i + 1), to_display_coord(j), width=4,
                                  fill='black')
                if (self.arr[i][j].right):
                    c.create_line(to_display_coord(i + 1), to_display_coord(j), to_display_coord(i + 1), to_display_coord(j + 1), width=4,
                                  fill='black')
                if (self.arr[i][j].down):
                    c.create_line(to_display_coord(i), to_display_coord(j + 1), to_display_coord(i + 1), to_display_coord(j + 1), width=4,
                                  fill='black')
                if (self.arr[i][j].value == 1):
                    c.create_line(to_display_coord(i), to_display_coord(j),to_display_coord(i + 1), to_display_coord(j + 1), fill='red', width = 4)
                    c.create_line(to_display_coord(i + 1), to_display_coord(j), to_display_coord(i) ,to_display_coord(j + 1), fill='red', width=4)
                if (self.arr[i][j].value == 2):
                    c.create_oval(to_display_coord(i) + a // 4,to_display_coord(j) + a // 4, to_display_coord(i) + a * 3 // 4,
                                  to_display_coord(j) + a * 3 // 4, fill='blue')


    def isFull(self):

        return self.emptySellCounter == 0

    def calulateScore(self):
        scoreA = 0
        scoreB = 0
        for i in range(self.arr.__len__()):
            for j in range(self.arr[i].__len__()):
                if (self.arr[i][j].value == 1):
                    scoreA += 1
                if (self.arr[i][j].value == 2):
                    scoreB += 1
        return scoreA, scoreB


class SquareField(Field):
    def __init__(self, n: int):
        super().__init__(n)
        for i in range(n):
            self.arr[i][0].up = True
            self.arr[i][n - 1].down = True
            self.arr[0][i].left = True
            self.arr[n - 1][i].right = True
            for j in range(n):
                self.arr[i][j].value = 0
        self.emptySellCounter = n * n


    #def draw(self, window, c):


class RombField(Field):
    def __init__(self, n: int):
        super().__init__(n)
        for i in range(n // 2 + 1):
            for j in range(n // 2 - i, n // 2 + i + 1):
                self.arr[i][j].value = 0

                if(j == n // 2 - i):
                    self.arr[i][j].left = True
                    self.arr[i][j].up = True
                if (j == n // 2 + i):
                    self.arr[i][j].left = True
                    self.arr[i][j].down = True
                    print(i, j)

        for i in range(n // 2):
            for j in range(n // 2 - i, n // 2 + i + 1):
                self.arr[n - 1 - i][j].value = 0
                if(j == n // 2 - i):
                    self.arr[n - 1 - i][j].right = True
                    self.arr[n - 1 - i][j].up = True
                if (j == n // 2 + i):
                    self.arr[n - 1 - i][j].right = True
                    self.arr[n - 1 - i][j].down = True
        self.arr[0][(n - 1) // 2].left = self.arr[0][(n - 1) // 2].right = self.arr[0][(n - 1) // 2].up = self.arr[0][(n - 1) // 2].down = True
        self.arr[n - 1][(n - 1) // 2].left = self.arr[n - 1][(n - 1) // 2].right = self.arr[n - 1][(n - 1) // 2].up = self.arr[n - 1][(n - 1) // 2].down = True
        self.arr[(n - 1) // 2][0].left = self.arr[(n - 1) // 2][0].right = self.arr[(n - 1) // 2][0].up = self.arr[(n - 1) // 2][0].down = True
        self.arr[(n - 1) // 2][n - 1].left = self.arr[(n - 1) // 2][n - 1].right = self.arr[(n - 1) // 2][n - 1].up = self.arr[(n - 1) // 2][n - 1].down = True

        self.arr[1][(n - 1) // 2].left = True
        self.arr[n - 2][(n - 1) // 2].right = True
        self.arr[(n - 1) // 2][1].up = True
        self.arr[(n - 1) // 2][n - 2].down = True
        self.arr[0][(n - 1) // 2].value = self.arr[n - 1][(n - 1) // 2].value = 1
        self.arr[(n - 1) // 2][0].value = self.arr[(n - 1) // 2][n - 1].value = 2
        self.emptySellCounter = n * n - (n - 1) // 2 * ((n - 1) // 2 + 1) * 2 - 4

