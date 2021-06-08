from madlib_cli.madlib_cli import read_template

def test_read_template():
    actual = read_template("./assets/oneline.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

from madlib_cli.madlib_cli import parse_template
def test_parse():
    actual_parts = parse_template(read_template("./assets/oneline.txt"),isTrue=False)
    expected_parts = ["Adjective", "Adjective", "Noun"]
    assert actual_parts == expected_parts