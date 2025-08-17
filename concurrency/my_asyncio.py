### --- Simple asyncio --- ###
import itertools
import asyncio
from asyncio import CancelledError

from concurrency.cpu_bound_operation import run


async def spin(msg: str):
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)

        try:
            await asyncio.sleep(.5)

        except CancelledError:
            break


async def slow() -> int:
    await asyncio.sleep(5)
    return 42


async def supervisor() -> int:
    spinner = asyncio.create_task(spin("think..."))
    print(f"spinner object: {spinner}")

    result = run()
    # result = await slow()
    spinner.cancel()

    return result


def main():
    result = asyncio.run(supervisor())
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
