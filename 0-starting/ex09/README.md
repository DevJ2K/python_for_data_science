# ft_package

A simple Python package that provides a function to count occurrences of an element in a list.

## Building the package
To build the package, run the following command in the root directory of the project:

```bash
python setup.py sdist bdist_wheel
```

⚠️ Make sure you have `setuptools` installed. You can install this using pip:

```bash
pip install setuptools
```

## Installing the package
To install the package, you can use pip with the following command:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Using the package
To use the package, you can import it in your Python code as follows:

```python
from ft_package import count_in_list

result = count_in_list([1, 2, 3, 1, 2, 1], 1)
print(result)  # Output: 3
```

## Uninstalling the package
To uninstall the package, you can use pip with the following command:

```bash
pip uninstall ft_package
```
