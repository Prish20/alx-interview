# Island Perimeter

This project involves creating a function that calculates the perimeter of an island represented in a grid. The grid is a 2D list where:

- `0` represents water.
- `1` represents land.

## Function Description

### `island_perimeter(grid)`

Calculates the perimeter of the island described in `grid`.

- **Parameters:**
  - `grid` (list of list of ints): The grid representing the island.
- **Returns:**
  - `int`: The perimeter of the island.

## Usage

```python
#!/usr/bin/python3
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(island_perimeter(grid))
```

### Output

```bash
12
```
