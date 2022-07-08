"""Tests for flake8_trio_anthropic"""
#!/usr/bin/env python3
import ast

from flake8_trio_anthropic import Plugin


def _results(code: str) -> set[str]:
    tree = ast.parse(code)
    plugin = Plugin(tree)
    return {f"{line-1}:{col} {msg}" for line, col, msg, _ in plugin.run()}


ERROR_MSG = "TRIO001: trio.move_on_after with no await"


def test_trivial_case():
    assert _results("") == set()


def test_simple_missing_await():
    code = "import trio\nwith trio.move_on_after(10):\n  pass"
    assert _results(code) == {f"1:0 {ERROR_MSG}"}


def test_simple_has_await():
    code = "import trio\nwith trio.move_on_after(10):\n  await trio.sleep(1)"
    assert _results(code) == set()


def test_simple_has_await2():
    code = (
        "import trio\n"
        "with trio.move_on_after(10):\n"
        "  pass\n"
        "  await trio.sleep(1)\n"
        "  print('hello')"
    )
    assert _results(code) == set()

def test_has_await_in_loop():
    code = (
        "import trio\n"
        "with trio.move_on_after(10):\n"
        "  pass\n"
        "  while True:\n"
        "    await trio.sleep(1)\n"
        "  print('hello')"
    )
    assert _results(code) == set()
