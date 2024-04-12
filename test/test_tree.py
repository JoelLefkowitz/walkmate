from src.tree import step, tree

# Fixtures folder structure:
#
# test
# └── fixtures
#     ├── one.py
#     ├── two.py
#     └── child
#         └── three.py


def test_step():
    steps = list(step("test/fixtures"))
    assert len(steps) == 2
    assert steps[0] == ("test/fixtures", ["one.py", "two.py"])
    assert steps[1] == ("test/fixtures/child", ["three.py"])

    steps = list(step("test/fixtures", depth=0))
    assert len(steps) == 0

    steps = list(step("test/fixtures", depth=1))
    assert len(steps) == 1
    assert steps[0] == ("test/fixtures", ["one.py", "two.py"])


def test_tree():
    assert tree("test/fixtures") == [
        "test/fixtures/one.py",
        "test/fixtures/two.py",
        "test/fixtures/child/three.py",
    ]

    assert tree("test/fixtures", r"one\.py$") == [
        "test/fixtures/one.py",
    ]

    assert tree("test/fixtures", r"\.py$", [r"one\.py$"]) == [
        "test/fixtures/two.py",
        "test/fixtures/child/three.py",
    ]

    assert tree("test/fixtures", depth=1) == [
        "test/fixtures/one.py",
        "test/fixtures/two.py",
    ]
