# Project Euler: 2
#    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

def euler_2(n, max_num): # def fib(n):
    a = 0
    b = 1
    l=[]
    if n < 2:
        return n 
    else: 
        for i in range(2,n+2): 
            c = a + b 
            a = b 
            b = c 
            if c < max_num:
                l.append(c)
            else:
                break       # Exit if max_num is reached
    print(l,"\n")                # Print all numbers
    
    x = [i for i in l if i%2 == 0]
    
    print(x,"\n")
    
    return sum(x)


if __name__ == "__main__":
    print("Sum:",euler_2(40, 4000000))


"""
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578] 

[2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578] 

Sum: 4613732
"""
