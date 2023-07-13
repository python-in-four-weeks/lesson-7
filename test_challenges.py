import pytest
from pytest_mock import MockerFixture
from io import StringIO

import challenges


@pytest.mark.parametrize(
    "start, end, expected_minimum_hops",
    [
        ((4, 4), (4, 4), 0),
        ((7, 6), (4, 3), 2),
        ((6, 4), (6, 5), 3),
    ],
)
def test_calculate_minimum_knight_hops_using_bfs(
    start: tuple[int, int], end: tuple[int, int], expected_minimum_hops: int
) -> None:
    minimum_hops = challenges.calculate_minimum_knight_hops_using_bfs(start, end)
    assert (
        minimum_hops == expected_minimum_hops
    ), f"The path from {start} to {end} should have taken {expected_minimum_hops} hops"


@pytest.mark.parametrize(
    "maze, start, end, expected_reachability_result",
    [
        (
            [
                [" ", "X", "X", "X", "X", " ", " "],
                [" ", " ", " ", " ", "X", " ", " "],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", " ", "X", " ", "X"],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", "X", "X", "X", "X"],
            ],
            (0, 0),
            (0, 6),
            True,
        ),
        (
            [
                [" ", "X", "X", "X", "X", " ", " "],
                [" ", " ", " ", "X", "X", " ", " "],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", " ", "X", " ", "X"],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", "X", "X", "X", "X"],
            ],
            (0, 0),
            (0, 6),
            False,
        ),
    ],
)
def test_check_end_reachable_from_start_in_maze_using_dfs(
    maze: list[list[challenges.Square]],
    start: tuple[int, int],
    end: tuple[int, int],
    expected_reachability_result: bool,
) -> None:
    reachability_result = challenges.check_end_reachable_from_start_in_maze_using_dfs(
        maze, start, end
    )
    assert (
        reachability_result == expected_reachability_result
    ), f"Expected end to {'be' if expected_reachability_result else 'not be'} reachable from start"


@pytest.mark.parametrize(
    "maze, start, end, expected_shortest_path_length",
    [
        (
            [
                [" ", "X", "X", "X", "X", " ", " "],
                [" ", " ", " ", " ", "X", " ", " "],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", " ", "X", " ", "X"],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", "X", "X", "X", "X"],
            ],
            (0, 0),
            (0, 6),
            10,
        ),
        (
            [
                ["X", "X", "X", "X", "X", "X", "X"],
                ["X", " ", " ", "X", " ", " ", "X"],
                ["X", " ", "X", "X", " ", " ", "X"],
                ["X", " ", " ", "X", "X", " ", "X"],
                ["X", "X", " ", " ", " ", " ", "X"],
                ["X", "X", "X", "X", "X", "X", "X"],
            ],
            (1, 2),
            (2, 4),
            11,
        ),
    ],
)
def test_find_length_of_shortest_path_in_maze_using_bfs(
    maze: list[list[challenges.Square]],
    start: tuple[int, int],
    end: tuple[int, int],
    expected_shortest_path_length: int,
) -> None:
    shortest_path_length = challenges.find_length_of_shortest_path_in_maze_using_bfs(
        maze, start, end
    )
    assert (
        shortest_path_length == expected_shortest_path_length
    ), f"Shortest path through maze should have been {expected_shortest_path_length} steps long"


@pytest.mark.parametrize(
    "maze, start, end, expected_exception_message",
    [
        (
            [
                [" ", "X", "X", "X", "X", " ", " "],
                [" ", " ", " ", "X", "X", " ", " "],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", " ", "X", " ", "X"],
                ["X", "X", "X", " ", " ", " ", "X"],
                ["X", "X", "X", "X", "X", "X", "X"],
            ],
            (0, 0),
            (0, 6),
            "End not reachable from start",
        ),
    ],
)
def test_find_length_of_shortest_path_in_maze_using_bfs_with_no_valid_path(
    maze: list[list[challenges.Square]],
    start: tuple[int, int],
    end: tuple[int, int],
    expected_exception_message: str,
) -> None:
    with pytest.raises(ValueError) as error:
        challenges.find_length_of_shortest_path_in_maze_using_bfs(maze, start, end)
    assert (
        str(error.value) == expected_exception_message
    ), f"Function should have raised ValueError with text {expected_exception_message}"


@pytest.mark.parametrize(
    "altitudes, start, expected_longest_path_length",
    [
        (
            [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 8, 8, 8, 8, 9, 9, 9, 9],
                [9, 9, 6, 5, 7, 8, 8, 9, 9, 9],
                [9, 8, 7, 9, 7, 8, 9, 9, 9, 9],
                [9, 9, 8, 7, 8, 9, 9, 9, 9, 9],
                [9, 9, 9, 8, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            ],
            (3, 1),
            4,
        ),
        (
            [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 8, 9, 9, 9, 9, 9],
                [9, 9, 9, 6, 7, 9, 9, 9, 9, 9],
                [9, 9, 9, 5, 4, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            ],
            (3, 3),
            5,
        ),
    ],
)
def test_find_length_of_longest_downhill_path_using_bfs(
    altitudes: list[list[int]],
    start: tuple[int, int],
    expected_longest_path_length: int,
) -> None:
    longest_path_length = challenges.find_length_of_longest_downhill_path_using_bfs(
        altitudes, start
    )
    assert (
        longest_path_length == expected_longest_path_length
    ), f"Expected longest downhill path to be {expected_longest_path_length} steps long"


