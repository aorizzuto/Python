"""
N non-negative integers representing an elevation map where the width of each bar is 1.

Compute how much water it is able to trap after raining.
"""

def trappingRainWater(arr):
    """Get trapped rain water."""
    drawArray(arr)      # Drawing the problem
    n = len(arr)    
    left = [0]*n        # "left" contains height of tallest bar from left to right
    right = [0]*n       # "right" contains height of tallest bar from right to left
 
    water = 0           # Initialize result
 
    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])
 
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
 
    print("From left to right -> ",left)
    print("From right to left -> ",right)
    print("Array ->              ",arr)
    print("\n")

    lst = []
    for i in range(0, n):
        lst.append(min(left[i], right[i]) - arr[i])
        water = sum(lst)
 
    print("Result ->             ",lst)
    print("\n")
    return water


def drawArray(arr):
    """Draw the array with blocks."""
    MAX = max(arr)

    print('\n')

    for i in range(MAX):
        lst=[]
        for j in range(len(arr)):
            if arr[j] >= (MAX-i):
                lst.append('█')
            else:
                lst.append(' ')
        print(''.join(lst))
    print('\n')



def main():
    """Start problem."""
    arr1 = (2, 1, 2)                                # Water = 1
    arr2 = (5, 1, 3, 0, 4)                          # Water = 8
    arr3 = (0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 3, 1)     # Water = 8

    water = trappingRainWater(arr1)
    print ("Water trapped is: ",water)

    water = trappingRainWater(arr2)
    print ("Water trapped is: ",water)

    water = trappingRainWater(arr3)
    print ("Water trapped is: ",water)


if __name__ == "__main__":
    main()