# Walkmate

Traverse the file tree.

## Installation

```bash
pip install walkmate
```

## Usage

Given a multi-level directory structure:

```ascii
.
├── one.py
├── two.py
└── child
    └── three.py
```

We can list all the files tree:

```python
>>> tree("test/fixtures")
["one.py", "two.py", "child/three.py"]
```

Filter with a regex:

```python
>>> tree("test/fixtures", r"one\.py$")
["one.py"]
```

Add exlude patterns too:

```python
>>> tree("test/fixtures", r"\.py$", [r"one\.py$"])
["two.py", "child/three.py"]
```

Specify the maximum depth:

```python
>>> tree("test/fixtures", depth=1)
["one.py", "two.py"]
```
