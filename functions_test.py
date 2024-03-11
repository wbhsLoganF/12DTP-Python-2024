import easygui

def greet():
    easygui.msgbox("Hello World!")

greet()

"""
def greet_v2(name):
    easygui.msgbox(f"Hello {name}")

greet_v2("Bruce")
"""

def hello():
    name = easygui.enterbox("Please enter your name")
    easygui.msgbox(f"Hello {name}")

    age = easygui.integerbox("Please enter your age")
    easygui.msgbox(f"Hello {name}, you are {age} years old!")

#hello()

def task1():
    num1 = 0
    num2 = 0

    num1 = easygui.integerbox("Choose a number:", upperbound = ("999"))
    operator = easygui.buttonbox("Choose an operator:", choices = ["+","-","*","/"])
    num2 = easygui.integerbox ("Choose another number:", upperbound = ("999"))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        result = num1 / num2
    easygui.msgbox(f"{num1} {operator} {num2} = {result}")
#task1()

#in development
def task2():
    numbers = [2,4,6,1,5,3,7,8,9,10,11,12,13,14]
    first = 0
    second = 1
    while second <= 6 and first <= 6:
        if numbers[first] > numbers[second]:
            easygui.msgbox(f"{numbers[first]} is bigger than {numbers[second]}")
            numbers.remove(numbers[second])
            if first < 6:
                first += 1
        else:
            easygui.msgbox(f"{numbers[first]} is smaller than {numbers[second]}")
            numbers.remove(numbers[first])
            if second < 6:
                second += 1

    easygui.msgbox(f"{numbers} is the biggest number in the list")
#task2()

def task4():
    word1 = easygui.enterbox("Pick a word")
    word2 = easygui.enterbox("Pick another word or the same word")
    if word1 == word2:
        easygui.msgbox("True")
    else:
        easygui.msgbox("False")
#task4()

def task5():
    e
#task5()

def task6():
    number = easygui.integerbox("Pick a number")
    if number % 2 == 0:
        easygui.msgbox(f"{number} is even")
    else:
        easygui.msgbox(f"{number} is odd")
#task6()

def task7():
    list1 = [1,2,3,4,5]
    list2 = [1,3,5,7,9]
    list3 = []
    term1 = 0
    term2 = 0
    for i in range(1,6):
        for i in range(1,6):
            if list1[term1] == list2[term2]:
                list3.append(list2[term2])
                term2 += 1
        term1 +=1
    easygui.msgbox(list3)
task7()
        



#done 1. Write a function that takes two numbers as arguments and returns the sum.

#2. Write a function that takes a list of numbers as an argument and returns the largest in the list.

#3. Write a function that takes a string as an argument and returns the number of vowels in the string.

#done 4. Write a function that takes two strings as arguments and returns True if the second string is identical to the first, and False if otherwise.

#5. Write a function that takes a list of strings as an argument and returns a new list containing only the strings that have a length greater than 3 characters.

#done 6. Write a function that takes a number as an argument and returns True if the number is even, and False otherwise.

#7. Write a function that takes two lists of numbers as arguments and returns a new list containing the elements that are common to both lists.