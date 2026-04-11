import sys

import pytest

from banking import __main__


def test_happy_path(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", [])

    assert 0 == __main__.main()
