class Prototype:

    value = 'default'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]
