def hey_deco(func):


    def inner1():
        print("THis is before function execution")


        func()
        print("This is after function execution")


    return inner1 


@hey_deco
def heyy():
    print("Dude")

heyy()    
