def element_and_greeting(*args,**kwargs):
    element=1
    for num in args:
        element*=num
    print(element)
    print(f"Hello{kwargs}")
