# Grokking Algorithms

My implementations of the algorithms from the book *Grokking Algorithms*.

## Progress

| Ch. | Algorithm      | Folder                                       | Complexity (average) |
|-----|----------------|----------------------------------------------|----------------------|
| 1   | Binary search  | [ch01_binary_search](ch01_binary_search)     | O(log n)             |
| 2   | Selection sort | [ch02_selection_sort](ch02_selection_sort)   | O(n²)                |
| 3   | Recursion      | [ch03_recursion](ch03_recursion)             | —                    |
| 4   | Quicksort      | [ch04_quicksort](ch04_quicksort)             | O(n log n)           |

## Structure

- `chNN_<topic>/` — one folder per book chapter.
- `data.py` — shared test lists (`SORTED_LIST`, `UNSORTED_LIST`, `SMALL_LIST`).

## How to run

Run from the repository root as a module, so the scripts can import `data.py`:

```bash
python -m ch04_quicksort.quicksort
```

Use dots instead of slashes and leave out `.py`.
Running the file directly (`python ch04_quicksort/quicksort.py`) fails with
`ModuleNotFoundError: No module named 'data'`.
