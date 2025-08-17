### --- Simple threading --- ###
import itertools
import time
from threading import Event, Thread

from concurrency.cpu_bound_operation import run


def spin(msg: str, event: Event):
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)

        if event.wait(timeout=.25):
            break


def slow() -> int:
    time.sleep(5)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=("think...", done))

    print(f"spinner object: {spinner}")
    spinner.start()

    result = run()  # slow
    done.set()
    spinner.join()

    return result


def main():
    result = supervisor()
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
