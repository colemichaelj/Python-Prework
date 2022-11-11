# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("What's Up!!??!! " + user_name.title() + "? ((:")

hello_name('Jimmy Choo')




# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for number in range(100):
        if number % 2 == 1:
            print(number)
first_odds()
# here the function is invoked.

def first_odds2():
    for number in range(1,101,2):
        if number % 2 == 1:
            print(number)
# here the function is not invoked.



# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
a_list = [1,2,3,4,6000000000]
print("Max number is:", max_num_in_list(a_list))



# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    if a_year % 100 == 0:
        leap = False 
    if a_year % 4 == 0:
        leap = True
    return leap
a_year = 2400
if(is_leap_year(a_year)):
    print("Leap Year! :))")
else:
    print("Not a Leap Year :((")



# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [1,2,3,4,5]
print(is_consecutive(a_list))
