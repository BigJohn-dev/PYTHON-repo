
def display_asterisks(func):
    def wrapper(*args, **kwargs):
        print('********')
        result = func(*args, **kwargs)
        print("********")
        return result
    return wrapper

@display_asterisks
def display_name(name):
    print(name)

display_name("Big John")
