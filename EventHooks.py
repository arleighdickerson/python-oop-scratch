'''
@see: http://www.voidspace.org.uk/python/weblog/arch_d7_2007_02_03.shtml#e616
'''

class EventHook(object):
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)  # added __ to self.handlers
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)  # added __ to self.handlers
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)



hooks = EventHook()
hooks += lambda event : print("caught event with name: " + str(event))
hooks.fire("fake event")
