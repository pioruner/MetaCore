import sys
from modules import terminal as ter_ui, logger as log_util


if __name__ == '__main__':
    log = log_util.get_logger()
    if len(sys.argv) > 1:
        if bool(sys.argv[1]):
            ter_ui.terminal_run_ui()
            log.info("TUI started")
    else:
        log.info("TUI not started")
