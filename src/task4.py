import time
import inspect
import contextlib
import datetime
import io

class Task4_class:
    '''Class decorator which executes the passed in function and prints its execution time, the number of time the function was called, and 
    a detailed information about the function, such that name, signature, arguments, docstring, source code and output of the function.
    The class prints all of this information into Task4.txt.
    
    The output of the original function is returned as normal by __call__().
    
    getTime() method returns the average execution time.
    
    If the function execution fails, then error message will appended to the Task4_log.txt file.'''

    # initialize the instance with the function call tracker, the function reference, and a list of execution times
    def __init__(self, func):
        self.count = 0
        self.func = func
        self.exec_time_list = []

    def __call__(self, *args, **kwargs):
        # put timestap into the file for better readability
        with open("Task4.txt", "a") as f:
            with contextlib.redirect_stdout(f):
                print(datetime.datetime.now())

        # calculate execution time
        timeVar = time.time()
        # try to call the function
        try:
            # redirect possible output from stdout
            with contextlib.redirect_stdout(io.StringIO()) as func_print:
                output = self.func(*args, **kwargs)
            
            timeVar = time.time() - timeVar

            # retrive the prints
            func_print = func_print.getvalue()
        # if it fails write to log file
        except Exception as err:
            with open("Task4_log.txt", "a") as f:
                with contextlib.redirect_stdout(f):
                    print(datetime.datetime.now())
                    print(err, end="\n\n")
            # set timeVar to None, so the fail time won't get saved
            timeVar = None
            output = None
            func_print = None

        # save the execution time
        if timeVar != None:
            self.exec_time_list.append(timeVar)

        # manage function call trace
        self.count += 1

        # collect information about the relevant function members
        members = dict(inspect.getmembers(self.func))
        signature = inspect.signature(self.func, follow_wrapped=True)
        # separate the docstring into line for a goodloking output; also remove leading spaces
        doc_lines = members['__doc__'].split("\n")
        doc_lines = [line.lstrip(" ") for line in doc_lines]
        # remove the leading spaces from the function source code for readability
        source_code = inspect.getsourcelines(self.func)[0]

        # open Task3.txt in append mode and redirect the stdout out to the file
        with open("Task4.txt", "a") as f:
            with contextlib.redirect_stdout(f):
                # print the tracked information
                print(f"Function {self.func.__name__} was called {self.count} times.")
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
                print(f"\nReturn:\t{output}\n")
                print(f"Prints:")
                print(f"{func_print}\n")

        return output

    def getTime(self):
        return sum(self.exec_time_list) / len(self.exec_time_list)