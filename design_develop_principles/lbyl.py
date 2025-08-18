"""
LBYL (Look Before You Leap, «Сначала посмотри, потом прыгай») - сначала
проверяем условия, и только потом выполняем действие (схоже с
"защитным программированием").
"""

my_dict = {"some_key": "some_value"}

if "key" in my_dict:
    value = my_dict["key"]
else:
    value = None
