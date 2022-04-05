from field import Field, SquareField
class Player:
    def __init__(self, par):
        self.hasMoved = False
        self.sign = par
    def move(self, field: Field):
        pass
class HumanPlayer(Player):
    def __init__(self,pa):
        super().__init__(pa)

    def move(self, field: Field, i, j, vertical : bool):
        print("Player"+str(self.sign))
        self.hasMoved = True
        if(vertical):
            field.arr[i][j].left = True
            if field.arr[i][j].left and field.arr[i][j].up and field.arr[i][j].down and field.arr[i][j].right:
                field.arr[i][j].value = self.sign
                field.emptySellCounter -= 1
                self.hasMoved = False

            if(i > 0):
                field.arr[i - 1][j].right = True
                if field.arr[i-1][j].left and field.arr[i-1][j].up  and field.arr[i-1][j].down and field.arr[i-1][j].right:
                    field.arr[i-1][j].value = self.sign
                    field.emptySellCounter -= 1
                    self.hasMoved = False

        else:
            field.arr[i][j].up = True
            if field.arr[i][j].left and field.arr[i][j].up and field.arr[i][j].down and field.arr[i][j].right:
                field.emptySellCounter -= 1
                field.arr[i][j].value = self.sign
                self.hasMoved = False
            if (j > 0):
                field.arr[i][j - 1].down = True
            if field.arr[i][j - 1].left and field.arr[i][j - 1].up and field.arr[i][j - 1].down and field.arr[i][j-1].right:
                field.emptySellCounter -= 1
                field.arr[i][j - 1].value = self.sign
                self.hasMoved = False
        print(field.emptySellCounter)



