"""
Used for the test suite run.
"""
from copy import deepcopy

from .base import *  # noqa
from .base import DATABASES

DEBUG = False

DATABASES = deepcopy(DATABASES)
del DATABASES["default"]["NAME"]
