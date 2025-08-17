### --- Simple multiprocessing --- ###
import time
import itertools
from multiprocessing import Event, Process, synchronize

from concurrency.cpu_bound_operation import run


def spin(msg: str, event: synchronize.Event):
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
    spinner = Process(target=spin, args=("think...", done))

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
