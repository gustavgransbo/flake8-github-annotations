# flake8-github-annotations

[![PyPI - Version](https://img.shields.io/pypi/v/flake8-github-annotations.svg)](https://pypi.org/project/flake8-github-annotations)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-github-annotations.svg)](https://pypi.org/project/flake8-github-annotations)

-----
A formatter plugin for flake8 that turns flake8 errors into Github Anotations.

![Example Annotations](/assets/example_annotation.png)

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Alternative project](#alternative-project)
- [License](#license)

## Installation

```console
pip install flake8-github-annotations
```

## Usage
To enable the formatter,
and turn flake8 output into Github Annotations,
provide the `--format` argument when invoking `flake8`.
```console
flake8 --format github-annotations
```

This turns flake8 output into lines like this:
```console
::error file=./src/flake8_github_annotations/file_with_error.py,line=1,col=1,title=F401::'collections' imported but unused
```

This is not useful when running flake8 locally,
but will be turned into Github Annotations if ran in a GitHub Action.

You could add a Github Action like this `.github/workflows/ci.yml`:

```yaml
name: Lint

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install flake8 flake8-github-annotations
      - name: Lint with flake8
        run: flake8 --format github-annotations
```

## Alternative project
Using this project to format flake8 output makes the output hard to read for a human,
and you will probably need to call flake8 without the `--format` argument when linting
locally.

If you don't wish to add an extra argument to flake8 when running in CI,
you can use the GithubAction
[rbialon/flake8-annotations](https://github.com/rbialon/flake8-annotations),
which uses regex to detect flake8 output.
A drawback of this apporach is that the project currently (2023-03-29),
only supports a predefined set of error code prefixes,
and might not detect errors from your favourite flake8 plugin.

## License

`flake8-github-annotations` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
