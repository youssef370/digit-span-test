import curses
import random
import time
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    key = start_screen(stdscr)
    forward_dgs(stdscr)


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(
        "Welcome to the digit span test. Press 1 for forward digit span, press 2 for reverse digit span\n"
    )
    stdscr.refresh()
    key = stdscr.getkey()

    return key


def forward_dgs(stdscr):
    i: int = 0

    while True:
        number = random.randint(10**i, 10 ** (i + 1))
        user_input = []

        # Display the digits one by one
        for digit in str(number):
            stdscr.clear()
            stdscr.addstr(digit)
            stdscr.refresh()
            time.sleep(2)

        stdscr.clear()
        stdscr.addstr(
            "Write the entire sequence of numbers you just saw and press 'Enter' when done\n"
        )
        stdscr.refresh()

        key = stdscr.getkey()
        user_input.append(key)
        stdscr.addstr(key)
        stdscr.refresh()

        # TODO: fix how user_input is displayed and handle backspace better
        while key not in (chr(13), "\n"):
            key = stdscr.getkey()
            if key in ("KEY_BACKSPACE", "\b", "\xf7"):
                if len(user_input) > 0:
                    user_input.pop()
            elif ord(key) == 27:
                ...
            else:
                user_input.append(key)

            stdscr.clear()
            stdscr.addstr(
                f"Write the entire sequence of numbers you just saw and press 'Enter' when done\n{''.join(user_input)}"
            )
            stdscr.refresh()

        try:
            if int("".join(user_input)) == number:
                i += 1
                stdscr.clear()
                stdscr.addstr("Next level: ")
                stdscr.refresh()
            else:
                raise ValueError
        except:
            stdscr.clear()
            stdscr.addstr(
                f"Number was: {number}\nYour input was: {''.join(user_input)}\nFinal score: {i}"
            )
            stdscr.refresh()
            stdscr.getkey()
            break


# TODO: implement function
def reverse_dgs(stdscr):
    ...


if __name__ == "__main__":
    wrapper(main)
