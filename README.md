# Walkmate

Traverse the file tree.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/walkmate/review.yml)
![Version](https://img.shields.io/pypi/v/walkmate)
![Downloads](https://img.shields.io/pypi/dw/walkmate)
![Quality](https://img.shields.io/codacy/grade/ea0bf72352d142519296cfcd0ce026ce)
![Coverage](https://img.shields.io/codacy/coverage/ea0bf72352d142519296cfcd0ce026ce)

## Installing

```bash
pip install walkmate
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/walkmate).

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

Add exclude patterns too:

```python
>>> tree("test/fixtures", r"\.py$", [r"one\.py$"])
["two.py", "child/three.py"]
```

Specify the maximum depth:

```python
>>> tree("test/fixtures", depth=1)
["one.py", "two.py"]
```

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
