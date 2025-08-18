"""
EAFP (Easier to Ask for Forgiveness than Permission,
«Проще просить прощения, чем разрешения») - сначала делаем действие, а потом
обрабатываем ошибку, если что-то пошло не так.
"""

my_dict = {"some_key": "some_value"}

try:
    value = my_dict["key"]
except KeyError:
    value = None
