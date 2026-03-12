import logging

BYTES_PER_KB = 1024

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(message)s')
