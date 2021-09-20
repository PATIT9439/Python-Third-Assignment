

def multiple_word(function):
    def wrapper(text,n):
        for i in range(0,n):
            print(text, end="\n")
        return function(text,n)
    return wrapper

@multiple_word
def take_input(text,n):
    pass
text=input("what you want to print? \n")
n=int(input("how many times you want to print? \n"))
take_input(text,n)




