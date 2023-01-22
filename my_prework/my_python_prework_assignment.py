#questin_1

def hello_name(user_name):
    print("hello_"+ user_name.upper())
user_name = input("Enter USERNAME:")
hello_name(user_name)


#question_2

def first_odds(min,max):
    if min>max:
        return
    if min&1:
        print(min,end=",\n ")
        return first_odds(min+1,max)
    else:
        return first_odds(min+1,max)
min=1;max=100
first_odds(min,max)
   

#question_3

def max_num_in_list(a_list):
    a_list = [12,33,2,5,86,54]
    max_num = max(a_list)
    print(max_num)
max_num_in_list(1000)


#question_4

def is_a_leap_year(year):
    if ((year % 400 == 0 or
        year % 100 != 0 and
        year % 4 == 0)):
        print("True")
    else:
        print("False")
is_a_leap_year(1988)

#question_5

def is_consecutive(a_list):
    return sorted(
        a_list) == list(range(min(a_list), max(a_list)+1))
     
num_list = [20,22,18,19,21]
print(is_consecutive(num_list))