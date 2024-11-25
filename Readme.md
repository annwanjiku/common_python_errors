# Common Python Errors

## 1. ZeroDivisionError
Occurs when a number is divided by zero.

**Example**:
```python
x = 10
y = 0
result = x / y  # ZeroDivisionError: division by zero
```

## 2. IndexError
Occurs when trying to access an index that is out of range in a list or similar data structure.

### Example:
```python
my_list = [1, 2, 3]
element = my_list[5]  # IndexError: list index out of range
```

## 3. KeyError
Occurs when trying to access a dictionary key that does not exist.

### Example:
```python
my_dict = {"name": "Alice", "age": 25}
value = my_dict["height"]  # KeyError: 'height'
```

## 4. TypeError
Occurs when an operation or function is applied to an object of inappropriate type.

### Example:
```python
x = "5"
y = 10
result = x + y  # TypeError: can only concatenate str (not "int") to str
```

## 5. ValueError
Occurs when a function receives an argument of the correct type but an invalid value.

### Example:
```python
x = "abc"
number = int(x)  # ValueError: invalid literal for int() with base 10: 'abc'
```
## 6. AttributeError
Occurs when attempting to access an attribute that does not exist for an object.

### Example:
```python
x = 10
x.append(5)  # AttributeError: 'int' object has no attribute 'append'
```

## 7. ImportError (or ModuleNotFoundError)
Occurs when an import statement fails because the module cannot be found.

### Example:
```python
import nonexistent_module  # ModuleNotFoundError: No module named 'nonexistent_module'
```

## 8. NameError
Occurs when a variable or function name is not defined.

### Example:
```python
print(unknown_variable)  # NameError: name 'unknown_variable' is not defined
```

## 9. IndentationError
Occurs when there is an incorrect indentation in the code.

### Example:

```python
def my_function():
print("Hello")  # IndentationError: expected an indented block
```

## 10. FileNotFoundError
Occurs when attempting to open a file that does not exist.

### Example:

```python
with open("nonexistent_file.txt", "r") as f:
    content = f.read()  # FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```
# Take-home
These errors are common in Python, and understanding them helps debug effectively. Use try-except blocks to handle exceptions gracefully and avoid program crashes.



