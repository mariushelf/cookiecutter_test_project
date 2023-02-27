import re

import cookiecutter_test_project

# TODO: implement your tests here!


def test_reminder():
    """Reminder to write tests."""
    assert (
        True
    ), "If this test runs it probably means that you have not written your own tests yet 😱 Do it now!"


def test_version_is_semver_string():
    """Test that the version in pyproject.toml is a proper semantic version."""
    semver_pattern = r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    version = cookiecutter_test_project.__version__
    print(f"Version is {version}")
    assert re.match(semver_pattern, version)
