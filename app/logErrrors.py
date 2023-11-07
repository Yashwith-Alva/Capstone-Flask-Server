'''
This file is used for SQL logging errors.
'''

import logging
from colorama import Fore, Style
from flask import current_app

class CapstoneLogger:
    def __init__(self, verbose=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.verbose = verbose
        ch = logging.StreamHandler()
        ch.setLevel(verbose)
        
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        
    def log(self, message, level=logging.INFO):
        if level == logging.CRITICAL:
            c_message = f"{Fore.MAGENTA}{message}{Style.BRIGHT}"
        elif level == logging.ERROR:
            c_message = f"{Fore.RED}{message}{Style.RESET_ALL}"
        elif level == logging.WARNING:
            c_message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
        elif level == logging.INFO:
            c_message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
        else:
            c_message = message
        
        self.logger.log(level, c_message)

clog = CapstoneLogger(logging.CRITICAL)