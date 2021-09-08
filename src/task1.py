import time

def Task1(func):
    '''Function decorator which executes the passed in function and prints its execution time. 
    Also, the decorator tracks the number of times the function was called.
    
    The original name of function and docstring will be preserved.'''

    # function call tracker
    count = 0

    def wrapper(*args, **kwargs):
        # saving the information from the passed in function to the wrapper function
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        # calculate execution time
        timeVar = time.time()
        output = func(*args, **kwargs)
        timeVar = time.time() - timeVar

        # manage function call trace
        nonlocal count
        count += 1

        # print the tracked information
        print(f"Function {func.__name__} was called {count} times.")
        print(f"Execution time of this call is {timeVar} seconds.")

        return output
    return wrapper