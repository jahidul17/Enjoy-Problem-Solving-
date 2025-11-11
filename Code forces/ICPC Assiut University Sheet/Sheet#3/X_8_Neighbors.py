import sys

# --- Start of Program Logic ---

try:
    # 1. Read n and m (dimensions)
    n, m = map(int, sys.stdin.readline().split())

    # 2. Read the grid
    grid = []
    for _ in range(n):
        # We use list(line.strip()) to get a list of characters for each row
        # This mirrors the char a[i] access in C
        grid.append(list(sys.stdin.readline().strip()))

    # 3. Read x and y (coordinates)
    x, y = map(int, sys.stdin.readline().split())

    # Convert to 0-based indexing
    r = x - 1 # row index
    c = y - 1 # column index

except Exception:
    # Handle cases where input is missing or malformed
    sys.exit()

# 4. Define the 8 directional offsets (dr, dc)
# (dr: change in row, dc: change in column)
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0),       # H/V
    (1, 1), (-1, -1), (1, -1), (-1, 1)      # Diagonal
]

all_x = True # Assume success initially

# 5. Check all neighbors
for dr, dc in directions:
    nr = r + dr # new row
    nc = c + dc # new column

    # Boundary Check: Is the neighbor within the grid (0 <= nr < n and 0 <= nc < m)?
    if 0 <= nr < n and 0 <= nc < m:
        # Character Check: If the neighbor exists, is its value NOT 'x'?
        if grid[nr][nc] != 'x':
            all_x = False
            break # Stop checking immediately

# 6. Output the result
if all_x:
    print("yes")
else:
    print("no")

# --- End of Program Logic ---