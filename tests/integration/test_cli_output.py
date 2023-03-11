import subprocess
import sys
import tempfile
from typing import Generator

import pytest


@pytest.fixture
def file_with_error() -> Generator[str, None, None]:
    """Yields a path to a temprary file that contains a F401 error"""
    with tempfile.NamedTemporaryFile("w+") as f:
        f.write("import foo\n")
        f.flush()
        yield f.name


def test_output_is_formated_as_github_error_annotation(file_with_error: str):
    output = subprocess.run(
        [
            sys.executable,  # This makes sure flake8 is ran from the correct venv
            "-m",
            "flake8",
            file_with_error,
            "--format",
            "github-annotations",
        ],
        capture_output=True,
    )
    expected_output = f"::error file={file_with_error},line=1,col=1,title=F401::'foo' imported but unused\n"  # noqa:E501
    assert output.stdout.decode() == expected_output
