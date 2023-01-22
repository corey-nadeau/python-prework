grocery_list = ['apple','banana','orange','spinach','kale','curry']

my_info=[x+1 for x in range(20) if x %2==0]

print(my_info)
for i in grocery_list:
    continue
    print("yeehaw")

#urgent_groceries = []
#for item in grocery_list:
#    if item[0]in['a','b','c']:
#        urgent_groceries.append(item)
#    else:
#        continue
#my_groceries=[item for item in grocery_list if item[0] in ['a','b','c']]

#print(urgent_groceries)
#print(my_groceries)