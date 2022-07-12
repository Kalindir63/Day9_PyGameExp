import pytest

from game.main import App


@pytest.mark.xfail
def test_launch():
    app = App()
    assert app.on_execute() is True


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
