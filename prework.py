#returns given username
def hello_name(user_name):
    print("hello_" + user_name + "!")

hello_name("USERNAME")

#returns odd numbers between 1-100
def first_odds():
    for i in range(1,101):
        if i % 2 == 1:
            print(i)
        
first_odds()

#returns the maximum number in a list
def max_num_in_list(a_list):
    print(max(a_list))

#returns True if given year is a leap year
def is_leap_year(a_year):
    if((a_year % 100 != 0) or
       (a_year % 400 == 0) and
       (a_year % 4 == 0)):
        return True
    return False


#returns True if given list is consecutive. 
def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    return False

