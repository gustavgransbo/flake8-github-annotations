import sys

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def test_entrypoint_registered():
    discovered_plugins = entry_points(group="flake8.report")
    matching_plugins = [
        plugin for plugin in discovered_plugins if plugin.name == "github-annotations"
    ]
    assert len(matching_plugins) == 1
