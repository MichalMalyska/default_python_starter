from default_python_starter import greet


def test_greet_includes_name() -> None:
    assert greet("Ada") == "Hello, Ada!"
