
def display_asterisks(*args, **kwargs):
    print('**********')
    print(*args, **kwargs)
    print("**********")

@display_asterisks
def display_name(name):
    print(name)

display_name("Big John")
