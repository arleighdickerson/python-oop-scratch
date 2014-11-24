def decorator(function):
    def inner():
        try:
            return function()
        except:
            print("Exception caught")
 
    return inner
 
@decorator
def someMethod():
    print("someFunction called - going to throw exception")
    raise Exception()

someMethod()
