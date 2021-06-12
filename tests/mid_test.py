
from madlib_cli.madlib_cli import read_template, parse_template, merge

import pytest

def test_read_template_returns_stripped_string():
    actual = read_template("assets/oneline.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_returns_stripped_string():
    actual = read_template("assets/oneline.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_parts = parse_template(read_template("assets/oneline.txt"),isTrue=False)
    expected_parts = ["Adjective", "Adjective", "Noun"]
    assert actual_parts == expected_parts


def test_merge():
    actual = merge(["dark", "stormy", "night"], parse_template(read_template("assets/oneline.txt"),isTrue=False) , read_template("assets/oneline.txt"))
    expected = "It was a dark and stormy night."
    assert actual == expected









