"""Little helper application to improve django choices (for fields)"""

from configparser import ConfigParser
from importlib.metadata import PackageNotFoundError, version as _get_version
from os import path

from .choices import Choices, OrderedChoices, AutoDisplayChoices, AutoChoices  # noqa: F401


def _extract_version(package_name):
    try:
        # if package is installed
        return _get_version(package_name)
    except PackageNotFoundError:
        # if not installed, so we must be in source, with ``setup.cfg`` available
        parser = ConfigParser()
        parser.read(path.join(path.dirname(__file__), "..", "setup.cfg"))
        return parser["metadata"]["version"]


EXACT_VERSION = str(_extract_version("django_extended_choices"))
VERSION = tuple(int(part) for part in EXACT_VERSION.split(".") if part.isnumeric())
