"""
Box Stacking problem

In this problem a set of different boxes are given, the length, breadth, and width may differ for different boxes. 
Our task is to find a stack of these boxes, whose height is as much as possible. We can rotate any box as we wish. 
But there is a rule to maintain. One can place a box on another box if the area of the top surface for the bottom box 
is larger than the lower area of the top box.
"""

class Box():

    def __init__(self, arr):
        self.A = arr[0]      # Height
        self.B = arr[1]      # Width
        self.C = arr[2]      # Deep

    def getMaxHeight(self):
        return max(self.A, self.B, self.C)

    def getResidualArea(self):
        lst = [self.A, self.B, self.C]

        lst.pop(lst.index(max(lst)))

        return lst[0]*lst[1]

def getMaxHeight(boxes):
    suma = 0
    for box in boxes:
        suma += box.getMaxHeight()
    return suma

def main():
    """Start app."""
    arr = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
    boxes = [Box(i) for i in arr]
    result = getMaxHeight(boxes)
    print(result,"\n")

    



if __name__ == '__main__':
    main()



