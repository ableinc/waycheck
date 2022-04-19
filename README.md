# Waycheck (Python Type Checker)

A lightweight Python type checker. Designed with the developer in mind. The Waycheck class is a decorator, which means you can use it by prepending '@' above the function you'd like to type check. No library dependencies under the hood - Pure Python ;)!

## Install

```bash
python -m pip --install waycheck
```

## Getting Started

You can refer to the ```demo.py``` file in this repository or the code block below
to see how ```Waycheck``` works.

```python
import waycheck

# Defining the type for each argument
@Waycheck(a=int, b=int)
def main(a, b):
    print('Total: ', a + b)


# Defining the default type for ALL arguments
@Waycheck(default_type=int)
def main2(a, b):
    print('Total: ', a + b)


if __name__ == '__main__':
    main(5, 10)  # this will pass
    main('5', 10)  # this will fail

    main2(5, 10)  # this will pass
    main2('5', 10)  # this will fail
```

## Accepted Types

Waycheck can type check any valid Python Type provided to it, as well as a wildcard type. A wildcard type
is used when an argument can be any value. This is handy when you're doing your own type checking within
your function and would like Waycheck to skip type checking that argument.

You can specify a wildcard by using '*'. See an example below:

```python
@Waycheck(a='*', b=bool)
def main(a, b):
    if b:
        return a
```

You can also pass a tuple of Types, instead of '*' (wildcat). See an example below:

```python
@Waycheck(a=(str, int))
def main(a):
    print('Argument a is: ', a, ' - type: ', type(a))
```

## Exmaples

Refer to ```demo.py``` file.

## FAQ

Q: My type checking is failling/passing, but I know it shouldn't be. Why is this happening?
A: This happens when you don't specify the correct order of appearance for the Waycheck class.
The order in which the arguments are passed to the function, should be the exact same order you
provide to the Waycheck class. By not doing this, unexpected type checking behavior will occur,
such as passing when it should fail or failing when it should pass.

Note: This will occur if the argument all have different expected type values. i.e if all arguments are supposed to be integers, then the order doesn't matter.
Example:

```python
# this works as expected
@Waycheck(a=int, b=int)
def main(a, b):
    ...


# this will fail if all the arguments
# are not the same expected type
@Waycheck(b=int, a=int)
def main(a, b):
    ...
```

Q: Can I pass my own custom error class?
A: No. The default error given is ```WaycheckTypeError```. You could use a blanket Exeception check (try/except) then throw whatever error you want.

Q: I keep getting an IndexError, why?
A: If you're going to type check the function you must provide Waycheck with the expected type for ALL the arguments, not just some of them.

## Changelog

April 2022:

* Initial Release - v0.0.1