@pytest.mark.parametrize(
    "pixels, start, replacement_value, expected_filled_pixels",
    [
        (
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "B", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
            (3, 4),
            "R",
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "R", "R", "W", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "W", "R", "R", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "B", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
        ),
        (
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
            (3, 4),
            "B",
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
        ),
    ],
)
def test_flood_fill_using_bfs(
    pixels: list[list[str]],
    start: tuple[int, int],
    replacement_value: str,
    expected_filled_pixels: list[list[str]],
) -> None:
    challenges.flood_fill_using_bfs(pixels, start, replacement_value)
    assert (
        pixels == expected_filled_pixels
    ), "Expected filled pixels don't match actual filled pixels"


@pytest.mark.parametrize(
    "pixels, start, replacement_value, expected_filled_pixels",
    [
        (
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "B", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
            (3, 4),
            "R",
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "R", "R", "W", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "R", "R", "R", "R", "W", "W"],
                ["W", "W", "W", "R", "R", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "B", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
        ),
        (
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
            (3, 4),
            "B",
            [
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "B", "B", "B", "B", "W", "W"],
                ["W", "W", "W", "B", "B", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
                ["W", "W", "W", "W", "W", "W", "W", "W"],
            ],
        ),
    ],
)
def test_flood_fill_using_dfs(
    pixels: list[list[str]],
    start: tuple[int, int],
    replacement_value: str,
    expected_filled_pixels: list[list[str]],
) -> None:
    challenges.flood_fill_using_dfs(pixels, start, replacement_value)
    assert (
        pixels == expected_filled_pixels
    ), "Expected filled pixels don't match actual filled pixels"


@pytest.mark.parametrize(
    "landscape, expected_island_count",
    [
        (
            [
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
            ],
            0,
        ),
        (
            [
                [" ", "X", " ", " ", " ", " ", " ", " "],
                [" ", "X", " ", " ", " ", " ", "X", " "],
                [" ", " ", " ", "X", "X", " ", " ", " "],
                [" ", " ", " ", "X", "X", " ", " ", " "],
                ["X", "X", " ", " ", " ", "X", " ", " "],
                [" ", "X", "X", " ", " ", " ", "X", "X"],
                [" ", " ", "X", " ", " ", " ", "X", " "],
                [" ", " ", " ", " ", " ", " ", "X", " "],
            ],
            6,
        ),
    ],
)
def test_count_number_of_islands_using_bfs(
    landscape: list[list[challenges.Square]], expected_island_count: int
) -> None:
    island_count = challenges.count_number_of_islands_using_bfs(landscape)
    assert (
        island_count == expected_island_count
    ), f"Expected landscape to have {expected_island_count} islands"


@pytest.mark.parametrize(
    "landscape, expected_island_count",
    [
        (
            [
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " "],
            ],
            0,
        ),
        (
            [
                [" ", "X", " ", " ", " ", " ", " ", " "],
                [" ", "X", " ", " ", " ", " ", "X", " "],
                [" ", " ", " ", "X", "X", " ", " ", " "],
                [" ", " ", " ", "X", "X", " ", " ", " "],
                ["X", "X", " ", " ", " ", "X", " ", " "],
                [" ", "X", "X", " ", " ", " ", "X", "X"],
                [" ", " ", "X", " ", " ", " ", "X", " "],
                [" ", " ", " ", " ", " ", " ", "X", " "],
            ],
            6,
        ),
    ],
)
def test_count_number_of_islands_using_dfs(
    landscape: list[list[challenges.Square]], expected_island_count: int
) -> None:
    island_count = challenges.count_number_of_islands_using_dfs(landscape)
    assert (
        island_count == expected_island_count
    ), f"Expected landscape to have {expected_island_count} islands"


def test_file_tree_print_using_dfs_simple_example(mocker: MockerFixture) -> None:
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    file = challenges.FileTreeNode("file.txt")
    file_tree = challenges.FileTree(file)
    file_tree.print_using_dfs()
    outputted_lines = mock_stdout.getvalue().splitlines()
    expected_output = "file.txt"
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_output
    ), f"Expected a single file, {expected_output}, to be printed"


def test_file_tree_print_using_dfs_complex_example(mocker: MockerFixture) -> None:
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    dir_1 = challenges.DirectoryNode("dir1")
    dir_2 = challenges.DirectoryNode("dir2")
    dir_3 = challenges.DirectoryNode("dir3")
    file_1 = challenges.FileTreeNode("file1.txt")
    file_2 = challenges.FileTreeNode("file2.txt")
    file_3 = challenges.FileTreeNode("file3.txt")
    dir_1.add_child(dir_2)
    dir_1.add_child(file_1)
    dir_1.add_child(dir_3)
    dir_2.add_child(file_2)
    dir_3.add_child(file_3)
    file_tree = challenges.FileTree(dir_1)
    file_tree.print_using_dfs()
    outputted_lines = mock_stdout.getvalue().splitlines()
    expected_outputted_lines = [
        "dir1/",
        "   -> dir2/",
        "      -> file2.txt",
        "   -> file1.txt",
        "   -> dir3/",
        "      -> file3.txt",
    ]
    assert len(outputted_lines) == len(
        expected_outputted_lines
    ), f"Expected there to be {len(expected_outputted_lines)} printed lines"
    assert set(outputted_lines) == set(
        expected_outputted_lines
    ), "Right number of lines printed but wrong values"
    assert (
        outputted_lines == expected_outputted_lines
    ), "Right lines printed but in wrong order"
