# Walkmate

Traverse the file tree.

## Installation

```bash
pip install walkmate
```

## Usage

Given a multi-level directory structure:

```ascii
├── one.py
├── two.py
├── child/
│   ├── three.py
```

We can list the files tree:

```python
>>> list(tree("test/fixtures"))
["one.py", "two.py", "child/three.py"]

>>> list(tree("test/fixtures", depth=1))
["one.py", "two.py"]

>>> list(tree("test/fixtures", regex=r"two\.py$"))
["two.py"]
```
