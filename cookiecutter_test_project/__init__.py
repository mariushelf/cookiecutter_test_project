import cookiecutter_test_project

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore

__version__ = version("cookiecutter_test_project")
