import os
import re
from math import floor
from typing import Generator, List, Optional, Tuple


def step(
    root: str, depth: Optional[int] = None
) -> Generator[Tuple[str, List[str]], None, None]:
    """
    Step into the file tree

    Args:
        root (str): The root directory.
        depth (Optional[int], optional): The maximum depth. Defaults to None.

    Yields:
        Generator[Tuple[str, List[str]], None, None]: A generator containing
        the folder and child files
    """
    for folder, subdirs, files in os.walk(root, topdown=True):
        if depth == 0:
            continue

        if depth == floor(len(os.path.relpath(root, folder)) / 2) + 1:
            subdirs.clear()

        if "__pycache__" in subdirs:
            subdirs.remove("__pycache__")

        yield (folder, files)


def tree(
    root: str,
    include: Optional[str] = None,
    exclude: Optional[List[str]] = None,
    depth: Optional[int] = None,
) -> List[str]:
    """
    Traverse the file tree

    Args:
        root (str): The root directory.
        include (Optional[str], optional): A regex to include. Defaults to None.
        exclude (Optional[List[str]], optional): Regexes to exclude. Defaults to None.
        depth (Optional[int], optional): The maximum depth. Defaults to None.

    Returns:
        Iterator[str]: An iterator containing the file paths
    """
    if exclude is None:
        exclude = []

    return [
        os.path.join(folder, file)
        for folder, files in step(root, depth)
        for file in files
        if (include is None or re.search(include, file))
        and not any(re.search(regex, file) for regex in exclude)
    ]
