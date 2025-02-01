# comment

"""  multi
line
comment
triple double quotes for multi line comments
"""

'''
triple single quotes for multi line comments
'''

"""
doc string is enclosed within triple double quotes
"""


# simple add function
def add(a,b):
    """This function is used to add any 2 numbers which is passed as a argument"""
    return a+b
add(1,2)
# docstring can be accesed using help() or __doc__
print("\n help  ------- of add()")
help(add)
# or
print("doc of add()----------")
print(add.__doc__)

# to see all docstrings
print("\n doc of this entire code ------------")
print(__doc__)
