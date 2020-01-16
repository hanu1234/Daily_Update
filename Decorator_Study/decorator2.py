def decor(func):

    def inner(name):
        if name == 'Sunny':
            print("Hello sunny good morning")
        else:
            func(name)
    return inner


# whenever you call wish function internally decor function will execute
@decor     # linking the decorator function to the wish function
def wish(name):
    print("Hello", name, "Good morning")


wish("Durga")
wish('Sunny')

# without decorator "decorfunction = decor(wish)"


