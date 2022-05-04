from field import Field, SquareField
class Player:

    def __init__(self, sign):
        self.hasMoved = False
        self.sign = sign

    def canMove(self, field, i, j, vertical):
        return (i >= 0 and j >= 0 and j < len(field.arr) and i < len(field.arr) and field.arr[i][j].value == 0 and (  ((not field.arr[i][j].left) and vertical) or ( not field.arr[i][j].up and (not vertical)) ) )

    def move(self, field: Field, i, j, vertical : bool):
        # stick is on left arr[i][j], if it is vertical
        # stick is upper arr[i][j], if it is horizontal
        print(i, j, vertical, end=' ')
        self.hasMoved = True
        if(vertical):
            field.arr[i][j].left = True
            field.arr[i][j].cnt += 1
            if field.arr[i][j].cnt == 4:
                field.arr[i][j].value = self.sign
                field.emptySellCounter -= 1
                self.hasMoved = False

            if(i > 0):
                field.arr[i - 1][j].right = True
                field.arr[i - 1][j].cnt += 1
                if field.arr[i - 1][j].cnt == 4:
                    field.arr[i - 1][j].value = self.sign
                    field.emptySellCounter -= 1
                    self.hasMoved = False

        else:
            field.arr[i][j].up = True
            field.arr[i][j].cnt += 1
            if field.arr[i][j].cnt == 4:
                field.emptySellCounter -= 1
                field.arr[i][j].value = self.sign
                self.hasMoved = False
            if (j > 0):
                field.arr[i][j - 1].down = True
                field.arr[i][j - 1].cnt += 1
                if field.arr[i][j - 1].cnt == 4:
                    field.emptySellCounter -= 1
                    field.arr[i][j - 1].value = self.sign
                    self.hasMoved = False
        print(" player", self.sign,(field.arr[i][j].cnt),(field.arr[i-1][j].cnt),(field.arr[i][j-1].cnt),(field.arr[i][j].value),(field.arr[i-1][j].value),(field.arr[i][j-1].value) )

class HumanPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)

def countOfSellsThatWeCanTake(field : Field, i, j):
    returnValue = 0
    if ( field[i][j].cnt == 3):
        if (field.arr[i][j].cnt == 3):
            if (not field.arr[i][j].left):
                field.arr[i - 1][j].right = True
                field.arr[i - 1][j].cnt += 1
                returnValue = countOfSellsThatWeCanTake(field, i - 1, j) + 1
                field.arr[i - 1][j].right = False
                field.arr[i - 1][j].cnt -= 1

            elif (not field.arr[i][j].right):
                field.arr[i + 1][j].left = True
                field.arr[i + 1][j].cnt += 1
                returnValue = countOfSellsThatWeCanTake(field, i + 1, j) + 1
                field.arr[i + 1][j].left = False
                field.arr[i + 1][j].cnt -= 1

            elif (not field.arr[i][j].up):
                field.arr[i][j - 1].down = True
                field.arr[i][j - 1].cnt += 1
                returnValue = countOfSellsThatWeCanTake(field, i, j - 1) + 1
                field.arr[i][j - 1].down = False
                field.arr[i][j - 1].cnt -= 1
            elif (not field.arr[i][j - 1].down):
                field.arr[i][j + 1].up = True
                field.arr[i][j + 1].cnt += 1
                returnValue = countOfSellsThatWeCanTake(field, i, j + 1) + 1
                field.arr[i][j + 1].up = False
                field.arr[i][j + 1].cnt -= 1
    return returnValue
class CompPlayer(Player):
    def __init__(self, sign):
        super().__init__(sign)
    def play(self, field: Field):
        n = field.arr.__len__()
        emptyStickCounter = 0
        canTakeSellCounter = 0
        for i in range(n):
            for j in range(n):
                if (i > 0 and field.arr[i - 1][j].value == 0 and field.arr[i][j].value == 0  and (
                not field.arr[i - 1][j].right) and field.arr[i - 1][j].cnt < 2 and field.arr[i][j].cnt < 2):
                    emptyStickCounter += 1
                if ( j > 0 and field.arr[i][j - 1].value == 0 and field.arr[i][j].value == 0 and (
                not field.arr[i][j - 1].down) and field.arr[i][j - 1].cnt < 2 and field.arr[i][j].cnt < 2):
                    emptyStickCounter += 1

                if(field.arr[i][j].cnt == 3):
                    canTakeSellCounter += 1

        x = -1
        y = -1
        vertical = True

        if (emptyStickCounter > 0):
            # there is a lot of empty sells

            if (canTakeSellCounter == 0):
                # there is no almost full sells
                haveFound = False
                for i in range(n):
                    if(haveFound):
                        break
                    for j in range(n):
                        if (field.arr[i-1][j].value == 0 and field.arr[i][j].value == 0 and i > 0 and (not field.arr[i - 1][j].right) and field.arr[i - 1][j].cnt < 2 and field.arr[i][j].cnt < 2):
                            x = i
                            y = j
                            vertical = True
                            haveFound = True
                            break
                        if (field.arr[i][j - 1].value == 0 and field.arr[i][j].value == 0 and j > 0 and (not field.arr[i][j - 1].down) and field.arr[i][j - 1].cnt < 2 and field.arr[i][j].cnt < 2):
                            x = i
                            y = j
                            vertical = False
                            haveFound = True
                            break

            else:
                for i in range(n):
                    for j in range(n):
                        if (field.arr[i][j].cnt == 3):
                            if (not field.arr[i][j].left):
                                x = i
                                y = j
                                vertical = True
                            elif (not field.arr[i][j].right):
                                x = i + 1
                                y = j
                                vertical = True
                            elif (not field.arr[i][j].up):
                                x = i
                                y = j
                                vertical = False
                            elif (not field.arr[i][j].down):
                                x = i
                                y = j + 1
                                vertical = False
        else:
            if(canTakeSellCounter):
                for i in range(n):
                    for j in range(n):
                        if(countOfSellsThatWeCanTake(field, i, j) > )





        self.move(field, x, y, vertical)

