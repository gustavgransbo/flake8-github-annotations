from typing import Optional

from flake8.formatting.base import BaseFormatter
from flake8.violation import Violation


class GithubAnnotationsFormatter(BaseFormatter):
    def format(self, error: Violation) -> Optional[str]:
        return (
            f"::error file={error.filename},line={error.line_number},"
            f"col={error.column_number},title={error.code}::{error.text}"
        )
