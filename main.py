import sys
import terminal as ter

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if bool(sys.argv[1]): ter.terminal_run_ui()
