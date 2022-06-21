import sys
import terminal as ter
import logger as log



if __name__ == '__main__':
    log=log.get_logger()
    if len(sys.argv) > 1:
        if bool(sys.argv[1]):
            ter.terminal_run_ui()
            log.debug("TUI started")
    else:
        log.debug("TUI not started")

