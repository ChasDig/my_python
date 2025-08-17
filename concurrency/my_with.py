import sys
import contextlib


class LookingGlass:

    def __enter__(self):
        self.original_writer = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "LookingGlass"


    def reverse_write(self, text):
        self.original_writer(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_writer


@contextlib.contextmanager
def looking_glass():
    original_writer = sys.stdout.write

    def reverse_write(text):
        original_writer(text[::-1])

    msg = ""
    sys.stdout.write = reverse_write
    try:
        yield "looking_glass_contextmanager"

    except Exception as ex:
        msg = ex

    finally:
        sys.stdout.write = original_writer
        if msg:
            print(msg)


@looking_glass()
def check_looking_glass():
    print("Test looking_glass_as_decorator")


check_looking_glass()


with LookingGlass() as lg_cls:
    print(lg_cls)
    print("test LookingGlass")


with looking_glass() as lg_cm:
    print(lg_cm)
    print("test looking_glass_contextmanager")
