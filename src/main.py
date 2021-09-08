import random, sys
from task1 import Task1
from task2 import Task2
from task3 import Task3
from task4 import Task4_class

# Test function 1
# some 'easy' random math
test1 = lambda a, b: a**random.randint(1, 100) / b**random.randint(1, 100)
# making the lambda function look like regular function
test1.__name__ = "test1"
test1.__doc__ = "A simple funtion that raises the passed in arguments to a random power between 1 and 100 (inclusive), \
divides the first number by the second, and then returns the output.\n\
Both a and b can be integers or floats."

# Test function 2
# output a list containing elements from listA which are not in listB
test2 = lambda listA, listB: [a for a in listA if not a in listB]
# making the lambda function look like regular function
test2.__name__ = "test2"
test2.__doc__ = "This function outputs a list containing elements from the listA, which are not included in the listB.\n\
Both listA and listB can be any iteratable object."

# Test function 3
# quadratic equation solver of the form: ax^2 + bx + c = 0
def test3(a:float, b:float, c:float) -> tuple:
    '''This function returns a solution to a given quadratic equation.
    The solution is returned in a form of tuple.
    a must be larger than zero.

    If the discriminant is equals to zero, the tuple will contain two identical numbers.'''

    discriminant = b*b - 4*a*c
    return ((-b + discriminant**(1/2)) / (2 * a), (-b - discriminant**(1/2)) / (2 * a))

# Test function 4
# prints a Pascal triangle of the given depth
def test4(n:int) -> None:
    '''This function prints a Pascal triangle of depth n to the stdout.
    If n is less than 1 this function doesn't print anything.'''

    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]

if __name__ == "__main__":
    # check for command line arguments; redirect the stdout to the second argument
    if len(sys.argv) > 1:
        sys.stdout = open(f"{sys.argv[1]}", "w")
    # testing the decorator from the Task 1
    # decorate test functions
    Task1_test1 = Task1(test1)
    Task1_test2 = Task1(test2)
    Task1_test3 = Task1(test3)
    Task1_test4 = Task1(test4)

    # run the decorated functions
    print("---   Testing Task 1:   ---\n")
    for i in [1, 2, 3]:
        print(f"Test run number {i}:")
        Task1_test1(10 * i, 11 * i)
        print("")
        Task1_test2([i, i + 1, 'a'], [i, i + 1, i +2])
        print("")
        Task1_test3(i, i + 1, -i)
        print("")
        Task1_test4(5 + i)
        print("")

    # testing the decorator from the Task 2
    # decorate test functions
    Task2_test1 = Task2(test1)
    Task2_test2 = Task2(test2)
    Task2_test3 = Task2(test3)
    Task2_test4 = Task2(test4)

    # run the decorated functions
    print("---   Testing Task 2:   ---\n")
    for i in [1, 2, 3]:
        print(f"Test run number {i}:")
        Task2_test1(10 * i, 11 * i)
        print("")
        Task2_test2([i, i + 1, 'a'], [i, i + 1, i +2])
        print("")
        Task2_test3(i, i + 1, -i)
        print("")
        Task2_test4(5 + i)
        print("")

    # testing the class decorator from the Task 3
    # decorate test functions
    Task3_test1 = Task3(test1)
    Task3_test2 = Task3(test2)
    Task3_test3 = Task3(test3)
    Task3_test4 = Task3(test4)

    # run the decorated functions
    # note: the decorator outputs everything to a file Task3.txt
    print("---   Testing Task 3:   ---\n")
    for i in [1, 2, 3]:
        print(f"Test run number {i}:")
        Task3_test1(10 * i, 11 * i)
        Task3_test2([i, i + 1, 'a'], [i, i + 1, i +2])
        Task3_test3(i, i + 1, -i)
        Task3_test4(5 + i)
        print("")

    # rank the functions in the order of increasing acerage execution time
    # first, collect the average execution times from the respective classes
    exec_time_list = []
    avg_time = 0
    for i in range(1, 5):
        exec(f"avg_time = Task3_test{i}.getTime()")
        # tuple(name, executionTime)
        exec_time_list.append((f"test{i}", avg_time))

    # sort the list to form the rank
    exec_time_list.sort(key = lambda pair : pair[1])

    # print the ranking table
    print("PROGRAM | RANK | TIME ELAPSED")
    for pair, rank in zip(exec_time_list, range(1,5)):
        print(f"{pair[0]}\t    {rank}\t {pair[1]}\ts")
    print("")

    # testing the class decorator from the Task 4
    # decorate test functions
    Task4_test1 = Task4_class(test1)
    Task4_test2 = Task4_class(test2)
    Task4_test3 = Task4_class(test3)
    Task4_test4 = Task4_class(test4)

    # run the decorated functions
    # note: the decorator outputs everything to a file Task3.txt
    print("---   Testing Task 4:   ---\n")
    for i in [1, 2, 3]:
        print(f"Test run number {i}:")
        Task4_test1(10 * i, 11 * i)
        Task4_test2([i, i + 1, 'a'], [i, i + 1, i +2])
        Task4_test3(i, i + 1, -i)
        Task4_test4(5 + i)
        print("")

    # rank the functions in the order of increasing acerage execution time
    # first, collect the average execution times from the respective classes
    exec_time_list = []
    avg_time = 0
    for i in range(1, 5):
        exec(f"avg_time = Task4_test{i}.getTime()")
        # tuple(name, executionTime)
        exec_time_list.append((f"test{i}", avg_time))

    # sort the list to form the rank
    exec_time_list.sort(key = lambda pair : pair[1])

    # print the ranking table
    print("PROGRAM | RANK | TIME ELAPSED")
    for pair, rank in zip(exec_time_list, range(1,5)):
        print(f"{pair[0]}\t    {rank}\t {pair[1]}\ts")
    print("")

    # test wrong input
    print(f"Testing wrong input:")
    Task4_test1("a", 3.14)
    Task4_test2("Hello world!")
    Task4_test3(0, 0, 0)
    Task4_test4(a = 5)
    print("The errors should be: (check the Task4_log.txt)")
    print("1) unsupported operand type(s) for ** or pow(): 'str' and 'int'")
    print("2) <lambda>() missing 1 required positional argument: 'listB'")
    print("3) float division by zero")
    print("4) test4() got an unexpected keyword argument 'a'")

    # if the stdout was redirected, close it
    if len(sys.argv) > 1:
        sys.stdout.close()