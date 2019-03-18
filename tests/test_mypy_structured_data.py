from mypy.plugin import Plugin
from mypy.version import __version__


def test_main(mypy_structured_data):
    assert mypy_structured_data


def test_plugin(mypy_structured_data):
    assert issubclass(mypy_structured_data.plugin(__version__), Plugin)
