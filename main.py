import os
from typing import List


def get_child_files(
    root: str, match_name: str = None, max_depth: str = None
) -> List[str]:
    return [
        os.path.join(rel_root, file_name)
        for rel_root, files in walk_child_files(root, max_depth)
        for file_name in files
        if match_name is None or file_name == match_name
    ]


def walk_child_files(root: str, max_depth: str = None):
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
