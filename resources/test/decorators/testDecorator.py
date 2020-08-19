def testDecorator(func):
    def wrappedFunc():
        print("\nFunction being executed ----   "  , func.__name__)
        print("Result : ")
        return func()
    return wrappedFunc