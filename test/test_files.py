from src.files import step, tree


def test_step():
    assert list(step("test/fixtures")) == [
        ("test/fixtures", ["one.py", "two.py"]),
        ("test/fixtures/child", ["three.py"]),
    ]


def test_tree():
    assert list(tree("test/fixtures", regex=r"two\.py$")) == ["test/fixtures/two.py"]
