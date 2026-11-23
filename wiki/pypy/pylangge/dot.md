# Python imports: `from module import name` vs `import package.submodule`

In Python, a dot (`.`) in an `import` path navigates **packages (folders) and modules (`.py` files)**—not functions or classes inside a file.

## `from indent import add`

- `indent` is a module (`indent.py`) or package (`indent/`).
- `add` is an object defined inside `indent` (a function, class, variable, or submodule).

```python
from indent import add

add(2, 3)
```

## `import indent.add` (or `from indent.add import ...`)

- The dot tells Python that `indent` is a **package (folder)** and `add` is a **submodule (`indent/add.py`) or subpackage (`indent/add/`)** inside it.
- This **cannot** be used to import a function from a `.py` file. Since [indent.py](../../../pypy/pylangge/indent.py) is a file containing `def add(a, b):`, `import indent.add` fails with `ModuleNotFoundError` (and Pylance `reportMissingImports`).
- `from indent.add` without a trailing `import ...` is also a `SyntaxError`.

## Quick comparison

| Syntax | `indent` must be | `add` must be | How you call `add` |
| --- | --- | --- | --- |
| `import indent` | Module (`.py`) or package | — | `indent.add(2, 3)` |
| `from indent import add` | Module (`.py`) or package | Function, class, variable, or submodule | `add(2, 3)` |
| `import indent.add` | Package (folder) | Submodule (`add.py`) or subpackage | `indent.add.<symbol>()` |

## Multi-level nesting (OSS example: Django)

In large open-source projects like [Django](https://github.com/django/django/blob/main/django/contrib/auth/__init__.py), packages are nested several folders deep before reaching the `.py` module that defines a class or function:

```text
django/                  # top-level package
└── contrib/             # subpackage
    └── auth/            # subpackage
        └── models.py    # module defining class User
```

* Every dot before `import` walks down a folder/module boundary (`django` → `contrib` → `auth` → `models.py`):

```python
from django.contrib.auth.models import User

# Or importing the module itself:
import django.contrib.auth.models
# Usage: django.contrib.auth.models.User
```

* You **cannot** put the class name (`User`) on the left side of `import` as a dotted module path:

```python
import django.contrib.auth.models.User  # ModuleNotFoundError: 'User' is a class, not a module
```