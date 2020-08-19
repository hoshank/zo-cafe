def testDecorator(func):
    def wrappedFunc():
        print("\nFunciton being executed ----   "  , func.__name__)
        print("Result : ")
        return func()
    return wrappedFunc