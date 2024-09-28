import logging
import os
import sys

os.makedirs('./log', exist_ok=True)
_error_log_file = os.path.expanduser('./log/error.log')
_critical_log_file = os.path.expanduser('./log/critical.log')
_warning_log_file = os.path.expanduser('./log/warning.log')
_info_log_file = os.path.expanduser('./log/info.log')

formatter = logging.Formatter('[%(asctime)s %(name)s] %(levelname)s: %(message)s')
default_handler = logging.StreamHandler(sys.stdout)
default_handler.setFormatter(formatter)
error_handler = logging.FileHandler(_error_log_file, encoding='utf8')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
critical_handler = logging.FileHandler(_critical_log_file, encoding='utf8')
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)
warning_handler = logging.FileHandler(_warning_log_file, encoding='utf8')
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)
info_handler = logging.FileHandler(_info_log_file, encoding='utf8')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

def new_logger(name, debug=True):
    logger = logging.getLogger(name)
    for h in logger.handlers:
        logger.removeHandler(h)
    if not logger.handlers:
        logger.addHandler(default_handler)
        logger.addHandler(error_handler)
        logger.addHandler(critical_handler)
        logger.addHandler(warning_handler)
        logger.addHandler(info_handler)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    return logger

def set_name(longger,name):
    logger = logging.getLogger(name)
