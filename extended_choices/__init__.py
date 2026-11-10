"""Little helper application to improve django choices (for fields)"""

from __future__ import annotations

from configparser import ConfigParser
from importlib.metadata import PackageNotFoundError, version as _get_version
from os import path
from typing import Tuple

from .choices import (  # noqa: F401
    AutoChoices as AutoChoices,
    AutoDisplayChoices as AutoDisplayChoices,
    Choices as Choices,
    OrderedChoices as OrderedChoices,
)


def _extract_version(package_name: str) -> str:
    try:
        # if package is installed
        return _get_version(package_name)
    except PackageNotFoundError:
        # if not installed, so we must be in source, with ``setup.cfg`` available
        parser = ConfigParser()
        parser.read(path.join(path.dirname(__file__), "..", "setup.cfg"))
        return parser["metadata"]["version"]


EXACT_VERSION: str = str(_extract_version("django_extended_choices"))
VERSION: Tuple[int, ...] = tuple(
    int(part) for part in EXACT_VERSION.split(".") if part.isnumeric()
)
