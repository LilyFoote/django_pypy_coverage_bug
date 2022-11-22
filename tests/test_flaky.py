import json

from django.utils.functional import SimpleLazyObject


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return repr(obj)


def test_flaky():
    class Foo:
        foo = "bar"

        def __eq__(self, other):
            return self.foo == other.foo

    def lazy():
        return Foo()

    data = SimpleLazyObject(lazy)
    dumped = json.dumps(data, cls=CustomJSONEncoder)
    assert "tests.test_flaky.test_flaky.<locals>.Foo object" in dumped
