"""ramalama client module."""

from ramalama.common import perror
from ramalama.cli import init_cli
import sys

assert sys.version_info >= (3, 6), "Python 3.6 or greater is required."

__all__ = ['perror', 'init_cli']
