import curses
import random
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(
        "Welcome to the digit span test. Press 1 for forward digit span, press 2 for reverse digit span"
    )


if __name__ == "__main__":
    wrapper(main)
