import os
import re
from typing import Generator, List, Optional, Tuple, Iterator


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
        if depth:
            subdirs.clear()

            paths = [
                os.path.relpath(f.path, root) for f in os.scandir(folder) if f.is_dir()
            ]

            subdirs.extend(
                [os.path.basename(f) for f in paths if len(f.split(os.sep)) <= depth]
            )

        if "__pycache__" in subdirs:
            subdirs.remove("__pycache__")

        yield (folder, files)


def tree(
    root: str, depth: Optional[int] = None, regex: Optional[str] = None
) -> Iterator[str]:
    """
    Traverse the file tree

    Args:
        root (str): The root directory.
        depth (Optional[int], optional): The maximum depth. Defaults to None.
        regex (Optional[str], optional): The regex to match. Defaults to None.

    Returns:
        Iterator[str]: An iterator containing the file paths
    """
    return (
        os.path.join(folder, file)
        for folder, files in step(root, depth)
        for file in files
        if regex is None or re.search(regex, file)
    )
