try:
    from waycheck import Waycheck
    from waycheck import WaycheckTypeError, WaycheckIndexError
except ImportError:
    from waycheck.main import Waycheck
    from waycheck.errors import WaycheckTypeError, WaycheckIndexError


# Defining the type for each argument
@Waycheck(a=int, b=int)
def main(a, b):
    print('Total: ', a + b)


# Defining the default type for ALL arguments
@Waycheck(default_type=int)
def main2(a, b):
    print('Total: ', a + b)


# Defining the type for each argument
@Waycheck(a=int, b=list)
def main3(a, b):
    b.append(a)
    print('List: ', b)


# Defining the type for each argument
@Waycheck(a=str, b=bool)
def main4(a, b):
    if b:
        print(a)


# Defining the type for each argument using Wildcard
@Waycheck(a='*', b=bool)
def main5(a, b):
    if b:
        return a
    else:
        return 'Passed type check!'


# Defining the type for each argument using tuple of Types
@Waycheck(a=(str, int))
def main6(a):
    print('Argument a is: ', a, ' - type: ', type(a))


# This will throw an error because you're only
# type checking one argument. You must type check
# all of them
@Waycheck(a=int)
def main7(a, b):
    print('Total: ', a + b)


if __name__ == '__main__':
    # Test by commenting/uncommenting function calls below
    try:
        main(5, 10)  # pass
        main('5', 10)  # fail

        main2(5, 10)  # pass
        main2('5', 10)  # fail

        main3(4, [1, 2, 3])  # pass
        main3(4, '[1, 2, 3]')  # fail

        main4('Passed type check!', True)  # pass
        main4('Passed type check!', 'False')  # fail

        # '*' wildcard
        result = main5('Passed type check!', True)  # pass
        print('Result 1: ', result)
        result = main5('Passed type check!', False)  # pass
        print('Result 2: ', result)
        result = main5('Passed type check!', 'True')  # fail
        print('Result 3: ', result)

        main6('Waycheck is so useful!')  # pass
        main6(1234567)  # pass
        main6(5.27)  # fail

        main7(5, 10)  # fail
    except WaycheckTypeError as error:
        print(error)
    except WaycheckIndexError as error:
        print(error)
