from mypy.plugin import Plugin

__version__ = "0.1.1"


class StructuredDataPlugin(Plugin):
    pass


def plugin(version: str):
    # ignore version argument if the plugin works with all mypy versions.
    return StructuredDataPlugin
