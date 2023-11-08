import logging
from colorama import Fore, Style

class CapstoneLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = CapstoneFormatter('%(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.addHandler(ch)

class CapstoneFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA
    }

    def format(self, record):
        log_message = super(CapstoneFormatter, self).format(record)
        log_level_color = self.COLORS.get(record.levelname, Fore.RESET)
        return f"{log_level_color}{log_message}{Style.RESET_ALL}"
