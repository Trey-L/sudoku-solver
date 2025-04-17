# Python Sudoku Solver

## Description

This script provides a simple command-line Sudoku solver written in Python. It uses a backtracking algorithm to find the solution for a given 9x9 Sudoku puzzle. The user provides the puzzle as a single string, and the script prints both the initial and the solved grid (if a solution exists).

## Features

*   Solves standard 9x9 Sudoku puzzles.
*   Accepts puzzle input via a single 81-character string.
*   Uses digits '1' through '9' for pre-filled cells.
*   Uses '0', 'x', or '.' to represent empty cells.
*   Prints the initial and solved grids in a readable, formatted way.
*   Includes basic input validation for string length and character type.
*   Includes basic validation for the initial board setup (detects immediate conflicts).

## Input Format

*   The input must be a single string containing exactly **81 characters**.
*   The string represents the Sudoku grid read **row by row**, from left to right, top to bottom.
*   Use digits `1` through `9` for cells that are already filled.
*   Use `0`, `x`, or `.` (case-insensitive for 'x') for empty cells.

**Example Input String:**

For the following puzzle:
<table class="sudoku-table"> <tr> <td>5</td> <td>3</td> <td class="empty-cell">.</td><td> </td><td class="empty-cell">.</td> <td>7</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> </tr> <tr> <td>6</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td>1</td> <td>9</td> <td>5</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> </tr> <tr> <td class="empty-cell">.</td> <td>9</td> <td>8</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td>6</td> <td class="empty-cell">.</td> </tr> <tr> <td colspan="11" style="border:0; height: 2px; padding:0; background:black;"></td> </tr> <tr> <td>8</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td>6</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td>3</td> </tr> <tr> <td>4</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td>8</td> <td class="empty-cell">.</td> <td>3</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td>1</td> </tr> <tr> <td>7</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td>2</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td>6</td> </tr> <tr> <td colspan="11" style="border:0; height: 2px; padding:0; background:black;"></td> </tr> <tr> <td class="empty-cell">.</td> <td>6</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td>2</td> <td>8</td> <td class="empty-cell">.</td> </tr> <tr> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td>4</td> <td>1</td> <td>9</td> <td> </td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td>5</td> </tr> <tr> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td>8</td> <td class="empty-cell">.</td> <td> </td> <td class="empty-cell">.</td> <td>7</td> <td>9</td> </tr> </table>


The input string would be (using '0' for empty):
`530070000600195000098000060800060003400803001700020006060000280000419005000080079`

## Output

The script will:
1.  Print the initial puzzle grid, formatted with separators, based on your input.
2.  If a solution is found, it will print the solved puzzle grid, also formatted.
3.  If the input string is invalid or the puzzle has no solution, it will print an error message.



