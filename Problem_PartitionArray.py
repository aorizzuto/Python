"""
For this problem, a given set can be partitioned in such a way, that sum of each subset is equal.

At first, we have to find the sum of the given set. If it is even, then there is a chance to divide it into two sets. Otherwise, it cannot be divided.

For even value of the sum, then we will create a table named partTable, now use the following condition to solve the problem.
"""

def isPartitioned(arr):
    """Check if array can be partitioned."""
    print(arr)
    lst = [sum(arr[:i]) == sum(arr[i:]) for i in range(len(arr))]
    if any(lst):
        position = [i for i in range(len(lst)) if lst[i] == True]
        for i in position:
            print(arr[:i],"-",arr[i:])
        return True
    else:
        return False

    # Fastest way
    #return any([sum(arr[:i]) == sum(arr[i:]) for i in range(len(arr))])



def main():
    """Start app."""
    arr = [3,4,2,2,2,5]
    result = isPartitioned(arr)
    print(result,"\n")

    arr = [3,1,6,2,2,5]
    result = isPartitioned(arr)
    print(result,"\n")

    arr = [3,1,1,2,2,5]
    result = isPartitioned(arr)
    print(result,"\n")



if __name__ == '__main__':
    main()