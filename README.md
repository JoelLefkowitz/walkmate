# walkmate

Recursively walk and find files.

## Status

| Source     | Shields                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield]  ![lines][lines_shield] ![languages][languages_shield]                    |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![travis][travis_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]     |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                        |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]              |

## Installing

```bash
pip install walkmate
```

## Usage

## Tests

To run unit tests and generate a coverage report:

```bash
grunt tests:unit
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before committing new code:

```bash
grunt precommit
```

This will run linters, formatters, tests, generate a test coverage report and the sphinx configuration.

## Continuous integration

This repository uses Travis CI to build and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->
[semver]: http://semver.org/

<!-- External links -->
[readthedocs]: https://walkmate.readthedocs.io/en/latest/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->
[author]: https://github.com/joellefkowitz

<!-- Project shields -->
[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/walkmate
[license_shield]: https://img.shields.io/github/license/joellefkowitz/walkmate
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/walkmate
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/walkmate

<!-- Health shields -->
[codacy_shield]: https://img.shields.io/codacy/grade/ea0bf72352d142519296cfcd0ce026ce
[readthedocs_shield]: https://img.shields.io/readthedocs/walkmate
[travis_shield]: https://img.shields.io/travis/com/joellefkowitz/walkmate
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/ea0bf72352d142519296cfcd0ce026ce

<!-- Repository shields -->
[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/walkmate
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/walkmate
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/walkmate
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/walkmate

<!-- Publishers shields -->
[pypi_shield]: https://img.shields.io/pypi/v/walkmate
[python_versions_shield]: https://img.shields.io/pypi/pyversions/walkmate
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/walkmate

<!-- Activity shields -->
[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/walkmate
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/walkmate
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/walkmate
