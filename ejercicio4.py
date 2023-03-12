
import sys 

var_ing = sys.argv

def my_function(*args):
    for i in args:
        print(i)

my_function(var_ing)        