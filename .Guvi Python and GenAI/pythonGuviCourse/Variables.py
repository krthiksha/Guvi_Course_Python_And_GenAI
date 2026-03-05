''' variable - used to store the values (which can be used later in the program) '''

# variables 
x=10
y=20.0     # python is dynamically typed language - we can assign any type of value to a variable without declaring the type of variable
print(x)   # treated as variable
print('x')  # treated as string 
print(y)   # treated as variable
print('y')  # treated as string 

# type check 
print(type(x), type(y))

# Type Casting 
a=int(3)
b=float(3)
c=str(3)
print(a, b, c)
print(type(a), type(b), type(c))

# Variable Rules 
# 1. variable name should start with a letter or underscore
var_can_be_long123_yes = 44
_var=56
# 2. cannot start with a number
'''1_var=44   # invalid variable name'''
# 3. variable name cannot contain special characters except underscore
'''var@=44    # invalid variable name
var$=44    # invalid variable name'''
# 4. variable name cannot be a keyword (reserved word in python)
'''def = 67 #invalid variable name - def is a keyword in python'''
# 5. variable name is case sensitive
age=1
Age=2
AGE=3
print(age, Age, AGE)


# Assign multiple values to multiple variables 
domain1, domain2, domain3 = "helthcare", "education", "finance"
print(domain1, domain2, domain3)
# One value to multiple variables 
ai = ml = dl = 100 
print(ai, ml, dl)
# NOTE: make sure to have a meaningful variable Name    - helpful for code readability 
first_name = "krithiksha"
last_name = "G"
print(first_name + ' ' + last_name)
# Multiple words in variable name  (different techniques) 
camelCase   = 90
PascalCase  = 90
Snake_case  = 90
# Constant Variables – define in capital letters 
PI = 3.14
GRAVITY = 9.8
print(PI, GRAVITY)