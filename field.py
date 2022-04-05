from tkinter import *


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
        a = 40  # side of a Sell
        n = k * a * 2
        window.geometry(str(n) + 'x' + str(n))

        for i in range(a, n, a):
            c.create_line(i, 0, i, n, width=1, fill='grey')
        for i in range(a, n, a):
            c.create_line(0, i, n, i, width=1, fill='grey')




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


    def draw(self, window, c):
        super().draw(window, c)
        k = self.arr.__len__()
        a = 40  # side of a Sell
        n = k * a * 2
        for i in range(k):
            for j in range(k):
                if (self.arr[i][j].left):
                    c.create_line(n // 4 + i * a, n // 4 + j * a, n // 4 + i * a, n // 4 + j * a + a, width=4,
                                  fill='black')
                if (self.arr[i][j].up):
                    c.create_line(n // 4 + i * a, n // 4 + j * a, n // 4 + i * a + a, n // 4 + j * a, width=4,
                                  fill='black')
                if (self.arr[i][j].right):
                    c.create_line(n // 4 + i * a + a, n // 4 + j * a, n // 4 + i * a + a, n // 4 + j * a + a, width=4,
                                  fill='black')
                if (self.arr[i][j].down):
                    c.create_line(n // 4 + i * a, n // 4 + j * a + a, n // 4 + i * a + a, n // 4 + j * a + a, width=4,
                                  fill='black')
                if (self.arr[i][j].value == 1):
                    c.create_line(n // 4 + i * a, n // 4 + j * a, n // 4 + i * a + a, n // 4 + j * a + a, fill='red', width = 4)
                    c.create_line(n // 4 + i * a + a, n // 4 + j * a, n // 4 + i * a , n // 4 + j * a + a, fill='red', width=4)
                if (self.arr[i][j].value == 2):
                    c.create_oval(n // 4 + i * a + a // 4, n // 4 + j * a + a // 4, n // 4 + i * a + a * 3 // 4,
                                  n // 4 + j * a + a * 3 // 4, fill='blue')



class RombField(Field):
    def __init__(self, n: int):
        super().__init__(n)
        for i in range(n):
            for j in range((n - 1) // 2 - i, (n - 1) // 2 + i + 1):
                self.arr[i][j].value = 0
        self.arr[0][(n - 1) // 2].value = self.arr[n - 1][(n - 1) // 2].value = 1
        self.arr[(n - 1) // 2][0].value = self.arr[(n - 1) // 2][n - 1].value = 2
        emptySellCounter = n * n - (n - 1) // 2 * ((n - 1) // 2 + 1) * 2 - 4
