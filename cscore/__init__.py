
from ._cscore import *
from ._logging import enableLogging

try:
    from .version import __version__
except ImportError:
    __version__ = 'master'
