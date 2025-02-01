# python datatypes

# NUMBERS
# integer
print(type(234))
print(type(-5789))
# float
print(type(7.33))
print(type(-58.33))
print(type(10.))
print(type(2e6))
# complex
print(type(2e5j))
print(type(5+12j))
print(type(234j))

# STRING
print(type("hello world"))
print(type('hello python'))

# Boolean - True and false
print(True)
print(False)
print(type(True))
print(type(False))

# None - empty value
print(None)
print(type(None))

# SEQUENCE datatypes  -- data will be in ordered
# strings
a = "apple"
print(a, "\n", type(a))
# lists
ls = [10, 20, 30, 40]
print(ls, "\n", type(ls))
# tuples
tu = (101, 202, 303, 404)
print(tu, "\n", type(tu))


# SET - unordered, contain unique data's, {"set"}
set_1 = {10, 20, 40, 80, 30, 20, 10}
print(set_1, "\n", type(set_1))

# ASSESSMENT question
a = {2, 3, 54, 4, 23}
b = set((1, 2, 3))
c = set([1, 2, 4, 3])
# d = set([[2,2],[3,4]])   #unhashable in set -- due to list is mutable
d = set([(22, 22), (22, 3)])   #hashable in set -- due to tuple is immutable
print(d)

print(a, b, c, sep="\n")

# DICTIONARY - key value pair
dict_1 = {
    'Name': 'elsa',
    'job role': 'data analyst',
    'salary in LPA': 6,
    'experience in Years': 1
}
print(dict_1, "\n", type(dict_1))





