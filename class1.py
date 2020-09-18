print('welcome to python class')
print('what is your favorate food?'input())

# check the data type

type('hello')
type([1,2,34])


# function 1 : add two number 


def add_two(num1, num2):
    return num1 + num2


add_two(2,3)

# function 2 : add from 0 to the number, this number must >0

def add_till(n): 
    init = 0 
    while n > 0: 
        init += n
        n -= 1 
    return init

add_till(3) # 1 + 2 + 3 = 6 



# Program to display the Fibonacci sequence up to n-th term n

''' from web'''

def fib():
    nterms = int(input("How many terms? "))
    # first two terms
    n1, n2 = 0, 1
    count = 0
# check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1