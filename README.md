# Python Programming Exercises, Gently Explained

Practice exercises from the book by Al Sweigart.

## Setup

A virtual environment with pytest is already configured. Activate it once per terminal session:

```bash
source .venv/bin/activate
```

## Structure

Each exercise has two files:

| File                   | Purpose                            |
| ---------------------- | ---------------------------------- |
| `ex##_<title>.py`      | Your solution                      |
| `test_ex##_<title>.py` | Tests that verify the requirements |

Example: `ex01_hello_world.py` and `test_ex01_hello_world.py`.

## Writing an exercise

1. Create `ex##_<title>.py` and implement the required function(s).
2. Add `if __name__ == "__main__":` at the bottom to run it directly.
3. Create `test_ex##_<title>.py` and import your function(s) to test them.

**Solution template:**

```python
# Exercise N - Title
# Requirements: <describe what the function must do>

def my_function(arg):
    # your code here
    pass


if __name__ == "__main__":
    print(my_function(...))
```

**Test template:**

```python
from ex##_title import my_function


def test_expected_case():
    assert my_function(...) == expected_value

def test_edge_case():
    assert my_function(...) == expected_value
```

## Running code

```bash
# Run a single exercise
python ex01_hello_world.py

# Run with the venv active
python ex01_hello_world.py
```

## Running tests

```bash
# Run all tests
pytest -v

# Run tests for one exercise
pytest test_ex01_hello_world.py -v

# Stop at first failure
pytest -x -v
```

Tests in VS Code are also available via the **Testing** sidebar (flask icon) — each test can be run or debugged individually.
