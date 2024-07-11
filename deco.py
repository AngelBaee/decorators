def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Dunno what's going on")

    print(greeting)

greet(shout)
greet(whisper)    