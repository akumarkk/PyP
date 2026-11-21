# Python indentation

Python uses indentation to group statements into blocks. A colon starts a
compound statement, such as a function definition or an `if` statement; the
statements in its body must be indented.

```python
def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    return a * b
```

The first `return` is inside the `if` block. The second is aligned with the
`if`, so it is inside the function but outside the `if`. When execution reaches
it, it returns the product.

## Rules and conventions

- Statements in the same block must have consistent indentation.
- Indent a nested block further than its parent. Dedent to end a block.
- Use four spaces per indentation level, the Python style convention. Python
  permits other consistent indentation widths, but mixing widths makes code
  harder to read.
- Prefer spaces over tabs. Inconsistent use of tabs and spaces can raise
  `TabError` or make the block structure misleading.
- Blank lines and comment-only lines do not change the block structure.

An unindented function body, for example, raises an `IndentationError`:

```python
def greet():
print("Hello")  # Expected an indented block
```

## Repository example

See [indent.py](../pypy/pylangge/indent.py). Its functions use different
indentation widths, but each function's blocks are internally consistent. In
`mul`, the zero case is nested inside the `if`; the final return is outside
that `if`. Running the example prints:

```text
5
3
3 4
12
```

The `3 4` line comes from the `print` inside `mul`, before it returns `12`.
