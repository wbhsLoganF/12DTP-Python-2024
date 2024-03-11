def print_hello(): 

    print("Hello!") 

print_hello() 

 

def print_numbers(): 

    number = 1 
    while number <= 10: 
        print(number) 
        number += 1 

print_numbers() 

 

def print_even_numbers(): 

    number = 2 
    while number <= 20: 
        print(number) 
        number += 2 

print_even_numbers() 

 

def print_odd_numbers(): 

    number = 1 
    while number <= 20: 
        print(number) 
        number += 2 

print_odd_numbers() 

 

def print_multiplication_table(): 

    number = 5 
    number2 = 1 
    for i in range (1, 11): 
        number3 = number * number2  
        print(number3) 
        number2 += 1 

print_multiplication_table() 



def print_sum():
    total = sum(range(1,11))
    print(f"sum: {total}")

print_sum()


def print_factorial():
    factorial = 1
    for i in range (1,6):
        factorial *= i
    print(f"Factorial of 5: {factorial}")

print_factorial()


def fibonacci():
    a = 0
    b = 1
    new = 0
    print(a)
    print(b)
    for i in range(1,10):
        new = a + b
        print(new)
        a = b
        b = new

fibonacci()



'''
def prime_numbers():
    for i in range(1,21):
        if i > 1:
            for i in range(2, i):
                if (i % 1) == 0:
                    break
                else:
                    print(i)


prime_numbers()
'''

def pattern():
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
pattern()