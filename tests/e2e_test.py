import csv
import sys

import pytest

from banking import __main__


def test_happy_path(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "argv", [])

    assert 0 == __main__.main()


def csv_to_dict_list(file_name: str, field_names: list[str]):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=field_names, skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
        result = [row for row in reader]

    return result
