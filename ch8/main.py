def addTwo(num):
    return num + 2
def addThree(num):
    return num + 3



def namePrinter(first, last, middle=''):
    return f"The name's {last}. {first}, {middle}, {last}."
print(namePrinter("James","Bond","freddie"))

def giveMeMyGroceries(thing_to_add):
    grocery_list = ['grapes','oragnges','bananas']
    grocery_list.append("thing_to_add")
    return grocery_list
print(giveMeMyGroceries)