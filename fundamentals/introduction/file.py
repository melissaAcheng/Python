num1 = 42 # variable declaration
num2 = 2.3  # variable declaration
boolean = True  # data type, primitive, boolean
string = 'Hello World'  # data type, primitive, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  # variable declaration, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuples, initialize
print(type(fruit))  # tuples, access value
print(pizza_toppings[1])  # list, access value
pizza_toppings.append('Mushrooms')  # list, add value
print(person['name']) # dictionary, access value
person['name'] = 'George' # dictionary, change value
person['eye_color'] = 'blue'  # dictionary, change value
print(fruit[2]) # tuples, access value

# conditional, if, else
if num1 > 45:     
    print("It's greater")
else:
    print("It's lower")   

# conditional, if, else if, else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)

# while loop
x = 0 # start
while(x < 5): #stop
    print(x)
    x += 1  # increment

# delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color') # delete value
print(person)

# for loop, conditionals
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():  # function
    for num in range(10): # for loop
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # function with argument
    for num in range(x):  # for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # function 
    for num in range(x):  # for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)