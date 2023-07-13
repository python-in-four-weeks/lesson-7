# Lesson 7 Independent Challenges

## Challenge 1: `calculate_minimum_knight_hops_using_bfs` (15 points)

Given a start coordinate and an end coordinate - both in the form `(row_index, col_index)` - belonging to a standard 8 x 8 chess board, use BFS to calculate and return the minimum number of hops a knight would require to move between the coordinates.

You are encouraged to check the allowed movements of a knight on a chess board online if in any doubt.

Assumptions you may make:
- The start and end coordinates given will both be in the bounds of the board

## Challenge 2: `check_end_reachable_from_start_in_maze_using_dfs` (10 points)

Given a start coordinate and an end coordinate - both in the form `(row_index, col_index)` - belonging to a maze consisting of `' '` characters (available spaces) and `'X'` characters (obstacles), use DFS to check and return whether there exists a valid path between the coordinates.

A valid path consists only of steps up, down, left and right, within the bounds of the maze.

Assumptions you may make:
- The start and end coordinates given will both be in the bounds of the maze
- Neither the start nor the end coordinate will coincide with an obstacle
- The maze will be rectangular
- The maze will be at least one row deep and one column wide

## Challenge 3: `find_length_of_shortest_path_in_maze_using_bfs` (15 points)

Given a start coordinate and an end coordinate - both in the form `(row_index, col_index)` - belonging to a maze consisting of `' '` characters (available spaces) and `'X'` characters (obstacles), use BFS to find the shortest path between the coordinates, if one exists.

A valid path consists only of steps up, down, left and right, within the bounds of the maze.

If there is no valid path between the coordinates, you should raise a `ValueError` with the following exact message:

```
End not reachable from start
```

Assumptions you may make:
- The start and end coordinates given will both be in the bounds of the maze
- Neither the start nor the end coordinate will coincide with an obstacle
- The maze will be rectangular
- The maze will be at least one row deep and one column wide

## Challenge 4: `find_length_of_longest_downhill_path_using_bfs` (10 points)

Given a grid of altitudes and a start coordinate, the latter in the form `(row_index, col_index)`, use BFS to find the longest strictly-downhill path from the start coordinate.

A valid path consists only of steps up, down, left and right, within the bounds of the altitudes grid.

Assumptions you may make:
- The start coordinate given will be in the bounds of the altitudes grid
- The altitudes grid will be rectangular
- The altitudes grid will be at least one row deep and one column wide
 
## Challenge 5: `flood_fill_using_bfs` (10 points)

Given a grid of pixels, a start coordinate in the form `(row_index, col_index)` and a replacement value, use BFS to change all pixels in the same region as the start coordinate to the replacement value.

A region consists of pixels with the same value that are immediately above, below, to the left or to the right of another pixel in the region.

Assumptions you may make:
- The start coordinate given will be in the bounds of the pixels grid
- The pixels grid will be rectangular
- The pixels grid will be at least one row deep and one column wide

## Challenge 6: `flood_fill_using_dfs` (10 points)

Given a grid of pixels, a start coordinate in the form `(row_index, col_index)` and a replacement value, use DFS to change all pixels in the same region as the start coordinate to the replacement value.

A region consists of pixels with the same value that are immediately above, below, to the left or to the right of another pixel in the region.

Assumptions you may make:
- The start coordinate given will be in the bounds of the pixels grid
- The pixels grid will be rectangular
- The pixels grid will be at least one row deep and one column wide

## Challenge 7: `count_number_of_islands_using_bfs` (10 points)

Given a landscape consisting of `' '` characters (sea) and `'X'` characters (land), use BFS to count the number of distinct islands.

An island consists of land squares that are immediately above, below, to the left or to the right of another land square belonging to the island.

Assumptions you may make:
- The landscape will be rectangular
- The landscape will be at least one row deep and one column wide

## Challenge 8: `count_number_of_islands_using_dfs` (10 points)

Given a landscape consisting of `' '` characters (sea) and `'X'` characters (land), use DFS to count the number of distinct islands.

An island consists of land squares that are immediately above, below, to the left or to the right of another land square belonging to the island.

Assumptions you may make:
- The landscape will be rectangular
- The landscape will be at least one row deep and one column wide

## Challenge 9: `FileTree.print_using_dfs` (10 points)

Two classes, `FileTreeNode` and `DirectoryNode`, have been implemented for you, and a third, `FileTree`, has been partially implemented. You need to complete its `print_using_dfs` method.

A file tree with a root node `dir1` with three children - `dir2` (containing `file2.txt`), `file1.txt` and `dir3` (containing `file3.txt`) would be printed in the following format:

```
dir1/
   -> dir2/
      -> file2.txt
   -> file1.txt
   -> dir3/
      -> file3.txt
```

Note the directory names are printed with a single trailing `/` (you may assume that the names do not include this character already), and that all nodes apart from the root node are printed with leading spaces and arrows to indicate their level in the file tree structure.

Note also that the contents of any particular directory should be printed in the order in which they are stored.
