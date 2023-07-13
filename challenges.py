from queue import Queue, LifoQueue as Stack
from typing import Literal

Square = Literal[" ", "X"]


def calculate_minimum_knight_hops_using_bfs(
    start: tuple[int, int], end: tuple[int, int]
) -> int:
    raise ValueError("End not reachable from start")


def check_end_reachable_from_start_in_maze_using_dfs(
    maze: list[list[Square]], start: tuple[int, int], end: tuple[int, int]
) -> bool:
    return False


def find_length_of_shortest_path_in_maze_using_bfs(
    maze: list[list[Square]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    raise ValueError("End not reachable from start")


def find_length_of_longest_downhill_path_using_bfs(
    altitudes: list[list[int]], start: tuple[int, int]
) -> int:
    return 0


def flood_fill_using_bfs(
    pixels: list[list[str]], start: tuple[int, int], replacement_value: str
) -> None:
    pass


def flood_fill_using_dfs(
    pixels: list[list[str]], start: tuple[int, int], replacement_value: str
) -> None:
    pass


def count_number_of_islands_using_bfs(landscape: list[list[Square]]) -> int:
    pass


def count_number_of_islands_using_dfs(landscape: list[list[Square]]) -> int:
    pass


class FileTreeNode:
    """
    A node in a file tree. You should not edit this class.
    """

    def __init__(self, name: str):
        self.name = name


class DirectoryNode(FileTreeNode):
    """
    A directory node in a file tree. You should not edit this class.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.contents = []

    def add_child(self, child_item: FileTreeNode):
        self.contents.append(child_item)


class FileTree:
    """
    A file tree with a root node.
    """

    def __init__(self, root: FileTreeNode):
        self.root = root

    def print_using_dfs(self) -> None:
        """
        You should implement this function.
        """
        pass


if __name__ == "__main__":
    # Try out your functions here
    pass
