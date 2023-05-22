from pathlib import Path
from typing import Optional

from flake8.formatting.base import BaseFormatter


class GithubAnnotationsFormatter(BaseFormatter):
    name = "GithubAnnotationsFormatter"

    def format(self, error) -> Optional[str]:
        return (
            f"::error file={self.path_prefix / error.filename},line={error.line_number}"
            f",col={error.column_number},title={error.code}::{error.text}"
        )

    @classmethod
    def add_options(cls, option_manager) -> None:
        option_manager.add_option(
            "--github-annotation-path-prefix",
            default="",
            parse_from_config=True,
            help=(
                "Path prefix to add to prepend to filenames"
                "when using --format github"
            ),
        )

    @classmethod
    def parse_options(cls, option_manager) -> None:
        cls.path_prefix = Path(option_manager.github_annotation_path_prefix)
