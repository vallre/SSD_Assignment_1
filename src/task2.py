import time
import inspect

def Task2(func):
    '''Function decorator which executes the passed in function and prints its execution time, the number of time the function was called, and 
    a detailed information about the function, such that name, signature, arguments, docstring, source code and output of the function.
    The output of the function both displayed in the stdout and returned as normal.
    
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

        # collect information about the relevant function members
        members = dict(inspect.getmembers(func))
        signature = inspect.signature(func, follow_wrapped=True)
        # separate the docstring into line for a goodloking output; also remove leading spaces
        doc_lines = members['__doc__'].split("\n")
        doc_lines = [line.lstrip(" ") for line in doc_lines]
        # remove the leading spaces from the function source code for readability
        source_code = inspect.getsourcelines(func)[0]

        # print the tracked information
        print(f"Function {func.__name__} was called {count} times.")
        print(f"Execution time of this call is {timeVar} seconds.")
        print(f"Name:\t{members['__name__']}")
        print(f"Type:\t{members['__class__']}")
        print(f"Sign:\t{signature}")
        print(f"Args:\tpositional: {args}")
        print(f"\tkeyworded: {kwargs}")
        print(f"\nDoc:", end="")
        for line in doc_lines:
            print(f"\t{line}")
        print(f"\nSource:", end="")
        for line in source_code:
            print(f"\t{line}", end="")
        print(f"\nOutput:\t{output}")


        return output
    return wrapper