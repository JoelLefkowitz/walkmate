from walker import get_child_files


def test_get_child_files():
    all_files = list(get_child_files("tests/fixtures/mock", 2))
    assert all_files == [
        "tests/fixtures/mock/one.py",
        "tests/fixtures/mock/two.py",
        "tests/fixtures/mock/child/three.py"
    ]

    matches = list(get_child_files("tests/fixtures/mock", 2, "three.py"))
    assert matches == [
        "tests/fixtures/mock/child/three.py"
    ]
