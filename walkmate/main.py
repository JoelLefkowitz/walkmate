import os
from typing import List, Generator, Tuple, Optional

FileGenerator = Generator[Tuple[str, List[str]], None, None]


def get_child_files(
    root: str, max_depth: Optional[int] = None, match_name: str = None
) -> Generator[str, None, None]:
    """
    Recursivly walks the file tree and optionally matches a filename

    Args:
        root (str): Root directory
        max_depth (Optional[int], optional): Maximum depth. Defaults to None.
        match_name (str, optional): Filename to match. Defaults to None.

    Returns:
        Generator[str, None, None]: Filename generator expression
    """


    return (
        os.path.join(rel_root, file_name)
        for rel_root, files in walk_child_files(root, max_depth)
        for file_name in files
        if match_name is None or file_name == match_name
    )


def walk_child_files(root: str, max_depth: Optional[int] = None) -> FileGenerator:
    """
    Recursivly walks the file tree up to the max depth

    Args:
        root (str): Root directory
        max_depth (Optional[int], optional): Maximum depth. Defaults to None.

    Yields:
        Iterator[FileGenerator]: Tuple of the relative root and files at the current depth
    """  
    for rel_root, dirs, files in os.walk(root, topdown=True):

        if max_depth:
            dirs.clear()
            dirs_paths = [
                os.path.relpath(f.path, root)
                for f in os.scandir(rel_root)
                if f.is_dir()
            ]
            dirs.extend(
                [
                    os.path.basename(f)
                    for f in dirs_paths
                    if len(f.split(os.sep)) <= max_depth
                ]
            )

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")

        yield rel_root, files
