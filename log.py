#-*- coding: utf-8 -*-
import logging
import sys

__log_console = "console"

logger = logging.getLogger("root")
__formatter = logging.Formatter("[%(levelname)-7s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s", "%d %b %Y %H:%M:%S")

if __log_console == "py":
    __streamHandler = logging.StreamHandler(sys.stdout)
    __streamHandler.setFormatter(__formatter)
    logger.addHandler(__streamHandler)
    
__fileHandler = logging.FileHandler("debug.log")
__fileHandler.setFormatter(__formatter)
logger.addHandler(__fileHandler)

logger.setLevel(logging.DEBUG)
