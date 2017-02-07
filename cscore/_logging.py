
import logging

from ._cscore import setLogger as _setLogger

def enableLogging(level=logging.DEBUG):
    logger = logging.getLogger('cscore')
    _setLogger(lambda lvl, file, line, msg: logger.log(lvl, '%s:%s %s', file, line, msg), level)
    