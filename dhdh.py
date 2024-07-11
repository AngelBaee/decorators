def decorator(func):
    def inner():
        print("**********")


        func()
        print("**********")

    return inner 

@decorator
def hey():
    print("Here we go bitch")

hey()            
