# M5-02_Parameters_and_Return - print_vs_return.py
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(5)
b = double_return(5)
print("a is", a)
print("b is", b)
